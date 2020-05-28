.. raw:: mediawiki

   {{Lowercase}}

The discussions on this page have been edited for clarity, ease of reading, collation of later questions, and to trim out some noise. The original transcript can be found here: `X264asm <X264asm>`__

\__TOC_\_

Example 1: predict_4x4_dc
-------------------------

Open common/x86/predict-a.asm, go to predict_4x4_dc_mmxext (`git link <http://git.videolan.org/?p=x264.git;a=blob;f=common/x86/predict-a.asm;h=a05e91beda809b5e113df8ba122496e756442df8;hb=HEAD#l292>`__). This function does the following:

::

     A B C D
   E X X X X
   F X X X X
   G X X X X
   H X X X X

It calculates (A+B+C+D+E+F+G+H+4)/8, and sets all the Xs equal to that value where those are 8-bit pixels in a 2D array with a stride of FDEC_STRIDE.

   <Q> What is FDEC_STRIDE?
   <A> x264 does all its pixel operations on the current macroblock in a temporary buffer of constant stride. It's faster that way, and better on cache. So for example, motion compensation will write to this buffer (or intra prediction).
   <Q> What's a stride?
   <A> Stride is the distance between (x,y) and (x,y+1), so to get from one row to the next.

Now that you understand what the function does, let's look at the asm.

::

   cglobal predict_4x4_dc_mmxext, 1,4

"cglobal" declares a function accessible from outside of asm. The function's name is ``x264_predict_4x4_dc_mmxext`` (the ``x264_`` is auto-added). The "1" means "we have one argument. Put it in ``r0``.", (that argument is uint8_t \*src). If we had a second argument, we'd say "2" and the second one would go in ``r1`` and if we had a third, it'd go in ``r2``, etc. So at the start of the function, ``r0`` contains uint8_t \*src.

   <Q> "that argument is uint8_t \*src", what does this mean?
   <A> See the comment above: ``void predict_4x4_dc( uint8_t *src )``
   <Q> What tells the function that it's uint8_t?
   <A> Nothing. It doesn't need to know. Types are a C-ism.

The "4" means we want x264 to give us 4 registers to use. ``r0``, ``r1``, ``r2``, ``r3``. This, of course, includes the ``r0`` used for the parameter. So in short, after the first line: ``r0`` = src, ``r1``/``r2``/``r3`` = free, ``r4`` and up: can't use.

   <Q> That's x86inc.asm's doing right?
   <A> Yes, but we aren't going into that.
   <Q> I assume it means we can use them, but if you do, it'll screw around with something you don't want to?
   <A> Yes, which is why you can't use it.

So now, this function as you can see has 4 real steps:

#. Sum up A through D
#. Sum up E through H
#. Do the math to get our final value
#. Store it into the 16 output Xs

So let's see how this asm implements these.

First, we'll look at step 1

::

   pxor mm7, mm7

``mm7`` is a 64-bit register. ``xor``, as you might know, is a nice way to zero things.

   <Q> How do you tell how large a register is?
   <A> ``mm*`` is 64-bit, ``xmm*`` is 128-bit. The mm registers have a fixed size, only the general purpose registers are wordsize-dependant on x86

So, now ``mm7`` is zero.

::

   movd mm0, [r0-FDEC_STRIDE]

This sets ``mm0`` equal to {A,B,C,D,0,0,0,0}

   <Q> Oh, and how do we know the mm\* registers are free?
   <A> They always are.

In x86, b = byte, w = word (16-bit), d = doubleword (32-bit), q = quadword (64-bit), dq = double quadword (128-bit). So ``movd`` = move doubleword = move 32 bits. So ``movd`` to ``mm0`` will load data to the first 4 bytes and zero the rest. Thus ``mm0`` is now ABCD0000. ``[r0-FDEC_STRIDE]`` is equivalent to ``*(src-FDEC_STRIDE)`` in C-style. Hence why it points to ABCD.

   <Q> Are the "A B C D" on top of the "X X X X" or do they start on top of the "E"?
   <A> Former

::

   psadbw mm0, mm7

This is what ``psadbw`` does:

::

   uint16_t psadbw( uint8_t in[8], uint8_t out[8] )
   {
       uint16_t sum = 0;
       for(int i = 0; i &lt; 8; i++)
           sum += abs(in[i]-out[i]);
       return sum;
   }

Parse that for a moment

   <Q> where is the sum stored?
   <A> ``psadbw X, Y``, ``X`` is where the output is stored. So ``X`` is overwritten. So it's stored in the low 16 bits of ``X``.

Now, of course, ``mm7`` is zero! So we get abs(A-0) + abs(B-0) + abs(C-0) + abs(D-0) + abs(0-0) ... Or A+B+C+D. So after ``psadbw``, ``mm0`` is A+B+C+D and ``mm7`` is still zero.

::

   movd r3d, mm0

Now, we move the result to ``r3d``, a general purpose register.

   <Q> Is ``r3d`` one of the things that come with the 4 registers that are free?
   <A> This is an optimization: on 64-bit, using 32-bit versions of registers results in smaller instruction opcode sizes. So it's really just ``r3``. ``r0``, ``r1``, ``r2``, ``r3`` are the 4 that are free. So we're using ``r3``. Note: the suffix 'd' means the 32-bit version, as opposed to the native-size version.

Get moving with part 2 of the algorithm.

Now ``r0`` has our source pointer, and ``r3`` has A+B+C+D. While the CPU is busy doing that, we'll go and do part 2, the E+F+G+H. Unfortunately, these bytes aren't in a straight line ("straight line" meaning "adjacent in memory"). So we can't just load EFGH and sad them. We'll have to do it the naive/slow way. So, now we're going to load E, F, G, H. Now you might notice some preprocessor commands here. ``%assign``, ``%rep``, etc are preprocessor commands.

So, first step: load E into ``r1d``

::

   movzx r1d, byte [r0-1]

``movzx`` means "move, with zero extend". In C this would be: int r1d = r0[-1];

   <Q> My C is a bit rusty, what does that do? does it just take the location in memory before r0[0]?
   <A> Yes, [] is just a dereference of a pointer. \*(r0-1) = r0[-1] = (r0-1)[0]
   <Q> what is r0-1 in that ascii matrix?
   <A> E.

So, here's what these 7 lines look like after the macro runs:

::

   movzx  r1d, byte [r0-1]
   movzx  r2d, byte [r0+FDEC_STRIDE*1-1]
   add    r1d, r2d
   movzx  r2d, byte [r0+FDEC_STRIDE*2-1]
   add    r1d, r2d
   movzx  r2d, byte [r0+FDEC_STRIDE*3-1]
   add    r1d, r2d

in order: load E, load F, add F to E, load G, add G to E, load H, add H to E

   <Q> Where is n stored?
   <A> It isn't. It's a preprocessor variable.
   <Q> Oh, so it's like a macro?
   <A> It is a macro. Note the pre-processed code above. Everything starting with % in yasm syntax is a macro.

Ok, now we have to do step 3: calculating A+B+C+D+E+F+G+H+4 / 8

::

   lea r1d, [r1+r3+4]

First, let's go over x86 addressing. What you can put inside the brackets is not infinite. Here's the capabilities, specifically: [REG1 + REG2 \* {1,2,4,8} + CONST]. A register, plus another register \* 1/2/4/8, plus a constant (positive or negative). As you might note, this is pretty useful for accessing things like arrays. E.g. array[n+5], where array is an int array, would be: [array + n*4 + 20]

   <Q> I suppose the [r0+FDEC_STRIDE*n-1] bit gets simplified on assembly to [register + const]?
   <A> Yes, yasm sums up constants for you.

So, as you might note, that's a pretty powerful addressing system. That's more powerful than, say... "add". So why not expose it in an instruction to let us use it for math? So Intel did. ``lea X, [expr]`` sets X equal to the value of expr just as fast as add. So that ``lea`` does r1d = r1 + r3 + 4

   <Q> Wait, how does that work?
   <A> ``lea`` runs the [REG1 + REG2 \* {1,2,4,8} + CONST] math on its second argument and adds to the first. ``lea`` doesn't actually address it. It just calculates the result and stores it instead of going to memory.
   <Q> And it's faster than add?
   <A> It's just as fast except that you can do more with it.

Now, technically, you can do more adds per cycle than ``lea``, so you shouldn't go replacing all your adds with ``lea``. But if you can use it to do more than one thing at a time, it's a big win. So this lets us add ``r3``, and add 4, in one op.

::

   shr r1d, 3

There's one that you can probably figure out yourself - shift right.

   <Q> Why are we shifting right?
   <A> +4 for correct rounding, >> 3 to divide (>>3 = /(2^3) = /8).

Now for the final part: storing the results.

::

   imul r1d, 0x01010101

This is called a "splat" and you may have seen it in C as well. We're turning an 8-bit value into 4x that value, e.g. A -> AAAA

   <Q> how does this work?
   <A> A \* 0x01010101 = A A A A

So now we have a 32-bit register, ``r1d`` with one copy of A in each 8-bit nibble of that register. Now we go ahead and store this 4 times and we're done.

Finally, we RET: x264 will automatically clean up after us.

Example 2: pixel_sad
--------------------

Ok, next. You may have noticed that ``psadbw`` is awesome. It does like 8 things in one. Whereas abs() is typically 4 instructions on x86. ``psadbw`` does 8 subtracts, 8 absolute values on those results and then adds them up. That's 8 + 32 + 7 = 47 instructions in one (at least, 47 equivalent).

   <Q> why is abs() so slow?
   <A> abs() isn't slow, there's just no instruction for it. The typical algorithm is:

::

   int sign = x &gt;&gt; 31;
   (x ^ sign) - sign;

   This needs a mov on x86, so that's 4 instructions.

So ``psadbw`` is pretty awesome. It's very awesome for doing what its name implies you should do with it, that is -- SADs -- sum of absolute differences. So let's open sad-a.asm and hop down to line 95 (`git link <http://git.videolan.org/?p=x264.git;a=blob;f=common/x86/sad-a.asm;h=0a96837aaa4c54f624b63c020872b74a790f1ffd;hb=HEAD#l95>`__). Also open common/pixel.c and look at the first function: SAD (`git link <http://git.videolan.org/?p=x264.git;a=blob;f=common/pixel.c;h=7fa497c7cf151df5795bb105895760fde89facb6;hb=HEAD#l44>`__). This function is pretty simple. You should be able to see how it works. Look only at the C for now.

So as you'll notice, the C SAD has 7 different versions for 16x16, 16x8, 8x16, etc and it's instantiated via a macro. So, for our asm, we also need 7 versions and we also don't want to write the function 7 times, just like in the case of C we didn't.

So in the asm, we define a macro: ``%macro SAD 2`` that means this macro has two parameters. They are accessed as %1 and %2. We call the macro 7 times, one for each size. The function takes 4 args (as you'd expect) and needs 4 regs (just the args)

   <Q> Is SAD_INC_2x%1P another macro?
   <A> Yes, it's one of three macros, look above, each one does 2 rows worth of SAD for width 4, width 8, and width 16. It picks the right one based on the width and it %reps it based on the height.

Now, start analyzing the 3 macros above (the sad macros) and trying to figure out how they work. Note mm0 is the accumulator which is why it's zeroed at the start.

   <Q> The order of args is the same as in the C function?
   <A> Yes
   <Q> What does punpckldq do?
   <A> Good question! punpck is a set of instructions that interleave their arguments in some fashion.

To start with, it can be l or h, low or high. So punpckl_\_ ABCD, EFGH will use AB and EF. And punpbkh_\_ ABCD, EFGH will use CD and GH.

The next two letters are the source size, and destination size. For example, ``punpcklbw`` interleaves bytes, to create words. So ``punpcklbw ABCD, EFGH`` gives you AEBF (if the letters are bytes). So ``punpckldq ABCDEFGH, IJKLMNOP`` gives us ABCDIJKL. So in other words, it stuffs the two sets of 4 bytes we just loaded into one register

So we can do only one SAD, instead of two. ``punpckldq ABCD0000, EFGH0000`` results in ABCDEFGH. So it effectively concatenates mm1 and mm2 for us. If we didn't do this, we'd have to do twice as many sads and adds. We do this because the registers are width 8, but our sad is width 4. So we need to stuff sad information side by side to fill the whole reg.

   <Q> Why are we punpckldq'ing the [r0+r1] and not [r0]?
   <A> We're concatenating row 0 and row 1 of each input.
   <Q>``lea r0, [r0+2*r1]`` Why are we doing this step? Doesn't it move r0 over 2*r1?
   <A> We're incrementing the pointer by 2*stride

Now you should understand what SAD_INC_2x4P does, the others work similarly except without the punpck magic because they don't need it.

   <Q> Why is the lea out of order in SAD_INC_2x8P? By out of order i mean not next to each other.
   <A> No particular reason.
   <Q> So we rep the SAD for however many times so the 2x%1 is completed?
   <A> Yes, so if it's height 8, we rep it 4 times
   <Q> Why are strides not hardcoded btw?
   <A> SAD can be called on a reference frame thus variable stride
   <Q> I don't really get it...
   A<> It's called on frames, as opposed to some temporary block of memory.

Now, for the kicker: the 16x16 SAD function declared here is 15 times faster than C.

   <Q> What? Why is it so much faster?
   <A> psadbw

Now let's get a bit to how we measure performance. For any asm instruction, there are three things that matter: latency, inverse throughput, and execution units. The first two are represented with notation like this: "3/1". This means a psadbw takes 3 clocks to finish from when it's started and you can do one of them per cycle. Another example is ``mov``. Between two registers it is 1/0.33, takes 1 cycle, and you can do 3 per clock.

Execution unit usage is a bit trickier. Not all execution units can do all instructions. Intel chips have 6 execution units: p0, p1, p2, p3, p4, p5

   <Q> Wait, what is latency?
   <A> time from start to finish, in clocks
   <Q> and inverse throughput and execution units?
   <A> Inverse throughput is how many you can do per clock. Execution units are the things in the chip that do stuff.

Of these 6 execution units, three can do math: p0, p1, p5. ``psadbw``, for example, can only use one of these (p1), ``pxor`` can use all three.

Generally execution units aren't important until you get into serious optimizing but they can often affect the best instruction choices. For example, if an execution unit is sitting around doing nothing for a whole function.

The instruction tables sheet here http://agner.org/optimize/ has all the information on latency, execution units, and inverse throughput for a wide variety of CPUs.

   <Q> How about branching? I heard branching ruins things.
   <A> Not generally unless it's unpredictable, branch mispredictions are the cause. We can get to a case of that later.

Now, let's just analyze SAD. Suppose we want to analyze the 8x8 SAD. In this function we do: 8 SADs, 8 adds (accumulates), 16 loads, plus the start, end, and calling overhead. 8 SADs: takes 8 cycles (inverse throughput of 1). 8 adds: takes 8 cycles (inverse throughput of 1), and can run at the same time as SADs. 16 loads: takes 16 cycles, and can run at the same time as the above.

So the loads are the bottleneck. This is an important thing to understand: it's possible for one type of operation to bottleneck a function. Loads are a common example. In this case, SAD is \*so fast\* that it is effectively free, as we're sitting around waiting for loads the whole time. The actual run-time of the function is about 22 clocks. Which is fitting for 16 + start + end + overhead.

So that's some basic performance analysis for you. How long the function should take in theory, how long each instruction takes in theory, and how you can be bottlenecked.

   <Q> Is there anything that does this automatically for you?
   <A> Analysis? not really. There are Intel performance counters and such on the chip but they're not magic. It might be useful to have some kind of tool to analyze asm functions. In general though, intuition is a powerful tool.

Example 3: pixel_avg2_w16_sse2
------------------------------

Let's move onto something else. Open common/x86/mc-a.asm, pixel_avg2_w16_sse2 (`git link <http://git.videolan.org/?p=x264.git;a=blob;f=common/x86/mc-a.asm;h=22fb8720c83b72bcd34b41553f4153bb62847462;hb=HEAD#l842>`__). This function interpolates between two inputs, and outputs to an output. The interpolation is the simplest possible: (A+B+1)>>1

Look at the function signature above: ``void pixel_avg2_w4( uint8_t *dst, int dst_stride`` etc. This function takes inputs from src1 and src2, averages them together, and writes to dst. src1 and src2 have src_stride and dst has dst_stride.

   <Q> What's the height?
   <A> How many lines to interpolate.

Now this function uses xmm registers (128-bit) so it does 16 bytes at a time. All 128-bit loads must be aligned unless movdqu is used. Since our inputs are unaligned, this is a lot of movdqu.

   <Q> What does movdqu do?
   <A> Loads 128 bits from an unaligned source.
   <Q> What is the difference between movdqa and movdqu?
   <A> movdqa is for aligned data, movdqu is for unaligned data. The output is always aligned, as we control it, whereas the input is an arbitrary pointer into a reference frame and so it could be anything.
   <Q> Why subtract r2 from r4?
   <A> Ah, now here's a fun trick. We need to increment three pointers, right? src1, src2, dst. But src1 and src2 have the same stride, so they're being incremented by the same amount. So we can take src2 and represent it as an offset from src1. Then we only have to increment src1. One lea removed per iteration, bam.
   <Q> And use r6 as the offset + stride?
   <A> Yes

Look through that function and see if there's anything you don't know about and ask questions.

   <Q> How do you keep track of which argument is which?
   <A> You can copy the description from w4 and annotate it.

::

   ; void pixel_avg2_w4( uint8_t *dst (r0), int dst_stride (r1),
   ;                     uint8_t *src1 (r2), int src_stride (r3),
   ;                     uint8_t *src2 (r4), int height (r5) );

   There is also a system that can be covered later which helps you keep track of registers or, well, makes it easier to.
   <Q> pavgb, I assume, does some sort of averaging?
   <A> Yes, (A+B+1)>>1 for each pair of input pixels.

Now we come to one of the many jumps that exists in x86, jump if greater than, so if r5d > 0.

   <Q> How does the jump work without a compare instruction?
   <A> The sub sets the same flags as a cmp.
   <Q> So why subtract two?
   <A> It handles two rows at a time.

Here is something to note. The REP_RET you might have been wondering about. In short, if you have a RET after a jump, use REP_RET. Blame AMD.

Helpful links
-------------

-  http://agner.org/optimize/ - PDFs containing instruction timing and a couple of related guides (mentioned above)
-  http://alien.dowling.edu/~rohit/nasmdocb.html - NASM manual, x86 instruction reference
-  http://alien.dowling.edu/~rohit/nasmdoc0.html - NASM manual, contents page
-  http://www.tortall.net/projects/yasm/manual/html/index.html - YASM manual, contents page (similar to the NASM manual)
-  http://www.tommesani.com/Docs.html - Some visual representations of MMX instructions
-  http://webster.cs.ucr.edu/AoA/Windows/HTML/TheMMXInstructionSeta2.html - More visual representations of instructions

`Category:x264 <Category:x264>`__
