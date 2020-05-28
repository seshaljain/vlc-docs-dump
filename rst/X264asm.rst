.. raw:: mediawiki

   {{Lowercase}}

An edited version can be found here: `X264 asm intro <X264_asm_intro>`__

::

   2010-11-22 00:35:03 < Jumpyshoes> cool
   2010-11-22 00:35:09 < Dark_Shikari> open common/x86/predict-a.asm
   2010-11-22 00:35:26 < Dark_Shikari> go to predict_4x4_dc_mmxext
   2010-11-22 00:35:29 < Dark_Shikari> this function does the following
   2010-11-22 00:35:32 < Dark_Shikari>   A B C D
   2010-11-22 00:35:34 < Dark_Shikari> E X X X X
   2010-11-22 00:35:36 < Dark_Shikari> F X X X X
   2010-11-22 00:35:37 < Dark_Shikari> G X X X X
   2010-11-22 00:35:40 < Dark_Shikari> H X X X X
   2010-11-22 00:35:48 < Kovensky> ascii graphs :D
   2010-11-22 00:35:51 < Dark_Shikari> It calculates (A+B+C+D+E+F+G+H+4)>>3, and sets all the Xs equal to that value.
   2010-11-22 00:36:06 < Dark_Shikari> where those are 8-bit pixels in a 2D array with a stride of FDEC_STRIDE.
   2010-11-22 00:36:12 < Dark_Shikari> got that?  throw questions at any time
   2010-11-22 00:36:19 < Jumpyshoes> actually, can you hold on for one minute?
   2010-11-22 00:36:28 < Dark_Shikari> ok
   2010-11-22 00:36:42 < Jumpyshoes> being a dumbass, i forgot x264 was on my other computer
   2010-11-22 00:36:46 < Kovensky> durf, iTerm2 locked up
   2010-11-22 00:38:54 < Jumpyshoes> okay
   2010-11-22 00:38:56 < Jumpyshoes> ready now
   2010-11-22 00:40:15  * Dark_Shikari waits for response
   2010-11-22 00:40:33 < Jumpyshoes> i think i should look up the intel docs
   2010-11-22 00:40:42 < Dark_Shikari> ?
   2010-11-22 00:40:50 < Dark_Shikari> I asked you if you understood my explanation of what a function does.
   2010-11-22 00:40:52 < Jumpyshoes> well, it's a bunch of assembly
   2010-11-22 00:40:53 < Jumpyshoes> OH
   2010-11-22 00:40:54 < Dark_Shikari> This has absolutely nothing to do with intel.
   2010-11-22 00:40:59 < Jumpyshoes> yes, i understand what the function does
   2010-11-22 00:41:19 < Dark_Shikari> ok, good
   2010-11-22 00:41:42 < Jumpyshoes> actually, what is FDEC_STRIDE?
   2010-11-22 00:41:54 < Dark_Shikari> x264 does all its pixel operations on the current macroblock in a temporary buffer
   2010-11-22 00:41:59 < Dark_Shikari> of constant stride
   2010-11-22 00:42:02 < Dark_Shikari> it's faster that way, and better on cache
   2010-11-22 00:42:16 < Jumpyshoes> what's a stride? <_<
   2010-11-22 00:42:16 < Dark_Shikari> so for example, motion compensation will write to this buffer
   2010-11-22 00:42:18 < Dark_Shikari> or intra prediction
   2010-11-22 00:42:26 < Kovensky> a stride is the distance from one line to the next IIRC
   2010-11-22 00:42:43 < Dark_Shikari> stride is the distance between (x,y) and (x,y+1)
   2010-11-22 00:43:07 < Jumpyshoes> i see
   2010-11-22 00:43:36 < Dark_Shikari> so to get from one row to the next
   2010-11-22 00:43:51 < Dark_Shikari> now that you understand what the function does, let's look at the asm
   2010-11-22 00:43:54 < Dark_Shikari> cglobal predict_4x4_dc_mmxext, 1,4
   2010-11-22 00:44:01 < Kovensky> yay, asm class
   2010-11-22 00:44:02  * Kovensky watches
   2010-11-22 00:44:12 < Dark_Shikari> cglobal: declares a function accessible from outside of asm
   2010-11-22 00:44:20 < Dark_Shikari> the function's name is x264_predict_4x4_dc_mmxext
   2010-11-22 00:44:24 < Dark_Shikari> the x264_ is auto-added.
   2010-11-22 00:44:33 < Dark_Shikari> the "1" means "we have one argument.  Put it in r0."
   2010-11-22 00:44:36 < Dark_Shikari> that argument is uint8_t *src
   2010-11-22 00:44:46 < Dark_Shikari> if we had a second argument, we'd say "2" and the second one would go in r1.
   2010-11-22 00:44:50 < Dark_Shikari> and if we had a third, it'd go in r2.
   2010-11-22 00:44:51 < Dark_Shikari> etc
   2010-11-22 00:44:53 < Dark_Shikari> got that?
   2010-11-22 00:45:04 < Dark_Shikari> so at the start of the function, r0 contains uint8_t *src.
   2010-11-22 00:45:04 < Jumpyshoes> that argument is uint8_t *src <-- what does this mean?
   2010-11-22 00:45:09 < Dark_Shikari> ; void predict_4x4_dc( uint8_t *src )
   2010-11-22 00:45:11 < Dark_Shikari> hurr hurr
   2010-11-22 00:45:15 < Jumpyshoes> oh
   2010-11-22 00:45:16 < Dark_Shikari> it's a function argument
   2010-11-22 00:45:16 < Jumpyshoes> okay
   2010-11-22 00:45:36 < Jumpyshoes> what tells the function that it's uint8_t?
   2010-11-22 00:45:39 < Dark_Shikari> Nothing.
   2010-11-22 00:45:42 < Dark_Shikari> It doesn't need to know.
   2010-11-22 00:45:44 < Dark_Shikari> types are a Cism
   2010-11-22 00:45:58 < Jumpyshoes> right
   2010-11-22 00:45:59 < Jumpyshoes> true
   2010-11-22 00:46:03 < Dark_Shikari> the "4" means we want x264 to give us 4 registers to use.
   2010-11-22 00:46:05 < Dark_Shikari> r0, r1, r2, r3.
   2010-11-22 00:46:10 < Dark_Shikari> This, of course, includes the r0 used for the parameter.
   2010-11-22 00:46:17 < Dark_Shikari> So in short, after the first line:
   2010-11-22 00:46:19 < Dark_Shikari> r0 = src
   2010-11-22 00:46:22 < Dark_Shikari> r1/r2/r3 = free
   2010-11-22 00:46:26 < Dark_Shikari> r5 and up: can't use.
   2010-11-22 00:46:37 < Kovensky> that's x86inc.asm's doing right?
   2010-11-22 00:46:42 < Dark_Shikari> yes, but we aren't going into that
   2010-11-22 00:46:58 < Jumpyshoes> i assume it means we can use, but if you do, it'll screw around with something you don't want to?
   2010-11-22 00:47:14 < Kovensky> which is why you can't use it
   2010-11-22 00:47:19 < Dark_Shikari> ^
   2010-11-22 00:47:23 < Jumpyshoes> kk
   2010-11-22 00:47:31 < Dark_Shikari> So now, this function as you can see has 4 real steps
   2010-11-22 00:47:36 < Dark_Shikari> 1) Sum up A through D
   2010-11-22 00:47:39 < Dark_Shikari> 2) Sum up E through H
   2010-11-22 00:47:46 < Dark_Shikari> 3) Do the math to get our final value
   2010-11-22 00:47:50 < Dark_Shikari> 4) Store it into the 16 output Xs
   2010-11-22 00:47:59 < Dark_Shikari> so let's see how this asm implements these.
   2010-11-22 00:48:22 < Dark_Shikari> First, we'll look at step 1)
   2010-11-22 00:48:27 < Dark_Shikari> pxor mm7, mm7: mm7 is now zeroed.
   2010-11-22 00:48:31 < Dark_Shikari> mm7 is a 64-bit register.
   2010-11-22 00:48:36 < Dark_Shikari> xor, as you might know, is a nice way to zero things.
   2010-11-22 00:48:40 < Jumpyshoes> how do you tell how large a register is?
   2010-11-22 00:48:51 < Dark_Shikari> mm* is 64-bit
   2010-11-22 00:48:54 < Dark_Shikari> xmm* is 128-bit
   2010-11-22 00:48:55 < Kovensky> the mm registers have a fixed size
   2010-11-22 00:48:58 < Jumpyshoes> ah, okay
   2010-11-22 00:49:09 < Dark_Shikari> stop me at any point if you are missing something.
   2010-11-22 00:49:13 < Dark_Shikari> so, now mm7 is zero.
   2010-11-22 00:49:20 < Dark_Shikari> movd mm0, [r0-FDEC_STRIDE]
   2010-11-22 00:49:24 < Kovensky> only the general purpose registers are wordsize-dependant on x86
   2010-11-22 00:49:31 < Dark_Shikari> this sets mm0 equal to {A,B,C,D,0,0,0,0}
   2010-11-22 00:49:42 < Jumpyshoes> oh, and how do we know the mm* registers are free?
   2010-11-22 00:49:45 < Dark_Shikari> They always are.
   2010-11-22 00:49:48 < Jumpyshoes> oh
   2010-11-22 00:49:50 < Jumpyshoes> kk
   2010-11-22 00:49:59 < Dark_Shikari> in x86, b = byte, w = word (16-bit), d = doubleword (32-bit), q = quadword (64-bit), dq = double quadword (128-bit)
   2010-11-22 00:50:04 < Dark_Shikari> so movd = move doubleword
   2010-11-22 00:50:05 < Dark_Shikari> = move 32 bits
   2010-11-22 00:50:14 < Dark_Shikari> so movd to mm0 will load data to the first 4 bytes
   2010-11-22 00:50:16 < Dark_Shikari> and zero the rest.
   2010-11-22 00:50:20 < Dark_Shikari> thus mm0 is now ABCD0000
   2010-11-22 00:50:32 < Dark_Shikari> [r0-FDEC_STRIDE] is equivalent to *(src-FDEC_STRIDE)
   2010-11-22 00:50:35 < Dark_Shikari> in Cstyle
   2010-11-22 00:50:43 < Dark_Shikari> Hence why it points to ABCD.
   2010-11-22 00:50:56 < Jumpyshoes> kk
   2010-11-22 00:51:08 < Dark_Shikari> got it so far?
   2010-11-22 00:51:11 < Jumpyshoes> yup
   2010-11-22 00:51:24 < Jumpyshoes> i tried to dabble in asm at some point in time
   2010-11-22 00:51:28 < Jumpyshoes> then got frustrated and gave up
   2010-11-22 00:51:31 < Jumpyshoes> <-- lazy ass
   2010-11-22 00:51:48 < Kovensky> 21:35.33 Dark_Shikari:  A B C D
   2010-11-22 00:51:48 < Kovensky> 21:35.35 Dark_Shikari: E X X X X
   2010-11-22 00:51:48 < Kovensky> are the "A B C D" on top of the "X X X X" or do they start on top of the "E"
   2010-11-22 00:51:55 < Dark_Shikari> former
   2010-11-22 00:51:58 < Dark_Shikari> your IRC client sucks
   2010-11-22 00:52:00 < Dark_Shikari> your spacing is wrong
   2010-11-22 00:52:11 < jarod> nothing wrong here
   2010-11-22 00:52:13 < Dark_Shikari> use a monospaced font
   2010-11-22 00:52:18 < Dark_Shikari> Jumpyshoes: next
   2010-11-22 00:52:18 < Kovensky> I'm using osaka-mono
   2010-11-22 00:52:20 < Kovensky> well, whatever
   2010-11-22 00:52:22 < Dark_Shikari> uint16_t psadbw( uint8_t in[8], uint8_t out[8] )
   2010-11-22 00:52:23 < Dark_Shikari> {
   2010-11-22 00:52:23 < Dark_Shikari>     uint16_t sum = 0;
   2010-11-22 00:52:23 < Dark_Shikari>     for(int i = 0; i < 8; i++)
   2010-11-22 00:52:23 < Dark_Shikari>         sum += abs(in[i]-out[i]);
   2010-11-22 00:52:25 < Dark_Shikari>     return sum;
   2010-11-22 00:52:27 < Dark_Shikari> }
   2010-11-22 00:52:33 < Dark_Shikari> that's what psadbw does
   2010-11-22 00:52:45 < Dark_Shikari> parse that for a moment, and tell me when you're ready
   2010-11-22 00:53:02 < Jumpyshoes> where is the sum stored?
   2010-11-22 00:53:14 < Kovensky> packed SAD byte words?
   2010-11-22 00:53:26 < Dark_Shikari> psadbw X, Y
   2010-11-22 00:53:30 < Dark_Shikari> X is where the output is stored.
   2010-11-22 00:53:37 < Dark_Shikari> So X is overwritten.
   2010-11-22 00:53:40 < Jumpyshoes> ah
   2010-11-22 00:53:43 < Dark_Shikari> so it's stored in the low 16 bits of X.
   2010-11-22 00:53:59 < Dark_Shikari> now, of course, mm7 is zero!
   2010-11-22 00:54:13 < Dark_Shikari> so we get abs(A-0) + abs(B-0) + abs(C-0) + abs(D-0) + abs(0-0) ...
   2010-11-22 00:54:16 < Dark_Shikari> or A+B+C+D.
   2010-11-22 00:54:28 < Dark_Shikari> So after psadbw mm0, mm7, mm0 is A+B+C+D and mm7 is still zero.
   2010-11-22 00:54:30 < Dark_Shikari> Got that?
   2010-11-22 00:54:31 < Jumpyshoes> wow, in three commands
   2010-11-22 00:54:36 < Jumpyshoes> yea
   2010-11-22 00:54:46 < Kovensky> nice trick
   2010-11-22 00:54:46 < Dark_Shikari> Now, we move the result to "r3d", a general purpose register
   2010-11-22 00:54:54 < Dark_Shikari> and get moving with part 2) of the algorithm.
   2010-11-22 00:55:03 < Dark_Shikari> Note: the suffix 'd' means the 32-bit version, as opposed to the native-size version.
   2010-11-22 00:55:13 < Jumpyshoes> is r3d one of the things that come with the 4 registers that are free>.
   2010-11-22 00:55:14 < Jumpyshoes> ?
   2010-11-22 00:55:15 < Dark_Shikari> This is an optimization: on 64-bit, using 32-bit versions of registers results in smaller instruction opcode sizes.
   2010-11-22 00:55:20 < Dark_Shikari> So it's really just r3.
   2010-11-22 00:55:24 < Dark_Shikari> r0, r1, r2, r3 are the 4 that are free.
   2010-11-22 00:55:27 < Dark_Shikari> So we're using r3.
   2010-11-22 00:55:31 < Jumpyshoes> kk
   2010-11-22 00:55:36 < Dark_Shikari> So now r0 has our source pointer, and r3 has A+B+C+D.
   2010-11-22 00:55:49 < Dark_Shikari> Now, while the CPU is busy doing that, we'll go and do part 2), the E+F+G+H.
   2010-11-22 00:55:53 < Kovensky> what does the movzx do?
   2010-11-22 00:55:59 < Dark_Shikari> we'll get to that
   2010-11-22 00:56:01 < Dark_Shikari> Unfortunately, these bytes aren't in a straight line.
   2010-11-22 00:56:07 < Dark_Shikari> So we can't just load EFGH and sad them.
   2010-11-22 00:56:15 < Dark_Shikari> We'll have to do it the naive/slow way.
   2010-11-22 00:56:26 < Dark_Shikari> well, s/straight line/adjacent in memory/
   2010-11-22 00:56:34 < Kovensky> oh, so %rep is a looping macro
   2010-11-22 00:56:43 < Dark_Shikari> so, now we're going to load E, F, G, H
   2010-11-22 00:56:48 < Jumpyshoes> oh
   2010-11-22 00:56:50 < Dark_Shikari> now you might notice some preprocessor commands here.
   2010-11-22 00:56:57 < Dark_Shikari> %assign, %rep, etc are preprocessor commands
   2010-11-22 00:57:04 < Dark_Shikari> so, first step: load E into r1d
   2010-11-22 00:57:09 < Dark_Shikari> "movzx" means "move, with zero extend"
   2010-11-22 00:57:15 < Dark_Shikari> movzx r1d, byte [r0-1]
   2010-11-22 00:57:20 < Dark_Shikari> in C this would be:
   2010-11-22 00:57:25 < Dark_Shikari> int r1d = r0[-1];
   2010-11-22 00:58:00 < Jumpyshoes> my C is a bit rusty, what does that do? does it just take the location in memory before r0[0]?
   2010-11-22 00:58:01 < Dark_Shikari> got that?
   2010-11-22 00:58:07 < Dark_Shikari> *(r0-1)
   2010-11-22 00:58:08 < Dark_Shikari> yes
   2010-11-22 00:58:14 < Dark_Shikari> [] is just a dereference of a pointer
   2010-11-22 00:58:23 < Jumpyshoes> ah
   2010-11-22 00:58:24 < Dark_Shikari> *(r0-1) = r0[-1] = (r0-1)[0]
   2010-11-22 00:58:51 < Dark_Shikari> So, here's what these 7 lines look like after the macro runs
   2010-11-22 00:58:53 < Kovensky> what is r0-1 in that ascii matrix?
   2010-11-22 00:59:09 < Dark_Shikari> E.
   2010-11-22 00:59:19 < Dark_Shikari>     movzx  r1d, byte [r0-1]
   2010-11-22 00:59:19 < Dark_Shikari>     movzx  r2d, byte [r0+FDEC_STRIDE*1-1]
   2010-11-22 00:59:19 < Dark_Shikari>     add    r1d, r2d
   2010-11-22 00:59:19 < Dark_Shikari>     movzx  r2d, byte [r0+FDEC_STRIDE*2-1]
   2010-11-22 00:59:19 < Dark_Shikari>     add    r1d, r2d
   2010-11-22 00:59:21 < Dark_Shikari>     movzx  r2d, byte [r0+FDEC_STRIDE*3-1]
   2010-11-22 00:59:24 < Dark_Shikari>     add    r1d, r2d
   2010-11-22 00:59:26 < Dark_Shikari> in order:
   2010-11-22 00:59:29 < Dark_Shikari> load E
   2010-11-22 00:59:31 < Dark_Shikari> load F
   2010-11-22 00:59:34 < Dark_Shikari> add F to E
   2010-11-22 00:59:36 < Dark_Shikari> load G
   2010-11-22 00:59:39 < Dark_Shikari> add G to E
   2010-11-22 00:59:41 < Dark_Shikari> load H
   2010-11-22 00:59:44 < Dark_Shikari> add H to E
   2010-11-22 00:59:47 < Dark_Shikari> any questions about that?
   2010-11-22 01:00:01 < Dark_Shikari> by the way, feel free to ask questions about WHY the code is like that, too, not just why it's correct.
   2010-11-22 01:00:23 < Jumpyshoes> i'm good so far
   2010-11-22 01:00:29 < Dark_Shikari> ok, now we have to do step 3
   2010-11-22 01:00:36 < Dark_Shikari> calculating A+B+C+D+E+F+G+H+4 >> 3
   2010-11-22 01:00:36 < Jumpyshoes> actually
   2010-11-22 01:00:42 < Jumpyshoes> where is n stored?
   2010-11-22 01:00:46 < Dark_Shikari> it isn't.
   2010-11-22 01:00:49 < Jumpyshoes> oh
   2010-11-22 01:00:53 < Dark_Shikari> It's a preprocessor variable.
   2010-11-22 01:00:56 < Jumpyshoes> oh, so it's like a macro?
   2010-11-22 01:00:58 < Dark_Shikari> Yes
   2010-11-22 01:00:59 < Dark_Shikari> It is a macro
   2010-11-22 01:01:00 < Kovensky> yes, it's a macro
   2010-11-22 01:01:06 < Jumpyshoes> that is handy
   2010-11-22 01:01:07 < Dark_Shikari> Note how I pasted the after-preprocessor code above.
   2010-11-22 01:01:11 < Jumpyshoes> yea
   2010-11-22 01:01:13 < Jumpyshoes> now i see
   2010-11-22 01:01:14 < Kovensky> everything starting with % in yasm syntax is a macro
   2010-11-22 01:01:14 < Dark_Shikari> No n left.
   2010-11-22 01:01:24 < Dark_Shikari> Now, so let's do step 3.
   2010-11-22 01:01:31 < Dark_Shikari> lea is the best non-simd opcode in x86
   2010-11-22 01:01:41 < Dark_Shikari> first, let's go over x86 addressing
   2010-11-22 01:01:45 < Dark_Shikari> what you can put inside the brackets is not infinite.
   2010-11-22 01:01:50 < Dark_Shikari> Here's the capabilities, specifically:
   2010-11-22 01:02:00 < Dark_Shikari> [REG1 + REG2 * {1,2,4,8} + CONST]
   2010-11-22 01:02:12 < Dark_Shikari> a register, plus another register * 1/2/4/8, plus a constant (positive or negative).
   2010-11-22 01:02:23 < Dark_Shikari> As you might note, this is pretty useful for accessing things like arrays
   2010-11-22 01:02:40 < Dark_Shikari> e.g. array[n+5], where array is an int array, would be
   2010-11-22 01:02:45 < Dark_Shikari> [array + n*4 + 20]
   2010-11-22 01:02:49 < Kovensky> I suppose the [r0+FDEC_STRIDE*n-1] bit gets simplified on assembly to [register + const]?
   2010-11-22 01:02:49 < Dark_Shikari> got that?
   2010-11-22 01:02:53 < Dark_Shikari> Kovensky: yes
   2010-11-22 01:02:58 < Dark_Shikari> yasm sums up constants for you.
   2010-11-22 01:03:00 < Jumpyshoes> yea, that's nice
   2010-11-22 01:03:10 < Dark_Shikari> so, as you might note, that's a pretty powerful addressing system.
   2010-11-22 01:03:16 < Dark_Shikari> That's more powerful than, say... "add".
   2010-11-22 01:03:24 < Dark_Shikari> So why not expose it in an instruction to let us use it for math?
   2010-11-22 01:03:26 < Dark_Shikari> So Intel did.
   2010-11-22 01:03:39 < Dark_Shikari> lea X, [expr] sets X equal to the value of expr.
   2010-11-22 01:03:42 < Dark_Shikari> just as fast as add.
   2010-11-22 01:03:55 < Dark_Shikari> so that lea does r1d = r1 + r3 + 4
   2010-11-22 01:04:07 < Jumpyshoes> wait, how does that work?
   2010-11-22 01:04:11 < Dark_Shikari> how does what work
   2010-11-22 01:04:23 < Jumpyshoes> so [] is addressing
   2010-11-22 01:04:28 < Dark_Shikari> yes
   2010-11-22 01:04:31 < Kovensky> lea runs the [REG1 + REG2 * {1,2,4,8} + CONST] math on its second argument and adds to the first
   2010-11-22 01:04:31 < Jumpyshoes> oh
   2010-11-22 01:04:33 < Dark_Shikari> lea doesn't actually address it
   2010-11-22 01:04:37 < Jumpyshoes> okay
   2010-11-22 01:04:40 < Dark_Shikari> It just calculates the result and stores it
   2010-11-22 01:04:42 < Dark_Shikari> instead of going to memory.
   2010-11-22 01:04:46 < Jumpyshoes> and it's faster than add?
   2010-11-22 01:04:50 < Dark_Shikari> It's just as fast
   2010-11-22 01:04:53 < Dark_Shikari> Except that you can do more with it.
   2010-11-22 01:04:58 < Kovensky> faster since you're doing 3 sums in one
   2010-11-22 01:05:02 < Kovensky> if you look it that way
   2010-11-22 01:05:04 < Jumpyshoes> o
   2010-11-22 01:05:05 < Jumpyshoes> true
   2010-11-22 01:05:06 < Kovensky> but cyclewise it's the same speed
   2010-11-22 01:05:06 < Dark_Shikari> now, technically, you can do more adds per cycle than lea, so you shouldn't go replacing all your adds with lea
   2010-11-22 01:05:14 < Kovensky> hm
   2010-11-22 01:05:17 < Dark_Shikari> But if you can use it to do more than one thing at a time, it's a big win.
   2010-11-22 01:05:26 < Dark_Shikari> So this lets us add r3, and add 4, in one op.
   2010-11-22 01:05:31 < Dark_Shikari> Got that
   2010-11-22 01:05:31 < Dark_Shikari> ?
   2010-11-22 01:05:33 < Jumpyshoes> yup
   2010-11-22 01:05:43 < Dark_Shikari> now shr r1d, 3: there's one that you can probably figure out yourself ;)
   2010-11-22 01:06:01 < Sean_McG> hm, shift halfword right?
   2010-11-22 01:06:05 < Dark_Shikari> just shift right
   2010-11-22 01:06:14 < Jumpyshoes> handy
   2010-11-22 01:06:18 < Jumpyshoes> why are we doing this?
   2010-11-22 01:06:25 < Dark_Shikari> doing what
   2010-11-22 01:06:28 < Jumpyshoes> shifting right
   2010-11-22 01:06:32 < Kovensky> it's part of the >>3 in the equation he gave during the description
   2010-11-22 01:06:37 < Jumpyshoes> right
   2010-11-22 01:06:39 < Kovensky> >>3 = /(2^3) = /8
   2010-11-22 01:06:50 < Dark_Shikari> DC prediction consists of averaging the pixels surrounding the block
   2010-11-22 01:06:52 < Dark_Shikari> using correct rounding
   2010-11-22 01:06:57 < Dark_Shikari> and then filling in the block with the result
   2010-11-22 01:07:04 < Dark_Shikari> hence A+B+C+D+E+F+G+H+4 >> 3
   2010-11-22 01:07:08 < Dark_Shikari> +4 for correct rounding
   2010-11-22 01:07:10 < Dark_Shikari>  >> 3 to divide
   2010-11-22 01:07:17 < Jumpyshoes> smart
   2010-11-22 01:07:25 < Dark_Shikari> now for the final part: storing the results
   2010-11-22 01:07:28 < Kovensky> the same trick as adding +0.5 to a float so you get it rounded when you cast to integer
   2010-11-22 01:07:37 < Dark_Shikari> imul r1d, 0x01010101
   2010-11-22 01:07:42 < Dark_Shikari> this is called a "splat" and you may have seen it in C as well
   2010-11-22 01:07:48 < Kovensky> splat? lol
   2010-11-22 01:07:48 < Dark_Shikari> we're turning an 8-bit value into 4x that value
   2010-11-22 01:07:51 < Dark_Shikari> e.g. A -> AAAAA
   2010-11-22 01:07:55 < Dark_Shikari> er, AAAA
   2010-11-22 01:07:58 < Jumpyshoes> i have never seen this before
   2010-11-22 01:08:08 < Jumpyshoes> how does this work?
   2010-11-22 01:08:09 < Dark_Shikari> so now we have a 32-bit register (r1d) with one copy of A in each 8-bit nibble of that register.
   2010-11-22 01:08:15 < Jumpyshoes> oh nevermind, i get it
   2010-11-22 01:08:17 < Dark_Shikari> A * 0x01010101 = A A A A
   2010-11-22 01:08:30 < Dark_Shikari> Now we go ahead and store this 4 times.
   2010-11-22 01:08:35 < Dark_Shikari> And we're done.
   2010-11-22 01:08:47 < Jumpyshoes> woah
   2010-11-22 01:08:51 < Dark_Shikari> Finally, we RET: x264 will automatically clean up after us.
   2010-11-22 01:09:03 < Kovensky> emms is only needed on sse code, right?
   2010-11-22 01:09:04 < Jumpyshoes> how much faster is this in asm than C?
   2010-11-22 01:09:10 < Dark_Shikari> Not much.
   2010-11-22 01:09:14 < Dark_Shikari> The only reason it's faster is psadbw.
   2010-11-22 01:09:23 < Dark_Shikari> Everything else is something GCC can do with properly written C.
   2010-11-22 01:09:34 < Dark_Shikari> I use it as an example because it's simple, and it mixes a lot of ideas in one function.
   2010-11-22 01:09:38 < Dark_Shikari> well, as a first example.
   2010-11-22 01:09:44 < Jumpyshoes> it does
   2010-11-22 01:09:57 < Jumpyshoes> so what's the point of having it in asm if it's only slightly faster?
   2010-11-22 01:09:57 < Dark_Shikari> It's probably 2-3 clocks faster at most.
   2010-11-22 01:10:00 < Dark_Shikari> Because we can.
   2010-11-22 01:10:02 < Dark_Shikari> lol
   2010-11-22 01:10:06 < Jumpyshoes> of course
   2010-11-22 01:10:09 < Jumpyshoes> this is open source
   2010-11-22 01:10:12 < Dark_Shikari> Because it probably took 5 minutes to write.
   2010-11-22 01:10:17 < Kovensky> isn't that a function that's called multiple times per frame too?
   2010-11-22 01:10:22 < Dark_Shikari> Kovensky: understatement
   2010-11-22 01:10:29 < Dark_Shikari> and this function only takes like 10 clocks
   2010-11-22 01:10:33 < Dark_Shikari> so saving 2 clocks is kind of meaningful there
   2010-11-22 01:10:34 < Dark_Shikari> (relatively)
   2010-11-22 01:10:42 < Kovensky> then yea, I guess 3 clocks per MB on a really hot function is worth it =p
   2010-11-22 01:10:53 < Dark_Shikari> anyways, that's a simple one.  Let's go on to some other concepts.
   2010-11-22 01:11:06 < Dark_Shikari> Throw any questions you ahve at me about this before we go.
   2010-11-22 01:11:34 < Jumpyshoes> are the preprocessor marcos in yasm or x264?
   2010-11-22 01:11:43 < Jumpyshoes> (also brb 1 minute)
   2010-11-22 01:11:49 < Dark_Shikari> x264 has its own macro system written in yasm
   2010-11-22 01:11:49 < Kovensky> they're in yasm
   2010-11-22 01:11:56 < Dark_Shikari> which handles stuff like arguments, pushing and popping of registers
   2010-11-22 01:12:00 < Dark_Shikari> and many more things which we will see soon
   2010-11-22 01:12:03 < Dark_Shikari> we call this "x264asm"
   2010-11-22 01:12:07 < Dark_Shikari> ffmpeg also uses this.
   2010-11-22 01:12:14 < Kovensky> wasn't it "pengvado asm"? :>
   2010-11-22 01:12:19 < Dark_Shikari> It's under a BSD license, so anyone in any project can and should use it to make their life less painful.
   2010-11-22 01:12:34 < Kovensky> or did you rename to "x264asm" after "pasm" was already taken? :p
   2010-11-22 01:12:47 < Dark_Shikari> bugmaster also wrote some of it
   2010-11-22 01:13:12 < Dark_Shikari> ok brb I'm grabbing some food
   2010-11-22 01:13:18 < Kovensky> right, the win64 part
   2010-11-22 01:14:12 < Jumpyshoes> okay back
   2010-11-22 01:14:15 < Jumpyshoes> whenever you're ready
   2010-11-22 01:15:13 < Jumpyshoes> i wonder how much of this i will retain
   2010-11-22 01:15:35 < j0sh> is this room logged somewhere?
   2010-11-22 01:15:44 < Jumpyshoes> well, my hard drive
   2010-11-22 01:15:59 < Kovensky> I have logs since ~2008 I think
   2010-11-22 01:18:43 < Dark_Shikari> pengvado logs this
   2010-11-22 01:18:52 < Dark_Shikari> Jumpyshoes: you don't need to retain individual instructions etc, you can look those up
   2010-11-22 01:18:59 < Dark_Shikari> ok, next
   2010-11-22 01:19:03 < Dark_Shikari> you may have noticed that psadbw is fucking awesome.
   2010-11-22 01:19:18 < Jumpyshoes> it does like 8 things in one
   2010-11-22 01:19:22 < Dark_Shikari> abs() is typically 4 instructions on x86
   2010-11-22 01:19:24 < Kovensky> 22:18.52 Dark_Shikari: Jumpyshoes: you don't need to retain individual instructions etc, you can look those up <-- indeed; you just need to know they exist so you know to look them up =p
   2010-11-22 01:19:33 < Dark_Shikari> psadbw does 8 subtracts
   2010-11-22 01:19:34 < Jumpyshoes> o
   2010-11-22 01:19:36 < Dark_Shikari> 8 absolute values on those results
   2010-11-22 01:19:40 < Dark_Shikari> and then adds them up
   2010-11-22 01:19:45 < Dark_Shikari> that's 8 + 32 + 7
   2010-11-22 01:19:46 < Jumpyshoes> that's a lot
   2010-11-22 01:19:48 < Dark_Shikari> 47 instructions in one
   2010-11-22 01:19:51 < Jumpyshoes> why is abs so slow?
   2010-11-22 01:19:51 < Dark_Shikari> (at least, 47 equivalent)
   2010-11-22 01:19:57 < Dark_Shikari> abs isn't slow, there's just no instructin for it
   2010-11-22 01:20:00 < Dark_Shikari> the typical algorithm is
   2010-11-22 01:20:03 < Dark_Shikari> int sign = x >> 31;
   2010-11-22 01:20:14 < Dark_Shikari> (x ^ sign) - sign;
   2010-11-22 01:20:20 < Dark_Shikari> this needs a mov on x86, so that's 4 instructions.
   2010-11-22 01:20:33 < Jumpyshoes> oh
   2010-11-22 01:20:46 < Jumpyshoes> okay
   2010-11-22 01:20:47 < Dark_Shikari> So psadbw is pretty awesome.
   2010-11-22 01:20:52 < Jumpyshoes> indeed
   2010-11-22 01:20:53 < Dark_Shikari> It's very awesome for doing what its name implies you should do with it
   2010-11-22 01:20:56 < Dark_Shikari> That is -- SADs
   2010-11-22 01:20:58 < Dark_Shikari> sum of absolute differences
   2010-11-22 01:21:05 < Dark_Shikari> so let's open sad-a.asm and hop down to line 95
   2010-11-22 01:21:17 < Dark_Shikari> also open common/pixel.c and look at the first function: SAD
   2010-11-22 01:21:23 < Dark_Shikari> This function is pretty simple.  You should be able to see how it works.
   2010-11-22 01:21:29 < Dark_Shikari> If you have any questions about its details, ask (the C, not the asm)
   2010-11-22 01:21:36 < Dark_Shikari> look only at the C for now.
   2010-11-22 01:21:51 < Jumpyshoes> pixel_sad_%1x%2_mmxext <-- you can have % in function names?
   2010-11-22 01:21:57 < Dark_Shikari> We'll get to that.
   2010-11-22 01:22:35 < Dark_Shikari> so as you'll notice, the C SAD has 7 different versions
   2010-11-22 01:22:40 < Dark_Shikari> for 16x16, 16x8, 8x16...
   2010-11-22 01:22:45 < Dark_Shikari> and it's instantiated via a macro.
   2010-11-22 01:23:18 < Jumpyshoes> okay, so for the C function
   2010-11-22 01:23:25 < Jumpyshoes> how do you pass the pix1 and i_stride_pix1 arguments?
   2010-11-22 01:23:33 < Dark_Shikari> One's a pointer, one's the stride.
   2010-11-22 01:23:35 < Dark_Shikari> They're just normal params.
   2010-11-22 01:23:52 < Dark_Shikari> the function has 4 parameters: two sources, two strides.
   2010-11-22 01:23:59 < Jumpyshoes> i mean, the define only has 3 parameters
   2010-11-22 01:24:03 < Kovensky> they come from image data
   2010-11-22 01:24:08 < Dark_Shikari> The define is defining things that ARENT parameters.
   2010-11-22 01:24:21 < Dark_Shikari> the name of the function
   2010-11-22 01:24:23 < Dark_Shikari> the width, and the height
   2010-11-22 01:24:25 < Kovensky> yes, the define just defines the name and the length of the sad
   2010-11-22 01:24:27 < Dark_Shikari> all those are HARDCODED upon compile time
   2010-11-22 01:24:34 < Jumpyshoes> oh
   2010-11-22 01:24:35 < Jumpyshoes> right
   2010-11-22 01:24:36 < Dark_Shikari> into 7 different versions of the function
   2010-11-22 01:24:38 < Dark_Shikari> with 7 different names.
   2010-11-22 01:24:50 < Jumpyshoes> right, i see
   2010-11-22 01:25:06 < Dark_Shikari> so, for our asm, we also need 7 versions
   2010-11-22 01:25:07 < Jumpyshoes> i haven't used defines extensively before, so you might get more stupid questions
   2010-11-22 01:25:13 < Dark_Shikari> that's fine, no such thing as stupid questions
   2010-11-22 01:25:19 < Dark_Shikari> and we also don't want to write the function 7 times, just like in the case of C we didn't.
   2010-11-22 01:25:21 < j0sh> only stupid mistakes :)
   2010-11-22 01:25:28 < Dark_Shikari> so in the asm, we define a macro
   2010-11-22 01:25:30 < Dark_Shikari> %macro SAD 2
   2010-11-22 01:25:30 < Kovensky> better than not ask and misunderstand everything
   2010-11-22 01:25:35 < Dark_Shikari> that means this macro has two paremeters.
   2010-11-22 01:25:43 < Jumpyshoes> oh, %1 and %2?
   2010-11-22 01:25:45 < Dark_Shikari> They are accessed as %1 and %2.
   2010-11-22 01:25:53 < Dark_Shikari> we call the macro 7 times, one for each size.
   2010-11-22 01:26:33 < Dark_Shikari> the function takes 4 args (as you'd expect)
   2010-11-22 01:26:36 < Dark_Shikari> and needs 4 regs (just the args)
   2010-11-22 01:26:41 < Jumpyshoes> and SAD_INC_2x%1P is another macro?
   2010-11-22 01:26:46 < Dark_Shikari> Yes, it's one of three macros
   2010-11-22 01:26:47 < Dark_Shikari> look above
   2010-11-22 01:26:53 < Dark_Shikari> each one does 2 rows worth of SAD
   2010-11-22 01:26:56 < Jumpyshoes> oh, cool
   2010-11-22 01:26:57 < Dark_Shikari> for width 4, width 8, and width 16.
   2010-11-22 01:27:02 < Dark_Shikari> so it picks the right one based on the width
   2010-11-22 01:27:07 < Dark_Shikari> and it %reps it based on the height
   2010-11-22 01:27:10 < Kovensky> punpckldq <-- cute instruction name
   2010-11-22 01:27:34 < Dark_Shikari> now, start analyzing the 3 macros above (the sad macros) and trying to figure out how they work.
   2010-11-22 01:27:37 < Dark_Shikari> ask questions.
   2010-11-22 01:27:53 < Dark_Shikari> note mm0 is the accumulator
   2010-11-22 01:27:56 < Dark_Shikari> which is why it's zeroed at the start.
   2010-11-22 01:27:58 < Jumpyshoes> the order of args is the same as in the C function?
   2010-11-22 01:28:01 < Dark_Shikari> yes
   2010-11-22 01:28:04 < Jumpyshoes> kk
   2010-11-22 01:28:20 < Jumpyshoes> what does punpckldq do?
   2010-11-22 01:28:24 < Kovensky> ^
   2010-11-22 01:28:30 < Dark_Shikari> good question!
   2010-11-22 01:28:39 < Dark_Shikari> punpck is a set of instructions that interleave their arguments in some fashion.
   2010-11-22 01:28:47 < Dark_Shikari> to start with, it can be l or h
   2010-11-22 01:28:48 < Dark_Shikari> low or high
   2010-11-22 01:29:01 < Dark_Shikari> so punpckl__ ABCD, EFGH will use AB and EF.
   2010-11-22 01:29:07 < Dark_Shikari> And punpbkh__ ABCD, EFGH will use CD and GH.
   2010-11-22 01:29:19 < Kovensky> hurf, little endian
   2010-11-22 01:29:20 < Dark_Shikari> the next two letters are the source size, and destination size.
   2010-11-22 01:29:26 < Dark_Shikari> for example, punpcklbw interleaves bytes, to create words.
   2010-11-22 01:29:36 < Dark_Shikari> So punpcklbw ABCD, EFGH gives you AEBF.
   2010-11-22 01:29:51 < Jumpyshoes> oh, okay
   2010-11-22 01:29:53 < Dark_Shikari> if the letters are bytes.
   2010-11-22 01:30:07 < Dark_Shikari> so punpckldq ABCDEFGH, IJKLMNOP
   2010-11-22 01:30:12 < Dark_Shikari> gives us ABCDIJKL
   2010-11-22 01:30:23 < Dark_Shikari> so in other words, it stuffs the two sets of 4 bytes we just loaded into one register.
   2010-11-22 01:30:26 < Dark_Shikari> So we can do only one SAD, instead of two.
   2010-11-22 01:30:43 < Dark_Shikari> punpcklbw ABCD0000, EFGH0000 --> ABCDEFGH
   2010-11-22 01:30:47 < Dark_Shikari> er, punpckldq
   2010-11-22 01:31:02 < Dark_Shikari> so it effectively concatenates mm1 and mm2 for us.
   2010-11-22 01:31:16 < Dark_Shikari> if we didn't do this, we'd have to do twice as many sads and adds.
   2010-11-22 01:31:42 < Dark_Shikari> we do this because the registers are width 8, but our sad is width 4.
   2010-11-22 01:31:50 < Dark_Shikari> So we need to stuff sad information side by side to fill the whole reg.
   2010-11-22 01:32:31 < Jumpyshoes> why are we punpckldq'ing the [r0+r1] and not [r0]?
   2010-11-22 01:32:41 < Jumpyshoes> oh wait, nevermind
   2010-11-22 01:32:59 < Dark_Shikari> we're concatenating row 0 and row 1
   2010-11-22 01:33:02 < Dark_Shikari> of each input.
   2010-11-22 01:33:06 < Kovensky> so the punpckldq does mm1 = mm1 & 0xFFFF<<16 | [src+stride]>>16?
   2010-11-22 01:33:30 < Dark_Shikari> no, each input is 32 bits
   2010-11-22 01:33:30 < Dark_Shikari> not 16
   2010-11-22 01:33:38 < Kovensky> orz
   2010-11-22 01:33:40 < Dark_Shikari> low 32 of src1, low 32 of src2, combine to make 64 bit output
   2010-11-22 01:33:44 < Kovensky> it's the same idea though right?
   2010-11-22 01:33:59 < Dark_Shikari> not really, it doesn't right shift anything
   2010-11-22 01:34:14 < Kovensky> hm
   2010-11-22 01:34:18 < Kovensky> me failing at bit math here
   2010-11-22 01:34:28 < Jumpyshoes> lea     r0,     [r0+2*r1] <-- why are we doing this step?
   2010-11-22 01:34:42 < Jumpyshoes> doesn't it move r0 over 2*r1?
   2010-11-22 01:34:49 < Dark_Shikari> btw Jumpyshoes http://alien.dowling.edu/~rohit/nasmdocb.html
   2010-11-22 01:34:59 < Jumpyshoes> and change the arg?
   2010-11-22 01:34:59 < Dark_Shikari> Jumpyshoes: we're incrementing the pointer by 2*stride
   2010-11-22 01:35:12 < Jumpyshoes> does the C code do that?
   2010-11-22 01:35:13 < Kovensky> you can do whatever you want with the arc
   2010-11-22 01:35:14 < Kovensky> arg*
   2010-11-22 01:35:21 < Jumpyshoes> oh, the rep
   2010-11-22 01:36:02 < Jumpyshoes> okay, i get what SAD_INC_2x4P
   2010-11-22 01:36:03 < Jumpyshoes> woohoo
   2010-11-22 01:36:11 < Dark_Shikari> the others work similarly
   2010-11-22 01:36:15 < Dark_Shikari> except without the punpck magic
   2010-11-22 01:36:17 < Dark_Shikari> because they don't need it.
   2010-11-22 01:36:35 < Jumpyshoes> wait, why is the lea out of order in SAD_INC_2x8P?
   2010-11-22 01:36:43 < Jumpyshoes> by out of order i mean not next to each other
   2010-11-22 01:36:44 < Kovensky> I'm still finishing 2x4...
   2010-11-22 01:36:46 < Dark_Shikari> No particular reason.
   2010-11-22 01:36:50 < Kovensky> k, got it
   2010-11-22 01:36:52 < Jumpyshoes> oh, okay
   2010-11-22 01:38:10 < Dark_Shikari> http://alien.dowling.edu/~rohit/nasmdocb.html have this open in another window for reference
   2010-11-22 01:38:13 < Dark_Shikari> very very useful
   2010-11-22 01:38:19 < Jumpyshoes> yea, have it open
   2010-11-22 01:38:37 < Jumpyshoes> so we rep the SAD for however many times so the 2x%1 is completed?
   2010-11-22 01:39:03 < Dark_Shikari> yes
   2010-11-22 01:39:03 < Kovensky> well, the SADs work in two rows at a time
   2010-11-22 01:39:08 < Dark_Shikari> so if it's height 8
   2010-11-22 01:39:10 < Dark_Shikari> we rep it 4 times
   2010-11-22 01:39:12 < Dark_Shikari> 4*2 = 8
   2010-11-22 01:39:13 < Kovensky> so you just need to do for rows/2 times
   2010-11-22 01:39:24 < Jumpyshoes> ah
   2010-11-22 01:39:40 < Kovensky> I dunno if I understood 2x8 / 2x16 or not; I have no questions about them but I also doubt that I'll remember this after a day
   2010-11-22 01:39:51 < Jumpyshoes> movq    mm2,    [r0+8] <-- why are we adding the 8?
   2010-11-22 01:40:03 < Jumpyshoes> if it's movq
   2010-11-22 01:40:20 < Kovensky> Jumpyshoes: because it's working now on 2 "columns" of 8 bytes each
   2010-11-22 01:40:31 < Jumpyshoes> oh, right
   2010-11-22 01:40:37 < Kovensky> Dark_Shikari: why are strides not hardcoded btw?
   2010-11-22 01:41:05 < Dark_Shikari> Kovensky: SAD can be called on a reference frame
   2010-11-22 01:41:08 < Dark_Shikari> thus variable stride
   2010-11-22 01:41:37 < Kovensky> I don't really get it but then I'd have to study more of x264 to know the reference frame memory layout
   2010-11-22 01:41:47 < Kovensky> oh wait
   2010-11-22 01:41:50 < Kovensky> I got it now lol
   2010-11-22 01:41:54 < Dark_Shikari> it's called on frames, as opposed to some temporary block of memory =p
   2010-11-22 01:42:26 < Jumpyshoes> okay, i think i understand the SAD_INC_* functions now
   2010-11-22 01:42:31 < Dark_Shikari> now, for the kicker
   2010-11-22 01:42:33 < Jumpyshoes> and the SAD
   2010-11-22 01:42:41 < Dark_Shikari> the 16x16 SAD function declared here is 15 times faster than C.
   2010-11-22 01:42:45 < Jumpyshoes> wat
   2010-11-22 01:43:13 < Jumpyshoes> why is it so much faster?
   2010-11-22 01:43:18 < Dark_Shikari> psadbw
   2010-11-22 01:43:33 < Jumpyshoes> oh, because you're doing the abs in the C function
   2010-11-22 01:44:24 < Jumpyshoes> okay, that is pretty awesome
   2010-11-22 01:44:40 < Dark_Shikari> now let's get a bit to how we measure performance
   2010-11-22 01:44:46 < Dark_Shikari> for any asm instruction, there are three things that matter
   2010-11-22 01:44:56 < Dark_Shikari> latency, inverse throughput, and execution units
   2010-11-22 01:45:05 < Dark_Shikari> the first two are represented like this
   2010-11-22 01:45:06 < Dark_Shikari> "3/1"
   2010-11-22 01:45:07 < Kovensky> inverse throughput?
   2010-11-22 01:45:15 < Dark_Shikari> this means a psadbw takes 3 clocks to finish from when it's started
   2010-11-22 01:45:19 < Dark_Shikari> and you can do one of them per cycle.
   2010-11-22 01:45:30 < Jumpyshoes> okay, what are all three? <_<
   2010-11-22 01:45:41 < Dark_Shikari> another example is "mov"
   2010-11-22 01:45:48 < Dark_Shikari> mov between two registers is 1/0.33
   2010-11-22 01:45:53 < Dark_Shikari> takes 1 cycle, and you can do 3 per clock.
   2010-11-22 01:45:56 < Dark_Shikari> execution unit usage is a bit trickier.
   2010-11-22 01:46:03 < Dark_Shikari> Not all execution units can do all instructions.
   2010-11-22 01:46:11 < Dark_Shikari> Intel chips have 6 execution units:
   2010-11-22 01:46:14 < Dark_Shikari> p0, p1, p2, p3, p4, p5
   2010-11-22 01:46:15 < Jumpyshoes> wait, what is latency?
   2010-11-22 01:46:20 < Dark_Shikari> time from start to finish, in clocks
   2010-11-22 01:46:24 < Jumpyshoes> and inverse throughput and execution units
   2010-11-22 01:46:33 < Dark_Shikari> inverse throughput is how many you can do per clock.
   2010-11-22 01:46:41 < Dark_Shikari> execution units are the things in the chip that do stuff.
   2010-11-22 01:46:41 < Jumpyshoes> oh
   2010-11-22 01:46:53 < Dark_Shikari> of these 6 execution units, three can do math: p0, p1, p5.
   2010-11-22 01:47:02 < Dark_Shikari> psadbw, for example, can only use one of these (p1)
   2010-11-22 01:47:06 < Dark_Shikari> pxor can use all three
   2010-11-22 01:47:08 < Dark_Shikari> and so forth
   2010-11-22 01:47:18 < Dark_Shikari> generally execution units aren't important until you get into serious optimizing
   2010-11-22 01:47:24 < Dark_Shikari> but they can often affect the best instruction choices
   2010-11-22 01:47:31 < Dark_Shikari> for example, if an execution unit is sitting around doing nothing for a whole function.
   2010-11-22 01:47:48 < Dark_Shikari> the instruction tables sheet here http://agner.org/optimize/ has all the information on latency, execution units, and inverse throughput
   2010-11-22 01:47:52 < Dark_Shikari> for a wide variety of CPUs
   2010-11-22 01:48:26 < Kovensky> I suppose AMD are roughly the same, for compatibility?
   2010-11-22 01:48:28 < Jumpyshoes> how about branching? i heard branching fucks you
   2010-11-22 01:48:35 < Dark_Shikari> not generally unless it's unpredictable
   2010-11-22 01:48:41 < Kovensky> branch mispredictions do
   2010-11-22 01:48:45 < Dark_Shikari> we can get to a case of that later if you want.
   2010-11-22 01:48:51 < Dark_Shikari> now, let's just analyze SAD.
   2010-11-22 01:48:57 < Dark_Shikari> suppose we want to analyze the 8x8 SAD
   2010-11-22 01:49:02 < Dark_Shikari> in this function we do:
   2010-11-22 01:49:03 < Dark_Shikari> 8 SADs
   2010-11-22 01:49:07 < Dark_Shikari> 8 adds (accumulates)
   2010-11-22 01:49:09 < Dark_Shikari> 16 loads
   2010-11-22 01:49:34 < Dark_Shikari> plus the start, end, and calling overhead
   2010-11-22 01:49:44 < Dark_Shikari> 8 SADs: takes 8 cycles (inverse throughput of 1)
   2010-11-22 01:49:54 < Dark_Shikari> 8 adds: takes 8 cycles (inverse throughput of 1), and can run at the same time as SADs
   2010-11-22 01:50:01 < Dark_Shikari> 16 loads: takes 16 cycles, and can run at the same time as the above.
   2010-11-22 01:50:04 < Dark_Shikari> So the loads are the bottleneck.
   2010-11-22 01:50:13 < Dark_Shikari> This is an important thing to understand: it's possible for one type of operation to bottleneck a function.
   2010-11-22 01:50:19 < Dark_Shikari> Loads are a common example.
   2010-11-22 01:50:34 < Dark_Shikari> In this case, SAD is *so fast* that it is effectively free, as we're sitting around waiting for loads the whole time.
   2010-11-22 01:50:47 < Jumpyshoes> oh.
   2010-11-22 01:50:56 < Dark_Shikari> the actual runtime of the function is about 22 clocks.
   2010-11-22 01:51:02 < Dark_Shikari> Which is fitting for 16 + start + end + overhead.
   2010-11-22 01:51:20 < Dark_Shikari> so that's some basic performance analysis for you.
   2010-11-22 01:51:29 < Jumpyshoes> is there anything that does this automatically for you?
   2010-11-22 01:51:30 < Dark_Shikari> How long the function should take in theory, how long each instruction takes in theory, and how you can be bottlenecked.
   2010-11-22 01:51:36 < Dark_Shikari> analysis?  not really.
   2010-11-22 01:51:43 < Dark_Shikari> There are intel performance counters and such on the chip
   2010-11-22 01:51:46 < Dark_Shikari> but they're not magic
   2010-11-22 01:51:53 < Dark_Shikari> It might be useful to have some kind of tool to analyze asm functions
   2010-11-22 01:52:08 < Jumpyshoes> ah
   2010-11-22 01:52:25 < Dark_Shikari> in general though, intuition is a powerful tool.
   2010-11-22 01:53:02 < Jumpyshoes> i see
   2010-11-22 01:53:15 < Dark_Shikari> so let's move on to some examples of powerful x264 macros.
   2010-11-22 01:53:45 < Jumpyshoes> cool
   2010-11-22 01:53:46 < Dark_Shikari> actualyl, let's start with something simpler
   2010-11-22 01:53:49 < Dark_Shikari> pixel_avg2_w16_sse2
   2010-11-22 01:53:51 < Dark_Shikari> mc-a.asm
   2010-11-22 01:53:54 < Dark_Shikari> find it, ping me when you have
   2010-11-22 01:54:19  * Kovensky found it
   2010-11-22 01:54:27 < Jumpyshoes> found it
   2010-11-22 01:55:20 < Dark_Shikari> ok, so this function interpolates between two inputs, and outputs to an output
   2010-11-22 01:55:31 < Dark_Shikari> the interpolation is the simplest possible
   2010-11-22 01:55:33 < Dark_Shikari> (A+B+1)>>1
   2010-11-22 01:55:56 < Dark_Shikari> look at the function signature above
   2010-11-22 01:55:59 < Dark_Shikari> ; void pixel_avg2_w4( uint8_t *dst, int dst_stride,
   2010-11-22 01:55:59 < Dark_Shikari> etc
   2010-11-22 01:56:12 < Dark_Shikari> so this function takes inputs from src1 and src2, averages them together, and writes to dst
   2010-11-22 01:56:16 < Dark_Shikari> src1 and src2 have src_stride
   2010-11-22 01:56:19 < Dark_Shikari> and dst has dst_stride.
   2010-11-22 01:56:20 < Dark_Shikari> got it?
   2010-11-22 01:56:50 < Jumpyshoes> what's the height?
   2010-11-22 01:57:12 < Dark_Shikari> how many lines to interpolate.
   2010-11-22 01:57:17 < Jumpyshoes> ah
   2010-11-22 01:58:29 < Dark_Shikari> now this function uses xmm registers (128-bit)
   2010-11-22 01:58:31 < Dark_Shikari> so it does 16 bytes at a time
   2010-11-22 01:58:44 < Dark_Shikari> all 128-bit loads must be aligned unless movdqu is used.
   2010-11-22 01:58:50 < Dark_Shikari> since our inputs are aligned, this is a lot of movdqu.
   2010-11-22 01:58:54 < Dark_Shikari> er, are unaligned
   2010-11-22 01:59:05 < Jumpyshoes> and what does movdqu do?
   2010-11-22 01:59:18 < Dark_Shikari> loads 128 bits from an unaligned source
   2010-11-22 01:59:28 < Jumpyshoes> ah
   2010-11-22 01:59:33 < Kovensky> why sub r2 from r4?
   2010-11-22 01:59:40 < Dark_Shikari> ah, now here's a fun trick
   2010-11-22 01:59:47 < Dark_Shikari> we need to increment three pointers, right?
   2010-11-22 01:59:50 < Jumpyshoes> yea, aren't you subtracting addressses?
   2010-11-22 01:59:51 < Dark_Shikari> src1, src2, dst
   2010-11-22 01:59:58 < Dark_Shikari> But src1 and src2 have the same stride.
   2010-11-22 02:00:03 < Dark_Shikari> So they're being incremented by the same amount.
   2010-11-22 02:00:11 < Dark_Shikari> So we can take src2 and represent it as an offset from src1.
   2010-11-22 02:00:14 < Dark_Shikari> Then we only have to increment src1.
   2010-11-22 02:00:18 < Dark_Shikari> One lea removed per iteration, bam.
   2010-11-22 02:00:28 < Kovensky> and use r6 as the offset + stride?
   2010-11-22 02:00:47 < Dark_Shikari> yes
   2010-11-22 02:01:31 < Jumpyshoes> that is a nice trick
   2010-11-22 02:01:52 < Dark_Shikari> so look through that function and see if there's anything you don't know about
   2010-11-22 02:01:53 < Dark_Shikari> and ask questions.
   2010-11-22 02:02:16 < Jumpyshoes> god how do you keep track of which argument is which
   2010-11-22 02:02:33 < Kovensky> I copied the description from w4
   2010-11-22 02:02:37 < Kovensky> and annotated it
   2010-11-22 02:02:45 < Kovensky> ; void pixel_avg2_w4( uint8_t *dst (r0), int dst_stride (r1),
   2010-11-22 02:02:48 < Kovensky> ;                     uint8_t *src1 (r2), int src_stride (r3),
   2010-11-22 02:02:51 < Kovensky> ;                     uint8_t *src2 (r4), int height (r5) );
   2010-11-22 02:02:55 < Jumpyshoes> good idea
   2010-11-22 02:03:04 < Dark_Shikari> Jumpyshoes: we have a system I'll show you later that helps you keep track of registers.
   2010-11-22 02:03:13 < Dark_Shikari> or, well, makes it easier to.
   2010-11-22 02:03:41 < Jumpyshoes> pavgb i assume does some sort of averagiing?
   2010-11-22 02:04:04 < Dark_Shikari> yes, (A+B+1)>>1 for each pair of input pixels
   2010-11-22 02:04:26 < Jumpyshoes> http://www.tommesani.com/SSEPrimer.html ooh this has pretty diagrams
   2010-11-22 02:04:43 < Kovensky> that one was easy to read, but I didn't bother much about u vs a
   2010-11-22 02:04:55 < Jumpyshoes> movdqa - mov dq to aligned?
   2010-11-22 02:05:13 < Dark_Shikari> same as movdqu, except for aligned
   2010-11-22 02:05:36 < Jumpyshoes> ah
   2010-11-22 02:05:46 < Dark_Shikari> the output is always aligned, as we control it
   2010-11-22 02:05:52 < Dark_Shikari> the input is an arbitrary pointer into a reference frame
   2010-11-22 02:05:54 < Dark_Shikari> and so it could be anything.
   2010-11-22 02:05:56 < Jumpyshoes> hoho one of the four billion jumps that exists in x86
   2010-11-22 02:06:04 < Dark_Shikari> jump if greater than
   2010-11-22 02:06:07 < Jumpyshoes> jump greater?
   2010-11-22 02:06:16 < Dark_Shikari> so if r5d > 0
   2010-11-22 02:06:18 < Jumpyshoes> ah
   2010-11-22 02:06:35 < Jumpyshoes> so why two?
   2010-11-22 02:06:44 < Dark_Shikari> it handles two rows at a time.
   2010-11-22 02:06:46 < Jumpyshoes> oh, right
   2010-11-22 02:07:04 < Kovensky> hm
   2010-11-22 02:07:14 < Kovensky> movdq moves doublequads
   2010-11-22 02:07:21 < Kovensky> but the registers are only quads
   2010-11-22 02:07:28 < Kovensky> unless on 64bit
   2010-11-22 02:07:32 < Kovensky> so what does it do
   2010-11-22 02:07:36 < Jumpyshoes> xmm2 is 128, isn't it?
   2010-11-22 02:07:37 < Kovensky> oh wait, not registers, memory addresses
   2010-11-22 02:07:43 < Kovensky> failed there
   2010-11-22 02:07:52 < Jumpyshoes> i thought it pads 0s
   2010-11-22 02:07:58 < Dark_Shikari> all the moves here are 128-bit
   2010-11-22 02:07:59 < Dark_Shikari> so there's no padding
   2010-11-22 02:08:11 < Kovensky> no, it moves 128bits from wherever the registers point to xmm / viceversa
   2010-11-22 02:08:24 < Jumpyshoes> ah, right
   2010-11-22 02:08:29 < Kovensky> I was failing just now and reading as if it was moving the register contents to xmm
   2010-11-22 02:09:20 < Jumpyshoes> okay, this is pretty awesome
   2010-11-22 02:09:26 < Jumpyshoes> except i have a headache now
   2010-11-22 02:09:37 < wipple> Dark_Shikari: i fixed configure --> http://cccp.project357.com/p/f1860e321
   2010-11-22 02:09:46 < wipple> any other good way to fix?
   2010-11-22 02:10:13 < Dark_Shikari> wipple: if it works, I'm fine with it.  you want to package that with an updated version of your other patch?
   2010-11-22 02:10:38 < wipple> Dark_Shikari: http://cccp.project357.com/p/f3c6e06e4
   2010-11-22 02:11:04 < Kovensky> Dark_Shikari: how faster is the SSE2 version of this func compared to C
   2010-11-22 02:11:53 < Dark_Shikari> wipple: applied
   2010-11-22 02:12:03 < Dark_Shikari> Kovensky: about 11 times faster
   2010-11-22 02:12:20 < Jumpyshoes> holy crap
   2010-11-22 02:12:59 < Jumpyshoes> okay, i think i get it
   2010-11-22 02:13:27 < Dark_Shikari> also, the REP_RET  you might have been wondering about
   2010-11-22 02:13:33 < Dark_Shikari> in short, if you have a RET after a jump, use REP_RET.
   2010-11-22 02:13:36 < Dark_Shikari> Blame AMD.
   2010-11-22 02:13:51 < Jumpyshoes> oh
   2010-11-22 02:13:54 < Kovensky> REP_RET is one of x86inc's macros I suppose
   2010-11-22 02:14:35 < Jumpyshoes> i sure hope these GCI tasks are easy
   2010-11-22 02:14:48 < Jumpyshoes> but in other news, this is pretty cool
   2010-11-22 02:14:50 < Kovensky> they are once you get the hang of it
   2010-11-22 02:14:54 < Jumpyshoes> how optimized this can get
   2010-11-22 02:14:58 < Kovensky> since you just need to take any silly function
   2010-11-22 02:15:00 < Kovensky> and write asm for it
   2010-11-22 02:15:11 < Kovensky> if I had merged x264-audio already, you could write asm for my resampler lol
   2010-11-22 02:15:18 < Kovensky> atm it's pure C
   2010-11-22 02:15:24 < Kovensky> er
   2010-11-22 02:15:31 < Kovensky> s/resample/sample format converter/
   2010-11-22 02:15:38 < Dark_Shikari> so, now let's look at some horrible macro abuse
   2010-11-22 02:15:38 < Jumpyshoes> ah
   2010-11-22 02:15:38 < Kovensky> +r
   2010-11-22 02:15:41 < Jumpyshoes> derp
   2010-11-22 02:15:56 < Dark_Shikari> dct-a.asm
   2010-11-22 02:15:59 < Dark_Shikari> cglobal add4x4_idct_mmx, 2,2
   2010-11-22 02:16:02 < Dark_Shikari> this does an inverse DCT
   2010-11-22 02:16:09 < Dark_Shikari> steps:
   2010-11-22 02:16:12 < Dark_Shikari> 1.  Load dct coeffs.
   2010-11-22 02:16:14 < Dark_Shikari> 2.  1D IDCT.
   2010-11-22 02:16:17 < Dark_Shikari> 2.  Transpose.
   2010-11-22 02:16:19 < Dark_Shikari> *3.
   2010-11-22 02:16:22 < Dark_Shikari> 4.  1D IDCT.
   2010-11-22 02:16:33 < Dark_Shikari> 5.  Load pixels, add idct output, clamp, store.
   2010-11-22 02:16:44 < Dark_Shikari> You might notice that this function looks curiously simple!
   2010-11-22 02:16:47 < Kovensky> the IDCT macro itself is probably cute
   2010-11-22 02:16:54 < Jumpyshoes> what does transpose do?
   2010-11-22 02:17:05 < Dark_Shikari> Exactly what you think it does.
   2010-11-22 02:17:06 < Kovensky> just a regular matrix transpose
   2010-11-22 02:17:19 < Jumpyshoes> isn't it 1D though?
   2010-11-22 02:17:27 < Kovensky> no, the source is 2D
   2010-11-22 02:17:32 < Kovensky> but the IDCT is 1D
   2010-11-22 02:17:34 < Jumpyshoes> oh, it is
   2010-11-22 02:17:52 < Kovensky> however, if you do it on the matrix on both orientations, it works like a 2D IDCT... somehow...
   2010-11-22 02:17:58 < Kovensky> idk the maths behind it lol
   2010-11-22 02:18:00 < Dark_Shikari> it's called a "separable transform"
   2010-11-22 02:18:08 < Dark_Shikari> it means you can do a 2D transform by doing two 1D transforms
   2010-11-22 02:18:09 < Dark_Shikari> one in each direction
   2010-11-22 02:18:12 < Dark_Shikari> the transform is designed that way.
   2010-11-22 02:18:24 < Jumpyshoes> right, works like the DCT derp derp
   2010-11-22 02:18:29 < Kovensky> is that specific of the HCT or has always been part of the DCT
   2010-11-22 02:18:40 < Jumpyshoes> concentrates the energy and shit woohoo
   2010-11-22 02:18:47 < Dark_Shikari> now notice how simple it is.
   2010-11-22 02:18:57 < Kovensky> I know nothing about the DCT, and I've read the wikipedia page like 5 times ._.
   2010-11-22 02:18:57 < Dark_Shikari> Macros hide all the complexity in little manageable chunks.
   2010-11-22 02:19:03 < Jumpyshoes> well, you're calling IDCT4_1D
   2010-11-22 02:19:06 < Dark_Shikari> Which can be edited separately.
   2010-11-22 02:19:16 < Kovensky> ,skip_prologue?
   2010-11-22 02:19:27 < Dark_Shikari> Kovensky: there are functions that call this, and have already set up the registers
   2010-11-22 02:19:30 < Dark_Shikari> so they jump directly to the start
   2010-11-22 02:19:34 < Dark_Shikari> instead of the init part
   2010-11-22 02:19:42 < Dark_Shikari> *asm functions that call this
   2010-11-22 02:19:49 < Kovensky> I see
   2010-11-22 02:19:53 < Dark_Shikari> Now, here's the fun part
   2010-11-22 02:19:53 < Kovensky> cheaters
   2010-11-22 02:19:54 < Kovensky> :P
   2010-11-22 02:20:07 < Dark_Shikari> IDCT and transpose are both composed of submacros and so on
   2010-11-22 02:20:12 < Jumpyshoes> oh god
   2010-11-22 02:20:17 < Dark_Shikari> for example
   2010-11-22 02:20:21 < Dark_Shikari> a transpose is a series of BUTTERFLY operations
   2010-11-22 02:20:23 < Dark_Shikari> see x86util.asm
   2010-11-22 02:20:26 < Dark_Shikari> it's actually pretty simple
   2010-11-22 02:20:33 < Kovensky> BUTTERFLY?
   2010-11-22 02:21:02 < Dark_Shikari> the catch is that in many cases, these macros output to different registers than they input from
   2010-11-22 02:21:11 < Dark_Shikari> so, in a crappy asm language, yo'ud have to track every single register manually
   2010-11-22 02:21:15 < Dark_Shikari> which would make you go batshit insane
   2010-11-22 02:21:16 < Jumpyshoes> argh
   2010-11-22 02:21:30 < Jumpyshoes> i hope there's a way around this
   2010-11-22 02:21:52 < Kovensky> why is the butterfly named butterfly
   2010-11-22 02:21:59 < Dark_Shikari> Jumpyshoes: But...
   2010-11-22 02:21:59 < Jumpyshoes> that too
   2010-11-22 02:22:09 < Dark_Shikari> in x264asm, you can do this:
   2010-11-22 02:22:12 < Dark_Shikari> SWAP 2,3
   2010-11-22 02:22:15 < Dark_Shikari> now m2 and m3 are swapped.
   2010-11-22 02:22:16 < Dark_Shikari> From now on.
   2010-11-22 02:22:22 < Dark_Shikari> It's the same as exchanging those registers' values.
   2010-11-22 02:22:25 < Dark_Shikari> But done without any ops.
   2010-11-22 02:22:30 < Dark_Shikari> Because it swaps all future uses of those registers.
   2010-11-22 02:22:41 < Dark_Shikari> Thus you offload the task of tracking registers to the assembler.
   2010-11-22 02:22:42 < Kovensky> now that's evil macro usage
   2010-11-22 02:22:50 < j0sh> Kovensky: because the swaps look like a butterfly https://secure.wikimedia.org/wikipedia/en/wiki/Butterfly_diagram
   2010-11-22 02:22:50 < Jumpyshoes> that is awesome
   2010-11-22 02:22:59 < Dark_Shikari> "m0, m1, m2" are aliased to mm0, mm1, mm2 etc if INIT_MMX is set
   2010-11-22 02:23:07 < Dark_Shikari> and xmm0, xmm1, xmm2... if INIT_XMM is set.
   2010-11-22 02:23:15 < Dark_Shikari> and mmsize is 8 in the former case, 16 in the latter.
   2010-11-22 02:23:19 < Kovensky> yeah, was about to ask what the m%d were
   2010-11-22 02:23:20 < Dark_Shikari> So you can declare a single function
   2010-11-22 02:23:27 < Dark_Shikari> then initialize it for both mmx and sse!
   2010-11-22 02:23:28 < Dark_Shikari> in one go!
   2010-11-22 02:23:58 < Dark_Shikari> here's a simple example: denoise, in quant-.asm
   2010-11-22 02:24:01 < Dark_Shikari> line 748
   2010-11-22 02:24:09 < Dark_Shikari> it loops over the coefficients in a dct block and denoises them
   2010-11-22 02:24:13 < Kovensky> why are the movqs in a weird order?
   2010-11-22 02:24:19 < Dark_Shikari> it's initted for both mmx and sse trivially
   2010-11-22 02:24:20 < Kovensky> on add4x4_idct
   2010-11-22 02:24:22 < Jumpyshoes> wait, where is it?
   2010-11-22 02:24:41 < Dark_Shikari> quant-a.asm
   2010-11-22 02:24:47 < Dark_Shikari> Kovensky: that's the order they're used
   2010-11-22 02:24:52 < Dark_Shikari> so it's a bit faster to do it that way
   2010-11-22 02:25:16 < Kovensky> so it's about the execution unit optimization I guess
   2010-11-22 02:25:20 < Dark_Shikari> no, just ordering
   2010-11-22 02:25:29 < Dark_Shikari> the cpu generally doesn't reorder loads/stores that much
   2010-11-22 02:25:29 < Jumpyshoes> oh, is there an updated version of x264?
   2010-11-22 02:25:36 < Dark_Shikari> git pull
   2010-11-22 02:25:37 < Jumpyshoes> cause 748 for me is     bsf   ecx, r3
   2010-11-22 02:25:38 < Dark_Shikari> now you have the latest
   2010-11-22 02:25:59 < Dark_Shikari> btw, add_idct_mmx 4x4 is about ~5.8x faster than c
   2010-11-22 02:26:17 < Kovensky> 748 is on zigzag_scan for me...
   2010-11-22 02:26:19  * Kovensky goes pull
   2010-11-22 02:26:47 < Dark_Shikari> 788-798 is were we init three copies of this function
   2010-11-22 02:26:50 < Dark_Shikari> mmx, sse2, and ssse3.
   2010-11-22 02:26:58 < Dark_Shikari> for mmx vs sse2, we just change from INIT_MMX to INIT_XMM
   2010-11-22 02:27:09 < Dark_Shikari> for sse2 vs ssse3, we change PABSW and PSIGNW to use the pabsw and psignw instructions, instead of emulations thereof.
   2010-11-22 02:27:20 < Dark_Shikari> (SSSE3 adds a "sign restore" and "absolute value" instruction)
   2010-11-22 02:27:27 < Dark_Shikari> which are really really useful.
   2010-11-22 02:27:47 < Jumpyshoes> okaaaaaay, so
   2010-11-22 02:27:51 < Jumpyshoes> finally caught up
   2010-11-22 02:28:02 < Jumpyshoes> why are some asm instructions capitalized?
   2010-11-22 02:28:47 < Jumpyshoes> like PSIGNW
   2010-11-22 02:29:27 < Jumpyshoes> i mean, why is it capitalized while other instructions aren't?
   2010-11-22 02:29:28 < Dark_Shikari> PSIGNW isn't an instruction, it's a macro
   2010-11-22 02:29:43 < Jumpyshoes> o
   2010-11-22 02:29:43 < Dark_Shikari> we %define it to PSIGNW_MMX for the mmx implementation
   2010-11-22 02:29:48 < Dark_Shikari> and when we make the ssse3 version
   2010-11-22 02:29:53 < Dark_Shikari> we %define it to PSIGNW_SSSE3
   2010-11-22 02:29:57 < Jumpyshoes> i see
   2010-11-22 02:30:10 < Dark_Shikari> the latter of which... is just psignw.
   2010-11-22 02:30:20 < Kovensky> so I heard you like instructions so we put instructions on your instructions so you can...
   2010-11-22 02:30:30 < Dark_Shikari> by the way
   2010-11-22 02:30:32 < Dark_Shikari> in INIT_XMM
   2010-11-22 02:30:33 < Dark_Shikari> mova == movdqa
   2010-11-22 02:30:35 < Dark_Shikari> movh == movq
   2010-11-22 02:30:38 < Dark_Shikari> movu == movdqu
   2010-11-22 02:30:42 < Dark_Shikari> init INIT_MMX
   2010-11-22 02:30:43 < Dark_Shikari> mova == movq
   2010-11-22 02:30:45 < Dark_Shikari> movh == movd
   2010-11-22 02:30:46 < Dark_Shikari> movu == movq
   2010-11-22 02:30:51 < Dark_Shikari> mova == move aligned
   2010-11-22 02:30:53 < Dark_Shikari> movh == move half
   2010-11-22 02:30:56 < Dark_Shikari> movu == move unaligned
   2010-11-22 02:31:55 < Jumpyshoes> oh boy
   2010-11-22 02:32:28 < Jumpyshoes> should i try to take a look at this denoise function?
   2010-11-22 02:32:37 < Dark_Shikari> Yes, feel free to look at the C.
   2010-11-22 02:32:39 < Dark_Shikari> It's not very complicated.
   2010-11-22 02:32:48 < Jumpyshoes> where can i find the C?C
   2010-11-22 02:32:51 < Dark_Shikari> C is in common/quant.c
   2010-11-22 02:32:53 < Dark_Shikari> as you might expect.
   2010-11-22 02:33:47 < Jumpyshoes> wait, so why is the macro 1-2?
   2010-11-22 02:33:52 < Jumpyshoes> DENOISE_DCT 1-2
   2010-11-22 02:33:59 < Dark_Shikari> variable number of arguments
   2010-11-22 02:34:03 < Dark_Shikari> Ah, I forgot the third number.
   2010-11-22 02:34:08 < Dark_Shikari> cglobal name, X, Y, Z
   2010-11-22 02:34:11 < Dark_Shikari> We only covered the X and Y.
   2010-11-22 02:34:29 < Dark_Shikari> on win64, xmmregs 6-15 need to be saved.
   2010-11-22 02:34:44 < Dark_Shikari> so if we use more than 6 xmmregs, we need to tell x264 about it
   2010-11-22 02:34:48 < Dark_Shikari> the last number is the number of xmmregs used.
   2010-11-22 02:34:49 < Dark_Shikari> It's optional.
   2010-11-22 02:34:55 < Dark_Shikari> So if we are using mmx, we don't bother setting it.
   2010-11-22 02:34:58 < Dark_Shikari> and it defaults to 0.
   2010-11-22 02:35:47 < Jumpyshoes> why is the C so simple and why is the asm so long
   2010-11-22 02:35:56 < Dark_Shikari> 1) C is more expressive than asm
   2010-11-22 02:36:03 < Dark_Shikari> 2) the asm is unrolled, doing more iterations per loop than the C
   2010-11-22 02:36:10 < Jumpyshoes> oh
   2010-11-22 02:37:25 < Dark_Shikari> asm is almost always longer than C.
   2010-11-22 02:37:44 < Kovensky> what does pabsw do
   2010-11-22 02:37:47 < Dark_Shikari> absolute value
   2010-11-22 02:37:53 < Kovensky> it isn't in that nasm reference :(
   2010-11-22 02:38:16 < Dark_Shikari> sure, because it's newer than sse2
   2010-11-22 02:38:37 < Kovensky> so pabsw dst, src strips the signs from src and stores result on dst?
   2010-11-22 02:38:43 < Dark_Shikari> yes
   2010-11-22 02:40:35 < Kovensky> and psignw?
   2010-11-22 02:43:03 < Jumpyshoes> you know what blows my mind? there's no xor or shr in the asm code
   2010-11-22 02:43:06 < Dark_Shikari> Kovensky: restores sign
   2010-11-22 02:43:24 < Dark_Shikari> Jumpyshoes: the c code is optimized
   2010-11-22 02:43:26 < Kovensky> I'm atm parsing the bunch of punpck
   2010-11-22 02:43:34 < Dark_Shikari> it's really more optimized than it needs to be
   2010-11-22 02:43:41 < Dark_Shikari> the +/^ is just abs
   2010-11-22 02:43:46 < Jumpyshoes> oh
   2010-11-22 02:43:47 < Dark_Shikari> and a sign restore at the end
   2010-11-22 02:43:54 < Dark_Shikari> the C was effectively rewritten to be more like the asm
   2010-11-22 02:44:26 < Kovensky> actually, I lost track of the registers already lol
   2010-11-22 02:44:42 < Jumpyshoes> soooooooo did i
   2010-11-22 02:45:18 < Dark_Shikari> add comments next to them or give them names if you need to
   2010-11-22 02:45:21 < Kovensky> why is m6 only read from
   2010-11-22 02:45:27 < Dark_Shikari> m6 is a zero register
   2010-11-22 02:45:31 < Dark_Shikari> it's initted at the start
   2010-11-22 02:45:45 < Jumpyshoes> it interleaves 0s?
   2010-11-22 02:45:51 < Kovensky> so it just supplies 0s to the punpcks
   2010-11-22 02:46:08 < Dark_Shikari> yes
   2010-11-22 02:46:13 < Dark_Shikari> Jumpyshoes: to convert from 16-bit to 32-bit
   2010-11-22 02:46:15 < Dark_Shikari> you add zeroes
   2010-11-22 02:46:22 < Kovensky> I actually should go sleep right now, finals week start tomorrow and it's 14 minutes to tomorrow =p
   2010-11-22 02:46:32 < Jumpyshoes> you know what my OCD self hates?
   2010-11-22 02:46:36 < Jumpyshoes> >paddd     m4, [r1+r3*4+0*mmsize]
   2010-11-22 02:46:40 < Jumpyshoes> f-f-f-f-f-fuck
   2010-11-22 02:46:47 < Dark_Shikari> what
   2010-11-22 02:46:52 < Jumpyshoes> m4 goes with 0
   2010-11-22 02:46:58 < Dark_Shikari> oh
   2010-11-22 02:46:58 < Dark_Shikari> lol
   2010-11-22 02:47:08 < Dark_Shikari> those were just regs I ended up with at the end
   2010-11-22 02:47:11 < Dark_Shikari> that's how you write these things
   2010-11-22 02:47:12 < Dark_Shikari> =p
   2010-11-22 02:48:36 < Jumpyshoes> okay
   2010-11-22 02:48:40 < Jumpyshoes> i get the gist of this function
   2010-11-22 02:49:08 < Kovensky> gl Jumpyshoes, I'll read the backlog later
   2010-11-22 02:49:08 < Dark_Shikari> it subtracts a value from each dct coeff
   2010-11-22 02:49:16  * Kovensky sleeps
   2010-11-22 02:49:20 < Jumpyshoes> yea, from the offsets?
   2010-11-22 02:49:22 < Dark_Shikari> (limiting it to zero, so they don't go negative)
   2010-11-22 02:49:22 < Jumpyshoes> cya Kovensky
   2010-11-22 02:49:25 < Dark_Shikari> it subtractss the offsets
   2010-11-22 02:49:31 < Dark_Shikari> then it adds the amounts subtracted to the accumulators
   2010-11-22 02:49:40 < Dark_Shikari> which are then used later in x264 to create new offsets.
   2010-11-22 02:50:17 < Jumpyshoes> i see
   2010-11-22 02:50:47 < Jumpyshoes> wait, now what's the conditions on this loop from breaking?
   2010-11-22 02:51:01 < Jumpyshoes> OH
   2010-11-22 02:51:02 < Jumpyshoes> the sub
   2010-11-22 02:51:05 < Jumpyshoes> WAY UP TOP
   2010-11-22 02:51:23 < Dark_Shikari> yeah, it kind of went walkabout
   2010-11-22 02:52:02 < Jumpyshoes> okay
   2010-11-22 02:52:05 < Jumpyshoes> now i think i understand
   2010-11-22 02:52:48 < Jumpyshoes> understanding 15 lines of asm takes me 30 minutes
   2010-11-22 02:52:50 < Jumpyshoes> woohoo
   2010-11-22 02:52:52 < Dark_Shikari> That's normal
   2010-11-22 02:53:12 < Dark_Shikari> for a newbie, writing is often easier than reading.
   2010-11-22 02:53:18 < Dark_Shikari> because when writing, you already know what youw ant
   2010-11-22 02:53:19 < Dark_Shikari> *want
   2010-11-22 02:53:20 < Jumpyshoes> are you serious?
   2010-11-22 02:53:23 < Dark_Shikari> when reading, you have to figure out what someone else wanted.
   2010-11-22 02:53:38 < Jumpyshoes> true
   2010-11-22 02:53:43 < Dark_Shikari> And you can pattern your functions on others
   2010-11-22 02:53:50 < Dark_Shikari> for example, like 1/3 of the functions in x264 are looping over some pixel input
   2010-11-22 02:53:57 < Dark_Shikari> using the same basic template.
   2010-11-22 02:54:04 < Jumpyshoes> oh
   2010-11-22 02:54:12 < Jumpyshoes> i have a feeling GCI is gonna kick my ass
   2010-11-22 02:54:15 < Dark_Shikari> in general, it's not as hard as you think.
   2010-11-22 02:54:17 < Jumpyshoes> but that's not the point
   2010-11-22 02:54:28 < Dark_Shikari> Actually, let's do that.  Let's write a function
   2010-11-22 02:54:29 < Jumpyshoes> do all asm functions have a C equivalent?
   2010-11-22 02:54:32 < Dark_Shikari> Yes
   2010-11-22 02:54:41 < kierank> [02:53] Dark_Shikari: when reading, you have to figure out what someone else wanted. --> or if it's compiler created asm who knows what you have to figure out
   2010-11-22 02:54:48 < Jumpyshoes> oh god, i'm gonna get my ass kicked
   2010-11-22 02:54:48 < Dark_Shikari> lol
   2010-11-22 02:55:51 < Jumpyshoes> well, at least there's c
   2010-11-22 02:55:53 < Jumpyshoes> to help me
   2010-11-22 02:55:57 < Jumpyshoes> read this
   2010-11-22 02:56:17 < Dark_Shikari> void foo( int16_t *dst, int16_t *src1, int16_t *src2 )
   2010-11-22 02:56:17 < Dark_Shikari> {
   2010-11-22 02:56:17 < Dark_Shikari>     for( int i = 0; i < 64; i++ )
   2010-11-22 02:56:17 < Dark_Shikari>         dst[i] = src1[i] - src2[i];
   2010-11-22 02:56:18 < Dark_Shikari> }
   2010-11-22 02:56:20 < Dark_Shikari> implement this.
   2010-11-22 02:56:25 < Dark_Shikari> ask questions as you go
   2010-11-22 02:56:25 < Jumpyshoes> ooooh boy
   2010-11-22 02:56:28 < Jumpyshoes> very well
   2010-11-22 02:56:39 < Dark_Shikari> cglobal foo_mmxext, 3,3
   2010-11-22 02:56:41 < Dark_Shikari> or sse2, take your pick
   2010-11-22 02:57:14 < Jumpyshoes> i hope you don't expect it to be optimized
   2010-11-22 02:57:54 < Dark_Shikari> I expect it to be reasonably fast, i.e. using SIMD
   2010-11-22 02:58:07 < Dark_Shikari> feel free to stop at any point and ask any question about anything
   2010-11-22 02:58:28 < Jumpyshoes> okay
   2010-11-22 03:03:32 < Jumpyshoes> wait, so a qw is 128bits?
   2010-11-22 03:03:42 < Dark_Shikari> no, quadword is 64
   2010-11-22 03:03:44 < Dark_Shikari> double quadword is 128
   2010-11-22 03:03:47 < Jumpyshoes> er
   2010-11-22 03:03:49 < Jumpyshoes> yea
   2010-11-22 03:03:49 < Dark_Shikari> word is 16
   2010-11-22 03:03:53 < Dark_Shikari> quad... 4*...
   2010-11-22 03:05:17 < darkbringer> what about overflows?
   2010-11-22 03:05:27 < Jumpyshoes> oh, yes <_<
   2010-11-22 03:06:10 < Dark_Shikari> not possible as far as I see
   2010-11-22 03:06:14 < Dark_Shikari> they're all int16_t
   2010-11-22 03:06:29 < Dark_Shikari> I mean, they could happen, but whatever, you won't have to care about them
   2010-11-22 03:08:09 < Jumpyshoes> okay, i think this is horribly wrong
   2010-11-22 03:08:17 < Dark_Shikari> use pastebin btw instead of pasting tons of shit
   2010-11-22 03:08:42 < Jumpyshoes> this is going to be wrong and i will be laughed at <_<
   2010-11-22 03:09:02 < Jumpyshoes> well whatever
   2010-11-22 03:09:05 < Jumpyshoes> i'm used to looking dumb
   2010-11-22 03:10:28 < Jumpyshoes> http://pastebin.com/2JCFdD4R
   2010-11-22 03:11:30 < Dark_Shikari> psubw should be lowercase, it's an instruction
   2010-11-22 03:11:41 < Dark_Shikari> your function has no stores
   2010-11-22 03:11:41 < Jumpyshoes> oh
   2010-11-22 03:11:59 < Jumpyshoes> stores?
   2010-11-22 03:12:05 < Dark_Shikari> you know, storing your output
   2010-11-22 03:12:14 < Jumpyshoes> oops
   2010-11-22 03:12:17 < Dark_Shikari> also, n*8, because each iteration handles 8 bytes.
   2010-11-22 03:12:27 < Dark_Shikari> also, can you make that a loop instead of %rep?
   2010-11-22 03:12:57 < Jumpyshoes> grah, 8 * 8 = 64
   2010-11-22 03:13:21 < Jumpyshoes> wouldn't i need another variable for a loop?
   2010-11-22 03:13:52 < Dark_Shikari> Yes.
   2010-11-22 03:13:54 < Dark_Shikari> you could do something like
   2010-11-22 03:13:59 < Dark_Shikari> mov r3d, 8
   2010-11-22 03:14:03 < Dark_Shikari> the dec r3d on each iteration
   2010-11-22 03:14:17 < Jumpyshoes> then wouldn't i need another variable declared in the func?
   2010-11-22 03:14:24 < Dark_Shikari> yes, you'd have to do 3,4 instead of 3,3
   2010-11-22 03:14:35 < Jumpyshoes> oh, okay
   2010-11-22 03:14:52 < Dark_Shikari> also, psubw can take input from memory
   2010-11-22 03:14:54 < Dark_Shikari> so you only need one load
   2010-11-22 03:14:55 < Dark_Shikari> i.e.
   2010-11-22 03:14:57 < Dark_Shikari> movq mm0, blah
   2010-11-22 03:15:00 < Dark_Shikari> psubw mm0, blah2
   2010-11-22 03:15:19 < Jumpyshoes> ooh
   2010-11-22 03:15:46 < Jumpyshoes> that is nice
   2010-11-22 03:15:59 < Dark_Shikari> all instructions can access memory in their second argument.
   2010-11-22 03:16:05 < Dark_Shikari> well, almost all.
   2010-11-22 03:16:27 < Jumpyshoes> what was the command for subtracting 1, dec?
   2010-11-22 03:16:47 < Dark_Shikari> yes
   2010-11-22 03:16:50 < Dark_Shikari> it's like sub val, 1
   2010-11-22 03:16:54 < Jumpyshoes> right
   2010-11-22 03:16:58 < Dark_Shikari> decrement
   2010-11-22 03:17:23 < Jumpyshoes> oh, and do i need a ret?
   2010-11-22 03:18:33 < Dark_Shikari> yes, at the end
   2010-11-22 03:18:41 < Dark_Shikari> just like in c
   2010-11-22 03:21:06 < Jumpyshoes> http://pastebin.com/HLCed9Jv
   2010-11-22 03:21:32 < Dark_Shikari> .loop should have a :
   2010-11-22 03:21:42 < Jumpyshoes> oh
   2010-11-22 03:21:47 < Dark_Shikari> in address expressions, you have to use native sizes
   2010-11-22 03:21:50 < Dark_Shikari> so inside the [], no d
   2010-11-22 03:22:01 < Dark_Shikari> other than that, you're done!
   2010-11-22 03:22:19 < Jumpyshoes> woah, that only took three revisions
   2010-11-22 03:22:37 < Jumpyshoes> actually wait
   2010-11-22 03:22:51 < Jumpyshoes> i'm dealing with int16, and looping 64 times
   2010-11-22 03:23:05 < Jumpyshoes> wouldn't i need to do more than 8 loops? since mm is 64 bits
   2010-11-22 03:23:27 < Dark_Shikari> ah yes, you'll have to do 16 loops.
   2010-11-22 03:23:41 < Dark_Shikari> now, btw, here's the big nice part about writing x264 asm
   2010-11-22 03:23:44 < Dark_Shikari> make checkasm;./checkasm
   2010-11-22 03:24:02 < Jumpyshoes> where do i do that?
   2010-11-22 03:24:26 < Dark_Shikari> in your terminal
   2010-11-22 03:24:44 < Jumpyshoes> right
   2010-11-22 03:25:00 < Jumpyshoes> lots of warnings thar
   2010-11-22 03:25:37 < Jumpyshoes> oh and there's an error
   2010-11-22 03:25:43 < Dark_Shikari> error?  what'd you do
   2010-11-22 03:25:50 < Jumpyshoes> i have no clue
   2010-11-22 03:26:08 < Jumpyshoes> common/x86/const-a.asm:50: error: undefined symbol `BIT_DEPTH' (first use)
   2010-11-22 03:26:09 < Jumpyshoes> common/x86/const-a.asm:50: error:  (Each undefined symbol is reported only once.)
   2010-11-22 03:26:14 < Dark_Shikari> you need to reconfigure
   2010-11-22 03:26:14 < darkbringer> ./configure
   2010-11-22 03:26:17 < Jumpyshoes> oh right
   2010-11-22 03:26:18 < Jumpyshoes> since i pulled it
   2010-11-22 03:28:04 < Jumpyshoes> x264: All tests passed Yeah :)
   2010-11-22 03:28:22 < Dark_Shikari> you just ran unit tests on every asm function in x264.
   2010-11-22 03:28:27 < Jumpyshoes> woah that is cool
   2010-11-22 03:28:40 < Jumpyshoes> so i can test my func
   2010-11-22 03:28:41 < Jumpyshoes> by adding it?
   2010-11-22 03:28:58 < Dark_Shikari> yes
   2010-11-22 03:29:02 < Dark_Shikari> well, I mean
   2010-11-22 03:29:06 < Dark_Shikari> your function doesn't have a C equivalent in x264
   2010-11-22 03:29:07 < Dark_Shikari> so not really
   2010-11-22 03:29:09 < Jumpyshoes> oh
   2010-11-22 03:29:10 < Jumpyshoes> right
   2010-11-22 03:29:12 < Dark_Shikari> but for anything with a C equivalent, it can test it
   2010-11-22 03:29:17 < Jumpyshoes> sexy
   2010-11-22 03:29:17 < Dark_Shikari> it of course needs unit test code in checkasm.c
   2010-11-22 03:29:24 < Dark_Shikari> but for  all existing C functions, there's unit test code
   2010-11-22 03:29:59 < Jumpyshoes> nice
   2010-11-22 03:32:01 < Dark_Shikari> also
   2010-11-22 03:32:03 < Dark_Shikari> ./checkasm --bench
   2010-11-22 03:33:22 < Jumpyshoes> is that the number of clock cycles?
   2010-11-22 03:33:32 < Dark_Shikari> 10ths of a clock cycle
   2010-11-22 03:33:48 < Jumpyshoes> oh
   2010-11-22 03:33:51 < Jumpyshoes> crazy
   2010-11-22 03:33:56 < Dark_Shikari> note not all benches are quite accurate, particularly in the case of functions heavily bound by branch mispredictions
   2010-11-22 03:34:07 < Jumpyshoes> add4x4_idct is like
   2010-11-22 03:34:09 < Dark_Shikari> most commonly where C is branchy
   2010-11-22 03:34:11 < Dark_Shikari> and asm isn't
   2010-11-22 03:34:14 < Dark_Shikari> but most aren't like that.
   2010-11-22 03:34:16 < Jumpyshoes> ah
   2010-11-22 03:34:27 < Jumpyshoes> when do GCI tasks come out?
   2010-11-22 03:34:34 < Dark_Shikari> probably tomorrow
   2010-11-22 03:34:38 < Dark_Shikari> I really need to get to writing up the rest of them
   2010-11-22 03:34:40 < Dark_Shikari> we only have 5
   2010-11-22 03:34:42 < Dark_Shikari> I need more :/
   2010-11-22 03:35:03 < Jumpyshoes> can you add stuff as the contest progresses?
   2010-11-22 03:35:13 < Dark_Shikari> I hope so
   2010-11-22 03:35:18 < Dark_Shikari> according to them I think yes
   2010-11-22 03:35:27 < Jumpyshoes> cool
   2010-11-22 03:35:28 < Dark_Shikari> as they said you can have a repeatable task just by re-adding it after someone takes it
   2010-11-22 03:36:42 < Jumpyshoes> how hard are these tasks?
   2010-11-22 03:37:10 < Dark_Shikari> http://wiki.videolan.org/X264_GCodeIn_Ideas
   2010-11-22 03:38:37 < Jumpyshoes> interesting
   2010-11-22 03:42:49 < ps-auxw> Dark_Shikari: Just wondering, is there a reason that PIXEL_SAD_C has a separate name argument, instead of constructing the function name using lx/ly and ## concatenation operator?
   2010-11-22 03:42:59 < Dark_Shikari> ps-auxw: nobody did it 5 years ago when it was written
   2010-11-22 03:43:01 < Dark_Shikari> and it hasn't bee modified since
   2010-11-22 03:43:05 < Dark_Shikari> *been
   2010-11-22 03:43:07 < ps-auxw> I see.
   2010-11-22 03:53:46 < ps-auxw> Would a patch be welcome? ;)
   2010-11-22 03:55:30 < Dark_Shikari> not relaly, kind of a waste of a patch =p
   2010-11-22 03:55:50 < ps-auxw> True, true.
   2010-11-22 08:42:15 < xxthink> < Dark_Shikari> x264 at crf 18 is "almost lossless" too
   2010-11-22 08:42:42 < xxthink> what's the recommend GOP structure that x264 should use to save the video content?
   2010-11-22 08:42:46 < xxthink> all I frames?
   2010-11-22 08:43:20 < xxthink> sorry, wrong channel
   2010-11-22 08:45:09 < rfw> so, i heard you guys have GCI tasks :D
   2010-11-22 08:45:17 < rfw> hurt me if people have been here about this before me
   2010-11-22 08:47:20 < dj_tjerk> you can check the logs anytime ;)
   2010-11-22 08:47:49 < rfw> heh
   2010-11-22 08:47:54 < rfw> the google site is still being lol :(
   2010-11-22 08:48:25 < dj_tjerk> http://wiki.videolan.org/X264_GCodeIn_Ideas <-- just some ideas, D_S will make an official list tomorrow/today (timezones)
   2010-11-22 08:48:36 < rfw> ah
   2010-11-22 08:48:43 < rfw> yeah i looked at that
   2010-11-22 08:48:51 < rfw> the regression testing tool looks fun
   2010-11-22 08:48:58 < dj_tjerk> but if you check the logs (see topic) you see D_S giving his awesome asm explanation
   2010-11-22 08:49:20 < rfw> 4MB of bzipped logs
   2010-11-22 08:49:31 < rfw> how big is that uncompressed
   2010-11-22 08:49:33 < dj_tjerk> log*
   2010-11-22 08:49:35 < dj_tjerk> 17MB
   2010-11-22 08:49:40 < rfw> derp
   2010-11-22 08:51:18 < rfw> --- Log opened Thu Jul 24 01:08:59 2008
   2010-11-22 08:51:26 < rfw> this is going to be fun to page through
   2010-11-22 08:51:31 < dj_tjerk> yeh.. you might wanna start reading from the bottom ;)
   2010-11-22 08:51:43 < dj_tjerk> and then scroll up to wherever his awesome asm explanation starts
   2010-11-22 08:53:42 < rfw> reading uncolored logs really isn't fun
   2010-11-22 08:54:05 < rfw> "I asked you if you understood my explanation of what a function does."
   2010-11-22 08:54:08 < rfw> somewhere near here?
   2010-11-22 08:54:44 < Kovensky> just a bit more above
   2010-11-22 08:54:49 < rfw> ohi Kovensky
   2010-11-22 08:56:02 < rfw> god i can't be bothered with this today
   2010-11-22 08:56:13 < rfw> it's probably going to be like this for another half a day
   2010-11-22 09:01:34 < rfw> bah, i'm not really having much luck at all
   2010-11-22 09:01:41 < rfw> i guess i'll be around tomorrow then
   2010-11-22 09:01:51 < dj_tjerk> :?
   2010-11-22 09:01:51 < rfw> night
   2010-11-22 09:02:04 < rfw> the gci website is still giving me 500 errors
   2010-11-22 09:02:09 < dj_tjerk> oh.. :|
   2010-11-22 09:02:12 < rfw> yeah :|
   2010-11-22 09:02:27 < rfw> probably from all the other high school kids ddosing google
   2010-11-22 09:04:21 < rfw> tomorrow then :(
   2010-11-22 09:04:22 < rfw> night
   2010-11-22 09:08:16 < Kovensky> http://pastebin.ca/1998693 <-- my version of that for loop (SSE2)
   2010-11-22 09:09:18 < Kovensky> though it's pretty much the same as the mmext, but with movdqu and xmm instead of movq and mm ._.
   2010-11-22 09:23:09 < Kovensky> http://pastebin.ca/1998700 <-- uh, moving the sub up, fixes out of bounds read / writes
   2010-11-22 09:58:34 < koda|work> hi all
   2010-11-22 09:59:21 < koda|work> is anyone experiencing
   2010-11-22 09:59:24 < koda|work> common/x86/const-a.asm:50: error: undefined symbol `BIT_DEPTH' (first use)
   2010-11-22 09:59:24 < koda|work> ?
   2010-11-22 10:00:44 < koda|work> oh nevermind i forgot to configure cleanly
   2010-11-22 10:06:12 < Dark_Shikari> hah
   2010-11-22 10:24:39 < wipple> Dark_Shikari: sorry, i found a mistake in my first patch
   2010-11-22 10:25:06 < wipple> line 207 should be +if [ "armv6" = "yes" ]; then
   2010-11-22 10:26:01 < Dark_Shikari> applied
   2010-11-22 10:26:12 < wipple> thx
   2010-11-22 10:34:34 < Kovensky> Dark_Shikari: is my loop there correct? (as in, do I need to do it by subing 2 at a time?)
   2010-11-22 10:34:46 < Kovensky> also, is it common for asm code to work backwards through memory?
   2010-11-22 10:35:01 < Dark_Shikari> link?
   2010-11-22 10:35:11 < Dark_Shikari> it's common to work backwards to avoid the "cmp" before the jump.
   2010-11-22 10:35:12 < Kovensky> http://pastebin.ca/1998700
   2010-11-22 10:35:30 < Dark_Shikari> should be mov r3d, 16 to start, not 8
   2010-11-22 10:36:10 < Dark_Shikari> also if your source is aligned
   2010-11-22 10:36:13 < Dark_Shikari> er, unaligned
   2010-11-22 10:36:19 < Dark_Shikari> you can't use memory arguments for psubw
   2010-11-22 10:36:29 < Kovensky> I see
   2010-11-22 10:36:50 < Kovensky> so then I either assume the whole thing is aligned and use movdqa, or use two movdqus before the psubw
   2010-11-22 10:37:04 < Dark_Shikari> yes
   2010-11-22 10:38:06 < Kovensky> I think the 8 was left there from when I tried using *16 on the addressing (which ofc failed to assemble)
   2010-11-22 10:38:35 < Dark_Shikari> the only purpose of the * is to save instruction space by using "dec"
   2010-11-22 10:38:36 < Dark_Shikari> instead of sub
   2010-11-22 10:38:43 < Dark_Shikari> so for clarity in your case you might as well just mov r3d, 128
   2010-11-22 10:38:45 < Dark_Shikari> and sub 16 on each iteration
   2010-11-22 10:38:54 < Kovensky> http://pastebin.ca/1998753 <-- unaligned, http://pastebin.ca/1998756 <-- aligned
   2010-11-22 10:38:58 < Kovensky> Dark_Shikari: ok
   2010-11-22 10:40:24 < Kovensky> http://pastebin.ca/1998759
   2010-11-22 10:40:49 < Dark_Shikari> I'd put the sub above the jg, and mov 112 instead of 128.
   2010-11-22 10:40:55 < Dark_Shikari> to reduce data dependencies.
   2010-11-22 10:41:19 < Dark_Shikari> and do jge instead of jg
   2010-11-22 10:41:39 < Dark_Shikari> http://pastebin.ca/1998761
   2010-11-22 10:42:04 < Kovensky> feels more natural, except for starting at 112
   2010-11-22 10:45:39 < Dark_Shikari> lololol, in the vp8 experimental branch they removed the low pass filtering from the H and V predictions
   2010-11-22 10:45:45 < Dark_Shikari> .... making them the same as h264's
   2010-11-22 10:48:08 < Kovensky> lol
   2010-11-22 10:52:01 < koda|work> hey Dark_Shikari, i once found a patch that brought speedbuffering to x264
   2010-11-22 10:52:12 < koda|work> is there any plan to implement it?
   2010-11-22 10:52:37 < Dark_Shikari> it can be done outside of x264
   2010-11-22 10:52:55 < Dark_Shikari> with the presets it should be easy to do now
   2010-11-22 10:53:24 < koda|work> that is a 'no'? :p
   2010-11-22 10:53:39 < Dark_Shikari> Probably not given that you can do it outside x264 in just a few lines of code
   2010-11-22 10:54:39 < koda|work> but how would you that like in vlc?
   2010-11-22 10:54:52 < Dark_Shikari> ?
   2010-11-22 10:57:04 < koda|work> i mean, i patched x264 to have speed and speed-buffer options and then i use them from vlc when i'm transcoding the video and send it on the net
   2010-11-22 10:57:29 < koda|work> without speed and speed-buffer the decoded video would not appear fluid
   2010-11-22 10:57:58 < Dark_Shikari> speed is for the encoder, not the decoder
   2010-11-22 10:58:12 < Dark_Shikari> it's only "not fluid" if you try to use really slow settings when you can't handle them
   2010-11-22 10:58:44 < Dark_Shikari> in VLC you could pretty easily add speed buffer code
   2010-11-22 10:58:50 < Dark_Shikari> e.g. adjust encoding speed settings based on how far behind you are
   2010-11-22 10:59:28 < koda|work> i see...
   2010-11-22 10:59:40 < koda|work> i'll do more testing then
   2010-11-22 10:59:52 < Dark_Shikari> speedcontrol is useful so that you can _always_ use the _slowest_ settings possible
   2010-11-22 11:05:40 < Alex_W> Dark_Shikari: do you know if professionally encoded blu-rays use explicit wpred?
   2010-11-22 11:06:14 < Dark_Shikari> I think so
   2010-11-22 11:06:19 < Dark_Shikari> prolly depends on the encoder
   2010-11-22 11:07:56 < Alex_W> so i wonder if they do it differently to x264 for compatibility reasons, i guess they don't use dupes at all...
   2010-11-22 11:08:13 < Dark_Shikari> most encoders don't
   2010-11-22 11:08:53 < Dark_Shikari> so quick, GCI starts today
   2010-11-22 11:09:02 < Dark_Shikari> we need more tasks
   2010-11-22 11:10:01 < Alex_W> then i wonder if it would be possible to have a blu-ray compatible weightp option in x264? ( i mean one that doesn't break on mediatek chipsets)
   2010-11-22 11:10:11 < Alex_W> what kind of tasks are you looking for?
   2010-11-22 11:10:18 < Dark_Shikari> http://wiki.videolan.org/X264_GCodeIn_Ideas
   2010-11-22 11:10:23 < Dark_Shikari> anything no harder than these
   2010-11-22 11:11:26 < Alex_W> maybe some psy testing?
   2010-11-22 11:11:39 < Dark_Shikari> we would need some psy things to test.
   2010-11-22 11:11:48 < Alex_W> aq-mode 1 vs 2
   2010-11-22 11:12:08 < Dark_Shikari> if you want to create a psy curve for someone to test, feel free
   2010-11-22 11:12:11 < Dark_Shikari> e.g. by adjusting AQ, etc, etc
   2010-11-22 11:12:39 < Dark_Shikari> but I think we need to have something available to test
   2010-11-22 11:12:42 < Dark_Shikari> as opposed to making htem write it
   2010-11-22 11:15:21 < Dark_Shikari> import ideas from http://wiki.videolan.org/X264_TODO etc
   2010-11-22 11:19:58 < Dark_Shikari> Alex_W: tl;dr this is a chance to test stuff
   2010-11-22 11:20:02 < Dark_Shikari> prepare stuff to be tested.
   2010-11-22 11:20:12 < Alex_W> well i'm already testing a different AQ curve at low variances, though i think the one i'm using atm is probably too aggressive
   2010-11-22 11:23:10 < Alex_W> unfortunately it seems like preserving low variance dark areas is going to take a lot of bits, at least based on testing with an elevated black level
   2010-11-22 11:25:59 < Alex_W> also i think RD bskip might be a problem for these areas as well
   2010-11-22 11:30:18 < Alex_W> anyway here's my current change to aq-mode 1 at low variances: http://pastebin.com/UVfMCC5p
   2010-11-22 11:38:36 < Dark_Shikari> I wonder if we can calculate the theoretically "correct" value?
   2010-11-22 11:38:41 < Dark_Shikari> i.e. considering the effect of BIT_DEPTH
   2010-11-22 11:38:49 < Dark_Shikari> er, correct curve
   2010-11-22 11:39:02 < Dark_Shikari> in other words, there are two contributors to variance-related quality:
   2010-11-22 11:39:06 < Dark_Shikari> 1) the normal effect
   2010-11-22 11:39:08 < Dark_Shikari> 2) truncation
   2010-11-22 11:39:17 < Dark_Shikari> at lower variance, the effect of 2) rises and the effect of 1) drops
   2010-11-22 11:39:22 < Dark_Shikari> well, the relative effect of 1) drops
   2010-11-22 11:50:10 < Alex_W> well i'm certainly open to any suggestions on how to improve this
   2010-11-22 11:52:11 < Alex_W> how low should the maximum negative QP offset be anyway? (i mean for variance=1)
   2010-11-22 11:52:25 < Dark_Shikari> -20?
   2010-11-22 11:52:44 < Dark_Shikari> -15?
   2010-11-22 11:53:26 < Alex_W> right now it's approximately the same as the one that was originally used in aq-mode 1 which was around -14.4
   2010-11-22 11:54:30 < Alex_W> and the difference between variance 512 and variance 1 is around -9 atm with my new curve
   2010-11-22 11:54:37 < Dark_Shikari> what did it used to be?
   2010-11-22 11:55:25 < Alex_W> the difference between 512 and 1 or the maximum negative offset for variance 1?
   2010-11-22 11:55:32 < Dark_Shikari> former
   2010-11-22 11:55:38 < Alex_W> lemme check
   2010-11-22 11:56:15 < Dark_Shikari> ok, I added a psy test task
   2010-11-22 11:56:16 < Dark_Shikari> what else
   2010-11-22 11:56:19 < Dark_Shikari> up to 6 tasks
   2010-11-22 11:57:37 < Alex_W> actually the difference in QPs is about the same but the shape of the curve between those two points is much different now
   2010-11-22 11:57:47 < Dark_Shikari> ah.
   2010-11-22 11:59:15 < Alex_W> but this new curve will likely increase bitrate quite a lot on clips with lots of low variance areas at the same crf
   2010-11-22 12:00:48 < Alex_W> but i really wonder if there could be a better way to deal with these areas than just throwing huge amounts of bits at them to exactly preserve their noise/dither
   2010-11-22 12:05:37 < Alex_W> Dark_Shikari: btw do you have any test content that shows noticeable banding/blocking in low variance areas even at reasonably high bitrates with the current aq-mode 1?
   2010-11-22 12:06:08 < Dark_Shikari> dunno.  you could just create an artificial gradient
   2010-11-22 12:06:30 < Dark_Shikari> possible solution: quantization-aware dither
   2010-11-22 12:06:40 < Alex_W> yeah i was thinking about doing that
   2010-11-22 12:06:55 < Alex_W> explain?
   2010-11-22 12:07:15 < Dark_Shikari> i.e. just make dither patterns consisting of basis functions
   2010-11-22 12:07:43 < Dark_Shikari> not sure how you would get that, but it's a desired result
   2010-11-22 12:07:48 < Alex_W> yes but how do you decide which basis functions to use
   2010-11-22 12:08:00 < Dark_Shikari> the highest frequency one.
   2010-11-22 12:08:24 < Dark_Shikari> to misquote gmaxwell (I think it was), "blur it out, then cover it up with ants"
   2010-11-22 12:08:31 < Alex_W> so [7][7] in the 8x8 transform?
   2010-11-22 12:08:34 < Dark_Shikari> yes
   2010-11-22 12:08:57 < Alex_W> just one basis function or a combination of a few different ones?
   2010-11-22 12:08:57 < Dark_Shikari> This might naturally happen if we did floyd-steinberg in the dct
   2010-11-22 12:09:07 < Dark_Shikari> or some other batching of nearby coeffs
   2010-11-22 12:09:45 < Alex_W> well this is really what psy-trellis would do ideally
   2010-11-22 12:11:08 < Alex_W> but yes if the noise has a low enough magnitude i think it could definitely be worthwhile to just remove it and then replace it with some that looks similar but costs a lot less bits
   2010-11-22 12:11:28 < Dark_Shikari> I wasn't thinking of that
   2010-11-22 12:11:32 < Dark_Shikari> I was thinking of e.g. 10-bit input
   2010-11-22 12:11:38 < Dark_Shikari> and then dithering internally to x264 somehow
   2010-11-22 12:11:42 < Dark_Shikari> not necessarily literally that
   2010-11-22 12:11:54 < Dark_Shikari> but rather doing something AS A DITHER
   2010-11-22 12:11:57 < Dark_Shikari> not as REPLACING NOISE
   2010-11-22 12:14:58 < Alex_W> well either way i think this would be much better than having to code some MBs as low as QP 6 just to stop the damn blocking/banding
   2010-11-22 12:15:18 < Dark_Shikari> if you had a quantizer that actually retained HF energy you wouldn't really need qp 6
   2010-11-22 12:15:54 < jenny`> hey dark - i figured out the issues i was having (if you are curious)
   2010-11-22 12:15:58 < Dark_Shikari> ?
   2010-11-22 12:16:19 < jenny`> the server was sending compressed frames at 30 Hz but the client wasnt able to keep up
   2010-11-22 12:16:37 < Dark_Shikari> common problem in systems with no client feedback for saying "I'm too slow"
   2010-11-22 12:16:57 < jenny`> decode was taking too long, and it indeed was buffering @ the network level
   2010-11-22 12:17:18 < jenny`> yep yep
   2010-11-22 12:19:45 < horlicks> thanks for the correction DS :p
   2010-11-22 12:20:45 < Dark_Shikari> weightp is an explicit weighting applied to one input
   2010-11-22 12:20:56 < Dark_Shikari> weightb is an implicit (or, optionally, explicit) weighting applied to two inputs
   2010-11-22 12:21:24 < horlicks> yeah I understand, seems kinda obvious now
   2010-11-22 12:22:02 < horlicks> maybe that's something I can do after mbaff :)
   2010-11-22 12:22:18 < Dark_Shikari> what is "that"
   2010-11-22 12:22:39 < horlicks> one sec
   2010-11-22 12:23:09 < horlicks> "Make weightp work with interlacing. Preferably abuse reference duplication to make it useful for MBAFF."
   2010-11-22 12:23:16 < Dark_Shikari> ah yes
   2010-11-22 12:23:36 < horlicks> anyway, I'm off
   2010-11-22 12:23:48 < Dark_Shikari> \o
   2010-11-22 12:31:54 < Alex_W> <Dark_Shikari> I wonder if we can calculate the theoretically "correct" curve? <-- how would you go about doing this anyway?
   2010-11-22 12:32:08 < Dark_Shikari> calculate the effect of truncation on quality loss
   2010-11-22 12:32:26 < Dark_Shikari> that is:
   2010-11-22 12:32:33 < Dark_Shikari> 1) Assume a Laplace distribution of coefficients.
   2010-11-22 12:33:05 < Dark_Shikari> 2) Calculate quality loss due to the quantization process
   2010-11-22 12:33:11 < Dark_Shikari> 3) Calculate quality loss due to truncation upon idct
   2010-11-22 12:33:24 < Dark_Shikari> 4) create a curve by combining the two
   2010-11-22 12:34:36 < Alex_W> i see, i doubt that the distribution would be laplacian for noise/dither in these cases though
   2010-11-22 12:34:48 < Dark_Shikari> why not?
   2010-11-22 12:36:56 < Alex_W> well if it's laplacian then bitrate should probably double every 4 - 6 QPs right? from what i've seen so far it doubles much quicker than that
   2010-11-22 12:37:50 < Dark_Shikari> it does once you get to the smooth domain of the curve
   2010-11-22 12:38:03 < Dark_Shikari> the reason it doesn't seem to do that is because there's a threshold beyond which everything is zeroed
   2010-11-22 12:38:07 < Dark_Shikari> because the magnitude of the noise is so low
   2010-11-22 12:38:20 < Dark_Shikari> so you need to get beyond the discontinuous part of the curve
   2010-11-22 12:38:23 < Dark_Shikari> then it's smooth and laplacian
   2010-11-22 12:40:48 < Alex_W> also because the idct always rounds up should we try to compensate for this by adding small negative offsets to the DC coeff or would that be useless?
   2010-11-22 12:41:00 < Dark_Shikari> probably useless
   2010-11-22 14:34:52 < Dark_Shikari> pengvado: ping
   2010-11-22 14:35:28 < Dark_Shikari> of the patches at http://pastebin.com/rW4dsM9J , which can I commit now?
   2010-11-22 14:41:42 < Dark_Shikari> I will push them all today if you don't complain
   2010-11-22 14:52:50 < jarod> so that patch
   2010-11-22 14:52:53 < jarod> --version
   2010-11-22 14:53:07 < jarod> is such inaccurate info useful?
   2010-11-22 14:53:53 < Dark_Shikari> go away troll
   2010-11-22 14:54:07 < jarod> its not to troll
   2010-11-22 14:54:23 < jarod> just saying one revision can make a huge difference
   2010-11-22 14:54:38 < jarod> unless you meant kierank
   2010-11-22 14:55:37 < jarod> but if you want troll
   2010-11-22 14:55:48 < jarod> allow me to <?php header('Location: http://www.webmproject.org/tools/vp8-sdk/'); ?>
   2010-11-22 14:57:52 < jarod> your mood swings are worst than a 8 month pregnant female
   2010-11-22 14:59:05 < pengvado> which one revision is inaccurate?
   2010-11-22 14:59:48 < pengvado> Dark_Shikari: 1,3,4,6,7,8 ok
   2010-11-22 15:00:00 < pengvado> 2: I agree with mru's comments regarding nulls
   2010-11-22 15:00:37 < pengvado> 5: that's a lot of repitions of that if/else block. sounds like a job for a macro.
   2010-11-22 15:00:52 < kierank> oh dear. one of the replicated x264 blu-rays has a problem
   2010-11-22 15:00:57 < Dark_Shikari> oh no
   2010-11-22 15:01:08 < Dark_Shikari> do we know what the issue is?
   2010-11-22 15:01:10 < Dark_Shikari> and if it's x264's problem?
   2010-11-22 15:01:20 < kierank> "We've tested the disc extensively without bumping into any problems, however after replication the customer is complaining the disc is pixelating at a certain scene in the movie."
   2010-11-22 15:01:52 < Dark_Shikari> :>
   2010-11-22 15:01:56 < Dark_Shikari> Do we have a sample?
   2010-11-22 15:02:12 < Dark_Shikari> Sean_McG: ^
   2010-11-22 15:02:38 < Dark_Shikari> what does "replicated" mean -- they've already printed all the blu-rays?
   2010-11-22 15:02:58 < kierank> I fear that's exactly what it means.
   2010-11-22 15:03:43 < Dark_Shikari> what could cause that, a problem on a particular Blu-ray player that they didn't test on?
   2010-11-22 15:03:58 < jarod> not testing and showing results @ devs ftf.... fuck commercialism, i hope its my fault
   2010-11-22 15:04:03 < kierank> I guess
   2010-11-22 15:05:49 < Dark_Shikari> kierank: can we get them to give a sample or something under NDA?
   2010-11-22 15:05:50 < Dark_Shikari> or whatnot
   2010-11-22 15:06:05 < kierank> yes i will ask
   2010-11-22 15:06:10 < Dark_Shikari> so we can see if we have to commit sepukku or not
   2010-11-22 15:06:19 < tjoener> I know there is a problem in x264 with dark scenes (bedroom scene with ellie and carl in up)
   2010-11-22 15:06:27 < tjoener> it gets quite pixelated
   2010-11-22 15:06:32 < Dark_Shikari> tjoener: that's not what they mean
   2010-11-22 15:06:40 < Dark_Shikari> that isn't a "problem in x264"
   2010-11-22 15:06:43 < tjoener> could be
   2010-11-22 15:06:43 < Dark_Shikari> that's "you not using enough bitrate" =p
   2010-11-22 15:06:48 < tjoener> haha
   2010-11-22 15:06:51 < CIA-98> x264: James Darnley  master * r8eaf8a66d5 x264/filters/video/resize.c: Fix resize filter rounding code
   2010-11-22 15:06:53 < tjoener> well its only in dark scenes
   2010-11-22 15:06:54 < Dark_Shikari> at blu-ray bitrates, such a thing is basically meaningless
   2010-11-22 15:06:59 < Dark_Shikari> or more accurately
   2010-11-22 15:07:02 < tjoener> bright scenes are very VERY nice
   2010-11-22 15:07:02 < Dark_Shikari> your monitor is very badly calibrated
   2010-11-22 15:07:03 < CIA-98> x264: Anton Mitrofanov  master * raf1a7413af x264/encoder/ (encoder.c slicetype.c):
   2010-11-22 15:07:03 < CIA-98> x264: Fix regression in chroma weightp
   2010-11-22 15:07:03 < CIA-98> x264: Missing cache calls could cause artifacts, encoder/decoder desync.
   2010-11-22 15:07:11 < Dark_Shikari> x264 assumes your monitor is calibrated correctly
   2010-11-22 15:07:12 < tjoener> well ok
   2010-11-22 15:07:13 < Dark_Shikari> i.e. blacks are black
   2010-11-22 15:07:19 < tjoener> my monitor could be the issue
   2010-11-22 15:07:19 < Dark_Shikari> if blacks are not black, the results will look very bad
   2010-11-22 15:07:27 < tjoener> monitors nowadays are quite crappy
   2010-11-22 15:07:42 < tjoener> havent had the time to look into it yet
   2010-11-22 15:08:01 < tjoener> Ive got a second one though, old acer flatscreen with far better colours as the new one
   2010-11-22 15:08:39 < Dark_Shikari> kierank: you can tell them that I can investigate it to see if there's anything weird about it that could cause problems in broken players, etc
   2010-11-22 15:08:44 < Dark_Shikari> i.e. any "common bug triggers"
   2010-11-22 15:09:40 < Dark_Shikari> I have a hunch, but I can't say what it is until I get a sample.
   2010-11-22 15:10:21 < tjoener> weightp (like flash?)
   2010-11-22 15:10:35 < Dark_Shikari> no
   2010-11-22 15:25:08 < Dark_Shikari> kierank: well, if this sinks everything, I'd like to know
   2010-11-22 15:26:45 < kierank> ok
   2010-11-22 16:11:58 < Jumpyshoes> hey Dark_Shikari, would it be too much if i took on the GCI task of writing an assembly function?
   2010-11-22 16:12:20 < Dark_Shikari> Of course not.
   2010-11-22 16:12:23 < Dark_Shikari> That's a repeatable task.
   2010-11-22 16:12:28 < Jumpyshoes> cool
   2010-11-22 16:12:29 < Dark_Shikari> If you take it, we'll add it in again
   2010-11-22 16:12:33 < Jumpyshoes> i think i will then
   2010-11-22 16:12:33 < holger_> Jumpyshoes:  do you have something specific on your mind?
   2010-11-22 16:12:40 < Dark_Shikari> Yeah, come up with something first
   2010-11-22 16:12:42 < Jumpyshoes> oh
   2010-11-22 16:12:45 < Jumpyshoes> i'll need to do that at home
   2010-11-22 16:12:51 < Dark_Shikari> keep in mind, almost all new opportunities in asm functions are in the category of "high bit depth"
   2010-11-22 16:12:52 < Jumpyshoes> and look for a simple function
   2010-11-22 16:12:59 < Dark_Shikari> as, before high bit depth, we had everything done basically (for x86, at least)
   2010-11-22 16:13:08 < Dark_Shikari> but now with high bit depth, there's tons of missing functions
   2010-11-22 16:13:12 < Dark_Shikari> for example, dequant.
   2010-11-22 16:13:23 < Jumpyshoes> so, for example, 10-bit?
   2010-11-22 16:13:32 < Dark_Shikari> high bit depth encompasses >8-bit
   2010-11-22 16:13:38 < Dark_Shikari> the thing that makes it different is:
   2010-11-22 16:13:41 < Dark_Shikari> 1) pixels are 16-bit instead of 8-bit
   2010-11-22 16:13:45 < Dark_Shikari> 2) dct coeffs are 32-bit instead of 16-bit
   2010-11-22 16:13:48 < Dark_Shikari> thus all the asm is different.
   2010-11-22 16:14:06 < Jumpyshoes> but, the same algorithms apply, no?
   2010-11-22 16:14:09 < Dark_Shikari> yes
   2010-11-22 16:14:18 < holger_> 3) some things can now overflow that couldn't before
   2010-11-22 16:14:25 < Dark_Shikari> 4) some things that could overflow before, now can't
   2010-11-22 16:14:37 < Dark_Shikari> e.g. in 8-bit, they overflowed, but in 16-bit, since all our inputs are no more than 10-bit, don't
   2010-11-22 16:15:08 < Dark_Shikari> e.g. in dequant, previously, we had two dequant branches, based on whether or not it needed 32-bit or 16-bit intermediate precision to work
   2010-11-22 16:15:08 < Jumpyshoes> isn't that easier to take care of then?
   2010-11-22 16:15:12 < Dark_Shikari> but now.... we can just do 32-bit
   2010-11-22 16:15:16 < Dark_Shikari> and have no branch
   2010-11-22 16:15:26 < Dark_Shikari> some things are easier, some are harder.
   2010-11-22 16:15:38 < Jumpyshoes> i see
   2010-11-22 16:16:17 < Jumpyshoes> is the high bit stuff in the same location in the code?
   2010-11-22 16:17:42 < holger_> pretty much, yeah. look for ifdef HIGH_BIT_DEPTH
   2010-11-22 16:18:27 < Jumpyshoes> thanks
   2010-11-22 16:18:29 < holger_> to see which functions are missing you could probably just run checkasm with and without high bit depth and compare the output
   2010-11-22 16:18:41 < holger_> erm. checkasm --bench of course ;)
   2010-11-22 16:21:46 < Jumpyshoes> how do i run checkasm w/ high bit depth?
   2010-11-22 16:22:04 < holger_> you configure for high bit depth, checkasm gets built accordingly
   2010-11-22 16:22:08 < BugMaster|work> compile it with high bit depth
   2010-11-22 16:22:12 < BugMaster|work> configure --bit-depth=10
   2010-11-22 16:22:26 < Jumpyshoes> ah, okay, thanks
   2010-11-22 16:23:22 < kierank> ^^ first gci person!!!
   2010-11-22 16:23:37 < holger_> we often have more than one asm function btw. _mmx, _sse2, _ssse3, _sse4 are selfexplaining. then there is _sse2_misalign (amd k10 allows misaligned data loads), _c32/_c64 (cacheline split optimized versions), _fastshuffle (denotes somewhat decent ssse3, excludes conroe and atom)
   2010-11-22 16:23:55 < Jumpyshoes> kierank: i'm a dumbass so don't expect much
   2010-11-22 16:27:14 < holger_> asm isn't that hard in itself. i see dark_shikari already gave you his crash course. you just need to visualize what you're doing (or if you're bad at that, waste a lot of paper documenting what you think you're doing ;)
   2010-11-22 16:27:49 < callahanafk> Just pick one and make a bad attempt.  Then DK's head will explode and he'll fix it for you.
   2010-11-22 16:27:51 < Jumpyshoes> well, it takes me a while to get used to stuff
   2010-11-22 16:28:00 < Jumpyshoes> haha, my initials are actually DK
   2010-11-22 16:28:07 < callahan> DS rather
   2010-11-22 16:28:45 < Jumpyshoes> hopefully it isn't too bad
   2010-11-22 16:28:54 < Jumpyshoes> it only took me three tries to write a three line C function!
   2010-11-22 16:30:01 < holger_> the harder part is debugging asm if it doesn't work. so you need to think before you code. even more than in any other language.
   2010-11-22 16:30:12 < Jumpyshoes> i'm bad at thinking
   2010-11-22 16:30:22 < Jumpyshoes> this will be interesting
   2010-11-22 16:32:04 < Dark_Shikari> so anyways, if more GCI people come on and I'm not here
   2010-11-22 16:32:08 < Dark_Shikari> and nobody else is here to help them
   2010-11-22 16:32:12 < Dark_Shikari> advise them to wait for me
   2010-11-22 16:32:16 < holger_> (visualize: have a mental picture of which register holds what, which values go where, etc. write it down if you have to)
   2010-11-22 16:33:02 < callahan> Meh, just pick one and do it, then fix it 10 times until it's right.
   2010-11-22 16:33:21 < Jumpyshoes> (more like 400 for me)
   2010-11-22 16:33:38 < Dark_Shikari> stop underestimating yourself
   2010-11-22 16:33:47 < callahan> If that's what it takes, start sooner rather than later :)
   2010-11-22 16:34:03 < Jumpyshoes> good thing i have two months
   2010-11-22 16:35:17 < Jumpyshoes> i have the lowbit and highbit functions if anyone wants them
   2010-11-22 16:36:01 < holger_> Jumpyshoes:  there is another task you can do to get your feet wet. (not a gci task though, because we can't seriously expect anyone to succeed) pick any asm function, try to modify it (do things differently, think outside the box) and keep it working. if you manage to get anything faster *g* we'll gladly add a gci task for you to submit your results and get credit
   2010-11-22 16:36:11 < Dark_Shikari> What holger_ said.
   2010-11-22 16:36:37 < Jumpyshoes> cool
   2010-11-22 16:36:57 < Jumpyshoes> that sounds more viable
   2010-11-22 16:37:04 < Dark_Shikari> no, I'd say it's harder
   2010-11-22 16:37:09 < Jumpyshoes> oh really?
   2010-11-22 16:37:19 < Dark_Shikari> making an asm function faster than C is easy
   2010-11-22 16:37:27 < Dark_Shikari> making an asm function faster than holger_'s is lunatic-mode
   2010-11-22 16:37:36 < Jumpyshoes> ._.
   2010-11-22 16:37:49 < Dark_Shikari> of course, not all the asm functions are by holger, so it's not that hard!
   2010-11-22 16:38:06 < Dark_Shikari> In general though, it's a good thing to do so that you learn why code is written like it is
   2010-11-22 16:38:12 < Dark_Shikari> which is a very fast way to learn
   2010-11-22 16:38:27 < Dark_Shikari> if you learn why function A is written with instructions B, C, and D, you'll know when to use them yourself, ec.
   2010-11-22 16:38:30 < Dark_Shikari> etc
   2010-11-22 16:38:44 < Jumpyshoes> i needa go, ttyl
   2010-11-22 16:53:29 < Kovensky> < Dark_Shikari> making an asm function faster than holger_'s is lunatic-mode <-- you mean extra stage ^ 3
   2010-11-22 16:56:40 < holger_> the cheat mode being "do it on k10"
   2010-11-22 16:56:58 < holger_> because we haven't been doing much k10-specific opts yet
   2010-11-22 17:47:46 < bgm0> if anyone insterested there are some good read material here: http://www.stanford.edu/class/ee368b/handouts.html
   2010-11-22 18:16:48 < rfw> mornin' #x264dev
   2010-11-22 18:17:32 < rfw> just stating my interest for doing the GCI regression test tool task
   2010-11-22 18:18:10 < Kovensky> hi rofflwaffls
   2010-11-22 18:18:17 < rfw> hi brazilian
   2010-11-22 18:18:28 < Kovensky> you kiwi :<
   2010-11-22 18:18:28 < rfw> You have requested to claim this task and the request is pending. Please don't submit any work until the request is approved.
   2010-11-22 18:18:29 < rfw> :<
   2010-11-22 18:18:31 < Kovensky> ok, back to topic
   2010-11-22 18:18:32 < Kovensky> lol
   2010-11-22 18:19:26 < rfw> i'm not totally sure how regression testing works though
   2010-11-22 18:19:36 < rfw> is it like unit testing but not unit testing
   2010-11-22 18:19:42 < JEEB> っ the FATE system in ffmpeg
   2010-11-22 18:20:29 < rfw> so, you have the basic tests, like building and configuring
   2010-11-22 18:20:47 < rfw> then you have a few tests that don't have pass or fail
   2010-11-22 18:20:53 < rfw> you just store the results of them
   2010-11-22 18:20:59 < rfw> then you compare those from version to version?
   2010-11-22 18:22:50 < kierank> rfw: for x264 it will be things like major filesize changes or major changes in psnr/ssim that are unexpected
   2010-11-22 18:22:57 < Kovensky> well
   2010-11-22 18:22:59 < kierank> or perhaps things like vbv uderflows
   2010-11-22 18:23:04 < kierank> underflows*
   2010-11-22 18:23:19 < rfw> you're going to tell me what those are, right
   2010-11-22 18:23:21 < kierank> segfaults too
   2010-11-22 18:23:25 < Kovensky> IIRC all what kierank said
   2010-11-22 18:23:33 < rfw> because i have no clue ;_;
   2010-11-22 18:23:34 < Kovensky> I'm epic lagging here so whatever I type is only appearing 20 seconds later D:
   2010-11-22 18:24:03 < kierank> rfw: well for example if you try to encode at 1000kbps and new commits are pushed. The next version ends up creating a file at 1500kbps that's a regression
   2010-11-22 18:24:15 < rfw> ah
   2010-11-22 18:24:22 < JEEB> and x264 outputs PSNR/SSIM data too
   2010-11-22 18:24:27 < rfw> no i meant the pnsr/ssim part
   2010-11-22 18:24:28 < rfw> lol
   2010-11-22 18:24:34 < JEEB> so you can check that and compare to before
   2010-11-22 18:24:43 < kierank> psnr/ssim is a mathematical measurement of the closeness to the source
   2010-11-22 18:24:56 < kierank> if there's a major drop in that it's likely that something went wrong
   2010-11-22 18:25:04 < rfw> ah
   2010-11-22 18:25:07 < rfw> got it
   2010-11-22 18:25:09 < kierank> ideally the regression tool will do a git bisect and find out what patch caused it
   2010-11-22 18:25:14 < kierank> caused the regression i mean
   2010-11-22 18:25:14 < Kovensky> it can be off, but by a max deviation
   2010-11-22 18:25:24 < rfw> so basically, all you need is a tool stores the data of each revision
   2010-11-22 18:25:31 < rfw> then compares it with other revisions?
   2010-11-22 18:25:44 < Kovensky> hurf, I should just stop writing since anything I say is already answered before it appears <_<
   2010-11-22 18:25:54  * rfw pats Kovensky
   2010-11-22 18:26:04 < kierank> rfw: yes something like that
   2010-11-22 18:26:16 < rfw> seems fun to do
   2010-11-22 18:26:52 < Kovensky> and have a cute and fluffy web interface for people to see
   2010-11-22 18:27:05 < kierank> Kovensky: not necessarily
   2010-11-22 18:27:07 < Kovensky> well, disregard the "cute and fluffy" part, unless you really want to :">
   2010-11-22 18:27:31 < Kovensky> well true, not necessary
   2010-11-22 18:27:39 < Kovensky> I'm just borrowing from FATE at this point
   2010-11-22 18:27:46 < Kovensky> but a simple tool to run locally is already p. good
   2010-11-22 18:28:11 < Kovensky> s/but //
   2010-11-22 18:31:56 < rfw> can i just have cute and fluffy cli output
   2010-11-22 18:31:58 < rfw> with colors
   2010-11-22 18:32:44 < holger_> rfw: speed regressions are interesting too. and obviously you'd want quite a diverse selection of videos, not just one.
   2010-11-22 18:33:17 < rfw> well, i'm probably going for a unit-testing fixtures approach
   2010-11-22 18:33:53 < rfw> so i guess that could be easily done
   2010-11-22 18:34:16 < holger_> it's quite possible for every single routine to become faster while x264 overall becomes slower.
   2010-11-22 18:34:37 < holger_> we'd probably see that if we unrolled everything
   2010-11-22 18:35:28 < rfw> heh
   2010-11-22 18:35:30 < rfw> isn't that always the case
   2010-11-22 18:35:32 < nattofriends> funroll loops !
   2010-11-22 18:36:35 < callahan> I always read that as fun roll
   2010-11-22 18:36:39 < holger_> just an example of something unit testing wouldn't catch
   2010-11-22 18:37:54  * microchip_ rollin'
   2010-11-22 18:37:59 < nattofriends> callahan: exactly
   2010-11-22 19:23:37 < rfw> so Kovensky
   2010-11-22 19:23:41 < rfw> where is Dark_Shikari :(
   2010-11-22 19:24:42 < Kovensky> somewhere in california
   2010-11-22 19:26:45 < rfw> no i mean
   2010-11-22 19:27:00 < rfw> didn't you say he was always here
   2010-11-22 19:27:15 < Kovensky> :P
   2010-11-22 19:27:26 < astrange> can't always be awake
   2010-11-22 19:27:41 < JEEB> he sleeps 2-3h at random times of the day and he will look through his pings as he gets back to his keyboard
   2010-11-22 19:27:44 < JEEB> just stay on the channel
   2010-11-22 19:27:46 < BugMaster_> sometimes he pretend to sleep
   2010-11-22 19:27:48 < rfw> lol
   2010-11-22 19:29:23 < rfw> writing python at 8am doesn't seem to be an agreeable experience
   2010-11-22 19:29:38  * Kovensky flames with perl
   2010-11-22 19:29:53 < rfw> TOO BAD YOU'RE GETTING YOUR REGRESSION TESITNG TOOL IN PYTHON
   2010-11-22 19:30:18 < Kovensky> nuu ;_;
   2010-11-22 19:30:31 < JEEB> python is mighty fine
   2010-11-22 19:30:32 < rfw> :D
   2010-11-22 19:31:35 < tjoener> indeed
   2010-11-22 19:31:39 < tjoener> I like Python
   2010-11-22 19:31:41 < tjoener> got a book
   2010-11-22 19:32:30 < rfw> i hope it's not an orly book
   2010-11-22 19:32:36 < komisar> tjoener: .chm from python distibution is fine
   2010-11-22 19:32:39 < komisar> :)
   2010-11-22 19:32:44 < tjoener> heh, I know
   2010-11-22 19:32:53 < tjoener> ive been reading the online documentation
   2010-11-22 19:33:05 < tjoener> but I dont know of anything to make with it
   2010-11-22 19:33:12 < tjoener> so I'm kind of letting it be
   2010-11-22 19:33:51 < komisar> very simple and powerfull script-language
   2010-11-22 19:34:08 < holger_> python makes everything seem so easy. and sometimes it does. in which case your problem was either a) really easy or b) didn't need much performance
   2010-11-22 19:34:37 < tjoener> well yeah
   2010-11-22 19:34:40 < tjoener> thats my idea too
   2010-11-22 19:34:49 < tjoener> I never find a good use for a scripting language
   2010-11-22 19:35:09 < tjoener> except for maybe batch/shell scripts, for which there are batch/shell scripts
   2010-11-22 19:35:18 < elenril> python isn't just scripting
   2010-11-22 19:35:30 < JEEB> > batch scripts
   2010-11-22 19:35:31  * elenril wrote an mpd client in it
   2010-11-22 19:35:31 < JEEB> eww
   2010-11-22 19:35:35 < tjoener> yeah I know
   2010-11-22 19:35:36 < djahandarie> I use Haskell for most everything I need
   2010-11-22 19:35:54 < Kovensky> tjoener: do you seriously consider batch scripts for stuff? D:
   2010-11-22 19:35:57 < Kovensky> plz2use perl
   2010-11-22 19:36:15 < tjoener> naah, mostly ridiculously evil stuff
   2010-11-22 19:36:24 < tjoener> running a few programes on a file
   2010-11-22 19:36:28 < tjoener> not much else
   2010-11-22 19:36:31 < Kovensky> though if you need good internationalization support you're better off with python3, assuming they did the win32 part right
   2010-11-22 19:37:00 < elenril> >implying anybody uses python3
   2010-11-22 19:37:12 < tjoener> whats wrong with python 3?
   2010-11-22 19:37:17 < tjoener> except for print()
   2010-11-22 19:37:42 < elenril> not enough support
   2010-11-22 19:37:51 < tjoener> ah
   2010-11-22 19:38:01  * elenril can't port his client to py3 because qt4 in debian only supports py2
   2010-11-22 19:38:18 < elenril> also scipy/numpy only support py2 iirc
   2010-11-22 19:38:19 < tjoener> hmmm
   2010-11-22 19:38:26 < tjoener> numpy is nice
   2010-11-22 19:39:46 < Kovensky> what is numpy
   2010-11-22 19:39:48 < Kovensky> numbers for python? :P
   2010-11-22 19:39:54  * elenril wishes they taught physicists how2write readable/maintainable code
   2010-11-22 19:40:10 < elenril> Kovensky: http://numpy.scipy.org/ =p
   2010-11-22 19:40:25 < komisar> py3/py2 usefull for self-made script/program... in mingw/*nix/windows... :)
   2010-11-22 19:40:30 < tjoener> http://www.boingboing.net/2010/11/22/howto-make-a-stupend.html?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+boingboing%2FiBag+%28Boing+Boing%29&utm_content=Google+Reader
   2010-11-22 19:40:35 < tjoener> lol
   2010-11-22 19:40:36 < tjoener> loved those when I was a kid
   2010-11-22 19:41:13 < tjoener> I'm thinking of skipping python and looking at something functional
   2010-11-22 19:41:21 < rfw> [08:39:47] <Kovensky> numbers for python? :P <-- o u
   2010-11-22 19:41:25 < tjoener> like lisp or scheme or ...
   2010-11-22 19:41:34  * Kovensky votes for common lisp
   2010-11-22 19:42:23 < tjoener> yeah
   2010-11-22 19:42:32 < tjoener> lisp isnt that bad
   2010-11-22 19:42:35 < tjoener> F#? :)
   2010-11-22 19:42:42 < Kovensky> idk about F#
   2010-11-22 19:43:15 < tjoener> naah
   2010-11-22 19:43:21 < tjoener> I'm to addicted to .NET allready
   2010-11-22 19:43:26 < tjoener> should learn something else
   2010-11-22 19:43:34 < elenril> >.net
   2010-11-22 19:43:39  * elenril runs away screaming
   2010-11-22 19:43:52 < tjoener> elenril: It's frikkin nice
   2010-11-22 19:44:28 < elenril> <a reply bashing microsoft>
   2010-11-22 19:45:32 < tjoener> and what about Mono?
   2010-11-22 19:45:50 < Kovensky> reply bashing novell?
   2010-11-22 19:45:58 < tjoener> lol :D
   2010-11-22 19:46:19 < tjoener> Kovensky: whats the most used common lisp interpreter/compiler/runtime?
   2010-11-22 19:46:40 < tjoener> I dont know what's with all the people bashing .NET and Mono
   2010-11-22 19:46:54 < komisar> .net -- suks
   2010-11-22 19:46:54 < tjoener> What did that language ever do to you? :)
   2010-11-22 19:47:05 < elenril> didn't novel get bought my microsoft sometime today?
   2010-11-22 19:49:36 < astrange> the most common free one is sbcl
   2010-11-22 19:49:48 < tjoener> lets see
   2010-11-22 19:51:37 < BugMaster> -> #x264 or anywhere else
   2010-11-22 19:52:21 < BugMaster> or this is for google project?
   2010-11-22 19:52:25 < tjoener> sorry BugMaster
   2010-11-22 19:55:21 < rfw> well then, that's a basic unit testing framework done
   2010-11-22 19:55:44 < astrange> unit or regression testing?
   2010-11-22 19:55:49 < rfw> well
   2010-11-22 19:55:56 < rfw> i'm starting with a unit testing framework
   2010-11-22 19:56:01 < rfw> then adding regression testing to it
   2010-11-22 19:56:11 < rfw> since regression testing has most aspects of unit testing
   2010-11-22 19:56:44 < astrange> not necessarily, running the entire system and making sure it has the same outputs (when you want it to have the same outputs) is an effective regression test
   2010-11-22 19:57:11 < rfw> well, i have classes that encapsulate results that compare values from revision to revision
   2010-11-22 19:57:33 < rfw> the whole thing is horrendously extensible
   2010-11-22 19:59:49 < holger_> rfw: we already have unit testing. for comparing asm implementations of functions to their c reference.
   2010-11-22 20:00:16 < rfw> i know
   2010-11-22 20:00:25 < rfw> but unit tests only have pass/fail results, right?
   2010-11-22 20:06:29 < BugMaster> and now the funny/sad fact. after fixing weight-p bug results of gcc 4.4.5 build and gcc 4.5.2 builds still differ: http://privatepaste.com/b4380671ef
   2010-11-22 20:06:29 < BugMaster> no artifacts and encoder/decoder desync, but wieght-p is used more and chroma psnr higher in *gcc 4.5.2* build
   2010-11-22 20:06:29 < BugMaster> so it seems like miscompilation in *gcc 4.4.5* which probably also prevent previous bug to occur in this version
   2010-11-22 20:06:29 < BugMaster> Dark_Shikari: ^
   2010-11-22 20:08:17 < BugMaster> or strange miscompilation in 4.5.2 which increase quality
   2010-11-22 20:08:33 < nattofriends> ^ i like this idea
   2010-11-22 20:09:44 < Kovensky> why
   2010-11-22 20:09:52 < tjoener> just compile it all with -S and see what the asm does :)
   2010-11-22 20:09:56 < Kovensky> it means that gcc provides better results while broken than when working properly
   2010-11-22 20:09:57 < BugMaster> --asm and --no-asm version identical for the same build. so this time it is not asm
   2010-11-22 20:11:44 < tjoener> and no-asm on both versions?
   2010-11-22 20:12:01 < BugMaster> no-asm between version differ
   2010-11-22 20:13:15 < tjoener> stupid gcc
   2010-11-22 20:13:36 < tjoener> I dont understand why they cant make a program compile right under different MINOR versions
   2010-11-22 20:13:55 < tjoener> Isnt that the whole point of a compiler?
   2010-11-22 20:15:27 < dj_tjerk> someone test with icc ;)
   2010-11-22 20:15:30 < BugMaster> hm. gcc 4.5.2 with -O0 same result as 4.4.5
   2010-11-22 20:15:49 < JEEB> interesting
   2010-11-22 20:16:03 < BugMaster> so now I more think about "or strange miscompilation in 4.5.2 which increase quality"
   2010-11-22 20:16:30 < BugMaster> that mean we missed some way to improve weight-p :-D
   2010-11-22 20:16:35 < JEEB> law
   2010-11-22 20:16:37 < JEEB> l
   2010-11-22 20:16:39 < Dark_Shikari> BugMaster: lolwhat
   2010-11-22 20:16:57 < Dark_Shikari> rfw: we already have unit tests
   2010-11-22 20:17:01 < Gramner> it means gcc has gained artificial intelligence and is able to improve the algorithms
   2010-11-22 20:17:02 < Dark_Shikari> we don't need more of it
   2010-11-22 20:17:06 < rfw> i know
   2010-11-22 20:17:11 < rfw> but what i mean
   2010-11-22 20:17:29 < rfw> is you have test cases that return results which can be compared from one revision to another
   2010-11-22 20:18:06 < Dark_Shikari> explicit test cases are a bad idea, it should test permutations
   2010-11-22 20:18:20 < rfw> what do you mean exactly
   2010-11-22 20:18:41 < tjoener> BugMaster: what about the different tests like those in fprofiled?
   2010-11-22 20:19:15 < BugMaster> "we missed some way to improve weight-p" <- probably use weight-p on chroma without weighted lume. because currently we not analyse it as I understand if we don't have luma weight
   2010-11-22 20:19:19 < tjoener> isnt that something that can narrow down what function gcc likes to change
   2010-11-22 20:19:20 < tjoener> ?
   2010-11-22 20:20:00 < Dark_Shikari> BugMaster: I tested that
   2010-11-22 20:20:12 < Dark_Shikari> useless to run when luma isn't weighted
   2010-11-22 20:20:14 < Dark_Shikari> and it saves a ton of time
   2010-11-22 20:20:40 < Dark_Shikari> rfw: see my regresion teest sript
   2010-11-22 20:20:43 < Dark_Shikari> http://pastebin.com/sHkmCak5
   2010-11-22 20:20:49 < Dark_Shikari> it works via permutations
   2010-11-22 20:20:59 < Dark_Shikari> whenever I find a case that my script missed, I make it 2x slower, lol
   2010-11-22 20:21:04 < Dark_Shikari> by adding another loop
   2010-11-22 20:21:13 < BugMaster> dunno. but this is the only thing what I think can be miscompiled and gain quality
   2010-11-22 20:21:23 < rfw> i wish i could read that lol
   2010-11-22 20:21:36 < Dark_Shikari> rfw: didn't the regression test task specifically tell you to look at mine? =p
   2010-11-22 20:21:37 < JEEB> it has lots of for loops
   2010-11-22 20:21:44 < Dark_Shikari> anyways my script is 2 minutes of work and shit
   2010-11-22 20:21:50 < Dark_Shikari> I'd rather randomly test than permutation-test
   2010-11-22 20:21:52 < Dark_Shikari> permutation test is too slow
   2010-11-22 20:22:12 < Dark_Shikari> "random" being rather pseudo, so it's replicable
   2010-11-22 20:22:25 < rfw> well
   2010-11-22 20:22:33 < rfw> can't you just do permutations in a single test case
   2010-11-22 20:22:35 < Amit> hi, i'd like to start working on the assembly task from the Google Code In contest, it says there that i should come here
   2010-11-22 20:22:40 < Dark_Shikari> welcome!
   2010-11-22 20:22:58 < Dark_Shikari> rfw: permutations define 2^N tests instead of N tests
   2010-11-22 20:23:05 < Dark_Shikari> where N is the number of test cases you've written
   2010-11-22 20:23:29 < Dark_Shikari> er, ok
   2010-11-22 20:23:37 < Dark_Shikari> Amit: yes, you're in the right place
   2010-11-22 20:23:42 < Amit> great
   2010-11-22 20:23:50 < Amit> what do i need to do now?
   2010-11-22 20:24:02 < rfw> i'm still kinda confused
   2010-11-22 20:24:04 < rfw> lol
   2010-11-22 20:24:11 < rfw> how does that work
   2010-11-22 20:24:17 < Dark_Shikari> rfw: ok, suppose I have 5 options, each of which can be 0 or 1
   2010-11-22 20:24:18 < rfw> how are the tests comparable to each other?
   2010-11-22 20:24:26 < Dark_Shikari> that involves 32 tests.
   2010-11-22 20:24:31 < Dark_Shikari> A0 B0 C0 D0 E0
   2010-11-22 20:24:34 < Dark_Shikari> A0 B0 C0 D0 E1...
   2010-11-22 20:24:36 < Dark_Shikari> etc
   2010-11-22 20:24:53 < rfw> so you're comparing each test against another?
   2010-11-22 20:24:55 < Dark_Shikari> Amit: ok, you'll need to check out a copy of x264
   2010-11-22 20:24:56 < Dark_Shikari> rfw: no
   2010-11-22 20:25:04 < Dark_Shikari> the regression test makes sure that JM decodes the file in the same way x264 thinks it should.
   2010-11-22 20:25:14 < Dark_Shikari> This is the simplest and easiest form of regression test.
   2010-11-22 20:25:17 < Dark_Shikari> It does not find all bugs.
   2010-11-22 20:25:21 < Dark_Shikari> But it finds most really really bad bugs
   2010-11-22 20:25:34 < Dark_Shikari> Amit: sorry, even my typing speed is limited here
   2010-11-22 20:25:35 < rfw> so you compare one set of results
   2010-11-22 20:25:38 < rfw> to another
   2010-11-22 20:25:39 < dj_tjerk> --dump-yuv?
   2010-11-22 20:25:42 < Dark_Shikari> rfw: --dump-yuv
   2010-11-22 20:25:45 < Amit> no probs :P help him first
   2010-11-22 20:25:50 < Dark_Shikari> it dumps x264's internal representation of the video
   2010-11-22 20:25:55 < Dark_Shikari> with that, you can compare to what the decoder sees
   2010-11-22 20:26:02 < Dark_Shikari> if it doesn't match bit-exact, it's wrong
   2010-11-22 20:26:05 < rfw> ah
   2010-11-22 20:26:19 < Dark_Shikari> This is exacerbated by the fact that the decoder is not always 100% trustworthy ;) ;)
   2010-11-22 20:26:25 < Dark_Shikari> That is, JM has bugs.
   2010-11-22 20:26:34 < Dark_Shikari> Amit: so, have you done asm before?
   2010-11-22 20:26:34 < rfw> that seems more of a unit test though
   2010-11-22 20:26:40 < Amit> yes
   2010-11-22 20:26:52 < pengvado> the whole encoder isn't a "unit"
   2010-11-22 20:27:05 < Dark_Shikari> unit test usually means test one function
   2010-11-22 20:27:17 < Dark_Shikari> which usually means you've gone so batshit crazy on your OO that you should be thrown into a fire
   2010-11-22 20:27:24 < Dark_Shikari> Amit: x86, altivec, or neon?
   2010-11-22 20:27:29 < Amit> x86
   2010-11-22 20:27:38 < Dark_Shikari> ok great, have you done mmx or sse?
   2010-11-22 20:28:43 < Dark_Shikari> (not required, obviously you can just use your friendly neighborhood nasm manual and instruction table to look things up if you haven't)
   2010-11-22 20:29:54 < Amit> i think that i haven't done any of them
   2010-11-22 20:29:55 < pengvado> well, it would be nice if we could unit test everything. but asm is the only case where it's easy.
   2010-11-22 20:30:04 < Dark_Shikari> yeah.
   2010-11-22 20:30:06 < Amit> i studied the language but haven't yet worked on a real project
   2010-11-22 20:30:32 < Dark_Shikari> you will have to do some learning, as x264 uses its own set of yasm macros to make asm coding easier
   2010-11-22 20:30:37 < Dark_Shikari> i.e. to do things like popping, pushing, etc for you
   2010-11-22 20:30:41 < Dark_Shikari> to track the stack
   2010-11-22 20:30:52 < Dark_Shikari> but of course, those are intended to make it easier, not harder.
   2010-11-22 20:31:04 < Amit> ok
   2010-11-22 20:31:06 < Dark_Shikari> so your tasks in order:
   2010-11-22 20:31:08 < Dark_Shikari> 1) check out x264
   2010-11-22 20:31:10 < Dark_Shikari> 2) build x264
   2010-11-22 20:31:14 < Dark_Shikari> 3) make checkasm
   2010-11-22 20:31:17 < Dark_Shikari> 4) run checkasm
   2010-11-22 20:31:27 < Dark_Shikari> you've now run the x264 asm unit tester, which automatically checks all enabled asm functions in x264 for errors.
   2010-11-22 20:31:40 < Dark_Shikari> once you have that, you can go to pick a function to write.
   2010-11-22 20:32:05 < tjoener> its that easy?
   2010-11-22 20:32:16 < Dark_Shikari> No, the writing is harder ;)
   2010-11-22 20:32:23 < Dark_Shikari> the number 1 rule of any of this: ask questions.  it is better to ask a dumb question than to get stuck in confusion.
   2010-11-22 20:32:23 < tjoener> hmmm, maybe I'll look into the asm then :)
   2010-11-22 20:32:36 < Dark_Shikari> also, there are no stupid questions, just stupid people.
   2010-11-22 20:32:37 < tjoener> used some intrinsics, so I know my way around SSE abit
   2010-11-22 20:32:52 < Dark_Shikari> btw, also, the asm tasks are unlimited
   2010-11-22 20:33:00 < Dark_Shikari> i.e. if we run out on GCI interface we can add more later
   2010-11-22 20:33:07 < Dark_Shikari> so don't worry if there aren't any left at any pointl.
   2010-11-22 20:33:20 < Dark_Shikari> well, I mean, they are limited by how much is available to complete, but I'm pretty sure we won't run out of that.
   2010-11-22 20:34:06 < Amit> where do i find which functions should be rewritten?
   2010-11-22 20:34:19 < tjoener> maybe some MPSADBW ?
   2010-11-22 20:34:46 < Dark_Shikari> Amit: well let's give an introduction to the situation first
   2010-11-22 20:34:58 < Dark_Shikari> In normal bit depth mode, pixels are 8-bit values (uint8_t)
   2010-11-22 20:35:04 < Dark_Shikari> and dct coefficients are 16-bit values (int16_t)
   2010-11-22 20:35:19 < Dark_Shikari> for this case, nearly all possible x86 asm is written and reasonably well-optimized.
   2010-11-22 20:35:26 < Dark_Shikari> High bit depth is new.
   2010-11-22 20:35:31 < Dark_Shikari> In high bit depth, pixels are uint16_t.
   2010-11-22 20:35:36 < Dark_Shikari> and dct coeffs are int32_t.
   2010-11-22 20:35:43 < Dark_Shikari> There's less asm in this mode; many critical functions are missing.
   2010-11-22 20:35:57 < Dark_Shikari> You can see this by running checkasm normally, then reconfiguring with --bit-depth=10, rebuilding checkasm, and running again.
   2010-11-22 20:36:24 < Dark_Shikari> By the way, if you decide you can optimize an existing asm function -- and you succeed -- I'll give you a GCI task-equivalent for that too.
   2010-11-22 20:37:36 < Amit> ok
   2010-11-22 20:37:58 < Dark_Shikari> Now, of course, you're expected to ask questions as we go through this
   2010-11-22 20:38:09 < Dark_Shikari> steps to adding a new asm function, or version of an asm function:
   2010-11-22 20:38:28 < Dark_Shikari> 1) All C code equivalents for asm functions is in common/X.c, where X is the name of the function category
   2010-11-22 20:38:37 < Dark_Shikari> so for example DCT code is in common/dct.c
   2010-11-22 20:39:07 < Dark_Shikari> 2) You'll find functions in those files that load function pointers for all the asm functions which exist.  Add yours there under the appropriate place (MMX, SSE, etc)
   2010-11-22 20:39:16 < Dark_Shikari> 3) Add your function declaration next to all the others in the appropriate .h file in common/x86/*
   2010-11-22 20:39:23 < Dark_Shikari> 4) Find the appropriate asm file in common/x86/*.asm
   2010-11-22 20:39:42 < Dark_Shikari> 5) Find the existing 8-bit code for the function, and figure out how it works, preferably by asking questions in addition to staring at it
   2010-11-22 20:39:55 < Dark_Shikari> (while keeping the C code as a reference)
   2010-11-22 20:40:15 < Dark_Shikari> 6) write your version of the high bit-depth version.
   2010-11-22 20:40:28 < Dark_Shikari> So for example, one that's missing is dequant, in quant-a.asm, with quant.c for the C stuff.
   2010-11-22 20:40:59 < Dark_Shikari> The C version of this function is about 10 lines and should be pretty easy to read.
   2010-11-22 20:42:03 < Dark_Shikari> don't worry too much about optimization when first writing the function: I can make comments on it later.
   2010-11-22 20:42:25 < Dark_Shikari> a good way to spot missing functions is to run ./checkasm --bench with and without --bit-depth=10 in configure.
   2010-11-22 20:42:37 < Dark_Shikari> it does a benchmark of *all* asm functions and nicely lists them for you.
   2010-11-22 20:45:56 < callahan> Dark_Shikari: Emergency mode works well so far.  You should commit it...
   2010-11-22 20:46:18 < Dark_Shikari> I'll get to it, maybe this week or next
   2010-11-22 20:46:22 < Dark_Shikari> I have a few other changes I have to make
   2010-11-22 20:46:23 < Dark_Shikari> and I'm busy
   2010-11-22 20:46:30 < nattofriends> emergency mode?
   2010-11-22 20:46:40 < nattofriends> does that give x264 big red flashing lights?
   2010-11-22 20:46:41 < callahan> Yeah, GCI craziness
   2010-11-22 20:46:46 < Dark_Shikari> lol
   2010-11-22 20:46:55 < Dark_Shikari> it makes x264 not die when you throw /dev/random at it
   2010-11-22 20:47:54 < rfw> Dark_Shikari: can i ask more dumb questions about regression testing
   2010-11-22 20:48:06 < rfw> since i still don't seem to be 100% clear about it
   2010-11-22 20:48:08 < Dark_Shikari> Don't ask to ask
   2010-11-22 20:48:12 < komisar> Dark_Shikari: what about auto-levels patch?
   2010-11-22 20:48:13 < rfw> well
   2010-11-22 20:48:13 < Dark_Shikari> just ask
   2010-11-22 20:48:19 < rfw> i still don't get what you mean by permutations
   2010-11-22 20:48:19 < Dark_Shikari> komisar: oh, that should be higher priority, I'll get it in next
   2010-11-22 20:49:00 < Dark_Shikari> Suppose I have options A, B, and C.
   2010-11-22 20:49:03 < rfw> oh, i get it now
   2010-11-22 20:49:09 < Dark_Shikari> I can test with no options
   2010-11-22 20:49:09 < rfw> replacing ; with ;\n helped a lot
   2010-11-22 20:49:10 < Dark_Shikari> just A
   2010-11-22 20:49:12 < Dark_Shikari> just B
   2010-11-22 20:49:12 < Dark_Shikari> just C
   2010-11-22 20:49:15 < Dark_Shikari> A and B
   2010-11-22 20:49:17 < Dark_Shikari> B and C
   2010-11-22 20:49:20 < Dark_Shikari> A, B and C
   2010-11-22 20:49:20 < rfw> yeah i understand
   2010-11-22 20:49:23 < Dark_Shikari> ok, so combinations, not permutations
   2010-11-22 20:49:25 < Dark_Shikari> but whatever! ;)
   2010-11-22 20:49:35 < rfw> cartesian product actually :)
   2010-11-22 20:50:23 < Gramner> you missed "A and C"!
   2010-11-22 20:50:30 < Dark_Shikari> ah yes.
   2010-11-22 20:56:41 < tjoener> damnit
   2010-11-22 20:56:47 < tjoener> terminal locked my alt keys :@
   2010-11-22 20:58:12 < j-b> Dark_Shikari: http://www.google-melange.com/gci/task/show/google/gci2010/videolan/t128908283186 and http://www.google-melange.com/gci/task/show/google/gci2010/videolan/t128908435924
   2010-11-22 20:58:38 < Dark_Shikari> I know
   2010-11-22 20:58:41 < Dark_Shikari> they've already shown up here
   2010-11-22 21:13:52 < j-b> Dark_Shikari: so you need to approve at some point, I guess
   2010-11-22 21:14:40 < Dark_Shikari> oh I do?
   2010-11-22 21:16:02 < Dark_Shikari> done
   2010-11-22 21:45:54 < rfw> i think i'm taking too much time to time to make a test suite than to actually make the tests
   2010-11-22 21:46:05 < rfw> and wow that sentence was badly formed
   2010-11-22 21:47:16 < Dark_Shikari> rfw: the tests are easy
   2010-11-22 21:47:19 < Dark_Shikari> the hard part is interpreting them
   2010-11-22 21:47:26 < Dark_Shikari> that is, for example
   2010-11-22 21:47:28 < rfw> ah
   2010-11-22 21:47:33 < Dark_Shikari> really easy interpretation: compare yuvs, see if encoder matches decoder
   2010-11-22 21:47:38 < Dark_Shikari> that's trivial: a binary decision
   2010-11-22 21:47:39 < Dark_Shikari> 1 or 0
   2010-11-22 21:47:42 < rfw> yeah
   2010-11-22 21:47:43 < Dark_Shikari> is it right or not.
   2010-11-22 21:47:52 < Dark_Shikari> But of course, we might also want to know what frame it's wrong on, if it failed.
   2010-11-22 21:47:57 < Dark_Shikari> Or if the decoder failed to output all the frames.
   2010-11-22 21:47:59 < Dark_Shikari> i.e. if it crashed, etc.
   2010-11-22 21:48:07 < Dark_Shikari> And what macroblock it's wrong on (i.e. where in the frame)
   2010-11-22 21:48:17 < Dark_Shikari> And then, we might want to investigate more complex things
   2010-11-22 21:48:21 < Dark_Shikari> like for example, compare PSNR between two revisions
   2010-11-22 21:48:27 < rfw> do you have examples testing for macroblocks
   2010-11-22 21:48:37 < Dark_Shikari> well that's very easy, you just have to do the math
   2010-11-22 21:48:40 < rfw> since i have no idea about how YUV data works
   2010-11-22 21:48:46 < Dark_Shikari> each frame is layed out as follows:
   2010-11-22 21:49:05 < Dark_Shikari> a 2D array of width WIDTH and height HEIGHT, containing Y
   2010-11-22 21:49:12 < Dark_Shikari> a 2D array of width WIDTH/2 and height HEIGHT/2, containing U
   2010-11-22 21:49:13 < Dark_Shikari> a 2D array of width WIDTH/2 and height HEIGHT/2, containing V
   2010-11-22 21:49:17 < rfw> ah
   2010-11-22 21:49:20 < Dark_Shikari> so the total size is 1.5 * WIDTH * HEIGHT
   2010-11-22 21:49:26 < rfw> so i just spew out the part where it mismatches?
   2010-11-22 21:49:28 < Dark_Shikari> so knowing the size of each frame, you can figure out from any offset in the file
   2010-11-22 21:49:31 < Dark_Shikari> a) what frame it's in
   2010-11-22 21:49:34 < Dark_Shikari> b) what macroblock it's in
   2010-11-22 21:49:42 < rfw> how is a macroblock defined
   2010-11-22 21:49:51 < Dark_Shikari> the frame is split into 16x16 blocks
   2010-11-22 21:49:59 < Dark_Shikari> (well, 16x16 of luma, obviously each 16x16 of Y is 8x8 of U and V)
   2010-11-22 21:50:04 < Dark_Shikari> since U and V are half size
   2010-11-22 21:50:08 < Dark_Shikari> these are arranged in raster order
   2010-11-22 21:50:11 < rfw> ah
   2010-11-22 21:50:15 < Dark_Shikari> so for example, frame 57 might be bad at macroblock (5,17)
   2010-11-22 21:50:38 < rfw> i see, so
   2010-11-22 21:50:44 < rfw> for a rudimentary comparison of two outputs
   2010-11-22 21:50:47 < rfw> i could just checksum them
   2010-11-22 21:50:51 < rfw> then if they mismatch
   2010-11-22 21:50:57 < rfw> i compare frames, then macroblocks?
   2010-11-22 21:52:01 < Dark_Shikari> no
   2010-11-22 21:52:12 < Dark_Shikari> first you check to see the filesize are the same
   2010-11-22 21:52:14 < Dark_Shikari> if not, report an error
   2010-11-22 21:52:28 < Dark_Shikari> second, you find the first byte in the two files that differs
   2010-11-22 21:52:33 < Dark_Shikari> then you calculate which frame and MB it belongs to.
   2010-11-22 21:52:58 < rfw> ah
   2010-11-22 21:53:05 < rfw> this sounded so much easier before
   2010-11-22 21:54:04 < Dark_Shikari> the more fancy part of the tool is wrapping around this comparison
   2010-11-22 21:54:05 < Dark_Shikari> for example
   2010-11-22 21:54:13 < Dark_Shikari> suppose I know the latest x264 is broken
   2010-11-22 21:54:16 < Dark_Shikari> and I want to know what broke it
   2010-11-22 21:54:28 < Dark_Shikari> your script could run git bisect using your comparison script
   2010-11-22 21:54:35 < Dark_Shikari> so in effect, it's modular:
   2010-11-22 21:54:37 < rfw> yeah
   2010-11-22 21:54:47 < Dark_Shikari> 1) Comparison: comparing two revisions in some way (whether it be via yuv dump, psnr, etc)
   2010-11-22 21:54:53 < rfw> but i'm decoupling the scm from the core so i can't really run git bisect
   2010-11-22 21:54:58 < Dark_Shikari> 2) How we use those comparisons (checking multiple revisions, etc)
   2010-11-22 21:55:32 < rfw> well, what my idea is is to create a couple of fixtures which can be used to test every revision
   2010-11-22 21:55:40 < rfw> which generates a dump of the results
   2010-11-22 21:55:49 < rfw> then those can be compared with the tool from revision to revision
   2010-11-22 21:56:39 < Dark_Shikari> well, keep in mind that whatever yours does, it must do more than my crappy script
   2010-11-22 21:56:42 < Dark_Shikari> ;)
   2010-11-22 21:56:44 < Dark_Shikari> i.e. enough to make it worthwhile
   2010-11-22 21:56:49 < rfw> oh it already does more
   2010-11-22 21:56:50 < rfw> lol
   2010-11-22 21:56:52 < Dark_Shikari> it should also be self-contained and not require really fancy other libs
   2010-11-22 21:56:55 < Dark_Shikari> if possible
   2010-11-22 21:57:02 < Dark_Shikari> though that's not required if you gt a big benefit from some other lib
   2010-11-22 21:57:09 < rfw> well
   2010-11-22 21:57:10 < Dark_Shikari> just don't cover it in boost or something
   2010-11-22 21:57:14 < rfw> oh it's python
   2010-11-22 21:57:15 < rfw> lol
   2010-11-22 21:57:17 < Dark_Shikari> good
   2010-11-22 21:57:17 < Dark_Shikari> lol
   2010-11-22 21:57:25 < rfw> boost gives me nightmares
   2010-11-22 21:57:32 < Dark_Shikari> you're not the only one
   2010-11-22 21:57:48 < Dark_Shikari> when I worked at facebook, one of my coworkers attempted to use almost every single boost feature in every project
   2010-11-22 21:58:17 < rfw> how many screens of template errors does that make
   2010-11-22 21:58:34 < Dark_Shikari> I've seen a single *symbol* in a C++ program that was over 30 kilobytes
   2010-11-22 21:59:25 < Jumpyshoes> hey Dark_Shikari, i'm taking a look at some functions, and some call macros (like TRANSPOSE4x4w), does the higher bit depth have an equivalent of these, or do i need to check on a case by case basis?
   2010-11-22 21:59:29 < checkers> I thought facebook used PHP? Do they write some stuff in C++?
   2010-11-22 21:59:39 < Dark_Shikari> flvtool++ is C++
   2010-11-22 21:59:42 < Dark_Shikari> along with lots of other internal tools
   2010-11-22 21:59:43 < djahandarie> Facebook uses all sorts of languages, but yeah mainly PHP
   2010-11-22 21:59:53 < Dark_Shikari> Jumpyshoes: If there isn't one, you'll have to write it!
   2010-11-22 22:00:05 < Dark_Shikari> A good start is to look at functions that use TRANSPOSE4x4W
   2010-11-22 22:00:19 < Dark_Shikari> if there's a high bit depth version, the high bit depth version likely calls the high bit depth version of TRANSPOSE4x4W
   2010-11-22 22:01:11 < Jumpyshoes> let's see
   2010-11-22 22:01:14 < Dark_Shikari> since the normal and high bit depth do the same thing, just with different data types.
   2010-11-22 22:01:26 < Jumpyshoes> TRANSPOSE4x4W calls other macros haha
   2010-11-22 22:02:12 < Dark_Shikari> yup, SBUTTERFLY
   2010-11-22 22:02:15 < Dark_Shikari> a transpose is a series of butterflies
   2010-11-22 22:02:23 < Dark_Shikari> see "butterfly diagram" on wikipedia
   2010-11-22 22:02:42 < Jumpyshoes> would i need to write that too?
   2010-11-22 22:03:37 < Dark_Shikari> no, a butterfly is a generic operation
   2010-11-22 22:03:44 < Dark_Shikari> not restrained to any data type
   2010-11-22 22:03:49 < Dark_Shikari> that is, you tell it the data type to take
   2010-11-22 22:03:51 < Dark_Shikari> it's a three line macro anyways!
   2010-11-22 22:04:00 < Jumpyshoes> true
   2010-11-22 22:04:36 < Jumpyshoes> TRANSPOSE4x4W <-- what does the W at the end signify?
   2010-11-22 22:05:11 < Dark_Shikari> words
   2010-11-22 22:05:13 < Dark_Shikari> 16-bit
   2010-11-22 22:05:27 < Dark_Shikari> so if the low bit depth function uses 16-bit intermediate data
   2010-11-22 22:05:35 < Dark_Shikari> and you decide to use 32-bit intermediates instead for high bit depth
   2010-11-22 22:05:38 < Dark_Shikari> you'll need TRANSPOSE4x4D
   2010-11-22 22:05:53 < Jumpyshoes> ah, i see
   2010-11-22 22:07:33 < Dark_Shikari> so transpose doesn't have a native "bit depth"
   2010-11-22 22:07:37 < Dark_Shikari> rather it has a size of element it operates on
   2010-11-22 22:07:42 < Dark_Shikari> and that may or may not be the size you need.
   2010-11-22 22:08:32 < Jumpyshoes> i see
   2010-11-22 22:08:54 < Dark_Shikari> note that intermediate sizes aren't always higher in high bit depth
   2010-11-22 22:09:02 < Dark_Shikari> for example, in satd, you can still get away with 16-bit intermediates with 10-bit input
   2010-11-22 22:09:05 < Dark_Shikari> this was a huge boon for speed
   2010-11-22 22:09:40 < Dark_Shikari> (satd is one of those that's done, since it's the most important asm function in x264)
   2010-11-22 22:10:03 < Jumpyshoes> out of curiosity, why do the sse* asm functions seem to be longer and more complicated then the mmx ones?
   2010-11-22 22:10:50 < Dark_Shikari> depends, which ones are you looking at?
   2010-11-22 22:11:10 < Jumpyshoes> add4x4_idct
   2010-11-22 22:11:17 < Dark_Shikari> that's a special case
   2010-11-22 22:11:24 < Dark_Shikari> a 4x4 idct needs, at most, 64 bits worth of register
   2010-11-22 22:11:28 < Dark_Shikari> i.e. 4 16-bit values
   2010-11-22 22:11:31 < Dark_Shikari> because, well, it's 4 wide
   2010-11-22 22:11:33 < Dark_Shikari> and the values are 16-bit
   2010-11-22 22:11:35 < Dark_Shikari> so, naturally
   2010-11-22 22:11:48 < Dark_Shikari> So, if you want to take advantage of SSE, you do multiple idcts at a time
   2010-11-22 22:11:55 < Dark_Shikari> as is done in the larger ones
   2010-11-22 22:11:57 < Dark_Shikari> But...
   2010-11-22 22:12:09 < Dark_Shikari> in some places in x264, we can only do a 4x4 idct for technical reasons, i.e. we can only do one at a time
   2010-11-22 22:12:27 < Dark_Shikari> So, for the fun of it and the challenge, holger wrote an SSE4 implementation that tries to take advantage of the extra register space
   2010-11-22 22:12:30 < Dark_Shikari> through horrible horrible munging
   2010-11-22 22:12:40 < Jumpyshoes> oh
   2010-11-22 22:12:42 < Dark_Shikari> It's a decent bit faster.
   2010-11-22 22:12:53 < Dark_Shikari> But it's far more complicated and harder to read because it's doing things in a completely nonintutive, ugly way.
   2010-11-22 22:12:57 < Dark_Shikari> In order to stuff more values into one register.
   2010-11-22 22:13:22 < Jumpyshoes> yea, it sure looks harder to read
   2010-11-22 22:13:51 < Dark_Shikari> remember width 4 SAD?
   2010-11-22 22:13:53 < Dark_Shikari> with the punpckldq?
   2010-11-22 22:14:01 < Dark_Shikari> that's an example of munging to take advantage of a register wider than your data.
   2010-11-22 22:14:11 < Dark_Shikari> sse4 idct 4x4 is another one.
   2010-11-22 22:14:41 < Jumpyshoes> aahh
   2010-11-22 22:14:42 < Dark_Shikari> In general, in high bit depth, you'll almost never have this problem, since high bit depth has much larger data types.
   2010-11-22 22:14:53 < Dark_Shikari> 4x4 idct, btw, I think has no high bit depth implementation.
   2010-11-22 22:15:02 < Dark_Shikari> so that could be a good starting point
   2010-11-22 22:15:03 < Jumpyshoes> yea, as far as i can tell, it doesn't
   2010-11-22 22:15:07 < Jumpyshoes> which is why i was looking at it
   2010-11-22 22:15:12 < Dark_Shikari> Yeah, that would be a good one
   2010-11-22 22:15:22 < Dark_Shikari> Not too complex, pretty straightforward
   2010-11-22 22:15:24 < Jumpyshoes> do you have a link that actually explains h264's DCT?
   2010-11-22 22:15:31 < Dark_Shikari> As long as you stay very very far away from the sse4 oen
   2010-11-22 22:15:37 < Dark_Shikari> how much do you know about DCTs?
   2010-11-22 22:15:46 < Jumpyshoes> i know JPEG's DCT
   2010-11-22 22:16:04 < Jumpyshoes> performs a seperable transformation which compacts energy
   2010-11-22 22:16:09 < Jumpyshoes> to the top coefficients
   2010-11-22 22:16:17 < Jumpyshoes> so you can effectively 0 out the lower ones
   2010-11-22 22:16:19 < Jumpyshoes> w/ quantization
   2010-11-22 22:16:35 < Dark_Shikari> JPEG's is just *THE* DCT
   2010-11-22 22:16:40 < Dark_Shikari> that is what a dct is
   2010-11-22 22:16:51 < Dark_Shikari> H.264's transform is often colloquially known as the HCT (H.264 Cosine Transform) as it isn't the DCT.
   2010-11-22 22:16:56 < Dark_Shikari> It's a very very rough approximation.
   2010-11-22 22:16:58 < Jumpyshoes> i heard h264's only used integer arithmetic?
   2010-11-22 22:17:03 < Dark_Shikari> More than just that
   2010-11-22 22:17:09 < Dark_Shikari> all real implementations of DCTs are integer-only
   2010-11-22 22:17:22 < Dark_Shikari> and all modern video ones (VC-1, H.264, VP8, RV40, etc) are bit-exact, too.
   2010-11-22 22:17:26 < Dark_Shikari> But H.264's is extra-special
   2010-11-22 22:17:37 < Dark_Shikari> It requires nothing more than shifts and adds.
   2010-11-22 22:17:41 < Dark_Shikari> and subtracts, I guess.
   2010-11-22 22:17:51 < Dark_Shikari> The 4x4 dct in particular requires no shifts larger than 1.
   2010-11-22 22:18:00 < Dark_Shikari> this makes it more like a Hadamard transform than a DCT.
   2010-11-22 22:18:13 < Dark_Shikari> It's slightly less compression-efficient (~1%) than the ideal DCT, but way way way way way faster.
   2010-11-22 22:18:21 < Dark_Shikari> Now, here's the catch with this
   2010-11-22 22:18:51 < Dark_Shikari> if you analyse this DCT, you'll find out that it isn't properly normalized, i.e. the values outputted by the DCT and inputted to the iDCT are scaled differently per coefficient
   2010-11-22 22:18:58 < Dark_Shikari> this is one of the consequences of the extremely simple implementation.
   2010-11-22 22:19:09 < Dark_Shikari> So what they did... they rolled these numbers into the quantization scaling factors.
   2010-11-22 22:19:16 < Dark_Shikari> Thus making multiplying by them cost nothing.
   2010-11-22 22:19:23 < Dark_Shikari> Since you're already multiplying for quantization.
   2010-11-22 22:19:40 < Dark_Shikari> so dct -> quant -> dequant -> idct
   2010-11-22 22:19:48 < Dark_Shikari> "quant" adds in the scaling factors for the dct
   2010-11-22 22:19:53 < Dark_Shikari> and "dequant" adds in the scaling factors for the idct.
   2010-11-22 22:19:58 < Dark_Shikari> (in addition to doing what they normally do)
   2010-11-22 22:20:01 < Jumpyshoes> huh, i see
   2010-11-22 22:20:12 < Dark_Shikari> You don't have to know about this when implementing a dct or idct, but it explains how it works.
   2010-11-22 22:20:41 < Jumpyshoes> well, i need to figure out what the C code does
   2010-11-22 22:20:52 < Dark_Shikari> This isn't involved in figuring out what it does.
   2010-11-22 22:20:59 < Jumpyshoes> true
   2010-11-22 22:21:00 < Dark_Shikari> The C code just does a 1D transform in each direction.
   2010-11-22 22:21:13 < Dark_Shikari> and the transform is rather obvious and simple, the challenge is if you want to figure out why it works.
   2010-11-22 22:21:20 < Dark_Shikari> Which you don't have to, of course.
   2010-11-22 22:21:26 < Dark_Shikari> since that's math and math is hard
   2010-11-22 22:21:37 < Jumpyshoes> what does x264_clip_pixel do?
   2010-11-22 22:22:05 < Dark_Shikari> It clips a pixel to within the valid range.
   2010-11-22 22:22:10 < Dark_Shikari> 0-255 for 8-bit
   2010-11-22 22:22:13 < Dark_Shikari> 0-511 for 9-bit
   2010-11-22 22:22:13 < Dark_Shikari> etc etc
   2010-11-22 22:22:28 < Jumpyshoes> ah
   2010-11-22 22:22:30 < Dark_Shikari> This is because, after an idct, pixel values can go outside the valid range.
   2010-11-22 22:22:33 < Dark_Shikari> the idct is required to clamp its output.
   2010-11-22 22:22:41 < Dark_Shikari> to avoid overflow
   2010-11-22 22:23:13 < Jumpyshoes> i see
   2010-11-22 22:24:50 < Dark_Shikari> this is trickier for high bit depth
   2010-11-22 22:24:57 < Jumpyshoes> does IDCT4_1D depend on the input size?
   2010-11-22 22:25:01 < Dark_Shikari> if our pixels are 8-bit, we can just do packusbw
   2010-11-22 22:25:04 < Dark_Shikari> which automatically saturates
   2010-11-22 22:25:17 < Dark_Shikari> but for larger values we can't.
   2010-11-22 22:25:22 < Dark_Shikari> Jumpyshoes: yes, go look at it
   2010-11-22 22:25:26 < Dark_Shikari> it probably uses word math (paddw, etc)
   2010-11-22 22:26:02 < Jumpyshoes> it calls a bunch of SUMSUBD2_AB and stuff
   2010-11-22 22:26:31 < Dark_Shikari> go look at what those do
   2010-11-22 22:26:35 < Dark_Shikari> they're pretty trivial
   2010-11-22 22:26:40 < Dark_Shikari> a SUMSUB calculates A+B and A-B
   2010-11-22 22:26:42 < Dark_Shikari> for inputs A and B
   2010-11-22 22:26:44 < Dark_Shikari> (surprise!)
   2010-11-22 22:27:40 < Jumpyshoes> ah, so it does depend on the bit depth
   2010-11-22 22:28:19 < Dark_Shikari> You could modify SUMSUB to take an argument for the data element size
   2010-11-22 22:28:24 < Dark_Shikari> e.g. "w" for 16-bit, "d" for 32-bit
   2010-11-22 22:28:30 < Dark_Shikari> then go around and find all existing calls to SUMSUB and add that
   2010-11-22 22:28:33 < Dark_Shikari> make sure it still works
   2010-11-22 22:28:39 < Dark_Shikari> then write your own passing "d" instead of "w"
   2010-11-22 22:28:45 < Dark_Shikari> so for example
   2010-11-22 22:28:57 < Dark_Shikari> SUMSUB mm0, mm1 would become SUMSUB w, mm0, mm1
   2010-11-22 22:29:00 < Dark_Shikari> or similar
   2010-11-22 22:29:13 < Jumpyshoes> wouldn't i need to replace it in every SUMSUB then?
   2010-11-22 22:30:14 < Dark_Shikari> yes, you'd have to add the "w" argument to every SUMSUB
   2010-11-22 22:30:19 < Dark_Shikari> There aren't that many calls though
   2010-11-22 22:30:27 < Dark_Shikari> most SUMSUB calls are in util
   2010-11-22 22:30:30 < Dark_Shikari> i.e. as part of other things
   2010-11-22 22:30:31 < Dark_Shikari> like transforms
   2010-11-22 22:30:40 < Jumpyshoes> ah
   2010-11-22 22:30:44 < Dark_Shikari> i.e. few functions call sumsub directly, they call it through macros
   2010-11-22 22:30:48 < Dark_Shikari> like IDCT4_1D
   2010-11-22 22:31:20 < Jumpyshoes> okay, time to try this out
   2010-11-22 22:33:00 < Jumpyshoes> what is passed if i have "w" as an argument?
   2010-11-22 22:33:11 < Jumpyshoes> is it just "w" in %0?
   2010-11-22 22:33:20 < Jumpyshoes> er, %1
   2010-11-22 22:33:43 < Dark_Shikari> yes
   2010-11-22 22:33:44 < Dark_Shikari> so for example
   2010-11-22 22:33:46 < Dark_Shikari> paddw becomes padd%1
   2010-11-22 22:33:50 < Dark_Shikari> cool, eh?
   2010-11-22 22:33:54 < Jumpyshoes> indeed
   2010-11-22 22:34:02 < Dark_Shikari> also, on an unrelated note, %0 is the number of macro parameters.
   2010-11-22 22:34:08 < Dark_Shikari> This is useful when making variadic macros.
   2010-11-22 22:34:49 < Jumpyshoes> yasm is pretty handy
   2010-11-22 22:35:30 < Dark_Shikari> yasm's preprocess is basically what C's should have been.
   2010-11-22 22:35:33 < Dark_Shikari> *preprocessor
   2010-11-22 22:37:15 < Jumpyshoes> what does mova do?
   2010-11-22 22:37:36 < Dark_Shikari> as mentioned yesterday, it's part of the templating system
   2010-11-22 22:37:39 < Dark_Shikari> if INIT_MMX is used, it's movq
   2010-11-22 22:37:43 < Dark_Shikari> if INIT_XMM is used, it'a movdqa
   2010-11-22 22:37:44 < Jumpyshoes> er, right
   2010-11-22 22:37:44 < Dark_Shikari> *it's
   2010-11-22 22:37:49 < Dark_Shikari> in short, "move a whole register, aligned"
   2010-11-22 22:37:59 < Dark_Shikari> in that macro it's just a register-to-register move.
   2010-11-22 22:38:02 < Dark_Shikari> iirc
   2010-11-22 22:44:55 < Sean_McG> 10:02 < Dark_Shikari> Sean_McG: ^ <-- what was this all about, it's scrolled off
   2010-11-22 22:45:41 < Dark_Shikari> pengvado had a comment for you
   2010-11-22 22:45:43 < Dark_Shikari> grab the log and read it
   2010-11-22 22:45:46 < Dark_Shikari> it's why I didn't commit your fix
   2010-11-22 22:47:44 < Sean_McG> oh regarding Mans note about 'strings'? Yeah, I understand... not sure how to fix it anymore though.
   2010-11-22 22:48:51 < Sean_McG> not discarding the whole commit though, are we? can we just roll back the change to configure?
   2010-11-22 22:49:38 < Sean_McG> back later -- meeting a co-worker for dinner
   2010-11-22 23:09:09 < Dark_Shikari> Sean_McG: I just discarded it for now
   2010-11-22 23:09:12 < Dark_Shikari> it'll be in the next commit spree if you fix it
   2010-11-22 23:16:42 < rfw> i should probably make my output easier to read
   2010-11-22 23:17:36 < rfw> Dark_Shikari: http://pastebin.com/g58FejEe is this painful in any way to read
   2010-11-22 23:18:33 < Dark_Shikari> It probably shouldn't use 4chan terminology.
   2010-11-22 23:18:47 < rfw> oh those are just my half-assed commit messages
   2010-11-22 23:18:48 < Dark_Shikari> Also most of that should be omitted in non-verbose mode
   2010-11-22 23:18:58 < rfw> from my testing repo
   2010-11-22 23:19:00 < rfw> don't mind that lol
   2010-11-22 23:19:01 < Dark_Shikari> in non-verbose mode, it should tell me just what I want to know
   2010-11-22 23:19:06 < Dark_Shikari> i.e. "X is broken, Y works"
   2010-11-22 23:19:11 < Dark_Shikari> not all the things it did to discover that.
   2010-11-22 23:19:14 < Dark_Shikari> in verbose mode it can tell me that
   2010-11-22 23:58:13 < kemuri-_9> what is the purpose of that large configure change for the 1/0 vs 1/undef in the preprocessor vars?
   --- Day changed Tue Nov 23 2010
   2010-11-23 00:00:58 < holger_> <Dark_Shikari> But it's far more complicated and harder to read because it's doing things in a completely nonintutive, ugly way. <-- mostly due to the fact that this actually was an exercise in optimizing for atom. you only took the sse4 version, so it's not entirely obvious anymore ;)
   2010-11-23 00:02:04 < Kovensky> kemuri-_9: being able to just use #if instead of having to use #ifdef
   2010-11-23 00:02:28 < kemuri-_9> the preprocessor defaults undef to 0 though
   2010-11-23 00:02:41 < Kovensky> and complains about it
   2010-11-23 00:02:47 < kemuri-_9> what compiler?
   2010-11-23 00:03:28 < Kovensky> gcc
   2010-11-23 00:04:02 < pengvado> #if works on undef, but any other forms of conditionals don't
   2010-11-23 00:04:27 < pengvado> ?:, &&, if(), ...
   2010-11-23 00:04:32 < kemuri-_9> do we use any other conditionals on those values?
   2010-11-23 00:04:49 < pengvado> not yet
   2010-11-23 00:05:41 < kemuri-_9> it would probably be easier to check at the end of the ./configure to see which values are missing from the config.h than if (x=yes) define x 1 else define x 0
   2010-11-23 00:05:50 < kemuri-_9> which is being splattered everywhere
   2010-11-23 00:06:44 < Kovensky> that's... awfully verbose
   2010-11-23 00:06:55 < Kovensky> just define x $(x=yes)
   2010-11-23 00:08:13 < pengvado> Kovensky: what language is that? not bash
   2010-11-23 00:08:47 < kemuri-_9> define x [ $x = yes ]  <--- would this not be what he was trying to do?
   2010-11-23 00:08:50 < Kovensky> it isn't, I'm just copying his pseudocode
   2010-11-23 00:09:10 < Kovensky> define x $([ $x = yes ] && echo 1 || echo 0)
   2010-11-23 00:09:17 < Kovensky> er
   2010-11-23 00:09:32 < Kovensky> hm nvm, that's correct
   2010-11-23 00:09:36 < Kovensky> $? would give wrong results
   2010-11-23 00:11:22 < kemuri-_9> and why all the changes to the makefile/config.mak? changing them to findstring x 1  from findstring x  works doesn't it?
   2010-11-23 00:11:30 < rfw> time for lunch then more regression testing
   2010-11-23 00:27:06 < Sean_McG> DS: both my submissions?
   2010-11-23 00:27:55 < rfw> there, that's the testing framework done
   2010-11-23 00:28:02 < rfw> what regression tests am i required to implement?
   2010-11-23 00:29:53 < Sean_McG> DS: my 2nd submission regarding the VIS asm is still OK, yes?
   2010-11-23 00:32:56 < Sean_McG> DS: for the 'configure' change... is it acceptable if we just extend the length of the array and manually terminate the string?
   2010-11-23 00:33:14 < Sean_McG> DS: and no one has been able to provide me with a platform to test where that breaks either.
   2010-11-23 00:40:23 < Dark_Shikari> Sean_McG: I don't care about configure.
   2010-11-23 00:40:27 < Dark_Shikari> All that matters is that pengvado is satisfied
   2010-11-23 00:40:36 < jarod> and the wife
   2010-11-23 00:40:37 < Dark_Shikari> rfw: ok, the most basic is the two dump yuv tests
   2010-11-23 00:40:38 < Sean_McG> OK... I'll try again
   2010-11-23 00:40:41 < Dark_Shikari> compare vs JM and ffmpeg
   2010-11-23 00:40:51 < Dark_Shikari> ffmpeg has some known decoding bugs, so JM is more important
   2010-11-23 00:40:54 < Dark_Shikari> but they work in the same way
   2010-11-23 00:41:00 < Dark_Shikari> for JM, just run ldecod -i inputfile
   2010-11-23 00:41:00 < rfw> ah so
   2010-11-23 00:41:02 < Dark_Shikari> it'll output to test_dec.yuv
   2010-11-23 00:41:07 < rfw> i get JM and ffmpeg
   2010-11-23 00:41:07 < Sean_McG> also, does r1789 fix the same artifacting issue BugMaster was talking about yesterday, with gcc 4.5.x?
   2010-11-23 00:41:14 < rfw> and get x264 to dump a yuv
   2010-11-23 00:41:15 < Dark_Shikari> for ffmpeg, do ffmpeg -i input -pix_fmt yuv420p -f rawvideo output.yuv
   2010-11-23 00:41:20 < Dark_Shikari> Sean_McG: yes
   2010-11-23 00:41:22 < rfw> yeah i know how to use ffmpeg
   2010-11-23 00:41:23 < Sean_McG> OK cool
   2010-11-23 00:41:29  * Sean_McG rebuilds
   2010-11-23 00:43:20 < rfw> time to get my msbuild ou
   2010-11-23 00:43:20 < rfw> t
   2010-11-23 00:44:01 < Dark_Shikari> msbuild?
   2010-11-23 00:45:46 < rfw> yeah, to buidl the JM solution
   2010-11-23 00:45:53 < Sean_McG> DS: can I revert my patch in my local tree without mucking with the commits I did afterwards? (I admit I'm so used to cvs and svn that I still don't fully grok how git workflows are supposed to be done)
   2010-11-23 00:46:04 < Dark_Shikari> "revert"?
   2010-11-23 00:46:10 < rfw> c:\users\tony\downloads\jm17.2\jm\lcommon\inc\win32.h(39): fatal error C1083: Cannot open include file: 'omp.h': No such file or directory [C:\Users\Tony\Downloads\jm17.2\JM\jm_vc9.sln]
   2010-11-23 00:46:10 < rfw>  118 Error(s)
   2010-11-23 00:46:15 < rfw> tihs isn't going very well
   2010-11-23 00:46:20 < Sean_McG> DS: pull it out so I can edit it and recommit later
   2010-11-23 00:46:27 < Dark_Shikari> git rebase -i
   2010-11-23 00:46:36 < Dark_Shikari> rfw: compile in cygwin/mingw
   2010-11-23 00:46:38 < Sean_McG> what does that do, cherry pick?
   2010-11-23 00:46:44 < Dark_Shikari> it lets you edit any past commit
   2010-11-23 00:46:50 < Dark_Shikari> just replace the word "pick" with the word "edit"
   2010-11-23 00:46:53 < Dark_Shikari> for the commit you want
   2010-11-23 00:47:01 < Dark_Shikari> and then when you're done, amend it and git rebase --continue
   2010-11-23 00:47:24 < kemuri-_9> http://kemuri9.net/dev/misc/jm/jm17.2.rar  <--- i built this a while back for someone else in msvc, can use it if you want
   2010-11-23 00:47:35 < Dark_Shikari> I just use cygwin, works fine here :>
   2010-11-23 00:47:42 < rfw> but i just finied building with cygwin :<
   2010-11-23 00:48:04 < kemuri-_9> pengvado: what do you think of http://pastebin.com/ZAb3crs1 ?
   2010-11-23 00:48:09 < Dark_Shikari> that doesn't look like an error from cygwin
   2010-11-23 00:48:26 < rfw> no i mean
   2010-11-23 00:48:32 < rfw> i just built it with cygwin
   2010-11-23 00:48:36 < rfw> (successfully)
   2010-11-23 00:48:46 < rfw> that was from vs2010 before
   2010-11-23 00:50:52 < Dark_Shikari> well that's what you get for trying to use vs2010
   2010-11-23 00:51:09 < rfw> :<
   2010-11-23 00:51:11 < kemuri-_9> lol
   2010-11-23 00:51:52 < kemuri-_9> speaking of which i should reinstall vs2008 and icl so i can mess with that crap again
   2010-11-23 00:56:07 < Jumpyshoes> Dark_Shikari: so i fell asleep, but would this work for SUMSUB_BA: http://pastebin.com/6Fms1SAB ?
   2010-11-23 00:57:09 < Dark_Shikari> no
   2010-11-23 00:57:44 < rfw> Dark_Shikari: how do i make x264 output raw YUV again?
   2010-11-23 00:57:59 < Dark_Shikari> Jumpyshoes: you probably want something like http://pastebin.com/xewaKQPt
   2010-11-23 00:58:05 < checkers> -o file.yuv
   2010-11-23 00:58:05 < Dark_Shikari> rfw: --dump-yuv file.yuv
   2010-11-23 00:58:09 < Jumpyshoes> oh
   2010-11-23 00:58:50 < rfw> ah okay
   2010-11-23 00:58:51 < Jumpyshoes> thanks
   2010-11-23 00:59:53 < rfw> Dark_Shikari: do you have any specific file or anything to test it on
   2010-11-23 00:59:58 < rfw> or do i just grab one of my videos
   2010-11-23 01:00:48 < Dark_Shikari> rfw: http://media.xiph.org/video/derf/ pick one
   2010-11-23 01:00:59 < Dark_Shikari> if you want to test breaking x264 to see if your tool detects it
   2010-11-23 01:01:13 < Dark_Shikari> in common/mc.c, find pixel_avg_wxh
   2010-11-23 01:01:14 < Dark_Shikari> remove the +1
   2010-11-23 01:01:23 < Dark_Shikari> then recompile and run x264 with --no-asm
   2010-11-23 01:01:29 < Dark_Shikari> it will fail all tests on the first b-frame
   2010-11-23 01:01:34 < rfw> ah
   2010-11-23 01:02:34 < Dark_Shikari> I chose that function because I and P-frames will still work
   2010-11-23 01:02:38 < Dark_Shikari> so it doesn't completely break things
   2010-11-23 01:02:41 < Dark_Shikari> allowing more meaningful testing
   2010-11-23 01:08:21 < Sean_McG> alright, I guess I need someone who gives a rip about this endian test... doesn't mean anything to Windows people. Does pengvado use Windows or Linux or..?
   2010-11-23 01:08:52 < Sean_McG> there *is* an autoconf macro: AC_C_BIGENDIAN... should I just adapt that?
   2010-11-23 01:09:39 < rfw> Fixture result: PASS, took 6.9245 seconds.
   2010-11-23 01:09:39 < rfw> Project result: PASS, took 6.9245 seconds.
   2010-11-23 01:09:40 < rfw> \o/
   2010-11-23 01:09:52 < Dark_Shikari> \o/
   2010-11-23 01:10:57 < rfw> Fixture result: FAIL.
   2010-11-23 01:10:58 < rfw> Project result: FAIL.
   2010-11-23 01:11:00 < rfw> it can fail too \o/
   2010-11-23 01:11:11 < Dark_Shikari> Now we just have to make that more descriptive.
   2010-11-23 01:11:18 < rfw> yup
   2010-11-23 01:11:35 < Jumpyshoes> Dark_Shikari http://pastebin.com/T0jbAwwv would this work for the rest?
   2010-11-23 01:11:39  * Dark_Shikari very much likes finding high school students who can python better than he can
   2010-11-23 01:11:48 < Dark_Shikari> also python is now a verb
   2010-11-23 01:11:54 < rfw> http://pastebin.com/GF1czXrr
   2010-11-23 01:12:02 < rfw> this probably would be much better suited for python projects, lol
   2010-11-23 01:12:15 < Dark_Shikari> Jumpyshoes: lgtm, you now have to modify the rest of x264 asm to call these correctly
   2010-11-23 01:12:18 < Dark_Shikari> i.e. grep for them, add ws
   2010-11-23 01:12:27 < Dark_Shikari> once you're done, compile in bit-depth 8 mode, and checkasm
   2010-11-23 01:12:31 < Dark_Shikari> and fix until it works
   2010-11-23 01:12:38 < Jumpyshoes> ws?
   2010-11-23 01:13:14 < Dark_Shikari> plural w
   2010-11-23 01:13:25 < Jumpyshoes> oh right
   2010-11-23 01:13:57 < Jumpyshoes> there's like 3 pages of SUMSUBs, is there any way to replace them in all files?
   2010-11-23 01:14:06 < Dark_Shikari> find/replace
   2010-11-23 01:14:13 < Dark_Shikari> SUMSUB -> SUMSUMB w,
   2010-11-23 01:14:22 < Jumpyshoes> can i ignore spacing for now?
   2010-11-23 01:14:29 < Dark_Shikari> find/replace should be able to handle spacing.
   2010-11-23 01:14:33 < Dark_Shikari> Anyways, it's just 15 minutes of work =p
   2010-11-23 01:14:34 < Jumpyshoes> true
   2010-11-23 01:14:42 < Jumpyshoes> <-- lazy butt
   2010-11-23 01:15:08 < Dark_Shikari> welcome to the club
   2010-11-23 01:15:20 < kierank> [01:15] Jumpyshoes: <-- lazy butt --> you'll fit right in
   2010-11-23 01:15:34 < Dark_Shikari> pretty much
   2010-11-23 01:15:47 < Dark_Shikari> like the other day when I spent 2 hours to finish chroma weightp.
   2010-11-23 01:15:47 < Jumpyshoes> oh excellent
   2010-11-23 01:15:49 < Dark_Shikari> wait -- you say -- that's work!
   2010-11-23 01:15:57 < Dark_Shikari> But it took one full year for me to get around to doing it
   2010-11-23 01:16:03 < Jumpyshoes> LOL
   2010-11-23 01:16:08 < Jumpyshoes> you sound exactly like one of my friends
   2010-11-23 01:16:19 < Dark_Shikari> and I only did it on a dare from boiled_sugar
   2010-11-23 01:17:07 < kemuri-_9> so dares are useful motivation?
   2010-11-23 01:17:25 < Kovensky> 22:16.19 Dark_Shikari: and I only did it on a dare from boiled_sugar <-- lol
   2010-11-23 01:17:26 < Kovensky> what was it
   2010-11-23 01:18:03 < Dark_Shikari> he kept yelling at me to do chroma weightp
   2010-11-23 01:18:07 < Dark_Shikari> so I said I'd do it that weekend
   2010-11-23 01:18:08 < Dark_Shikari> so I did
   2010-11-23 01:18:40 < Jumpyshoes> haha, 97 of the SUMSUBs are arm
   2010-11-23 01:18:47 < Jumpyshoes> that's half my work done!
   2010-11-23 01:18:49 < Dark_Shikari> saves you some time eh!
   2010-11-23 01:18:50 < Dark_Shikari> lol
   2010-11-23 01:25:51 < rfw> Running test yuv_compare... failed, due to x264-output.yuv is not the same as jm-output.yuv (69076e2a5a9a76d5b483abe953b4a6ce vs 19becfba7cf53d773756095d8a355938)
   2010-11-23 01:26:04 < rfw> there's some more verbosity
   2010-11-23 01:26:06 < Dark_Shikari> don't need to hash imo
   2010-11-23 01:26:08 < Dark_Shikari> waste of time
   2010-11-23 01:26:16 < rfw> yeah but i haven't implemented all the macroblocking
   2010-11-23 01:26:17 < rfw> and stuff
   2010-11-23 01:26:24 < rfw> so i'm just doing that for now
   2010-11-23 01:27:14 < Dark_Shikari> you could just give a file offset
   2010-11-23 01:27:17 < Dark_Shikari> like diff does
   2010-11-23 01:27:27 < rfw> ah
   2010-11-23 01:27:34 < Dark_Shikari> btw, you should test your thing on files larger than ram
   2010-11-23 01:27:38 < Dark_Shikari> i.e. you should not rely on O(N) ram usage
   2010-11-23 01:27:44 < Dark_Shikari> because yuv files get really fucking huge.
   2010-11-23 01:28:44 < rfw> yeah i know
   2010-11-23 01:28:55 < rfw> i'm reading it into a buffer and then puking it out again
   2010-11-23 01:29:13 < Dark_Shikari> yeah, don't do that
   2010-11-23 01:29:24 < rfw> what?
   2010-11-23 01:29:30 < Dark_Shikari> I mean, don't read the whole file into a buffer
   2010-11-23 01:29:35 < rfw> no i'm not doing that
   2010-11-23 01:29:35 < rfw> lol
   2010-11-23 01:29:36 < Dark_Shikari> oh ok
   2010-11-23 01:29:37 < Dark_Shikari> lol
   2010-11-23 01:29:41 < rfw> i'm reading 8k bytes at a time
   2010-11-23 01:29:46 < Dark_Shikari> good, so you're not like the author of flvtool2
   2010-11-23 01:29:49 < rfw> lol
   2010-11-23 01:29:58 < Dark_Shikari> aka "ruby programmers"
   2010-11-23 01:30:10 < rfw> i could never get into ruby
   2010-11-23 01:30:11 < rfw> lol
   2010-11-23 01:30:54 < Dark_Shikari> btw, remember that your script will have to pass through pengvado
   2010-11-23 01:30:59 < Dark_Shikari> think of him as gandalf, and you as the balrog
   2010-11-23 01:31:21 < rfw> it's not so much a script as a huge python library
   2010-11-23 01:31:36 < kemuri-_9> lol @ that analogy
   2010-11-23 01:31:44 < rfw> wait a minute, doesn't that mean i lose
   2010-11-23 01:33:22 < Dark_Shikari> lol
   2010-11-23 01:33:30 < Dark_Shikari> it's a great analogy for professors
   2010-11-23 01:33:33 < Dark_Shikari> YOU SHALL NOT PASS etc
   2010-11-23 01:33:46 < Dark_Shikari> "huge python library"?
   2010-11-23 01:34:00 < rfw> well
   2010-11-23 01:34:12 < rfw> http://pastebin.com/GF1czXrr
   2010-11-23 01:34:35 < Dark_Shikari> what's digress?
   2010-11-23 01:34:43 < rfw> what i called it
   2010-11-23 01:34:49 < Dark_Shikari> Oh, and where will we get that?
   2010-11-23 01:34:59 < rfw> i haven't finished writing it you know
   2010-11-23 01:34:59 < rfw> :3
   2010-11-23 01:35:01 < Dark_Shikari> will it be included in the source tree or just a lib the regtest tool requires?
   2010-11-23 01:35:04 < Dark_Shikari> lol
   2010-11-23 01:35:07 < Dark_Shikari> hahaha
   2010-11-23 01:35:14 < Dark_Shikari> works for me as long as it works =p
   2010-11-23 01:36:55 < Dark_Shikari> the main issue being that since your tool isn't part of x264, dependency issues aren't as big a deal
   2010-11-23 01:37:03 < Dark_Shikari> for x264 itself, we make a big deal about not requiring external dependencies
   2010-11-23 01:37:07 < Dark_Shikari> but for dev tools, whateva
   2010-11-23 01:37:36 < rfw> well
   2010-11-23 01:37:39 < rfw> it only depends on python
   2010-11-23 01:38:05 < rfw> i guess you could include my package that's more or less standalone in the source tree
   2010-11-23 01:38:23 < rfw> (i sorta wanted to use it for my own projects in future too :P)
   2010-11-23 01:38:32 < Dark_Shikari> we could put it in extras/
   2010-11-23 01:38:50 < Dark_Shikari> like we put the avisynth C header there, and getopt, and other system-dependent imports that not everyone has
   2010-11-23 01:39:22 < rfw> ah
   2010-11-23 01:47:49 < rfw> alright Dark_Shikari
   2010-11-23 01:47:51 < rfw> that's that done
   2010-11-23 01:47:53 < rfw> what else do i need
   2010-11-23 01:48:10 < Jumpyshoes> hey Dark_Shikari, i'm getting the error: undefined symbol `w' in preprocessor, how do i set it to be a word again? bw is in other places in the code, is it that?
   2010-11-23 01:48:46 < Dark_Shikari> where do you get this error?
   2010-11-23 01:48:53 < Dark_Shikari> you will only get that error if you attempt to use it as a symbol
   2010-11-23 01:48:55 < Dark_Shikari> which you shouldn't
   2010-11-23 01:49:16 < Jumpyshoes> common/x86/dct-a.asm:178: error: (SUMSUBD2_AB:3) undefined symbol `w' in preprocessor
   2010-11-23 01:49:58 < Dark_Shikari> what's the third line of SUMSUBd@_AB?
   2010-11-23 01:50:18 < Dark_Shikari> Ah, 79-85 in your paste is wrong
   2010-11-23 01:50:21 < Dark_Shikari> it should be psra%1
   2010-11-23 01:50:24 < Dark_Shikari> like in the other cases
   2010-11-23 01:51:09 < Jumpyshoes> oh
   2010-11-23 01:51:20 < Dark_Shikari> if you want to do a comparison, you'd do
   2010-11-23 01:51:22 < Dark_Shikari> %ifidn %1, w
   2010-11-23 01:51:26 < Dark_Shikari> But you don't need to.
   2010-11-23 01:51:40 < Jumpyshoes> google lied to me ;-;
   2010-11-23 01:52:09 < Jumpyshoes> no it didn't
   2010-11-23 01:52:11 < Jumpyshoes> i'm just a dumbass
   2010-11-23 01:52:23 < rfw> you know if google lied to us this competition could all be a lie
   2010-11-23 01:52:24 < rfw> !!
   2010-11-23 01:52:44 < Jumpyshoes> oh shit
   2010-11-23 01:52:52 < Jumpyshoes> are you also a high school student?
   2010-11-23 01:52:55 < rfw> yeah
   2010-11-23 01:52:57 < rfw> lol
   2010-11-23 01:53:11 < rfw> i don't know shit about asm though
   2010-11-23 01:53:15 < Jumpyshoes> where are you from?
   2010-11-23 01:53:21 < rfw> new zealand
   2010-11-23 01:53:23 < Dark_Shikari> google lied to you?
   2010-11-23 01:53:24 < rfw> lol
   2010-11-23 01:53:39 < Jumpyshoes> i googled the instruction
   2010-11-23 01:53:41 < Dark_Shikari> GOOGLE LIED, PEOPLE DIED
   2010-11-23 01:53:43 < Jumpyshoes> and uh
   2010-11-23 01:53:50 < Jumpyshoes> missed the instruction in the pages that came up
   2010-11-23 01:53:51 < Jumpyshoes> somehow
   2010-11-23 01:53:55 < Dark_Shikari> ?
   2010-11-23 01:54:09 < rfw> where are you from, Jumpyshoes
   2010-11-23 01:54:27 < rfw> washdc.fios.verizon.net lolnevermind
   2010-11-23 01:54:30 < Jumpyshoes> yup
   2010-11-23 01:54:43 < Jumpyshoes> i googled PSRAD but somehow thought it didn't exist
   2010-11-23 01:54:48 < Dark_Shikari> Jumpyshoes: google lies
   2010-11-23 01:54:51 < Dark_Shikari> =p
   2010-11-23 01:55:07 < Dark_Shikari> psrad is too rad for google
   2010-11-23 01:55:29 < Jumpyshoes> well, it did show up
   2010-11-23 01:55:36 < Jumpyshoes> i just somehow missed every page that came up
   2010-11-23 01:55:38 < Jumpyshoes> or something
   2010-11-23 01:56:13 < pengvado> Sean_McG: AC_C_BIGENDIAN is implemented by 200 lines of m4. if by "adapt" you mean "throw out everything except the grep that's just like the one we already have", ok.
   2010-11-23 01:56:26 < pengvado> null-termination is good enough for me
   2010-11-23 01:57:21 < Sean_McG> pengvado: how do you "null terminate" an int?
   2010-11-23 01:57:58 < pengvado> int i[2] = {0x42494745,0};
   2010-11-23 01:58:20 < Sean_McG> and those are guaranteed to be sequential and fix the issue that Mans was pointing out?
   2010-11-23 01:58:24 < pengvado> yes
   2010-11-23 01:58:44 < Sean_McG> hmmm, OK. I'll fix and resend my patch as soon as 1790 is built
   2010-11-23 01:59:24 < pengvado> mru is right that clang's intermediate representation isn't real asm and thus still breaks, but since I don't know of any method that *would* work there, sucks to be clang
   2010-11-23 01:59:35 < Dark_Shikari> lol
   2010-11-23 01:59:40 < Sean_McG> aye, that was my thought too
   2010-11-23 02:00:18 < Sean_McG> the endian test would have to be "if { not building with clang }"
   2010-11-23 02:01:20 < Sean_McG> and here we go... fprofiled just finished on my Sol10 VM. just need to package it up and post it on my webserver
   2010-11-23 02:01:41 < Jumpyshoes> okay Dark_Shikari
   2010-11-23 02:01:43 < Jumpyshoes> i think i am done
   2010-11-23 02:02:18 < Dark_Shikari> does it pass checkasm?
   2010-11-23 02:02:21 < Jumpyshoes> yea
   2010-11-23 02:02:27 < Dark_Shikari> in 8 and 10-bit?
   2010-11-23 02:02:30 < Jumpyshoes> oh
   2010-11-23 02:02:34 < Jumpyshoes> haven't tested 10bit
   2010-11-23 02:02:39 < Dark_Shikari> just check to make sure you didn't break it
   2010-11-23 02:02:49 < Dark_Shikari> Once you're done with that, you can write your IDCT_1D high bit depth version
   2010-11-23 02:02:50 < Dark_Shikari> or, even better...
   2010-11-23 02:02:56 < Dark_Shikari> make IDCT4_1D take a w or d :) :)
   2010-11-23 02:03:04 < Jumpyshoes> i actually have a geo quiz tomorrow
   2010-11-23 02:03:07 < Jumpyshoes> that everyone failed
   2010-11-23 02:03:10 < Jumpyshoes> even though it's GEO
   2010-11-23 02:03:16 < Jumpyshoes> so i actually need to study for that
   2010-11-23 02:03:22 < pengvado> kemuri-_9: `[ ... ]` fails, because [ sets an exit code whereas `` captures stdout
   2010-11-23 02:03:25 < rfw> how old are you Jumpyshoes, out of interest
   2010-11-23 02:03:27 < Jumpyshoes> 17
   2010-11-23 02:03:31 < Jumpyshoes> you?
   2010-11-23 02:03:32 < pengvado> just let the !GPL case be handled by the same loop as everything else
   2010-11-23 02:03:33 < rfw> 16
   2010-11-23 02:03:39 < kemuri-_9> ok
   2010-11-23 02:03:40 < Jumpyshoes> <-- 12th grade
   2010-11-23 02:03:40 < Dark_Shikari> I was 17 when I started on x264
   2010-11-23 02:03:50 < Jumpyshoes> i can't wait for that point in school
   2010-11-23 02:03:55 < Jumpyshoes> where i can just give up
   2010-11-23 02:03:55  * Sean_McG is... not that young :(
   2010-11-23 02:03:56 < rfw> <-- some wacky new zealand schooling level
   2010-11-23 02:03:58 < Dark_Shikari> Jumpyshoes: the "I got accepted to college, now I can slack"
   2010-11-23 02:04:04 < Jumpyshoes> yes.
   2010-11-23 02:04:12 < Dark_Shikari> "senioritis"
   2010-11-23 02:04:13 < rfw> heh i'm applying for university
   2010-11-23 02:04:16 < Jumpyshoes> same
   2010-11-23 02:04:33 < rfw> well not so much applying as having my parents tell me i can then i can't then i can
   2010-11-23 02:05:24 < rfw> anyway Dark_Shikari
   2010-11-23 02:05:28 < rfw> what are all the tests i need to implement/
   2010-11-23 02:05:40 < Dark_Shikari> it's less so need and moreso want
   2010-11-23 02:05:47 < Dark_Shikari> But there are a few basic tests:
   2010-11-23 02:05:48 < rfw> lol
   2010-11-23 02:05:51 < Dark_Shikari> 1) Compare YUV: JM
   2010-11-23 02:05:54 < rfw> done
   2010-11-23 02:05:55 < Dark_Shikari> 2) Compare YUV: ffmpeg
   2010-11-23 02:06:07 < Dark_Shikari> 3) test PSNR: just run x264 and grab the Global PSNR value
   2010-11-23 02:06:13 < Dark_Shikari> 4) test SSIM: same, except grab the SSIM value
   2010-11-23 02:06:13 < Jumpyshoes> okay, i think i broke something
   2010-11-23 02:06:15 < Jumpyshoes> checkasm isn't compile
   2010-11-23 02:06:20 < Jumpyshoes> compiling
   2010-11-23 02:06:21 < rfw> is that all?
   2010-11-23 02:06:27 < Dark_Shikari> Jumpyshoes: ?
   2010-11-23 02:06:39 < Dark_Shikari> rfw: well, then you have to implement something to let it do useful things with git
   2010-11-23 02:06:42 < Dark_Shikari> like tell me where things broke.
   2010-11-23 02:06:48 < Dark_Shikari> and finally, you have to test multiple x264 options, that's the main thing
   2010-11-23 02:06:48 < rfw> i have bisection integration already
   2010-11-23 02:06:57 < Dark_Shikari> i.e. be able to run test 1) with different x264 options, automatically
   2010-11-23 02:07:00 < Dark_Shikari> to attempt to find various bugs
   2010-11-23 02:07:00 < kemuri-_9> pengvado: care for any particular order in the HAVE list?
   2010-11-23 02:07:08 < Dark_Shikari> that's the most important part
   2010-11-23 02:07:11 < Dark_Shikari> testing one set of options isn't helpful
   2010-11-23 02:07:15 < Dark_Shikari> testing a ton is useful
   2010-11-23 02:07:48 < Jumpyshoes> for some reason, i think trying to compile 8-bit, and then 10-bit breaks gcc until i restart cygwin
   2010-11-23 02:08:19 < Dark_Shikari> make distclean
   2010-11-23 02:08:27 < Jumpyshoes> oh
   2010-11-23 02:08:31 < Jumpyshoes> that will probably solve things
   2010-11-23 02:08:43 < Sean_McG> aye, you have to do that because HIGH_BIT_DEPTH is in config.mak
   2010-11-23 02:10:18 < rfw> Running test ffmpeg... failed: x264-output.yuv is not the same size as ffmpeg-output.yuv (11404800 vs 9542016)
   2010-11-23 02:10:21 < rfw> lol i think my ffmpeg is broken
   2010-11-23 02:12:08 < Jumpyshoes> sexy, checkasm passed
   2010-11-23 02:12:18 < Dark_Shikari> rfw: ffmpeg commandline?
   2010-11-23 02:12:29 < rfw> [ "ffmpeg", "-i", "akiyo_qcif.264", "-pix_fmt", "yuv420p", "-f", "rawvideo", "ffmpeg-output.yuv" ]
   2010-11-23 02:12:33 < pengvado> kemuri-_9: no preference
   2010-11-23 02:12:58 < rfw> actually
   2010-11-23 02:13:03 < rfw> i probably don't need all those params
   2010-11-23 02:13:26 < Dark_Shikari> none of those should affect file length, hmmph
   2010-11-23 02:14:03 < rfw> maybe my ffmpeg just sucks
   2010-11-23 02:14:04 < rfw> lol
   2010-11-23 02:14:56 < Dark_Shikari> you could look at the output of ffmpeg
   2010-11-23 02:15:19 < rfw> hold on
   2010-11-23 02:15:22 < rfw> let me just ignore filesize
   2010-11-23 02:15:58 < rfw> Running test ffmpeg... failed: x264-output.yuv is not the same as ffmpeg-output.yuv (offset 269008)
   2010-11-23 02:16:14 < Dark_Shikari> check the ffmpeg output on stderr
   2010-11-23 02:16:15 < Jumpyshoes> does SWAP care about whether it's w, or d? i don't think so
   2010-11-23 02:16:39 < Dark_Shikari> nope
   2010-11-23 02:16:42 < Dark_Shikari> SWAP just swaps registers
   2010-11-23 02:17:00 < Jumpyshoes> cool
   2010-11-23 02:17:04 < rfw> oh also is there a flag to stop ffmpeg telling me if i want to overwrite
   2010-11-23 02:17:19 < Jumpyshoes> can i claim IDCT4_1D, even though it isn't actually a function?
   2010-11-23 02:17:42 < Dark_Shikari> "claim"?
   2010-11-23 02:17:54 < Dark_Shikari> I mean, you'll have to write a function using it at some point!
   2010-11-23 02:17:57 < Jumpyshoes> true
   2010-11-23 02:17:58 < Dark_Shikari> even if it's nigh-identical to the mmx
   2010-11-23 02:18:01 < Jumpyshoes> okay, might as well do it
   2010-11-23 02:18:19 < Dark_Shikari> "writing a function" just means creating a new function really
   2010-11-23 02:18:25 < Dark_Shikari> whether or not it involved writing
   2010-11-23 02:18:47 < rfw> video:9318kB audio:0kB global headers:0kB muxing overhead 0.000000%
   2010-11-23 02:18:57 < rfw> oh
   2010-11-23 02:18:57 < rfw> Seems stream 0 codec frame rate differs from container frame rate: 29.97 (30000/1001) -> 25.00 (25/1)
   2010-11-23 02:19:11 < rfw> that's probably it, then?
   2010-11-23 02:19:12 < Jumpyshoes> i forgot the fricking function i was planning to write in the first place
   2010-11-23 02:19:44 < espes> Dark_Shikari: For the GCI task, off the top of your head do you know any basic candidates for neon-ing?
   2010-11-23 02:20:32 < Dark_Shikari> Tons of stuff
   2010-11-23 02:20:36 < Dark_Shikari> oh you mean easy ones?
   2010-11-23 02:20:44 < Dark_Shikari> I mean, x264 has tons and tons of functions that are missing neon
   2010-11-23 02:20:48 < Dark_Shikari> including many simple ones, like variance
   2010-11-23 02:20:55 < Dark_Shikari> and chroma mc needs to be updated
   2010-11-23 02:21:08 < Dark_Shikari> your best bet is to just run a profile and look at all the C dsp functions high on the list :)
   2010-11-23 02:21:23 < Dark_Shikari> Jumpyshoes: idct 4x4
   2010-11-23 02:21:25 < espes> Dark_Shikari: I'll have a look, thanks.
   2010-11-23 02:21:35 < Jumpyshoes> i thought that was a macro?
   2010-11-23 02:21:51 < Dark_Shikari> add_idct4_mmx?  no, that's a function
   2010-11-23 02:21:52 < Dark_Shikari> or whatever it's called
   2010-11-23 02:22:15 < Jumpyshoes> oh, add4x4_idct_mmx i believe
   2010-11-23 02:22:38 < rfw> where is the psnr data in the x264 output?
   2010-11-23 02:22:39 < Sean_McG> sweet... can confirm that 1789 fixes the corruption here too
   2010-11-23 02:23:58 < pengvado> rfw: did you enable the --psnr option?
   2010-11-23 02:24:12 < rfw> oh that makes more sense
   2010-11-23 02:24:12 < rfw> lol
   2010-11-23 02:24:25 < rfw> thanks
   2010-11-23 02:27:37 < kemuri-_9> Dark_Shikari: http://pastebin.com/99HiveUE instead of the patch you have currently
   2010-11-23 02:29:50 < rfw> alright, that's the psnr done
   2010-11-23 02:30:09 < rfw> i hope you don't mind regular expressions
   2010-11-23 02:31:53 < Dark_Shikari> kemuri-_9: done
   2010-11-23 02:32:34 < rfw> x264 [[]info[]]: PSNR Mean Y:\d+[.]\d+ U:\d+[.]\d+ V:\d+[.]\d+ Avg:\d+[.]\d+ Global:(\d+[.]\d+) kb/s:\d+[.]\d+
   2010-11-23 02:32:37 < rfw> this should be fine, right
   2010-11-23 02:33:14 < Jumpyshoes> hrm, 16*4 fits in an mm*, so isn't changing IDCT4_1D really easy?
   2010-11-23 02:33:24 < Dark_Shikari> 32*4 doesn't
   2010-11-23 02:33:30 < Dark_Shikari> Of course, if you convert the function to use SSE instead of MMX
   2010-11-23 02:33:32 < Dark_Shikari> it's DEAD simple
   2010-11-23 02:33:36 < Dark_Shikari> i.e. nothing whatsoever changes
   2010-11-23 02:33:41 < Dark_Shikari> since 4x32 is the same as 4x16
   2010-11-23 02:34:06 < Jumpyshoes> oh right, these are DCT coefficients
   2010-11-23 02:34:39 < Jumpyshoes> oh gosh, that's kinda annoying in mmx
   2010-11-23 02:34:43 < Dark_Shikari> You just do it twice.
   2010-11-23 02:34:50 < Dark_Shikari> OK, so the transpose will get a bit tricky, that's it.
   2010-11-23 02:34:52 < Dark_Shikari> But do the SSE version first.
   2010-11-23 02:34:58 < Dark_Shikari> Since the SSE version is going to be mindnumbingly trivial
   2010-11-23 02:35:04 < Dark_Shikari> i.e. swap w for d, swap mm for xmm, done
   2010-11-23 02:35:06 < Dark_Shikari> in fact
   2010-11-23 02:35:08 < Dark_Shikari> you could just template it
   2010-11-23 02:35:23 < Jumpyshoes> template it?
   2010-11-23 02:35:48 < Sean_McG> DS: is my HIGH_BIT_DEPTH fix going to be pushed next commit storm, or was there an issue with that too?
   2010-11-23 02:36:39 < Dark_Shikari> Sean_McG: I think that's fine.
   2010-11-23 02:36:42 < Sean_McG> OK
   2010-11-23 02:36:43 < Dark_Shikari> pengvado only had issues with two patches.
   2010-11-23 02:36:45 < Dark_Shikari> Only one was yours.
   2010-11-23 02:36:58 < Sean_McG> I'll be sending a new one RSN
   2010-11-23 02:37:44 < Jumpyshoes> wait Dark_Shikari, IDCT4_1D uses the aliases already
   2010-11-23 02:37:53 < Jumpyshoes> so m%* already
   2010-11-23 02:38:00 < Jumpyshoes> isn't it basically set for SSE?
   2010-11-23 02:40:05 < Dark_Shikari> Yup
   2010-11-23 02:40:08 < Dark_Shikari> All you have to do is template the function
   2010-11-23 02:40:10 < Dark_Shikari> i.e.
   2010-11-23 02:40:18 < Dark_Shikari> %macro MY_MACRO_NAME 1
   2010-11-23 02:40:25 < Dark_Shikari> cglobal function_name_%1
   2010-11-23 02:40:26 < Dark_Shikari> ...
   2010-11-23 02:40:28 < Dark_Shikari> %endmacro
   2010-11-23 02:40:28 < Dark_Shikari> then
   2010-11-23 02:40:40 < Dark_Shikari> INIT_MMX
   2010-11-23 02:40:42 < Dark_Shikari> MY_MACRO_NAME mmx
   2010-11-23 02:40:44 < Dark_Shikari> INIT_XMM
   2010-11-23 02:40:47 < Dark_Shikari> MY_MACRO_NAME sse2
   2010-11-23 02:40:55 < Dark_Shikari> though of course you'll have to intersperse the aprpopriate high bit depth ifdefs
   2010-11-23 02:41:10 < Jumpyshoes> and i would need to redo the transpose
   2010-11-23 02:41:15 < Jumpyshoes> oh boy
   2010-11-23 02:41:26 < Jumpyshoes> wait
   2010-11-23 02:41:33 < Jumpyshoes> there's no transpose in the IDCT4_1D
   2010-11-23 02:41:34 < Jumpyshoes> yay
   2010-11-23 02:42:11 < Dark_Shikari> You'll need a TRANSPOSE_4x4D, yes
   2010-11-23 02:42:14 < Dark_Shikari> I think there already is one though
   2010-11-23 02:42:22 < Jumpyshoes> yea, there is
   2010-11-23 02:53:22 < rfw> Dark_Shikari: http://pastebin.com/GuM6bSXZ
   2010-11-23 02:54:32 < Dark_Shikari> nice
   2010-11-23 02:55:15 < rfw> i think my thresholds are a bit too high
   2010-11-23 02:55:25 < rfw> by how much do psnr and ssim differ?
   2010-11-23 02:55:28 < Dark_Shikari> "thresholds"?
   2010-11-23 02:55:35 < rfw> you know
   2010-11-23 02:55:42 < rfw> floating point arithmetic
   2010-11-23 02:55:50 < rfw> or should i just take the value as it is
   2010-11-23 02:55:59 < rfw> without converting it to a double
   2010-11-23 02:56:51 < Dark_Shikari> I'm not sure what you're talking about
   2010-11-23 02:56:58 < rfw> well
   2010-11-23 02:57:02 < rfw> they're floating point numbers, right
   2010-11-23 02:57:06 < Dark_Shikari> yeah
   2010-11-23 02:57:12 < rfw> so you can't perform direct comparisons
   2010-11-23 02:57:20 < rfw> so how much allowance should i give the values of psnr and ssim
   2010-11-23 02:57:25 < Dark_Shikari> "allowance"?
   2010-11-23 02:57:28 < Dark_Shikari> this isn't for a regression test
   2010-11-23 02:57:30 < Dark_Shikari> at least, not directly
   2010-11-23 02:57:33 < rfw> well
   2010-11-23 02:57:36 < Dark_Shikari> this is so we can see change in psnr and ssim over time at a given setting
   2010-11-23 02:57:39 < Dark_Shikari> e.g. to make a graph
   2010-11-23 02:57:42 < rfw> oh
   2010-11-23 02:57:47 < rfw> ah oh
   2010-11-23 02:58:01 < rfw> i need to stop thinking of this as a unit test
   2010-11-23 02:58:07 < Dark_Shikari> yeah
   2010-11-23 02:58:53 < nattofriends> LIFE AS UNIT TEST
   2010-11-23 03:01:01 < Dark_Shikari> Also, you script should be able to catch things like crashes
   2010-11-23 03:01:04 < Dark_Shikari> i.e. say "x264 crashed"
   2010-11-23 03:01:10 < Dark_Shikari> or, more usefully, SIGSEGV etc
   2010-11-23 03:01:14 < Dark_Shikari> *your script
   2010-11-23 03:01:21 < Dark_Shikari> As that's important to know too.
   2010-11-23 03:01:21 < Jumpyshoes> oh hi nattofriends
   2010-11-23 03:01:29 < Sean_McG> not using dejagnu for unit tests? ;)
   2010-11-23 03:01:33 < Dark_Shikari> another TJ resident?
   2010-11-23 03:01:34 < nattofriends> hi Jumpyshoes
   2010-11-23 03:01:41 < Jumpyshoes> nope
   2010-11-23 03:01:47 < Jumpyshoes> know him from elsewhere
   2010-11-23 03:01:54 < Dark_Shikari> the story of my life
   2010-11-23 03:02:18 < rfw> i swear i've seen nattofriends somewhere else too
   2010-11-23 03:02:26 < nattofriends> darkhold?
   2010-11-23 03:02:31 < rfw> oh probably
   2010-11-23 03:02:47 < rfw> i've probably seen everyone there is on that terrible network
   2010-11-23 03:03:42 < rfw> time to compile a program that segfaults
   2010-11-23 03:03:43 < kierank> [03:02] Dark_Shikari: the story of my life --> lol
   2010-11-23 03:04:03 < kierank> are you the Dark_Shikari from eve-online...
   2010-11-23 03:04:28 < Dark_Shikari> hurr hurr yes
   2010-11-23 03:04:30 < Dark_Shikari> exactly
   2010-11-23 03:05:27 < rfw> int main() { int *a = 0; int b = *a; }
   2010-11-23 03:05:34 < rfw> let's see what happens when i replace x264.exe with this
   2010-11-23 03:05:41 < Dark_Shikari> you could just add a 1/0
   2010-11-23 03:06:22 < rfw> heh it just gives me the windows blah blah has stopped working dialog
   2010-11-23 03:06:36 < Jumpyshoes> wait Dark_Shikari, can you macro on macros? basically can i template IDCT4_1D even if it's a macro?
   2010-11-23 03:06:53 < rfw> not sure how to handle segfaults in subprocesses
   2010-11-23 03:07:29 < Sean_McG> OK... I'mma go watch Panty & Stocking
   2010-11-23 03:08:56 < rfw> how do you even detect a segfault in a subprocess
   2010-11-23 03:09:16 < Sean_McG> you can't
   2010-11-23 03:09:26 < rfw> herp
   2010-11-23 03:09:37 < Sean_McG> other than grep the return text
   2010-11-23 03:09:50 < rfw> well i already dump the output to the terminal
   2010-11-23 03:09:53 < rfw> so i guess that's fine
   2010-11-23 03:10:37 < Dark_Shikari> Jumpyshoes: just make the size a parameter
   2010-11-23 03:10:41 < Dark_Shikari> IDCT4_1D w, blah, blah, blah
   2010-11-23 03:10:44 < Dark_Shikari> or d, blah, blah, blah
   2010-11-23 03:10:54 < Jumpyshoes> ah, okay
   2010-11-23 03:12:30 < Jumpyshoes> so when i reference variables, does it reset inside the inner macro?
   2010-11-23 03:12:35 < Dark_Shikari> ?
   2010-11-23 03:12:56 < Jumpyshoes> so i have something like
   2010-11-23 03:13:02 < Jumpyshoes> %macro IDCT 2
   2010-11-23 03:13:02 < Jumpyshoes> %macro IDCT4_1D_%1 %2 5-6
   2010-11-23 03:13:03 < Jumpyshoes> i guess
   2010-11-23 03:13:14 < Dark_Shikari> No
   2010-11-23 03:13:16 < Dark_Shikari> don't do that
   2010-11-23 03:13:18 < Dark_Shikari> there's no reason to
   2010-11-23 03:13:45 < Jumpyshoes> oh
   2010-11-23 03:16:37 < rfw> time to clone the git repo and build it o9k times
   2010-11-23 03:17:34 < Dark_Shikari> Sean_McG: you get a faster respons eif you post things here
   2010-11-23 03:18:25 < Sean_McG> DS: I like a record, but I can pastebin it if you like?
   2010-11-23 03:19:18 < rfw>       0 [main] python 5232 C:\cygwin\bin\python.exe: *** fatal error - unable to remap \\?\C:\cygwin\lib\python2.6\lib-dynload\select.dll to same address as parent: 0x360000 != 0x3F0000
   2010-11-23 03:19:22 < rfw> wtf cygwin ;_;
   2010-11-23 03:20:13 < Dark_Shikari> Sean_McG: sure
   2010-11-23 03:20:22 < Dark_Shikari> rfw: I think I've seen that before lol
   2010-11-23 03:20:54 < rfw> oh i have to rebaseall
   2010-11-23 03:22:34 < Sean_McG> http://www.pastebin.ca/1999626
   2010-11-23 03:24:06 < Dark_Shikari> Sean_McG: applied
   2010-11-23 03:24:11 < Sean_McG> thank you
   2010-11-23 03:24:21 < Sean_McG> OK, I go watch anime now ^^;
   2010-11-23 03:29:22 < rfw> Dark_Shikari: Running test ffmpeg... passed, took 2.7280 seconds (True)
   2010-11-23 03:29:28 < rfw> i think my x264 was just broken
   2010-11-23 03:29:28 < rfw> lol
   2010-11-23 03:29:34 < Dark_Shikari> lol
   2010-11-23 03:29:55 < Dark_Shikari> it might be useful to automatically check if ffmpeg or jm or similar is installed
   2010-11-23 03:29:59 < Dark_Shikari> and tell the user if it isn't, and don't run the test
   2010-11-23 03:30:06 < rfw> ah
   2010-11-23 03:30:06 < rfw> well
   2010-11-23 03:30:19 < rfw> i just check if it's the path?
   2010-11-23 03:30:34 < Dark_Shikari> I guess?
   2010-11-23 03:30:38 < Dark_Shikari> you could add an option to specify paths
   2010-11-23 03:31:50 < Dark_Shikari> also, one issue we have is that there are some known decoding issues in JM
   2010-11-23 03:31:54 < Dark_Shikari> particularly, it doesn't support x264's lossless mode
   2010-11-23 03:32:07 < Dark_Shikari> so if we e.g. just randomly tried parameters, we'd get some spurious failures
   2010-11-23 03:33:00 < rfw> ah
   2010-11-23 03:33:09 < rfw> Running test ffmpeg... failed: x264-output.yuv is not the same size as ffmpeg-output.yuv (11404800 vs 9542016)
   2010-11-23 03:33:13 < rfw> never mind it is my ffmpeg
   2010-11-23 03:33:19 < rfw> why do i have so many ffmpegs installed
   2010-11-23 03:35:05 < Dark_Shikari> they're like gremlins
   2010-11-23 03:35:09 < Dark_Shikari> don't feed them video after midnight
   2010-11-23 03:36:06 < rfw> ahaha i keep deleting folders that are opne in explorer
   2010-11-23 03:36:09 < rfw> causing it to crash
   2010-11-23 03:40:15 < rfw> Dark_Shikari: are there any revisions that don't compile?
   2010-11-23 03:43:22 < kemuri-_9> revisions of x264?
   2010-11-23 03:44:27 < rfw> yeah
   2010-11-23 03:48:59 < kemuri-_9> hmm... i think there have a been a few, they're usually fairly rare (well it depends on the architecture, x86 being the primary - others are usually broken on a major change until someone coughs up a patch)
   2010-11-23 03:49:27 < rfw> ah
   2010-11-23 03:49:33 < rfw> i'm just looking to test my automatic bisection
   2010-11-23 03:53:17 < Dark_Shikari> probably nothing won't compile on x86 on gcc 3.4.5
   2010-11-23 03:53:20 < Dark_Shikari> i.e. what I compile on
   2010-11-23 03:53:23 < Dark_Shikari> you could easily test it though!
   2010-11-23 03:53:24 < Dark_Shikari> make a local commit!
   2010-11-23 03:53:25 < Dark_Shikari> :)
   2010-11-23 04:02:00 < rfw> lol
   2010-11-23 04:10:05 < rfw> Bisecting between 8eaf8a (good) and HEAD (bad)...
   2010-11-23 04:10:17 < rfw> let's hope this works
   2010-11-23 04:11:51 < Dark_Shikari> also, GCI students, feel free to hang out in #x264
   2010-11-23 04:12:06 < Dark_Shikari> where we discuss a wide variety of topics that are, in fact, totally x264-related
   2010-11-23 04:12:12 < Dark_Shikari> like touhou and starcraft
   2010-11-23 04:17:03 < rfw> coincidentally i have touhou music on
   2010-11-23 04:17:39 < Dark_Shikari> I would if I wasn't watching the gomtv live starcraft stream
   2010-11-23 04:17:56 < Dark_Shikari> what's with this high correlation between "working on x264" and "touhou"
   2010-11-23 04:18:36 < rfw> :P
   2010-11-23 04:18:46 < saintdev> sadly touhou is not such a good candidate for ffaac hacking :(
   2010-11-23 04:19:09 < Dark_Shikari> why not
   2010-11-23 04:19:13 < Dark_Shikari> there's touhou music for every genre
   2010-11-23 04:19:46 < rfw> Project result: FAILED, took 5.0750 seconds.
   2010-11-23 04:19:46 < rfw> No tests failed on 85d4e2df22e8a894b3746f9a5ead33bfdbee9566; revision is good.
   2010-11-23 04:19:52 < rfw> wtf i definitely broke something here
   2010-11-23 04:20:05 < Dark_Shikari> also can you make it take revision numbers instead of git hashes?
   2010-11-23 04:20:07 < Dark_Shikari> see version.sh
   2010-11-23 04:20:19 < rfw> let me fix this first lol
   2010-11-23 04:20:31 < Dark_Shikari> well, both would be good too
   2010-11-23 04:20:32 < Dark_Shikari> and yeah
   2010-11-23 04:24:05 < rfw> 8f95149b2a1943930968f098c904d84ef4b33555 determined to be bad.
   2010-11-23 04:24:06 < rfw> 8f95149b2a1943930968f098c904d84ef4b33555 eye am broken!
   2010-11-23 04:24:08 < rfw> hoory
   2010-11-23 04:24:11 < rfw> +a
   2010-11-23 04:25:21 < Dark_Shikari> the strongest revision?
   2010-11-23 04:26:16 < rfw> lol
   2010-11-23 04:26:21 < rfw> glad you get the reference
   2010-11-23 04:26:43 < Dark_Shikari> I get references, even really really stupid ones
   2010-11-23 04:26:52 < Dark_Shikari> pun (fortunately) not intended
   2010-11-23 04:26:59 < rfw> lol
   2010-11-23 04:31:37 < saintdev> <fozzy bear>baka baka baka</fozzy>
   2010-11-23 04:54:34 < Alex_W> so any news on the problem with the replicated blu-ray that kierank mentioned yesterday?
   2010-11-23 04:57:21 < Dark_Shikari> ask him
   2010-11-23 04:57:30 < Dark_Shikari> he had an interesting quote on it but I can't give it to you
   2010-11-23 04:57:34 < Dark_Shikari> without ok from him
   2010-11-23 04:57:45 < Dark_Shikari> (tl;dr: they don't think its x264's problem)
   2010-11-23 05:02:39 < Alex_W> i see, so there are no known issues with the revision they're using that could cause any compatibility problems?
   2010-11-23 05:03:52 < Dark_Shikari> don't know what revision
   2010-11-23 05:03:57 < Dark_Shikari> but that's doubtufl
   2010-11-23 05:04:00 < Dark_Shikari> they did massive testing
   2010-11-23 05:04:03 < Dark_Shikari> on tons of boxes
   2010-11-23 05:04:10 < Dark_Shikari> and the box that's having problems is also having subtitle issues
   2010-11-23 05:04:14 < Dark_Shikari> so they think it isn't x264-related
   2010-11-23 05:05:27 < Alex_W> right, so it could just be a faulty box
   2010-11-23 05:09:53 < rfw> Dark_Shikari: http://pastebin.com/JxgRJ0kh
   2010-11-23 05:10:02 < rfw> looking for something like this?
   2010-11-23 05:11:40 < Dark_Shikari> except with revision #s, that looks really awesome
   2010-11-23 05:11:46 < rfw> lol
   2010-11-23 05:13:03 < Dark_Shikari> psnr test should use --tune psnr
   2010-11-23 05:13:05 < Dark_Shikari> ssim test should use --tune ssim
   2010-11-23 05:13:14 < Dark_Shikari> and we'll need some way to integrate "trying lots of options" into this
   2010-11-23 05:15:41 < rfw> --tune psnr in the regression tester/
   2010-11-23 05:15:44 < rfw> ?
   2010-11-23 05:16:11 < Dark_Shikari> in the x264 options
   2010-11-23 05:16:15 < rfw> ah
   2010-11-23 05:16:20 < Dark_Shikari> when measuring psnr we use tune psnr (to tell x264 to optimize for psnr)
   2010-11-23 05:16:27 < Dark_Shikari> psnr values aren't very useful if the encoder isn't optimizing for it
   2010-11-23 05:17:29 < rfw> oh goddammit notepad++
   2010-11-23 05:17:32 < rfw> clicked the wrong button
   2010-11-23 05:18:15 < Dark_Shikari> hmm, there is one thing that bugs me
   2010-11-23 05:18:19 < Dark_Shikari> "PSNR" is generally tested with a single set of settings
   2010-11-23 05:18:27 < Dark_Shikari> i.e. I want to know "how psnr has changed over time given some set of settings"
   2010-11-23 05:18:29 < Dark_Shikari> But...
   2010-11-23 05:18:40 < Dark_Shikari> for regressions, we really just want to know whether it's working or not.
   2010-11-23 05:18:49 < Dark_Shikari> so regressions conceptually cover all settings
   2010-11-23 05:18:54 < Dark_Shikari> while a psnr or ssim test covers just one.,
   2010-11-23 05:41:22 < wipple> Dark_Shikari: my first patch was replaced by kemuri-_9's?
   2010-11-23 05:41:27 < Dark_Shikari> yes
   2010-11-23 05:41:51 < wipple> ic
   2010-11-23 05:42:03 < Dark_Shikari> your second one, the one that actually affects output, is still in =p
   2010-11-23 05:43:39 < wipple> i have to fix second patch
   2010-11-23 05:44:00 < Dark_Shikari> ah ok
   2010-11-23 05:44:08 < Dark_Shikari> give me the new version and I'll update it
   2010-11-23 05:55:43 < Jumpyshoes> hey Dark_Shikari, i thought about it some more, and wouldn't add4x4_idct basically need to be rewritten from scratch for mmx? mmx can only hold 64bits, so you need to have all the registers used to store all the data (if coef are 32bit)
   2010-11-23 05:55:50 < Dark_Shikari> Yes
   2010-11-23 05:55:55 < Dark_Shikari> It wouldn't be very *difficult*
   2010-11-23 05:56:07 < Dark_Shikari> the approach would generally be the same
   2010-11-23 05:56:12 < Dark_Shikari> but you certainly can't just template it outright
   2010-11-23 05:56:16 < Jumpyshoes> ah
   2010-11-23 05:56:20 < Dark_Shikari> If you want to make that your second asm function, you could
   2010-11-23 05:56:23 < Jumpyshoes> i think i can for SSE though
   2010-11-23 05:56:28 < Dark_Shikari> for the first, do see
   2010-11-23 05:56:29 < Dark_Shikari> *sse
   2010-11-23 05:56:40 < Jumpyshoes> okay
   2010-11-23 06:00:59 < Jumpyshoes> what is pw_32?
   2010-11-23 06:01:39 < Dark_Shikari> {32, 32, 32, 32...}
   2010-11-23 06:01:43 < Dark_Shikari> words
   2010-11-23 06:01:45 < Dark_Shikari> packed word 32
   2010-11-23 06:01:48 < Dark_Shikari> see const-a.asm
   2010-11-23 06:01:50 < Dark_Shikari> where they're declared
   2010-11-23 06:01:53 < Jumpyshoes> ah
   2010-11-23 06:06:15 < rfw> class factories -- ah the miracles of python metaprogramming
   2010-11-23 06:06:43 < Dark_Shikari> factoryfactoryfactory
   2010-11-23 06:07:40 < rfw> time to turn implement your clusterfuck permutations
   2010-11-23 06:07:44 < rfw> :3
   2010-11-23 06:07:59 < saintdev> just write it in brainfuck
   2010-11-23 06:08:03 < rfw> this isn't going to look pretty though
   2010-11-23 06:12:34 < nattofriends> SingletonFactorySingleton
   2010-11-23 06:13:22 < rfw> that doesn't even make sense!
   2010-11-23 06:13:49 < Jumpyshoes> error: instruction expected after label <-- what does this error mean?
   2010-11-23 06:14:05 < Dark_Shikari> syntax error
   2010-11-23 06:14:11 < Jumpyshoes> oh
   2010-11-23 06:14:12 < Jumpyshoes> bleh
   2010-11-23 06:14:41 < rfw> http://pastebin.com/X3x7Fb57
   2010-11-23 06:15:16 < Dark_Shikari> rfw: it might be nicer to try to cover more options than mine, but without as exhaustive a search
   2010-11-23 06:15:22 < Dark_Shikari> mine for example only tests CRF ratecontrol mode
   2010-11-23 06:15:25 < Dark_Shikari> not ABR, CBR, 2-pass, etc
   2010-11-23 06:16:04 < Dark_Shikari> for example, you can use a pseudorandom combination of options
   2010-11-23 06:16:13 < rfw> TypeError: unbound method run() must be called with YUVOutputComparison_film___ultrafast instance as first argument (got nothing instead)
   2010-11-23 06:16:14 < rfw> blah wtf
   2010-11-23 06:16:38 < rfw> oh
   2010-11-23 06:16:42 < rfw> forgot to instantiate the class
   2010-11-23 06:16:43 < rfw> hurr hurr
   2010-11-23 06:20:41 < Jumpyshoes> Dark_Shikari, if i write an implementation of an asm function, how do i test it?
   2010-11-23 06:20:49 < Dark_Shikari> 1) declare it in the appropriate C header file
   2010-11-23 06:20:58 < Dark_Shikari> 2) assign it to the appropriate function pointer (in your case, in common/dct.c)
   2010-11-23 06:21:02 < Dark_Shikari> there's a big init function
   2010-11-23 06:21:10 < Dark_Shikari> with stuff like dctf->myfunc = myfuncname_sse2;
   2010-11-23 06:21:16 < Dark_Shikari> put it in the right place based on its type (sse2, etc)
   2010-11-23 06:21:21 < Dark_Shikari> 3) make checkasm;./checkasm
   2010-11-23 06:21:27 < Dark_Shikari> if yours is high bit depth, of course, make sure that:
   2010-11-23 06:21:40 < Dark_Shikari> a) it's assigned under the #if high bit depth in common/dct.c
   2010-11-23 06:21:44 < Dark_Shikari> b) you configured with high bit depth
   2010-11-23 06:22:40 < Jumpyshoes> k
   2010-11-23 06:32:40 < Jumpyshoes> oh wow, it compiled
   2010-11-23 06:32:44 < Jumpyshoes> off to a good start
   2010-11-23 06:32:54 < Jumpyshoes> segfault!
   2010-11-23 06:32:58 < Jumpyshoes> lovel
   2010-11-23 06:32:59 < Jumpyshoes> y
   2010-11-23 06:38:51 < wipple> Dark_Shikari: i misunderstood, don't need to fix my second patch.
   2010-11-23 06:38:56 < Dark_Shikari> ah ok
   2010-11-23 06:39:40 < wipple> it might be better to fix commit message? i replaced avformat_license() with swscale_license()
   2010-11-23 06:39:49 < wipple> but there in no mention
   2010-11-23 06:39:53 < wipple> about it
   2010-11-23 06:42:08 < Jumpyshoes> yay, no more segfaulting
   2010-11-23 06:43:23 < wipple> *there _is_ no mention
   2010-11-23 06:44:04 < Jumpyshoes> wait, why can i see pw_32, but not pw_64?
   2010-11-23 06:45:29 < rfw> Dark_Shikari: cartesian product regression testing sure takes lolforever
   2010-11-23 06:45:45 < rfw> i better implement that pseudorandom thing
   2010-11-23 06:47:15 < Dark_Shikari> rfw: yeah, my thought is to define a massive set of parameters and some sane ranges
   2010-11-23 06:47:27 < Dark_Shikari> and make your script take a seed + a number of tests
   2010-11-23 06:47:31 < Dark_Shikari> and it randomly picks combinations thereof
   2010-11-23 06:50:04 < rfw>     if randint(0, 4):
   2010-11-23 06:50:04 < rfw>         YUVOutputComparison.test_jm = disabled("randomly disabled")(YUVOutputComparison.test_jm)
   2010-11-23 06:50:05 < rfw>         YUVOutputComparison.test_ffmpeg = disabled("randomly disabled")(YUVOutputComparison.test_ffmpeg)
   2010-11-23 06:50:05 < rfw> :3
   2010-11-23 06:50:21 < Dark_Shikari> I don't mean random choice of tests
   2010-11-23 06:50:24 < Dark_Shikari> I mean random choice of parameters =p
   2010-11-23 06:50:30 < rfw> yeah
   2010-11-23 06:50:34 < rfw> it is a random choice of parameters
   2010-11-23 06:50:52 < Dark_Shikari> btw, the parameter array (and sane ranges) should be easily editable by us
   2010-11-23 06:50:54 < Dark_Shikari> so we can change it later
   2010-11-23 06:51:01 < rfw> http://pastebin.com/FRdfXbpp
   2010-11-23 06:51:03 < Dark_Shikari> i.e. with new params, etc
   2010-11-23 06:51:05 < rfw> it's sorta editable
   2010-11-23 06:51:05 < rfw> lol
   2010-11-23 06:51:20 < Dark_Shikari> It will need to be about 100 lines longer than that
   2010-11-23 06:51:27 < Dark_Shikari> so that format will probably not be very readable
   2010-11-23 06:51:34 < Dark_Shikari> i.e. you'll have to mentally match up the for index with the line number
   2010-11-23 06:51:49 < Dark_Shikari> so if this was C, I'd want something like this
   2010-11-23 06:51:52 < rfw> derp
   2010-11-23 06:51:59 < Dark_Shikari> {"subme", 0, 10}
   2010-11-23 06:52:09 < Dark_Shikari> makes sense?
   2010-11-23 06:52:38 < rfw> not really no
   2010-11-23 06:52:40 < rfw> lol
   2010-11-23 06:52:53 < Dark_Shikari> in order to generate a commandline, for each of N parameters, you pick one of M values
   2010-11-23 06:53:03 < Dark_Shikari> so for example, if your parameters are A and B
   2010-11-23 06:53:06 < Dark_Shikari> and their min values are 0 and max are 10
   2010-11-23 06:53:10 < rfw> ah
   2010-11-23 06:53:10 < Dark_Shikari> you might do --A 5 --B 7
   2010-11-23 06:53:13 < rfw> ah i get you
   2010-11-23 06:53:14 < Dark_Shikari> or --A 2 --B 9
   2010-11-23 06:53:37 < rfw> you're not giving those 4 points away that easily are you ;__;
   2010-11-23 06:53:48 < Dark_Shikari> This isn't actually that hard, I imagine it's just a big array that you iterate over.
   2010-11-23 06:54:08 < Dark_Shikari> If you make it extensible, you don't have to write the whole thing
   2010-11-23 06:54:10 < Dark_Shikari> We can add it later.
   2010-11-23 06:54:13 < rfw> yeah
   2010-11-23 06:54:17 < rfw> it is extensible
   2010-11-23 06:54:17 < rfw> lol
   2010-11-23 06:54:21 < rfw> to the point it's silly
   2010-11-23 06:54:30 < Dark_Shikari> A for loop like that is not very readable with 100 options
   2010-11-23 06:54:45 < rfw> well
   2010-11-23 06:54:46 < rfw> it is
   2010-11-23 06:54:50 < rfw> you just add more elements to the array
   2010-11-23 06:54:56 < rfw> i flattened your nested loop
   2010-11-23 06:54:58 < rfw> into one loop
   2010-11-23 06:55:07 < Dark_Shikari> for option in A,C,Q,Y,X,D,I,S,B,W,C
   2010-11-23 06:55:08 < Dark_Shikari> 1
   2010-11-23 06:55:08 < Dark_Shikari> 2
   2010-11-23 06:55:08 < Dark_Shikari> 3
   2010-11-23 06:55:08 < Dark_Shikari> 4
   2010-11-23 06:55:11 < Dark_Shikari> 5
   2010-11-23 06:55:13 < Dark_Shikari> 6
   2010-11-23 06:55:16 < Dark_Shikari> 7
   2010-11-23 06:55:18 < Dark_Shikari> 8
   2010-11-23 06:55:21 < Dark_Shikari> 9
   2010-11-23 06:55:24 < Dark_Shikari> which option goes with which line?
   2010-11-23 06:55:26 < Dark_Shikari> fucked if I know!
   2010-11-23 06:55:30 < rfw> um
   2010-11-23 06:55:31 < rfw> what?
   2010-11-23 06:55:35 < rfw> YUVOutputComparison.options = filter(None, reduce(operator.add, [ opt.split(" ") for opt in options ]))
   2010-11-23 06:55:36 < Dark_Shikari> your for loop has all your option names on one line
   2010-11-23 06:55:40 < Dark_Shikari> the one you pasted
   2010-11-23 06:55:43 < rfw> oh
   2010-11-23 06:55:44 < rfw> whoops
   2010-11-23 06:55:46 < Dark_Shikari> and then it has one line for each option
   2010-11-23 06:55:53 < Dark_Shikari> and mapping the two to each other is difficult visually
   2010-11-23 06:56:00 < rfw> well
   2010-11-23 06:56:02 < rfw> it's fixed now :p
   2010-11-23 06:56:13 < Dark_Shikari> good =
   2010-11-23 06:56:14 < Dark_Shikari> =p
   2010-11-23 06:56:16 < rfw> http://pastebin.com/G0qeRJqZ
   2010-11-23 06:56:32 < rfw> just add more parameters to the product function
   2010-11-23 06:56:33 < rfw> lol
   2010-11-23 06:56:53 < Dark_Shikari> ah, sweet
   2010-11-23 06:57:03 < Dark_Shikari> what's the randint 0,4 for?
   2010-11-23 06:57:07 < rfw> oh
   2010-11-23 06:57:10 < rfw> random test selection
   2010-11-23 06:57:14 < rfw> so you don't run all of them
   2010-11-23 06:58:09 < Dark_Shikari> huh?
   2010-11-23 06:58:27 < rfw> well
   2010-11-23 06:58:38 < rfw> it generates a random number from 0-4
   2010-11-23 06:58:48 < rfw> so there's a 1 in 5 chance of a test running
   2010-11-23 06:59:01 < rfw> you can seed it of course
   2010-11-23 06:59:03 < Dark_Shikari> ?  I don't see how that applies to the algorithm I mentioned
   2010-11-23 06:59:04 < rfw> so it's consistent
   2010-11-23 06:59:13 < Dark_Shikari> for any given test, you should randomly assemble a commandline
   2010-11-23 06:59:13 < rfw> wait
   2010-11-23 06:59:18 < Dark_Shikari> at no point in there is a "random chance of running a test"
   2010-11-23 06:59:18 < rfw> yeah
   2010-11-23 06:59:30 < rfw> isn't this more or less the same thing
   2010-11-23 06:59:32 < Dark_Shikari> If you're going to iterate over all possible commandlines
   2010-11-23 06:59:34 < Dark_Shikari> and only run some of them
   2010-11-23 06:59:40 < Dark_Shikari> well, good luck when there are 10^100 possible commandlines
   2010-11-23 06:59:50 < rfw> wait what
   2010-11-23 06:59:52 < rfw> i'm confused now
   2010-11-23 07:00:00 < Dark_Shikari> You will run N tests.
   2010-11-23 07:00:07 < Dark_Shikari> In each test, you will randomly assemble a commandline.
   2010-11-23 07:00:13 < Dark_Shikari> And test it.
   2010-11-23 07:00:21 < Dark_Shikari> The randomness will be based on a user-supplied seed.
   2010-11-23 07:00:25 < Dark_Shikari> The N will be user-supplied.
   2010-11-23 07:00:30 < Jumpyshoes> Dark_Shikari: are there different constants for high bit?
   2010-11-23 07:00:31 < rfw> but aren't i randomly assembling a command here
   2010-11-23 07:00:38 < Dark_Shikari> No, you're iterating over all possible commandlines
   2010-11-23 07:00:41 < Dark_Shikari> and only running some of them
   2010-11-23 07:00:42 < Dark_Shikari> right?
   2010-11-23 07:00:45 < rfw> yeah
   2010-11-23 07:00:46 < rfw> isn't that
   2010-11-23 07:00:50 < Dark_Shikari> Jumpyshoes: if you need a new one, make it
   2010-11-23 07:00:51 < rfw> functionally equivalent?
   2010-11-23 07:00:53 < Dark_Shikari> NO!
   2010-11-23 07:00:56 < rfw> :(
   2010-11-23 07:00:57 < Dark_Shikari> If there are 10^100 possible commandlines
   2010-11-23 07:00:58 < Dark_Shikari> and I want 100 of them
   2010-11-23 07:01:03 < rfw> oh
   2010-11-23 07:01:06 < Dark_Shikari> your solution will take longer than the life of the universe!
   2010-11-23 07:01:19 < rfw> derp
   2010-11-23 07:01:27 < Jumpyshoes> i made one in the const-a.asm file
   2010-11-23 07:01:33 < Dark_Shikari> Jumpyshoes: make sure there isn't already one
   2010-11-23 07:01:35 < Dark_Shikari> there might be a pd_32
   2010-11-23 07:01:38 < Jumpyshoes> but yasm can't see it for some reason
   2010-11-23 07:01:39 < Jumpyshoes> oh
   2010-11-23 07:01:46 < Dark_Shikari> you have to add it in your file
   2010-11-23 07:01:48 < Dark_Shikari> extern pd_32
   2010-11-23 07:01:53 < Dark_Shikari> see the top of your file
   2010-11-23 07:01:56 < Jumpyshoes> aah
   2010-11-23 07:02:07 < rfw> actually Dark_Shikari i don't see how
   2010-11-23 07:02:10 < rfw> if i just randomized the options
   2010-11-23 07:02:17 < rfw> then picked the first 100
   2010-11-23 07:02:19 < Dark_Shikari> No
   2010-11-23 07:02:24 < Dark_Shikari> that isn't what I asked for
   2010-11-23 07:02:26 < Dark_Shikari> read what I said again
   2010-11-23 07:02:30 < Dark_Shikari> let me write it in C, ok?
   2010-11-23 07:02:34 < rfw> um okay
   2010-11-23 07:02:37 < Dark_Shikari> for(int i = 0; i < numruns; i++) {
   2010-11-23 07:02:55 < Dark_Shikari> String commandline = randomCommandline();
   2010-11-23 07:03:02 < Dark_Shikari> test(commandline);
   2010-11-23 07:03:03 < Dark_Shikari> }
   2010-11-23 07:03:11 < Dark_Shikari> "randomcommandline" generates one, exactly one, random commandline.
   2010-11-23 07:03:14 < Dark_Shikari> just one.  not zero, not two, one.
   2010-11-23 07:03:50 < Dark_Shikari> you aren't shuffling all possible commandlines
   2010-11-23 07:03:55 < Dark_Shikari> you are just generating one random one
   2010-11-23 07:04:02 < Dark_Shikari> randomCommandline is as follows:
   2010-11-23 07:04:07 < rfw> yes i get what you mean
   2010-11-23 07:04:09 < Dark_Shikari> for all options in optionArray:
   2010-11-23 07:04:26 < rfw> but what i'm saying is shuffle the individual subcommands
   2010-11-23 07:04:28 < Dark_Shikari>     optionValue = random option in optionArray[option]
   2010-11-23 07:04:30 < rfw> like [ "--tune %s" % t for t in ("film", "zerolatency") ]
   2010-11-23 07:04:38 < rfw> wait never mind i'm being silly
   2010-11-23 07:04:51 < rfw> yeah i see what you mean
   2010-11-23 07:05:07 < rfw> i feel kinda dumb now ._.
   2010-11-23 07:05:36 < Dark_Shikari> feeling dumb is fine, happens all the time
   2010-11-23 07:05:41 < Dark_Shikari> just grep the commit logs for "10L"
   2010-11-23 07:06:26 < Dark_Shikari> well, 1[0]*[l|L]
   2010-11-23 07:12:23 < Dark_Shikari> so in terms of committing this regression tester of yours
   2010-11-23 07:12:29 < Dark_Shikari> what about the actual lib it depends on which you said isn't finished?
   2010-11-23 07:23:18 < rfw> it's part of my regression tester
   2010-11-23 07:23:27 < rfw> sorry, had to do something
   2010-11-23 07:24:27 < Dark_Shikari> no worries, not going to push you or anything
   2010-11-23 07:27:08 < rfw> Dark_Shikari: http://pastebin.com/vybYV0VR
   2010-11-23 07:27:16 < rfw> is this more along the lines of what you were looking for?
   2010-11-23 07:27:30 < Dark_Shikari> yup, exactly
   2010-11-23 07:27:33 < rfw> :D
   2010-11-23 07:27:38 < Dark_Shikari> fyi I can't really read python very well
   2010-11-23 07:27:42 < Dark_Shikari> I haven't used it in like 5 years
   2010-11-23 07:27:42 < rfw> lol
   2010-11-23 07:27:52 < Dark_Shikari> I last used python seriously for AI class in high school
   2010-11-23 07:27:52 < rfw> it's more readable than perl
   2010-11-23 07:28:05 < rfw> you know, the old elbows on keyboard joke
   2010-11-23 07:28:36 < Dark_Shikari> yes yes
   2010-11-23 07:29:39 < rfw> also, version numbers instead of commit hashes?
   2010-11-23 07:29:47 < Dark_Shikari> see version.sh
   2010-11-23 07:29:57 < Dark_Shikari> since x264 uses a completely linear git tree, version numbers are more usable than hashes
   2010-11-23 07:30:09 < rfw> why did i just try to run it in cmd
   2010-11-23 07:30:14 < Dark_Shikari> e.g. the current x264 is r1790
   2010-11-23 07:32:30 < rfw> oh god i can't read bash
   2010-11-23 07:33:46 < Dark_Shikari> You don't have to
   2010-11-23 07:33:49 < Dark_Shikari> It just basically counts commits.
   2010-11-23 07:33:49 < Dark_Shikari> lol
   2010-11-23 07:34:01 < Dark_Shikari> pengvado could explain it though.
   2010-11-23 07:34:13 < rfw> so why not just
   2010-11-23 07:34:15 < rfw> git log --format=oneline | wc -l
   2010-11-23 07:34:16 < rfw> :|
   2010-11-23 07:34:36 < rfw> why the git rev-list origin/master | sort | join config.git-hash - | wc -l | awk '{print $1}'
   2010-11-23 07:35:24 < Dark_Shikari> Because it does a bit of extra magic
   2010-11-23 07:35:28 < Dark_Shikari> specifically, it does the following
   2010-11-23 07:35:33 < Dark_Shikari> suppose latest x264 is 1790
   2010-11-23 07:35:33 < dj_tjerk> origin/master doesn't make any sense if you do local regression testing does it?
   2010-11-23 07:35:36 < Dark_Shikari> suppose I have 5 local commits
   2010-11-23 07:35:41 < Dark_Shikari> it'll show my version as 1790+5
   2010-11-23 07:35:47 < Dark_Shikari> suppose I also have a modified local tree when I do it
   2010-11-23 07:35:50 < Dark_Shikari> it'll show my version as 1790+5M
   2010-11-23 07:35:53 < rfw> oh
   2010-11-23 07:35:53 < Dark_Shikari> or something like that
   2010-11-23 07:35:58 < rfw> i see
   2010-11-23 07:36:43 < Dark_Shikari> in your case, it might be useful to distinguish between local and otherwise
   2010-11-23 07:36:52 < Dark_Shikari> e.g. if my bug is in revision 1790+4
   2010-11-23 07:36:55 < Dark_Shikari> as opposed to 1794
   2010-11-23 07:37:08 < rfw> ah
   2010-11-23 07:37:10 < Dark_Shikari> but the latter might be fine too.
   2010-11-23 07:39:13 < rfw> is there any reason why the bash script does a sort
   2010-11-23 07:39:23 < rfw> oh nvm
   2010-11-23 07:40:37 < Dark_Shikari> You'll probably want to cache these revision numbers at the start to avoid recalculating them repeatedly.
   2010-11-23 07:40:43 < Dark_Shikari> i.e. the mapping of hash to revnum
   2010-11-23 07:40:45 < Dark_Shikari> or similar
   2010-11-23 07:40:51 < rfw> yeah
   2010-11-23 07:53:22 < rfw> welp, now to write a routine to  convert it the other way
   2010-11-23 07:58:19 < rfw> Testing project x264 at revision 1790+4M...
   2010-11-23 08:01:43 < Dark_Shikari> You could just internally use hashes
   2010-11-23 08:01:46 < Dark_Shikari> and convert only for display purposes
   2010-11-23 08:01:49 < rfw> i do
   2010-11-23 08:01:55 < Dark_Shikari> though I geuss you need to convert the other way for user input
   2010-11-23 08:01:59 < Dark_Shikari> i.e. "I want to test revision X through Y"
   2010-11-23 08:02:05 < rfw> yeah
   2010-11-23 08:02:14 < Dark_Shikari> Though the most common thing for that isn't revision numbers
   2010-11-23 08:02:17 < Dark_Shikari> but rather something like
   2010-11-23 08:02:19 < Dark_Shikari> HEAD~10
   2010-11-23 08:02:22 < Dark_Shikari> like in git parlance
   2010-11-23 08:02:26 < Dark_Shikari> i.e. "I want to test the last 10 revisions"
   2010-11-23 08:02:28 < rfw> safsagdshasd
   2010-11-23 08:02:35 < rfw> TIME TO FIX
   2010-11-23 08:02:46 < Dark_Shikari> anyways, let's get down how this interface will work
   2010-11-23 08:02:57 < Dark_Shikari> so you don't keep changing things
   2010-11-23 08:02:59 < Dark_Shikari> and doing unnecessary work
   2010-11-23 08:03:05 < Dark_Shikari> if you have to use hashes, that's ok
   2010-11-23 08:03:10 < rfw> nah it's fine
   2010-11-23 08:03:24 < rfw> i'm just checking if ~ is in revnumber
   2010-11-23 08:03:31 < rfw> though
   2010-11-23 08:03:42 < rfw> then what if somebody tries to 1780+4~3
   2010-11-23 08:03:57 < rfw> can i just assume nobody's going to do that
   2010-11-23 08:05:19 < Dark_Shikari> lol
   2010-11-23 08:05:20 < Dark_Shikari> probably
   2010-11-23 08:05:24 < Dark_Shikari> yes you can assume people are not stupid
   2010-11-23 08:05:41 < rfw> \o/
   2010-11-23 08:06:44 < Dark_Shikari> this is for devs, not users
   2010-11-23 08:06:48 < Dark_Shikari> it can have less tolerance for bad input
   2010-11-23 08:07:01 < Dark_Shikari> though it should at least error out cleanly if you give it stupid shit
   2010-11-23 08:07:29 < rfw> why the hell is windows not letting me delete the x264 folder
   2010-11-23 08:07:44 < rfw> "you need the computer administrator's permissions to change this folder"
   2010-11-23 08:07:49 < rfw> but i am the computer administrator :(
   2010-11-23 08:11:06 < Dark_Shikari> try not having it open in a cygwin window
   2010-11-23 08:11:37 < rfw> i don't
   2010-11-23 08:11:42 < rfw> i don't even have ownership of the folder
   2010-11-23 08:11:50 < rfw> wtf
   2010-11-23 08:12:10 < Dark_Shikari> lol
   2010-11-23 08:12:16 < Dark_Shikari> try removing it in cygwin
   2010-11-23 08:12:31 < rfw> nothing
   2010-11-23 08:12:43 < rfw> $ cd x264
   2010-11-23 08:12:44 < rfw> bash: cd: x264: Permission denied
   2010-11-23 08:12:45 < rfw> :(
   2010-11-23 08:12:49 < rfw> can't even enter it
   2010-11-23 08:13:08 < rfw> drwxr-x---  1 ????????       ????????    0 2010-11-23 21:05 x264
   2010-11-23 08:13:39 < rfw> i can't even get group/owner information
   2010-11-23 08:14:22 < nattofriends> restart! restart!
   2010-11-23 08:14:44 < rfw> nevar!
   2010-11-23 08:16:59 < Dark_Shikari> o.0
   2010-11-23 08:20:51 < Rodeo> Dark_Shikari: FWIW, http://paste.handbrake.fr/pastebin.php?show=1883
   2010-11-23 08:22:46 < Rodeo> not that the current behavior bother me (on the contrary), but if this the correct behavior, then you have a patch
   2010-11-23 08:24:49 < Dark_Shikari> I dunno if that'll work
   2010-11-23 08:25:09 < Dark_Shikari> I don't think the cplxr_sum stuff is used in 2-pass
   2010-11-23 08:26:51 < Rodeo> well, without the patch, I get the final ratefactor for ./x264 infile -o outfile --pass 1 bitrate b
   2010-11-23 08:26:57 < Rodeo> with the patch, it's not printed
   2010-11-23 08:27:02 < Dark_Shikari> Is it *accurate*?
   2010-11-23 08:27:03 < rfw> wow, the gci rankings haven't changed at all
   2010-11-23 08:27:26 < Dark_Shikari> Rodeo: wait I'm confused
   2010-11-23 08:27:29 < Dark_Shikari> what does your patch do?
   2010-11-23 08:27:33 < Dark_Shikari> are you trying to print it in 2-pass mode?
   2010-11-23 08:27:36 < Dark_Shikari> on the second pass?
   2010-11-23 08:27:37 < Dark_Shikari> or what
   2010-11-23 08:27:52 < Dark_Shikari> rfw: what, trying to win the grand prize? =p
   2010-11-23 08:27:56 < Rodeo> currently, it's printed in the first pass of a 2-pass encode
   2010-11-23 08:28:04 < Rodeo> with that patch, this no longer happens
   2010-11-23 08:28:07 < rfw> i'm allowed to be ambitious, no :p
   2010-11-23 08:28:19 < Dark_Shikari> Rodeo: er, that's removing a feature
   2010-11-23 08:28:45 < Dark_Shikari> rfw: I assume the grand prize will be won by a very very dedicated nerd in a very small basement, taking massive numbers of overrated tasks.
   2010-11-23 08:28:49 < Rodeo> OK, I thought that it wasn't supposed to do this
   2010-11-23 08:28:52 < rfw> lol
   2010-11-23 08:28:52 < Dark_Shikari> No, it is.
   2010-11-23 08:28:57 < Rodeo> but if current behavior is OK, then ignore my patch
   2010-11-23 08:29:05 < Dark_Shikari> Rodeo: I thought you wanted it in the second pass
   2010-11-23 08:29:07 < Dark_Shikari> _that_ would be cool.
   2010-11-23 08:29:08 < rfw> i don't want to make surveys or posters
   2010-11-23 08:29:16 < Dark_Shikari> rfw: I lol at those tasks
   2010-11-23 08:29:20 < Dark_Shikari> MAKE A POSTER FOR MY PROJECT
   2010-11-23 08:29:24 < Dark_Shikari> Actually, here's an idea
   2010-11-23 08:29:25 < Rodeo> gotta go, I'll see what I can do about the altter later
   2010-11-23 08:29:25 < rfw> lolol
   2010-11-23 08:29:28 < Dark_Shikari> outsource
   2010-11-23 08:29:36 < Dark_Shikari> find the easiest projects which can be done for like $5
   2010-11-23 08:29:38 < Dark_Shikari> and outsource them
   2010-11-23 08:29:46 < Dark_Shikari> through some mechanical turk like website
   2010-11-23 08:29:54 < Dark_Shikari> 2) ???
   2010-11-23 08:29:55 < Dark_Shikari> 3) profit
   2010-11-23 08:30:33 < rfw> oh god, i have to rethink my side-by-side comparison output
   2010-11-23 08:30:38 < rfw> because of the lol fixtures
   2010-11-23 08:31:07 < Dark_Shikari> I feel sorry for people trying to game GCI
   2010-11-23 08:31:23 < Dark_Shikari> it's just so extraordinarily silly
   2010-11-23 08:33:51 < Dark_Shikari> Let's hope pengvado can read python to review your code =p
   2010-11-23 08:34:38 < rfw> is there no more ./configure?
   2010-11-23 08:35:12 < rfw> either that or something is very wrong
   2010-11-23 08:35:15 < Dark_Shikari> o.0
   2010-11-23 08:35:30 < rfw> where did it go
   2010-11-23 08:36:58 < rfw> oh
   2010-11-23 08:37:01 < rfw> there we go
   2010-11-23 08:37:52 < rfw> i had my revision list upside down
   2010-11-23 08:48:41 < Kovensky> 05:13.39 rfw: i can't even get group/owner information <-- broken ACLs?
   2010-11-23 08:48:55 < rfw> Kovensky: looks like it
   2010-11-23 08:48:59 < rfw> super-broken ACLs
   2010-11-23 08:49:10 < Kovensky> try chown yourusername:Administrator -R /path/to/folder && chmod 777 -R /path/to/folder
   2010-11-23 08:49:25 < Kovensky> if that doesn't work, you may need to chkdsk
   2010-11-23 08:49:31 < nattofriends> takeown
   2010-11-23 08:49:35 < Kovensky> Administrators*
   2010-11-23 08:49:36 < rfw> nattofriends: did that
   2010-11-23 08:49:44 < rfw> chown: cannot read directory `../x264': Permission denied
   2010-11-23 08:49:51 < rfw> ;_;
   2010-11-23 08:49:58 < nattofriends> can copy folder?
   2010-11-23 08:50:01 < rfw> nope
   2010-11-23 08:50:26 < nattofriends> drop to a bootcd with ntfs mounting, try copying it to FAT
   2010-11-23 08:50:34 < nattofriends> then reboot and copy elsewhere?
   2010-11-23 08:51:09 < Kovensky> the bootcd will just give more errors
   2010-11-23 08:51:20 < Kovensky> run a chkdsk on readonly mode, if it whines you found your culprit
   2010-11-23 08:51:29 < Dark_Shikari> Aren't there windows tools to override ACLs?
   2010-11-23 08:52:09 < Kovensky> Dark_Shikari: they're not working
   2010-11-23 08:52:21 < Kovensky> which is why I assume the ACLs are completely broken there
   2010-11-23 09:09:55 < rfw> well then, i think i've finished
   2010-11-23 09:10:02 < rfw> oh wait
   2010-11-23 09:10:09 < rfw> still haven't done that macroblock frame calculation thing
   2010-11-23 09:10:10 < rfw> hnngh
   2010-11-23 09:10:15 < Dark_Shikari> that's not too hard =p
   2010-11-23 09:10:17 < Dark_Shikari> that's like 3 lines of code
   2010-11-23 09:10:23 < Dark_Shikari> though you have to know the video width and height to do that.
   2010-11-23 09:10:31 < rfw> but i'm tired
   2010-11-23 09:10:31 < rfw> D:
   2010-11-23 09:10:46 < rfw> also do you mind if i commit my library to github
   2010-11-23 09:10:57 < rfw> since i'm paranoid
   2010-11-23 09:11:02 < rfw> about my computer exploding
   2010-11-23 09:11:04 < rfw> while i sleep
   2010-11-23 09:25:20 < J_Darnley> What a lot of discussion where was overnight.  It nearly ran off the top of my buffer
   2010-11-23 09:25:31 < tjoener> indeed J_Darnley
   2010-11-23 09:25:34 < tjoener> just read them too
   2010-11-23 09:26:22 < Kovensky> means your buffer is too small :>
   2010-11-23 09:27:28 < Dark_Shikari> pengvado: can you explain cbr_decay?
   2010-11-23 09:28:11 < Dark_Shikari> and specifically the formula used to calculate it
   2010-11-23 09:28:18 < Dark_Shikari> and what "1.0" vs "0.0" etc would mean
   2010-11-23 09:29:46 < Dark_Shikari> and why is printing of ratefactor disabled with high cbr decay?
   2010-11-23 09:29:59 < Dark_Shikari> high cbr decay can happen with e.g. --vbv-bufsize 30000 --vbv-maxrate 40000 --bitrate 4000
   2010-11-23 09:32:35 < Rodeo> and low cbr decay when vbv maxrate and/or bufsize are closer to the avg. bitrate
   2010-11-23 09:33:25 < Rodeo> I used these high values in my test, but I think I'd have gotten the same results with no vbv at all
   2010-11-23 09:37:31 < Dark_Shikari> Oh, I see
   2010-11-23 09:37:40 < Dark_Shikari> 1.0 --> no cbr decay
   2010-11-23 09:37:47 < Dark_Shikari> less than 1.0 --> lots of cbr decay
   2010-11-23 09:38:01 < Dark_Shikari> ratefactor is only printed if there's no cbr decay, or nearso
   2010-11-23 09:38:23 < Dark_Shikari> there's no cbr decay in my example (1.0) because vbv is much larger than bitrate.
   2010-11-23 09:44:31 < Rodeo> that was my guess
   2010-11-23 09:44:58 < Rodeo> doesn't explain what cbr decay actually is though
   2010-11-23 09:45:09 < Rodeo> though it probably makes more sense to you
   2010-11-23 09:45:15 < Dark_Shikari> rc->cplxr_sum *= rc->cbr_decay;
   2010-11-23 09:45:17 < Dark_Shikari> rc->wanted_bits_window *= rc->cbr_decay;
   2010-11-23 09:45:24 < Dark_Shikari> it's how fast the ABR state decays over time
   2010-11-23 09:45:26 < Dark_Shikari> 1.0 has no effect
   2010-11-23 09:45:30 < Dark_Shikari> 0.0 means it immediately decays
   2010-11-23 09:45:36 < Dark_Shikari> in CBR, you want it to decay fast
   2010-11-23 09:45:44 < Dark_Shikari> in ABR with no VBV, you don't want it to decay at all
   2010-11-23 09:45:52 < Dark_Shikari> so its a measure of a guess at the effect of CBR on the ABR algorithm
   2010-11-23 09:48:13 < Rodeo> so there's no issue then
   2010-11-23 09:48:35 < Dark_Shikari> well, it might be useful to have ratefactor if cbr_decay is < 1
   2010-11-23 09:48:39 < Dark_Shikari> I don't know if it'd be meaningful or not
   2010-11-23 11:47:46 < Alex_W> Dark_Shikari: I just saw your post on doom9 about using weightp with 1 ref for blu-ray compatibility, is it confirmed then that dupes are the problem on mediatek chipsets?
   2010-11-23 12:01:31 < j-b> Dark_Shikari: http://socghop.appspot.com/gci/task/show/google/gci2010/videolan/t129045717568
   2010-11-23 12:02:46 < kierank> j-b: that guy already failed ;)
   2010-11-23 12:06:13 < kierank> melange is awful
   2010-11-23 12:11:45 < Dark_Shikari> Alex_W: yes
   2010-11-23 12:11:56 < Dark_Shikari> j-b: what?
   2010-11-23 12:12:04 < Dark_Shikari> 4032 hours lol?
   2010-11-23 12:13:07 < Alex_W> ok, then would you accept a patch that disables dupes? maybe something like --weightp bluray?
   2010-11-23 12:13:37 < Dark_Shikari> I don't like the idea of actively supporting broken players
   2010-11-23 12:13:42 < Dark_Shikari> it creates more fragmentation
   2010-11-23 12:13:58 < JEEB> Alex_W, wipple wrote something similar IIRC
   2010-11-23 12:14:09 < JEEB> but yeah, gotta go by D_S's opinion here
   2010-11-23 12:14:15 < Dark_Shikari> I think we could have a patch, maybe
   2010-11-23 12:14:20 < Dark_Shikari> but committed?  probably not
   2010-11-23 12:15:12 < Alex_W> the problem is that replicators probably won't use weightp at all because of this, imo a slightly less useful weightp without dupes is better than no weightp at all...
   2010-11-23 12:15:47 < Alex_W> also we already have an --open-gop bluray, how is this any different?
   2010-11-23 12:16:25 < JEEB> because it's in the spec :|
   2010-11-23 12:16:56 < JEEB> normal weightp is completely within the spec and most players play it fine
   2010-11-23 12:17:09 < JEEB> (as it is in the spec AFAICS)
   2010-11-23 12:18:02 < wipple> i wrote this patch before ---> http://cccp.project357.com/p/f3b5731a7
   2010-11-23 12:18:14 < Dark_Shikari> Alex_W: also, at very low quants, weightp is less useful
   2010-11-23 12:18:17 < wipple> and rejected by Dark_Shikari
   2010-11-23 12:18:40 < Alex_W> the problem is that the spec probably doesn't really matter to replicators, the only thing that's going to matter to them is whether real world players will actually play the discs without any problems
   2010-11-23 12:18:55 < j-b> Dark_Shikari: I believe you should approve it
   2010-11-23 12:19:17 < Dark_Shikari> j-b: really, for someone who didn't follow instructions ands how up?
   2010-11-23 12:19:20 < Dark_Shikari> I guess I can hope they do after.
   2010-11-23 12:19:44 < j-b> Dark_Shikari: then reject it
   2010-11-23 12:19:53 < Dark_Shikari> well, they might be waiting for acceptance
   2010-11-23 12:19:55 < Dark_Shikari> and then show up
   2010-11-23 12:19:59 < Dark_Shikari> so whatever I'll accept can't hurt
   2010-11-23 12:20:06 < j-b> melange is awful
   2010-11-23 12:22:47 < Alex_W> Dark_Shikari: wipple's patch seems like it should be fine to me, it could be interesting to be able to disable dupes in ordinary encodes anyway
   2010-11-23 12:23:37 < Dark_Shikari> dunno
   2010-11-23 12:24:07 < Dark_Shikari> we could add a b_bluray mode to enable stupid blu-ray hacks
   2010-11-23 12:24:07 < JEEB> is it explicitly dupes that all of those players have/had problems with?
   2010-11-23 12:24:16 < Dark_Shikari> there's only one chipset with a bug
   2010-11-23 12:24:17 < Dark_Shikari> mediatek
   2010-11-23 12:24:20 < Dark_Shikari> and it's fixed in a firmware update
   2010-11-23 12:24:46 < Alex_W> b_bluray would be the same as --device bluray right?
   2010-11-23 12:25:41 < Dark_Shikari> no
   2010-11-23 12:25:55 < Dark_Shikari> it'd be for stupid shit like the max frame size limitation we stuck in
   2010-11-23 12:26:00 < Dark_Shikari> it's currently under if( hrd && level 4.1)
   2010-11-23 12:26:22 < Alex_W> what frame size limitation is that?
   2010-11-23 12:26:37 < Dark_Shikari> mincr
   2010-11-23 12:26:41 < Dark_Shikari>         /* Blu-ray requires this */
   2010-11-23 12:26:41 < Dark_Shikari>         if( l->level_idc == 41 && h->param.i_nal_hrd )
   2010-11-23 12:26:41 < Dark_Shikari>             mincr = 4;
   2010-11-23 12:26:58 < Kovensky> 09:13.37 Dark_Shikari: I don't like the idea of actively supporting broken players <-- shifting the blame? :)
   2010-11-23 12:27:14 < JEEB> So that problem was with dupes? I still don't get it, I get it's a single chipset but was the problem explicitly with dupes regarding weightp?
   2010-11-23 12:27:15 < Dark_Shikari> it's my fault that mediatek fucked up?
   2010-11-23 12:27:18 < Dark_Shikari> yes
   2010-11-23 12:27:21 < Dark_Shikari> it's a single chipset
   2010-11-23 12:27:22 < JEEB> ok
   2010-11-23 12:27:25 < Dark_Shikari> which has ALREADY BEEN FIXED
   2010-11-23 12:27:29 < JEEB> :)
   2010-11-23 12:27:29 < Dark_Shikari> and which people need to stop bitching about
   2010-11-23 12:27:34 < JEEB> Indeed
   2010-11-23 12:28:00 < Alex_W> it's only fixed if people actually bother to update their firmware though :/
   2010-11-23 12:28:10 < JEEB> I wish you could update the firmware through blu-ray discs
   2010-11-23 12:28:23 < JEEB> "To watch this movie you need to update your player bleh bleh bleh"
   2010-11-23 12:28:41 < Kovensky> "And if the power fail or otherwise stuff goes wrong you'll have yourself a heavy brick"
   2010-11-23 12:28:42 < kierank> JEEB: well that implies they have a decent internet connection at hand
   2010-11-23 12:28:43 < Dark_Shikari> Alex_W: discs already come with instructions on how to upgrade firmware
   2010-11-23 12:28:45 < Kovensky> +s
   2010-11-23 12:28:52 < Alex_W> ok, so apart from the mincr thing and dupes are there any other stupid hacks that blu-ray requires?
   2010-11-23 12:29:10 < Dark_Shikari> not that aren't encapsulated in other options
   2010-11-23 12:29:20 < JEEB> kierank, I mean having the updates for those crappy pieces of shit on the disc... :| But I guess that's impossible.
   2010-11-23 12:29:41 < Kovensky> Dark_Shikari: the opengop one? I mean, the bluray suboption is specifically a bluray hack, isn't it
   2010-11-23 12:29:46 < Dark_Shikari> oh, that's true.
   2010-11-23 12:29:59 < Alex_W> ok so that too then
   2010-11-23 12:30:14 < Dark_Shikari> ok, proposal
   2010-11-23 12:30:22 < Dark_Shikari> replace weightp 1 with weightp without dupes.
   2010-11-23 12:30:32 < Dark_Shikari> that is, 1 becomes SMART minus dupes
   2010-11-23 12:30:38 < Dark_Shikari> instead of SMART minus analysis
   2010-11-23 12:30:45 < JEEB> sounds good 'nuff
   2010-11-23 12:30:46 < Dark_Shikari> I will commit that patch
   2010-11-23 12:31:25 < Alex_W> ok that sounds reasonable
   2010-11-23 12:31:42 < Dark_Shikari> this is in part because analysis is really faster than we expected it to be
   2010-11-23 12:31:50 < Dark_Shikari> I'll have to retune the presets but that's not too hard
   2010-11-23 12:31:53 < Dark_Shikari> just give me a patch and I'll do the rest
   2010-11-23 12:32:18  * Alex_W goes to look at the code
   2010-11-23 12:32:38 < Dark_Shikari> NB: grep for all places where we check against WEIGHTP_SMART
   2010-11-23 12:32:43 < Dark_Shikari> most of those, we'll have to just check for weightp
   2010-11-23 12:32:49 < Dark_Shikari> also note WEIGHTP_FAKE as an internal value
   2010-11-23 12:32:53 < Dark_Shikari> (for psy + weightp = 0)
   2010-11-23 12:33:08 < Dark_Shikari> and we can replace BLIND with WEIGHTP_SIMPLE or something
   2010-11-23 12:37:49 < Alex_W> so WEIGHTP_SIMPLE would be weightp without dupes and WEIGHTP_SMART would be weightp + dupes?
   2010-11-23 12:38:13 < pengvado> Dark_Shikari: you got your explanation of cbr_decay?
   2010-11-23 12:38:14 < pengvado> we don't print rate_factor in cbr mode, because it would be the rate_factor of just the last few seconds of the movie
   2010-11-23 12:39:05 < Dark_Shikari> what about ABR with some VBV?
   2010-11-23 12:39:31 < Dark_Shikari> I guess given how cbr_decay works, it wouldn't work.
   2010-11-23 12:39:34 < Dark_Shikari> you'd have to somehow recalculate it.
   2010-11-23 12:39:39 < Dark_Shikari> sorta makes sense.
   2010-11-23 12:40:41 < pengvado> the soft threshold of "cbr mode is when vbv-maxrate < 1.5*bitrate" is not at all tested, but yes
   2010-11-23 12:46:48 < Alex_W> why does WEIGHTP_SMART add 2 dupes atm?
   2010-11-23 12:47:10 < Dark_Shikari> the normal blind dupe, plus the smart dupe
   2010-11-23 12:47:23 < Dark_Shikari> that is, there are three copies of a given frame:
   2010-11-23 12:47:28 < Dark_Shikari> OPTIMAL (optimal weight)
   2010-11-23 12:47:32 < Dark_Shikari> OPTIMAL-1 (blind dupe of optimal)
   2010-11-23 12:47:35 < Dark_Shikari> ORIGINAL (original frame)
   2010-11-23 12:47:43 < Dark_Shikari> if OPTIMAL and ORIGINAL are the same, ORIGINAL is omitted.
   2010-11-23 12:47:46 < Dark_Shikari> i.e. if there's no weight
   2010-11-23 12:47:58 < Dark_Shikari> having both optimal and original is very useful if part of the frame isn't fading in
   2010-11-23 12:48:04 < Dark_Shikari> or is otherwise useful unweighted
   2010-11-23 12:49:01 < Alex_W> well i'll have to change that so that optimal replaces original for the new weightp 1 right?
   2010-11-23 12:49:13 < Dark_Shikari> no, ORIGINAL is a dupe
   2010-11-23 12:49:16 < Dark_Shikari> optimal already does replace original
   2010-11-23 12:49:18 < Dark_Shikari> i.e. ref0 is optimal
   2010-11-23 12:49:23 < Dark_Shikari> all you have to do is _stop_ the creation of dupes
   2010-11-23 12:49:26 < Alex_W> ah
   2010-11-23 12:49:29 < Dark_Shikari> there's no new code to be added
   2010-11-23 12:51:28 < Alex_W> lines 242 and 243 in common/macroblock.c can be removed then right since WEIGHTP_SIMPLE won't add any dupes?
   2010-11-23 12:51:54 < Dark_Shikari> yes
   2010-11-23 12:52:00 < Alex_W> k
   2010-11-23 12:52:20 < Dark_Shikari> also we could just rename them
   2010-11-23 12:52:22 < Dark_Shikari> to 0, 1, 2, 3
   2010-11-23 12:52:24 < Dark_Shikari> 1 == fast
   2010-11-23 12:52:25 < Dark_Shikari> 2 == medium
   2010-11-23 12:52:28 < Dark_Shikari> 3 == slow (I'l do this)
   2010-11-23 12:52:35 < Dark_Shikari> anyways, for now, just do your part and I'll futz with the rest later
   2010-11-23 12:52:41 < Dark_Shikari> brb sleep
   2010-11-23 12:53:16 < Alex_W> what about > 8 bit, do we want dupes in WEIGHTP_SMART?
   2010-11-23 12:54:22 < Dark_Shikari> not the -1 dupe
   2010-11-23 12:54:25 < Dark_Shikari> yes the original vs optimal
   2010-11-23 12:54:45 < Alex_W> k
   2010-11-23 15:27:56  * koda|work pings Dark_Shikari
   2010-11-23 17:39:47 < reid_> Is this the channel for Google Code-In?
   2010-11-23 17:41:16 < kierank> yes
   2010-11-23 17:41:31 < kierank> reid_: yes
   2010-11-23 17:42:48 < reid_> I am looking at completing one of the 'C to assembly function' problems and it said to come here first
   2010-11-23 17:45:31 < kierank> reid_: how much assembly do you know?
   2010-11-23 17:48:58 < reid_> I know how the language works, but I would  have to look up most commands. I wanted to look at the code before making a decision to see If it was out of my skill level.
   2010-11-23 17:49:49 < reid_> Is there a link to the specific methods in question?
   2010-11-23 17:51:31 < kierank> reid_: Dark_Shikari will teach you when he wakes up
   2010-11-23 17:52:06 < callahan> reid_: Basically they are the 10 bit functions that are slow when you run the checkasm program.
   2010-11-23 17:52:22 < callahan> Although I couldn't tell you which ones other people are working on.
   2010-11-23 17:52:57 < callahan> Or that it matters.  Step 1 would be to get the code and compile it for 10 bit, then run checkasm.
   2010-11-23 17:53:08 < callahan> While you wait for D_S.
   2010-11-23 17:54:43 < reid_> where is the code? There is no reference to it on the task page.
   2010-11-23 17:55:17 < callahan> git clone git://git.videolan.org/x264.git
   2010-11-23 17:55:56 < callahan> Will check you out a copy, assuming that you have the git program installed.
   2010-11-23 17:56:10 < callahan> If not start by googling up and installing git.
   2010-11-23 17:56:27 < jarod> what is the main x264 google code in website?
   2010-11-23 17:57:07 < reid_> is it an x86 instruction set?
   2010-11-23 17:57:30 < callahan> git is a revision control system
   2010-11-23 17:57:37 < callahan> for managing code bases
   2010-11-23 17:59:04 < jarod> reid_ what link did you use to get here? :P
   2010-11-23 18:01:07 < reid_> From the GCI task list on google-melange.com, it said it is required to come here before claiming the task.
   2010-11-23 18:01:35 < kierank> reid_: what OS are you on?
   2010-11-23 18:01:41 < jarod> yes that good, i just couldn't mind it :)
   2010-11-23 18:03:30 < reid_> Right now i'm on an Ubuntu variant.
   2010-11-23 18:05:13 < kierank> reid_: then download the git package, open a terminal and run the command callahan posted
   2010-11-23 18:08:27 < reid_> Ok it completed.
   2010-11-23 18:09:56 < callahan> the source will be in the x264 directory
   2010-11-23 18:10:18 < holger_> and the asm will be in x264/common/x86
   2010-11-23 18:11:10 < callahan> I'm not sure what the configure command is to get checkasm and 10 bit going.  Anyone else?
   2010-11-23 18:12:14 < holger_> ./configure --bit-depth=10 ; make ; make checkasm
   2010-11-23 18:12:32 < callahan> Yeah that, except use && instead of ;
   2010-11-23 18:12:39 < callahan> in case one fails :)
   2010-11-23 18:12:46 < jarod> \doc
   2010-11-23 18:12:47 < jarod> regression_test.txt
   2010-11-23 18:12:52 < jarod> svn co svn://svn.videolan.org/x264/trunk x264
   2010-11-23 18:12:54 < jarod> =)
   2010-11-23 18:14:49 < callahan> reid_: anyway, do the holger_ commands to compile it.
   2010-11-23 18:14:53 < holger_> i'm currently wondering which of the .asm files would be the least scary for a noob to look at. can't decide. they all seem to have parts that are going to be way over the head for someone who's pretty new to asm.
   2010-11-23 18:15:36 < reid_> so what exactly am I doing with this code?
   2010-11-23 18:15:52 < callahan> Shikari has been recommending people try either one of two things.  Pick a missing 10 bit asm function and implement it, or make random changes to an existing function and see if it's faster.
   2010-11-23 18:16:10 < reid_> Am I just translating a few functions into c?
   2010-11-23 18:16:19 < callahan> reid_: You're making it faster, either by implementing a missing function or making one of the existing ones faster.
   2010-11-23 18:17:03 < holger_> erm. you're going to translate c into asm. or optimize existing asm.
   2010-11-23 18:17:34 < callahan> reid_: Best would be to get it to compile and poke around while you wait for Dark_Shikari to get back.
   2010-11-23 18:17:43 < irock> personally I though sad was easiest to understand and write; it was the first code I implemented for high depth
   2010-11-23 18:18:49 < callahan> get checkasm running first, that gives you a profile of the existing asm functions.
   2010-11-23 18:20:56 < holger_> configure for 10 bit, build, run ./checkasm --bench. configure for 8 bit, do the same. compare the output. the differences tell you what's missing.
   2010-11-23 18:22:22 < reid_> so checkasm will tell you how efficient your code is?
   2010-11-23 18:22:53 < callahan> A good estimate, yes
   2010-11-23 18:22:56 < holger_> it measures runtime. for the c reference and the asm routines (often there is more than one, for different instruction sets)
   2010-11-23 18:23:39 < holger_> so pick a routine that exists for 8 bit but not 10 bit, look it up in the source and see if you can understand how it works.
   2010-11-23 18:25:08 < reid_> where can I get checkasm. Do I need a specific repository?
   2010-11-23 18:25:23 < holger_> you already have it. it's in the tools directory. make checkasm builds it.
   2010-11-23 18:25:54 < callahan> It's an x264 specific regression test.
   2010-11-23 18:26:20 < reid_> Oh wow sorry, I thought it was a tool.
   2010-11-23 18:26:27 < holger_> yup that too. if you work on optimizing asm, it's good to have a way of telling if you broke it.
   2010-11-23 18:29:13 < reid_> Am I supposed to get tons of errors?
   2010-11-23 18:29:16 < callahan> no
   2010-11-23 18:29:17 < irock> no
   2010-11-23 18:29:21 < holger_> if you get stuck trying to understand the asm, dark_shikari is probably happy to give you his crash course to x264 asm.
   2010-11-23 18:29:55 < irock> reid_: make sure do a make clean before/after you reconfigure for another bit depth.
   2010-11-23 18:30:30 < reid_> I pointed my terminal over to /x264/tools and ran 'make checkasm'
   2010-11-23 18:30:30 < holger_> oh and you want to install yasm if you don't have it already
   2010-11-23 18:30:45 < irock> you should be standing in x264 root
   2010-11-23 18:30:45 < callahan> nah, make checkasm from the x264 directory
   2010-11-23 18:31:00 < callahan> also make sure you ran the configure command listed above first
   2010-11-23 18:31:17 < callahan> ./configure && make && make checkasm
   2010-11-23 18:31:21 < callahan> will get you the 8 bit code
   2010-11-23 18:37:28 < reid_> Ok I got it. did that just compile the whole project?
   2010-11-23 18:37:34 < irock> yep
   2010-11-23 18:38:10 < irock> now you have two binaries, x264 and checkasm
   2010-11-23 18:38:28 < reid_> This is true.
   2010-11-23 18:38:30 < irock> if you run ./checkasm --bench the aforementioned benchmark will be created
   2010-11-23 18:39:03 < irock> tip: pipe it to a file for review
   2010-11-23 18:42:55 < reid_> It gave me a big long list of what I assume to be the ASM method name followed by a number representing how long it took?
   2010-11-23 18:43:04 < irock> correct
   2010-11-23 18:43:30 < irock> the measured number of cycles it took to be exact iirc
   2010-11-23 18:44:01 < irock> as you can see, the mxx/sse2/ssse3/... are faster than their C equivalents
   2010-11-23 18:45:15 < irock> now, if you run `make clean && ./configure --bit-depth=10 && make && make checkasm` you end up with two new binaries
   2010-11-23 18:46:51 < reid_> Ok it's running.
   2010-11-23 18:47:17 < reid_> So what are you looking for to consider the task completed?
   2010-11-23 18:48:24 < irock> if you compare the output from 8-bit (first run) checkasm and the output of 10-bit (second run) checkasm you'll see that there are missing some functions in 10-bit mode
   2010-11-23 18:48:49 < irock> quite a lot of asm optimized functions actually
   2010-11-23 18:49:24 < irock> so what we're looking for is you creating one function that doesn't exist yet for 10-bit
   2010-11-23 18:50:00 < irock> OR rewrite an existing one for either 8-bit or 10-bit to make it faster
   2010-11-23 18:50:00 < reid_> A method that exists in c but not in asm, for 10 bet mode?
   2010-11-23 18:50:06 < irock> yes
   2010-11-23 18:51:30 < irock> but, rewriting a 8-bit asm function is probably very hard, 10-bit version maybe not so (I wrote that, and I started learning asm in july)
   2010-11-23 18:52:13 < reid_> So once I complete my method do I upload the source file containing the method I added/optimized and tell you which one it is?
   2010-11-23 18:52:56 < irock> well, I think we could help you get started if you choose one and let us know to begin with
   2010-11-23 18:54:12 < irock> however, I suggest that you wait an hour or two for Dark_Shikari to wake up. he'll teach you the basics of x264 asm
   2010-11-23 18:54:55 < reid_> Ok I'll monitor the channel.
   2010-11-23 18:56:04 < reid_> I just requested the task, thanks for all the help guys.
   2010-11-23 19:03:16 < lnandor> hello everyone!
   2010-11-23 19:45:44 < rfw> i think i'm done
   2010-11-23 19:45:47 < rfw> who do i give this to
   2010-11-23 19:49:00 < reid_> Is anyone from VideoLAN on here?
   2010-11-23 19:50:19 < BugMaster> reid_: try ping j-b
   2010-11-23 19:50:49 < dj_tjerk> pastebin for review?
   2010-11-23 19:50:58 < reid_> ping j-b
   2010-11-23 19:51:46 < reid_> Who is in charge of accepting a claim request?
   2010-11-23 19:52:06 < Jumpyshoes> Dark_Shikari as far as i'm aware
   2010-11-23 19:52:17 < reid_> Is he up yet?
   2010-11-23 19:54:22 < reid_> Jumpyshoes, are you part of the videoLAN team?
   2010-11-23 19:54:25 < nattofriends> does Dark_Shikari sleep?
   2010-11-23 19:54:35 < Jumpyshoes> reid_: no
   2010-11-23 19:55:00 < rfw> sure is GCI in here
   2010-11-23 19:55:30 < Jumpyshoes> i actually need to talk to Dark_Shikari myself
   2010-11-23 19:55:34 < reid_> I think it's pretty much only GCI in here.
   2010-11-23 19:55:34 < Jumpyshoes> since i'm failing at this asm thing
   2010-11-23 19:55:40 < rfw> <-- GCI
   2010-11-23 19:55:43 < rfw> so is Jumpyshoes
   2010-11-23 19:55:44 < rfw> lol
   2010-11-23 19:55:58 < reid_> jumpyshoes, yea me too.
   2010-11-23 19:56:09 < mferrell> are you guys doing the code-in thing?
   2010-11-23 19:56:13 < rfw> yeah
   2010-11-23 19:56:37 < reid_> Jumpyshoes, are you writing the 10 bit asm functions?
   2010-11-23 19:56:47 < Jumpyshoes> yes
   2010-11-23 19:56:49 < Jumpyshoes> i've gotten a few macros down
   2010-11-23 19:56:58 < rfw> this makes me glad i didn't choose to do the ASM thing
   2010-11-23 19:57:20 < Jumpyshoes> it's fucking with my mind
   2010-11-23 19:57:42 < reid_> I havent found any that are written only in c and not asm.
   2010-11-23 19:58:12 < irock> Jumpyshoes: what function are you working on?
   2010-11-23 19:58:31 < Jumpyshoes> add4x4_idct or w/e
   2010-11-23 19:58:41 < Jumpyshoes> add4x4_idct, yea
   2010-11-23 19:58:51 < Jumpyshoes> which comes along with 15 different macros
   2010-11-23 19:59:03 < reid_> where are you looking?
   2010-11-23 19:59:18 < Jumpyshoes> what do you mean by that?
   2010-11-23 19:59:43 < reid_> are you using checkasm?
   2010-11-23 20:00:00 < Jumpyshoes> yea
   2010-11-23 20:00:33 < irock> Jumpyshoes: do you have a paste of your current work?
   2010-11-23 20:00:49 < reid_> are you looking through the list it dumps out?
   2010-11-23 20:00:56 < Jumpyshoes> my current work spans across about 5 files, but i have the current ASM function i'm working on
   2010-11-23 20:01:07 < Jumpyshoes> i can also point out what the problem is (probably)
   2010-11-23 20:01:26 < irock> Jumpyshoes: or run git diff
   2010-11-23 20:01:43 < Jumpyshoes> currently, the code is a mess though, since i've been mucking around with it
   2010-11-23 20:01:54 < irock> ok, I remember that :) np
   2010-11-23 20:02:14 < Jumpyshoes> hrm?
   2010-11-23 20:02:54 < irock> I remember how it was when I wrote my first asm this summer
   2010-11-23 20:03:10 < Jumpyshoes> oh
   2010-11-23 20:03:14 < Jumpyshoes> it's terrible
   2010-11-23 20:03:32 < Jumpyshoes> i'm not actually sure what something in the original function is doing
   2010-11-23 20:03:39 < Jumpyshoes> so i was planning on asking someone about it
   2010-11-23 20:03:44 < irock> good idea
   2010-11-23 20:06:25 < irock> well, start asking is good to begin with
   2010-11-23 20:06:45 < Jumpyshoes> i was planning on waiting till D_S got back
   2010-11-23 20:07:21 < irock> alright
   2010-11-23 20:07:24 < Jumpyshoes> unless you feel like helping me
   2010-11-23 20:07:53 < rfw> Jumpyshoes: what's your task rated
   2010-11-23 20:08:06 < Jumpyshoes> not sure, whatever the code a function in assembly is
   2010-11-23 20:08:15 < irock> Jumpyshoes: I might be able to help, but I need a question first
   2010-11-23 20:08:21 < Jumpyshoes> google's awesome open source tool to list projects crashes my browser, so i can't tell
   2010-11-23 20:08:22 < rfw> i would check but the list tasks page takes fucking forever to load
   2010-11-23 20:08:27 < rfw> haha
   2010-11-23 20:08:30 < reid_> dificult
   2010-11-23 20:08:34 < rfw> ah
   2010-11-23 20:08:44 < kierank> yes melange is completely useless
   2010-11-23 20:08:50 < reid_> yes they list crashes all my browsers.
   2010-11-23 20:08:58 < irock> yep, the lists particularly
   2010-11-23 20:08:59 < Jumpyshoes> irock: http://pastebin.com/jyhm0z4w reid_
   2010-11-23 20:09:04 < Jumpyshoes> oops, fail tab completion
   2010-11-23 20:09:13 < rfw> i think i'm going to go for plone next
   2010-11-23 20:09:18 < Jumpyshoes> FDEC_STRIDE = 32
   2010-11-23 20:09:27 < Jumpyshoes> i don't understand what the STORE_DIFF  m0, m4, m7, [r0+0*FDEC_STRIDE] is doing
   2010-11-23 20:09:30 < Jumpyshoes> (etc.)
   2010-11-23 20:09:35 < Jumpyshoes> since it's moving up by 32 each time
   2010-11-23 20:09:54 < Jumpyshoes> and that's a lot of bytes
   2010-11-23 20:11:53 < irock> actually you need to double FDEC_STRIDE for high depth
   2010-11-23 20:12:18 < irock> check sub4x4_dct_mmx e.g
   2010-11-23 20:12:25 < Jumpyshoes> yea, but that's secondary
   2010-11-23 20:13:06 < reid_> Jumpyshoes: has you request been accepted yet?
   2010-11-23 20:13:07 < Jumpyshoes> doesn't that go beyond a 4x4 array of bytes
   2010-11-23 20:13:19 < Jumpyshoes> reid_: nope
   2010-11-23 20:13:42 < Jumpyshoes> i mean, i didn't file for one
   2010-11-23 20:13:44 < Jumpyshoes> but D_S knows
   2010-11-23 20:14:19 < irock> well, it's not a 4x4 array of bytes in high depth, it's an 4x4 array of uint16_t.
   2010-11-23 20:14:32 < Jumpyshoes> i mean, i'm just talking about 8 bit for now
   2010-11-23 20:14:46 < irock> ah, ok
   2010-11-23 20:15:02 < Jumpyshoes> doesn't 32 go over the 1x4 row?
   2010-11-23 20:15:36 < rfw> oh god
   2010-11-23 20:15:39 < rfw> melange is broken
   2010-11-23 20:15:43 < rfw> Time to complete:     6 mins
   2010-11-23 20:15:54 < rfw> I HAVE 6 MINUTES TO COMPLETE THIS 7 DAY TASK I STARTED YESTERDAY
   2010-11-23 20:15:59 < Jumpyshoes> LOL
   2010-11-23 20:16:12 < rfw> Time to complete:     59 mins
   2010-11-23 20:16:16 < rfw> slightly better!
   2010-11-23 20:16:20 < reid_> to be fair, melange never really worked to begin with.
   2010-11-23 20:16:28 < Jumpyshoes> interesting how they use crappy open source software to promote open source
   2010-11-23 20:17:32 < rfw> i think i should join #melange
   2010-11-23 20:17:37 < irock> Jumpyshoes: take a look at the C code
   2010-11-23 20:17:41 < rfw> and ask why the fuck i have 58 minutes left
   2010-11-23 20:17:50 < reid_> rf
   2010-11-23 20:18:00 < Jumpyshoes> yea, what about it?
   2010-11-23 20:18:04 < irock> we're writing 4 pixels first, then we add the stride, write 4 more pixels, and so on
   2010-11-23 20:18:33 < Jumpyshoes> OH MY GOD
   2010-11-23 20:18:37 < BugMaster> Dark_Shikari: http://privatepaste.com/8b80558011
   2010-11-23 20:18:37 < BugMaster> For information. It fix non critical difference between gcc 4.4.5 and gcc 4.5.2, which was due different processing of division by zero (early termination doesn't work in gcc 4.5.2 with division by zero).
   2010-11-23 20:18:37 < BugMaster> Removed one weight_cache which was really needed only due the absent of luma weights initialization (which can be set in lookahead)
   2010-11-23 20:18:40 < Jumpyshoes> i've had this file open for AGES
   2010-11-23 20:18:49 < Jumpyshoes> and i haven't noticed that
   2010-11-23 20:18:51 < Jumpyshoes> thank you irock
   2010-11-23 20:19:13 < irock> Jumpyshoes: just ask :)
   2010-11-23 20:19:15 < tjoener> Jumpyshoes: Microsoft used Windows to promote themselves
   2010-11-23 20:19:26 < tjoener> just use crappy software and youre rich :)
   2010-11-23 20:19:46 < Jumpyshoes> i'm on windows 7 and i like it
   2010-11-23 20:19:52 < Jumpyshoes> DON'T BE HATIN'
   2010-11-23 20:19:55  * JEEBsv high-fives BugMaster 
   2010-11-23 20:20:02 < tjoener> Ive got win7too
   2010-11-23 20:20:03 < rfw> Jumpyshoes: me too, but not the liking part
   2010-11-23 20:20:05 < JEEBsv> great, so I guess that problem is mostly behind us the?
   2010-11-23 20:20:06 < JEEBsv> *then
   2010-11-23 20:20:14 < tjoener> I meant in the old days
   2010-11-23 20:20:56 < reid_> can we port c methods from 8bit to 10 bit or do they have to be the asm ones?
   2010-11-23 20:21:08 < Jumpyshoes> ask Dark_Shikari
   2010-11-23 20:21:21 < irock> reid_: the C functions are already working for high depth (10-bit)
   2010-11-23 20:21:24 < reid_> where is he?
   2010-11-23 20:21:32 < reid_> is he still sleeping!
   2010-11-23 20:21:35 < Jumpyshoes> he's probably sleeping or something
   2010-11-23 20:21:42 < tjoener> sleeping?
   2010-11-23 20:21:49 < tjoener> DS does not need sleep!
   2010-11-23 20:21:53 < tjoener> He's undead
   2010-11-23 20:21:55 < Jumpyshoes> no clue, out with hot girls or something else
   2010-11-23 20:21:55 < tjoener> or immortal
   2010-11-23 20:21:57 < tjoener> or whatever
   2010-11-23 20:22:09 < tjoener> now THAT would be the only reason to get away :)
   2010-11-23 20:22:32 < irock> reid_: if you can't wait for a live tutorial, you can check the logs a few days back
   2010-11-23 20:22:48 < Jumpyshoes> oh yea, D_S gave me a crash course on asm
   2010-11-23 20:22:49 < irock> I think Jumpyshoes and someone more has done the tutorial quite recently
   2010-11-23 20:23:02 < irock> check topic for the logs
   2010-11-23 20:23:32 < reid_> irock: the c functions are not showing up on checkasm
   2010-11-23 20:23:46 < reid_> at least not all of them.
   2010-11-23 20:23:51 < irock> reid_: they are only showing up if there's an asm equivalent
   2010-11-23 20:23:55 < Jumpyshoes> yea
   2010-11-23 20:24:03 < reid_> oh
   2010-11-23 20:25:57 < reid_> is there an easy way to tell where the function are located?
   2010-11-23 20:26:21 < irock> ~all x86 asm functions are located in common/x86
   2010-11-23 20:26:58 < irock> sometimes it's quite easy to guess from the name, otherwise you could ask or grep
   2010-11-23 20:27:11 < reid_> I know, I was wondering if there was a way so i dont have to go hunting for them.
   2010-11-23 20:27:30 < reid_> I'm about to write a java app to do it for me.
   2010-11-23 20:28:05 < irock> that's overkill
   2010-11-23 20:28:37 < reid_> yea, bit it will take my mind off of asm.
   2010-11-23 20:29:50 < kierank> ctags?
   2010-11-23 20:30:36 < Gramner> >java
   2010-11-23 20:30:41 < Gramner> blasphemy
   2010-11-23 20:32:06 < Dark_Shikari> reid_: /me is now here
   2010-11-23 20:33:06 < Dark_Shikari> rfw: keep in mind that if melange sucks and randomly steals all your time, I'm happy to re-issue the tasks.
   2010-11-23 20:33:13 < rfw> :D
   2010-11-23 20:33:24 < rfw> apparently they know about it, though
   2010-11-23 20:33:44 < Dark_Shikari> BugMaster: applied
   2010-11-23 20:34:09 < rfw> Dark_Shikari: so do i have to wait for pengvado to look at my script?
   2010-11-23 20:34:19 < Dark_Shikari> When you think you're done, post a git format-patch.
   2010-11-23 20:34:32 < Dark_Shikari> And then the other devs here can try it out!
   2010-11-23 20:34:44 < rfw> put it in extra?
   2010-11-23 20:35:08 < Dark_Shikari> tools/
   2010-11-23 20:35:10 < Dark_Shikari> like checkasm
   2010-11-23 20:35:34 < reid_> are the 10 bit methods compiled when HIGH_BIT_DEPTH is defined and 8 bit methods compiled when it is not?
   2010-11-23 20:35:48 < Dark_Shikari> Yup
   2010-11-23 20:36:01 < Dark_Shikari> The primary difference between 8-bit and 10-bit, for the asm:
   2010-11-23 20:36:03 < Dark_Shikari> for 8-bit
   2010-11-23 20:36:13 < Dark_Shikari> pixels are uint8_t, and dct coeffs are int16_t
   2010-11-23 20:36:15 < Dark_Shikari> for 10-bit
   2010-11-23 20:36:21 < Dark_Shikari> pixels are uint16_t, and dct coeffs are int32_t
   2010-11-23 20:36:27 < Dark_Shikari> (of course, the pixels can't exceed 1023 in that case)
   2010-11-23 20:36:51 < Dark_Shikari> Some functions may need more internal precision than they did with 8-bit.
   2010-11-23 20:36:53 < Dark_Shikari> Others might not.
   2010-11-23 20:37:01 < JEEBsv> rfw: what kind of a script did you do?
   2010-11-23 20:37:18 < Dark_Shikari> regression tester
   2010-11-23 20:37:20 < Dark_Shikari> that does magic
   2010-11-23 20:37:25 < reid_> So All I have to do is change the data types and make sure nothing overflows and what not?
   2010-11-23 20:38:31 < Dark_Shikari> of course, this involves writing new asm
   2010-11-23 20:38:37 < rfw> JEEBsv: python
   2010-11-23 20:38:39 < Dark_Shikari> you can't just "
   2010-11-23 20:38:44 < Dark_Shikari> "change the data types" -- at least not usually
   2010-11-23 20:38:47 < Dark_Shikari> of course, sometimes you can
   2010-11-23 20:38:48 < rfw> JEEBsv: a whole pile of python... :V
   2010-11-23 20:39:01 < Dark_Shikari> for example, in Jumpyshoes' case, he found a function that could be converted from MMX 8-bit to SSE 10-bit with almost no changes
   2010-11-23 20:39:09 < Dark_Shikari> as in MMX 8-bit, it worked on 4x16-bit values
   2010-11-23 20:39:09 < JEEBsv> rfw: I'll be looking forward to it
   2010-11-23 20:39:15 < Dark_Shikari> and in SSE 10-bit, it'll work on 4x32-bit values
   2010-11-23 20:39:26 < rfw> JEEBsv: that sounds ominous
   2010-11-23 20:39:26 < Dark_Shikari> so the basic structure stayed identical
   2010-11-23 20:40:11 < Jumpyshoes> except i'm failing at life
   2010-11-23 20:40:35 < reid_> what are dct's?
   2010-11-23 20:40:37 < Dark_Shikari> s/failing at life/not asking questions and posting your code/
   2010-11-23 20:40:44 < Jumpyshoes> well
   2010-11-23 20:40:49 < Jumpyshoes> i need to go in 10 minutes
   2010-11-23 20:40:53 < Jumpyshoes> school being over and all
   2010-11-23 20:40:59 < Jumpyshoes> so i will be doing that when i get back home
   2010-11-23 20:41:02 < Dark_Shikari>  ok =p
   2010-11-23 20:41:13 < Dark_Shikari> reid_: a DCT is a discrete cosine transform.  You don't have to understand how/why it works, just that there's nice pretty C code for it in common/dct.c
   2010-11-23 20:41:53 < reid_> so all I have to worry about is pixel depth?
   2010-11-23 20:42:38 < Dark_Shikari> and all consequences thereof
   2010-11-23 20:42:45 < Dark_Shikari> and learning to write asm in x264
   2010-11-23 20:43:19 < reid_> what is x264? what architecture is that?
   2010-11-23 20:43:31 < Dark_Shikari> x264 is the program you're planning to work on
   2010-11-23 20:43:47 < Dark_Shikari> the architectures to pick from are x86 (MMX/SSE), PPC (Altivec), and ARM (NEON)
   2010-11-23 20:44:53 < rfw> fuck
   2010-11-23 20:44:54 < rfw> fuuuuuuuuck
   2010-11-23 20:45:02 < reid_> all I see is MMX/SSE
   2010-11-23 20:45:08 < Dark_Shikari> NEON would be in common/arm
   2010-11-23 20:45:10 < rfw> i just deleted
   2010-11-23 20:45:12 < rfw> fuuuuuuuuck
   2010-11-23 20:45:13 < Dark_Shikari> altivec would be in common/ppc
   2010-11-23 20:45:18 < Jumpyshoes> reid_: change directory!
   2010-11-23 20:45:22 < Dark_Shikari> rfw: stop.  stop right now.
   2010-11-23 20:45:25 < Dark_Shikari> don't do anything else
   2010-11-23 20:45:28 < rfw> too late
   2010-11-23 20:45:31 < Dark_Shikari> Go get a data recovery tool
   2010-11-23 20:45:34 < rfw> oh
   2010-11-23 20:45:55 < irock> rfw: what file system are you using?
   2010-11-23 20:45:57 < rfw> ntfs
   2010-11-23 20:46:00 < Dark_Shikari> By the way, this is why you POST YOUR SHIT
   2010-11-23 20:46:10 < irock> ah, then it's probably np
   2010-11-23 20:46:15 < rfw> okay, i have testdisk
   2010-11-23 20:46:17 < Dark_Shikari> Do not write to any other files
   2010-11-23 20:46:24 < reid_> i'm in the root.
   2010-11-23 20:46:35 < Jumpyshoes> okay going home
   2010-11-23 20:46:40 < Jumpyshoes> i shall bug you with questions later
   2010-11-23 20:46:54 < reid_> but it doesn't matter i'm only working on x86
   2010-11-23 20:47:02 < Dark_Shikari> rfw: http://www.officerecovery.com/index.htm#freeundelete
   2010-11-23 20:47:27 < Dark_Shikari> This fact also dictates the following procedure for using FreeUndelete:
   2010-11-23 20:47:27 < Dark_Shikari>    1. Stop any activity on the disk you are going to undelete files from! Remember that writing to that disk can damage the contents of the deleted files. Examples of disastrous activity include: copying files to the disk, installing programs there or running programs that use the disk as their swap media.
   2010-11-23 20:47:32 < Dark_Shikari>    2. Download and install FreeUndelete. Whenever possible, save the setup executable and install the program to a disk that does not hold files you need to undelete.
   2010-11-23 20:47:36 < Dark_Shikari>    3. Run and use FreeUndelete.
   2010-11-23 20:47:36 < Dark_Shikari> I've used it before.
   2010-11-23 20:47:47 < Dark_Shikari> Now go grab a flash drive, stick it in, install freeundelete on it, and get your files back
   2010-11-23 20:47:50 < Dark_Shikari> and next time, learn to post your shit.
   2010-11-23 20:47:53 < rfw> yeah
   2010-11-23 20:47:59 < Dark_Shikari> because stuff on the internet can't be deleted.
   2010-11-23 20:48:00 < rfw> i'm so silly
   2010-11-23 20:48:14 < irock> (or learn to do regular backups)
   2010-11-23 20:48:22 < JEEBsv> A true (9) you are, aren't you rfw :3
   2010-11-23 20:48:36 < rfw> 天才
   2010-11-23 20:48:45 < Dark_Shikari> Or just use a revision control system
   2010-11-23 20:48:46 < Dark_Shikari> like git
   2010-11-23 20:48:48 < Dark_Shikari> which saves your shit
   2010-11-23 20:48:50 < JEEBsv> yeah
   2010-11-23 20:48:52 < reid_> who backs up hourly?
   2010-11-23 20:48:57 < Dark_Shikari> Someone who uses git
   2010-11-23 20:48:58 < rfw> i did but
   2010-11-23 20:49:01 < irock> reid_: I do
   2010-11-23 20:49:06 < JEEBsv> you rm -rf'd the whole folder?
   2010-11-23 20:49:08 < rfw> yeah
   2010-11-23 20:49:09 < rfw> >_>
   2010-11-23 20:49:14 < rfw> need to learn to look
   2010-11-23 20:49:15 < rfw> when i type
   2010-11-23 20:51:54 < rfw> Dark_Shikari: not there D:
   2010-11-23 20:52:04 < rfw> it's not reading the Users folder
   2010-11-23 20:52:12 < Dark_Shikari> I highly doubt you've managed to run the entire program on your entire drive already.
   2010-11-23 20:52:18 < Dark_Shikari> It is much slower than that.
   2010-11-23 20:52:30 < rfw> i scanned C
   2010-11-23 20:52:34 < rfw> and it finished
   2010-11-23 20:52:45 < Dark_Shikari> Did you check stuff like the unnamed folders and files and such?
   2010-11-23 20:52:50 < Dark_Shikari> i.e. the stuff with no metadata?
   2010-11-23 20:52:58 < rfw> hm, where?
   2010-11-23 20:53:02 < rfw> it only shows 3 folders
   2010-11-23 20:53:08 < Dark_Shikari> Open them.
   2010-11-23 20:53:11 < rfw> programdat, program files and config.msi
   2010-11-23 20:53:40 < Dark_Shikari> Also, don't you still have your editor open?
   2010-11-23 20:53:49 < rfw> no
   2010-11-23 20:53:55 < rfw> well
   2010-11-23 20:53:59 < rfw> i only have test_x264.py open
   2010-11-23 20:54:26 < Dark_Shikari> well then you're good aren't you?
   2010-11-23 20:55:15 < rfw> no
   2010-11-23 20:55:25 < rfw> since all of digress is gone
   2010-11-23 20:55:49 < Dark_Shikari> er... you were making a library
   2010-11-23 20:55:51 < Dark_Shikari> and you never put it on github?
   2010-11-23 20:56:07 < Dark_Shikari> you never copied it into the x264 directory, instead you _moved_ it?
   2010-11-23 20:56:10 < Dark_Shikari> leaving no original?
   2010-11-23 20:56:24 < Dark_Shikari> what kind of crack are you on?
   2010-11-23 20:56:30 < rfw> i don't know
   2010-11-23 20:56:32 < rfw> it's 9a,
   2010-11-23 20:56:33 < rfw> 9am
   2010-11-23 20:56:36 < rfw> i don't think clearly
   2010-11-23 20:56:50 < Dark_Shikari> er... this means you've been actively stupid for the past couple months you've been working on this "digress" thing
   2010-11-23 20:56:59 < rfw> er no
   2010-11-23 20:57:03 < rfw> i just started yesterday
   2010-11-23 20:57:08 < rfw> i wrote a library first, then the tests
   2010-11-23 20:57:12 < rfw> as part of the whole thing
   2010-11-23 20:57:20 < rfw> i don't write a regression testing suite for no reason, you know
   2010-11-23 20:57:34 < Dark_Shikari> maybe you can regression-test your brain first?
   2010-11-23 20:57:48 < rfw> i probably need to D:
   2010-11-23 20:58:13 < Dark_Shikari> check your editor temp files or something
   2010-11-23 20:58:18 < rfw> oh
   2010-11-23 20:58:20 < rfw> recuva works
   2010-11-23 20:58:36 < JEEBsv> 'grats
   2010-11-23 20:58:38 < Dark_Shikari> Now, once you recover this
   2010-11-23 20:58:40 < Dark_Shikari> make a repository on github
   2010-11-23 20:58:43 < Dark_Shikari> and commit your shit.
   2010-11-23 20:58:52 < Dark_Shikari> and don't ever do that again.
   2010-11-23 20:59:08 < rfw> yes sir
   2010-11-23 20:59:13 < tjoener> yeah rfw recuva helped me out a tight spot a few times (read thesis)
   2010-11-23 20:59:20 < Dark_Shikari> lol
   2010-11-23 20:59:22 < JEEBsv> lol
   2010-11-23 20:59:24 < Dark_Shikari> >thesis oh god
   2010-11-23 20:59:30 < JEEBsv> it helped me get back some rare'ish files
   2010-11-23 20:59:40 < JEEBsv> although I think I wasn't using recuva then, but that other open source app
   2010-11-23 21:00:17 < holger_> as Dark_Shikari said: that was pretty lucky. at least you got your stuff back. also note we do not accept the "dog ate my homework" excuse, so you better recover your work from the dog erm disk ;) ;)
   2010-11-23 21:00:36 < Dark_Shikari> github ---> your closest friend
   2010-11-23 21:00:38 < Dark_Shikari> or gitosis or whatever
   2010-11-23 21:00:48 < rfw> >estimated time left 7 hours
   2010-11-23 21:01:01 < koda> umh would there be any hope of having this http://forum.doom9.org/showthread.php?t=154606 included in the stable branch?
   2010-11-23 21:01:06 < tjoener> Ive got a public git repo, if someone wants to post some code for backup I could probably arrange something easy
   2010-11-23 21:01:23 < tjoener> a few extra ssh keys or whatnot
   2010-11-23 21:01:34 < koda> this patch to be more precise http://pastebin.com/ErL2eAW8
   2010-11-23 21:01:56 < reid_> how do we submit our code?
   2010-11-23 21:02:08 < JEEBsv> git format-patch
   2010-11-23 21:02:12 < Dark_Shikari> you make a local commit
   2010-11-23 21:02:14 < Dark_Shikari> you use git format-patch
   2010-11-23 21:02:17 < Dark_Shikari> and then we review it!
   2010-11-23 21:02:20 < Dark_Shikari> You should do this obvious
   2010-11-23 21:02:21 < Dark_Shikari> er, often
   2010-11-23 21:02:26 < Dark_Shikari> preferably, before it's even working!
   2010-11-23 21:02:34 < Dark_Shikari> Because when things are broken, we may be able to help you figure out what's wrong
   2010-11-23 21:02:47 < Dark_Shikari> git format-patch -> pastebin
   2010-11-23 21:02:59 < Dark_Shikari> pastebin.com, pastebin.ca, etc
   2010-11-23 21:03:28 < reid_> im using gitg
   2010-11-23 21:04:25 < rfw> haha yes
   2010-11-23 21:04:28 < rfw> got them all back
   2010-11-23 21:04:29 < rfw> now
   2010-11-23 21:04:31 < rfw> time to not be stupid
   2010-11-23 21:04:43 < JEEBsv> time to add, commit and push to something non-local
   2010-11-23 21:04:51 < rfw> oh wait
   2010-11-23 21:04:55 < rfw> >.pyc
   2010-11-23 21:04:59 < rfw> >_>
   2010-11-23 21:05:00 < holger_> and it's always a good idea to sync your work directory to another machine, locally or even remote, if you have one. on linux you could set up a cron job running rsync for that
   2010-11-23 21:05:10 < rfw> well, that was half-helpful
   2010-11-23 21:07:20 < reid_> you want all the source?
   2010-11-23 21:07:44  * koda pings Dark_Shikari with http://pastebin.com/ErL2eAW8
   2010-11-23 21:08:19 < rfw> yeah
   2010-11-23 21:09:00 < kierank> koda: the plan is to get it into the main branch
   2010-11-23 21:09:02 < kierank> but it needs some work
   2010-11-23 21:09:19 < Dark_Shikari> koda: there's no way that will get into trunk in its current state
   2010-11-23 21:09:31 < Dark_Shikari> and really IMO speedcontrol should be outside libx264
   2010-11-23 21:09:42 < Dark_Shikari> the only justification for it being _in_ x264 is to stop people from having to implement it themselves
   2010-11-23 21:10:03 < koda> Dark_Shikari: it's just so convenient to have it all in one tool
   2010-11-23 21:10:05 < Dark_Shikari> rfw: you can decompile python
   2010-11-23 21:10:11 < koda> kierank: how can i help in the process?
   2010-11-23 21:10:17 < rfw> Dark_Shikari: not very well
   2010-11-23 21:10:26 < Dark_Shikari> at least it's not .pyo
   2010-11-23 21:10:44 < irock> .pyc even have comments, no?
   2010-11-23 21:19:26 < tjoener> I'm off
   2010-11-23 21:19:27 < tjoener> taa
   2010-11-23 21:21:41 < rfw> YES
   2010-11-23 21:21:44 < rfw> THANK YOU UNPYC
   2010-11-23 21:22:08 < reid_> what are you using python for?
   2010-11-23 21:22:17 < rfw> regression testing thing
   2010-11-23 21:23:39 < dj_tjerk> pastebin nao
   2010-11-23 21:24:19 < rfw> oh, it failed on my more complex files
   2010-11-23 21:24:46 < rfw> sigh
   2010-11-23 21:24:51 < rfw> at this rate i'm going to have to withdraw
   2010-11-23 21:25:35 < reid_> seriously melange
   2010-11-23 21:29:11 < checkers> the worst part about stupid backup stories is nobody learns from them except the protagonist
   2010-11-23 21:31:58 < dj_tjerk> rfw > writing python doesn't take that much time does it?
   2010-11-23 21:32:26 < checkers> 0/10
   2010-11-23 21:32:27 < rfw> i suppose not but
   2010-11-23 21:32:34 < rfw> :(
   2010-11-23 21:33:57 < checkers> ps use dropbox
   2010-11-23 21:34:47 < checkers> also it's probably worth trying another undelete tool
   2010-11-23 21:35:08 < checkers> http://ntfsundelete.com/ <-- I generally use this one
   2010-11-23 21:36:44 < rfw> everything just froze
   2010-11-23 21:36:47 < rfw> argh not having a good day
   2010-11-23 21:44:03 < callahan> Sounds like you're learning alot :)
   2010-11-23 22:00:25 < doron> Hi, I Registered your assembly task in the Google Code In competition. Can you please confirm me and explain to me what I need to do?
   2010-11-23 22:01:00 < JEEBsv> one thing: keep on the channel, devs will talk to you eventually
   2010-11-23 22:01:53 < doron> ah thank
   2010-11-23 22:02:04 < reid_> doron:  do you know assembly?
   2010-11-23 22:02:16 < rfw> i guess i'm going to have to go with plan B
   2010-11-23 22:02:22 < doron> yes
   2010-11-23 22:07:29 < Dark_Shikari> rfw: it took you a day
   2010-11-23 22:07:33 < Dark_Shikari> surely couldn't take that long to rewrite parts of it =p
   2010-11-23 22:07:42 < Dark_Shikari> doron: will get to you in a moment, busy in class atm
   2010-11-23 22:08:00 < Dark_Shikari> in the meantime you can check the log in the topic and see above where all previous students asked the same question ;)
   2010-11-23 22:15:22 < checkers> back at college?
   2010-11-23 22:15:31 < checkers> I thought you had a big break over christmas?
   2010-11-23 22:15:43 < Dark_Shikari> is it christmas yet?
   2010-11-23 22:15:45 < checkers> oh, you have that during your summer, dont you
   2010-11-23 22:15:57 < Dark_Shikari> no...
   2010-11-23 22:15:59 < astrange> it's not even thanksgiving break yet
   2010-11-23 22:16:09 < Dark_Shikari> the stores seem to think it's already christmas
   2010-11-23 22:16:11 < Dark_Shikari> but nobody else does
   2010-11-23 22:16:12 < checkers> uni people here got out a few weeks ago
   2010-11-23 22:16:12 < astrange> actually i think it is at every GA school except this one
   2010-11-23 22:16:20 < checkers> so they have a break from mid-november to march 1
   2010-11-23 22:16:50 < rfw> Dark_Shikari: i think i might withdraw from this
   2010-11-23 22:16:54 < rfw> i'm sorry :(
   2010-11-23 22:16:59 < Dark_Shikari> rfw: but you had such a cool script!
   2010-11-23 22:17:03 < rfw> i know!
   2010-11-23 22:17:08 < rfw> i can't believe how fucking stupid i am
   2010-11-23 22:17:10 < Dark_Shikari> get a better python decompiler
   2010-11-23 22:17:14 < rfw> i tried everything
   2010-11-23 22:17:26 < Dark_Shikari> go put in three hours and rewrite it, it's easier when you've done it before
   2010-11-23 22:18:03 < rfw> time to figure out all the classes i had
   2010-11-23 22:19:36 < rfw> or i could make it
   2010-11-23 22:19:37 < rfw> um
   2010-11-23 22:19:46 < rfw> better, stronger and faster
   2010-11-23 22:19:49 < Dark_Shikari> rewriting is great, it means you can fix all the stupid things you did the first time
   2010-11-23 22:19:52 < Dark_Shikari> lol
   2010-11-23 22:20:01 < rfw> yeah
   2010-11-23 22:20:06 < rfw> but that's one day wasyed
   2010-11-23 22:20:08 < rfw> wasted
   2010-11-23 22:20:13 < rfw> well
   2010-11-23 22:20:15 < checkers> I believe you mean harder, better, faster, stronger
   2010-11-23 22:20:16 < rfw> i guess i get the experience
   2010-11-23 22:20:20 < Dark_Shikari> no it isn't, because most of the day was spent figuring out how to do things
   2010-11-23 22:20:22 < Dark_Shikari> and what needed to be done
   2010-11-23 22:20:24 < rfw> yup
   2010-11-23 22:20:32 < Dark_Shikari> you're actually more than half done at this point.
   2010-11-23 22:20:41 < Dark_Shikari> This time around, do it with git, and make commits often
   2010-11-23 22:20:42 < rfw> checkers: are you going to throw a longer and thicker in there too
   2010-11-23 22:21:04 < Dark_Shikari> rfw: more than after hour never
   2010-11-23 22:21:09 < Dark_Shikari> our work is never over (oh wait)
   2010-11-23 22:53:17 < Jumpyshoes> Dark_Shikari: http://pastebin.com/hyNZL78m here's the code that wasn't working for me
   2010-11-23 22:54:29 < Jumpyshoes> i changed the mov to move double quadwords, transpose/idct to d, pw --> pd, and used the updated version of STORE_DIFF
   2010-11-23 22:54:33 < Jumpyshoes> isn't working though
   2010-11-23 22:55:08 < Dark_Shikari> 1) is pd_32 times 4 or times 2?
   2010-11-23 22:55:13 < Dark_Shikari> i.e. is it 4 values or 2?  check that, it should b4
   2010-11-23 22:55:37 < Jumpyshoes> let's see
   2010-11-23 22:55:38 < Jumpyshoes> const pw_32,       times 8 dw 32
   2010-11-23 22:55:41 < Jumpyshoes> const pd_32,       times 8 dd 32
   2010-11-23 22:55:46 < Dark_Shikari> it should be times 4 unless you didn't create it
   2010-11-23 22:55:54 < Jumpyshoes> oh
   2010-11-23 22:55:56 < Jumpyshoes> i created it
   2010-11-23 22:55:57 < Dark_Shikari> that won't affect it though
   2010-11-23 22:56:00 < Dark_Shikari> 8 is obviously enough
   2010-11-23 22:56:06 < Dark_Shikari> where's your updated store_diff, how about posting the whole patch?
   2010-11-23 22:56:14 < Dark_Shikari> you mean checkasm fails, right?
   2010-11-23 22:56:20 < Jumpyshoes> yea, checkasm fails
   2010-11-23 22:56:30 < Jumpyshoes> and store_diff was already written
   2010-11-23 22:56:39 < Jumpyshoes> how do i post a whole patch?
   2010-11-23 22:56:50 < Dark_Shikari> STORE_DIFF was written for high bit dept?h
   2010-11-23 22:56:52 < Dark_Shikari> git diff
   2010-11-23 22:56:56 < Jumpyshoes> yea, it was
   2010-11-23 22:57:27 < Jumpyshoes> git diff prints to the terminal, how do i get it to a file? pipe?
   2010-11-23 22:57:48 < dj_tjerk> > test.diff
   2010-11-23 22:58:25 < dj_tjerk> if you didn't tinker with color settings, it should be fine (i think you can set it to always output color, and not check if it's outputting to a file or stdout)
   2010-11-23 22:59:08 < Jumpyshoes> and i just pastebin it?
   2010-11-23 23:00:38 < Dark_Shikari> yes
   2010-11-23 23:00:50 < Dark_Shikari> also, you can add printfs to the checkasm unit test
   2010-11-23 23:00:54 < Dark_Shikari> to look at the output and try to see what might be wrong
   2010-11-23 23:01:03 < Jumpyshoes> how do i do that?
   2010-11-23 23:01:24 < Dark_Shikari> by editing checkasm.c
   2010-11-23 23:01:26 < Dark_Shikari> and adding printfs
   2010-11-23 23:01:28 < Jumpyshoes> http://pastebin.com/6r91qxH0 i did a bunch of mucking around
   2010-11-23 23:01:28 < Dark_Shikari> assuming you know basic C
   2010-11-23 23:01:41 < Jumpyshoes> why on earth would i try to learn asm before C ._.
   2010-11-23 23:01:44 < Dark_Shikari> you should use "diff" highlighting for your pastebinsd
   2010-11-23 23:01:55 < Jumpyshoes> oops, sorry
   2010-11-23 23:02:41 < Dark_Shikari> aha.
   2010-11-23 23:02:48 < Dark_Shikari> Your idct needs to clamp!
   2010-11-23 23:03:08 < Jumpyshoes> oh
   2010-11-23 23:03:15 < Jumpyshoes> lesse
   2010-11-23 23:03:20 < Jumpyshoes> does the clamp happen after the IDCT?
   2010-11-23 23:03:31 < Jumpyshoes> seems like it does
   2010-11-23 23:03:35 < Dark_Shikari> ok, so here's how it works
   2010-11-23 23:03:37 < Dark_Shikari> look at how STORE_DIFF works
   2010-11-23 23:03:59 < Dark_Shikari> actually.  wait a minute.  where is store_diff actually used?
   2010-11-23 23:04:12 < Jumpyshoes>     STORE_DIFF m0, m4, m5, [r0+0*FDEC_STRIDE], [r0+1*FDEC_STRIDE]
   2010-11-23 23:04:14 < Jumpyshoes> ...
   2010-11-23 23:04:16 < Jumpyshoes>     STORE_DIFF m3, m4, m5, [r0+6*FDEC_STRIDE], [r0+7*FDEC_STRIDE]
   2010-11-23 23:04:32 < Dark_Shikari> .... oh god
   2010-11-23 23:04:33 < Dark_Shikari> irock: !
   2010-11-23 23:04:35 < Dark_Shikari> come on
   2010-11-23 23:04:44 < Dark_Shikari> your STORE_DIFF doesn't do a STORE_DIFF, it's used for a completely unrelated purpose
   2010-11-23 23:04:47 < Dark_Shikari> lol
   2010-11-23 23:04:51 < Jumpyshoes> :(
   2010-11-23 23:04:59 < Jumpyshoes> why is it called the same thing
   2010-11-23 23:05:03 < Dark_Shikari> irock
   2010-11-23 23:05:04 < Dark_Shikari> blame him
   2010-11-23 23:05:09 < Dark_Shikari> anyways, for now, make your own macro that does it
   2010-11-23 23:05:13 < Dark_Shikari> first start by copying the low bit depth STORE_DIFF
   2010-11-23 23:05:21 < Dark_Shikari> second, you'll need to change it around a bit
   2010-11-23 23:05:26 < Jumpyshoes> well, i can't exactly delete his
   2010-11-23 23:05:26 < Dark_Shikari> punpcklbw will become punpcklwd
   2010-11-23 23:05:31 < Dark_Shikari> No, just call yours STORE_DIFF2
   2010-11-23 23:05:35 < Dark_Shikari> I'll fix it later.
   2010-11-23 23:05:41 < Jumpyshoes> oh, kk
   2010-11-23 23:05:42 < Dark_Shikari> so:
   2010-11-23 23:05:44 < Dark_Shikari>     movh       %2, %4
   2010-11-23 23:05:44 < Dark_Shikari>     punpcklbw  %2, %3
   2010-11-23 23:05:44 < Dark_Shikari>     psraw      %1, 6
   2010-11-23 23:05:44 < Dark_Shikari>     paddsw     %1, %2
   2010-11-23 23:05:47 < Dark_Shikari>     packuswb   %1, %1
   2010-11-23 23:05:49 < Dark_Shikari>     movh       %4, %1
   2010-11-23 23:05:54 < Dark_Shikari> we need to modify this for high bit depth and add clamping.
   2010-11-23 23:06:01 < Dark_Shikari> punpcklbw -> punpcklwd (since the data type is 16-bit)
   2010-11-23 23:06:15 < Dark_Shikari> psraw -> psrad
   2010-11-23 23:06:22 < pengvado> how about pack first, then add?
   2010-11-23 23:06:27 < Dark_Shikari> Oh, you could do that too
   2010-11-23 23:06:32 < Dark_Shikari> yeah, that'd better, you can pack before adding
   2010-11-23 23:06:41 < Jumpyshoes> what?
   2010-11-23 23:06:49 < Dark_Shikari> Jumpyshoes: remember, the formula is
   2010-11-23 23:07:02 < Dark_Shikari> pix + ((dctcoeff + 32) >> 6)
   2010-11-23 23:07:08 < Dark_Shikari> the above code does that
   2010-11-23 23:07:18 < Dark_Shikari> so we could do something like this:
   2010-11-23 23:07:33 < Dark_Shikari> oh, but remember the 32 is already handled inside the idct above, so you don't have to worry about that
   2010-11-23 23:07:37 < Dark_Shikari> so we're really doing
   2010-11-23 23:07:38 < Dark_Shikari> pix + (dctcoeff >> 6)
   2010-11-23 23:07:47 < Dark_Shikari> the pd_32 is the adding of the 32.
   2010-11-23 23:07:53 < Jumpyshoes> yea
   2010-11-23 23:07:53 < Dark_Shikari> so, here's what we do:
   2010-11-23 23:07:59 < Dark_Shikari> 1) dctcoeff >>= 6
   2010-11-23 23:08:03 < Dark_Shikari> 2) pack dctcoeff from 32-bit to 16-bit
   2010-11-23 23:08:07 < Dark_Shikari> 3) add dctcoeff to pix
   2010-11-23 23:08:24 < Dark_Shikari> 4) clamp pix to [0,(1<<BIT_DEPTH)-1]
   2010-11-23 23:08:28 < Dark_Shikari> 5) store
   2010-11-23 23:08:38 < Dark_Shikari> so, right here in chat, write out the instructions you'd use to do each step
   2010-11-23 23:08:47 < Jumpyshoes> in that order?
   2010-11-23 23:08:50 < Dark_Shikari> yes
   2010-11-23 23:09:11 < Jumpyshoes> i assume pack means (in C talk) to cast?
   2010-11-23 23:11:46 < Dark_Shikari> not quite, you're rearranging the data values
   2010-11-23 23:11:51 < Dark_Shikari> e.g. 4x32-bit -> 4x16-bit
   2010-11-23 23:11:58 < Dark_Shikari> this clearly involves modifying the data in the register
   2010-11-23 23:12:33 < Jumpyshoes> ah
   2010-11-23 23:13:18 < Jumpyshoes> 1) dctcoeff >>= 6: psrad      %1, 6
   2010-11-23 23:13:41 < Dark_Shikari> just use variables in your asm for now
   2010-11-23 23:13:45 < Dark_Shikari> e.g. psrad dctcoeff, 6
   2010-11-23 23:13:48 < Dark_Shikari> consider it pseudocode
   2010-11-23 23:13:50 < Jumpyshoes> ah okay
   2010-11-23 23:14:18 < Jumpyshoes> i have no idea how to pack data, unless you can do it by shifting like crazy
   2010-11-23 23:14:53 < Dark_Shikari> using the pack instruction
   2010-11-23 23:14:54 < Dark_Shikari> duh
   2010-11-23 23:15:10 < Dark_Shikari> use your manual
   2010-11-23 23:15:12 < Dark_Shikari> packssdw
   2010-11-23 23:15:34 < Jumpyshoes> oh
   2010-11-23 23:15:40 < Jumpyshoes> bleh, i need to get better at looking stuff up
   2010-11-23 23:16:44 < Jumpyshoes> 2) pack dctcoeff from 32-bit to 16-bit: packssdw tmp1, dctcoeff
   2010-11-23 23:16:55 < Dark_Shikari> no
   2010-11-23 23:17:01 < Dark_Shikari> go read what packssdw does
   2010-11-23 23:17:46 < Jumpyshoes> oh derp
   2010-11-23 23:17:49 < Dark_Shikari> and look at how it's used in the existing STORE_DIFF
   2010-11-23 23:18:06 < rfw> Dark_Shikari: it is better \o/
   2010-11-23 23:18:18 < rfw> though i still have to rewrite all that fucking bisection code
   2010-11-23 23:18:37 < Jumpyshoes> wait, how can you tell if an instruction can be used on the same register?
   2010-11-23 23:18:40 < Jumpyshoes> PACKSSDW xmm1,
   2010-11-23 23:18:41 < Jumpyshoes> xmm2/m128
   2010-11-23 23:18:57 < Dark_Shikari> Jumpyshoes: does it exist?  if so, it can be used on the same register
   2010-11-23 23:19:04 < Jumpyshoes> oh <_<
   2010-11-23 23:19:19 < Dark_Shikari> irock: I am copmletely lost with regadrs to the end of your dct mmx functions.  why do we need 32-bit dct coeff precision if your dct function can't even generate that?
   2010-11-23 23:19:31 < Jumpyshoes> then, 2) pack dctcoeff from 32-bit to 16-bit: packssdw dctcoeff, dctcoeff ?
   2010-11-23 23:19:58 < Dark_Shikari> yes
   2010-11-23 23:23:16 < pengvado> that works, but you probably want to pack 2 regs together. no sense in wasting half the throughput.
   2010-11-23 23:23:29 < Dark_Shikari> and what pengvado said
   2010-11-23 23:23:31 < Dark_Shikari> so you can do something like
   2010-11-23 23:23:39 < Dark_Shikari> psrad dctcoeffreg1, 6
   2010-11-23 23:23:41 < Dark_Shikari> psrad dctcoeffreg2, 6
   2010-11-23 23:23:50 < Dark_Shikari> packssdw dctcoeffreg1, dctcoeffreg2
   2010-11-23 23:25:14 < Jumpyshoes> wouldn't i need to modify the storediff? i thought only one set of dctcoeff were passed at a time
   2010-11-23 23:25:23 < Dark_Shikari> you're writing your own
   2010-11-23 23:25:29 < Dark_Shikari> if you want, start by not even making it a macro
   2010-11-23 23:25:31 < Dark_Shikari> you can macroize it later
   2010-11-23 23:25:34 < Dark_Shikari> just write out the instructions
   2010-11-23 23:25:42 < Jumpyshoes> right
   2010-11-23 23:27:40 < Dark_Shikari>  so do 1) and 2) for all your dct coeff registers
   2010-11-23 23:28:53 < Jumpyshoes> psrad dctcoeffreg1, 6
   2010-11-23 23:28:53 < Jumpyshoes> psrad dctcoeffreg2, 6
   2010-11-23 23:28:53 < Jumpyshoes> packssdw dctcoeffreg1, dctcoeffreg2
   2010-11-23 23:28:53 < Jumpyshoes> psrad dctcoeffreg3, 6
   2010-11-23 23:28:53 < Jumpyshoes> psrad dctcoeffreg4, 6
   2010-11-23 23:28:54 < Jumpyshoes> packssdw dctcoeffreg3, dctcoeffreg4
   2010-11-23 23:28:58 < Dark_Shikari> yes
   2010-11-23 23:29:13 < Jumpyshoes> oh, and now they're 16bit
   2010-11-23 23:29:19 < Dark_Shikari> now load up your pixels, which are also 16-bit, and add them
   2010-11-23 23:29:28 < Jumpyshoes> right
   2010-11-23 23:29:29 < Dark_Shikari> so e.g.
   2010-11-23 23:29:36 < Dark_Shikari> movq tmp1, [r0+0*FDEC_STRIDE]
   2010-11-23 23:29:41 < Dark_Shikari> movq tmp2, [r0+1*FDEC_STRIDE]
   2010-11-23 23:29:44 < Dark_Shikari> punpcklqdq tmp1, tmp2
   2010-11-23 23:29:50 < Dark_Shikari> which gives you two rows of pixels in "tmp1"
   2010-11-23 23:30:01 < Dark_Shikari> which is what you want, as you have two rows of dct coeffs in "dctcoeffreg1"
   2010-11-23 23:30:03 < rfw> To git@github.com:rofflwaffls/digress.git
   2010-11-23 23:30:03 < rfw>  * [new branch]      master -> master
   2010-11-23 23:30:09 < rfw> there
   2010-11-23 23:30:12 < Jumpyshoes> yea
   2010-11-23 23:30:37 < Dark_Shikari> actually, better yet
   2010-11-23 23:30:38 < Dark_Shikari> do
   2010-11-23 23:30:41 < Dark_Shikari> movq tmp1, [r0+0*FDEC_STRIDE]
   2010-11-23 23:30:46 < Dark_Shikari> movhps tmp1, [r0+1*FDEC_STRIDE]
   2010-11-23 23:30:51 < Dark_Shikari> same thing, two instructions instead of three.
   2010-11-23 23:30:57 < Dark_Shikari> movhps --> move to the high half
   2010-11-23 23:31:09 < Jumpyshoes> oh, isn't that for floating point though?
   2010-11-23 23:31:15 < Dark_Shikari> It's a move, do you think the cpu cares? =p
   2010-11-23 23:31:24 < Jumpyshoes> true
   2010-11-23 23:31:40 < Jumpyshoes> now i need to add these
   2010-11-23 23:33:23 < Jumpyshoes> paddsw dctcoeffreg1, tmp1
   2010-11-23 23:33:23 < Jumpyshoes> paddsw dctcoeffreg3, tmp2
   2010-11-23 23:33:23 < Jumpyshoes> ?
   2010-11-23 23:35:12 < Dark_Shikari> yes
   2010-11-23 23:36:32 < Jumpyshoes> can i use PACKSSDW or something similar to clamp? or will that not work
   2010-11-23 23:37:09 < Dark_Shikari> ah, now here comes in the problem
   2010-11-23 23:37:18 < Dark_Shikari> you're clamping to between, for example
   2010-11-23 23:37:19 < Dark_Shikari> 0 and 1023
   2010-11-23 23:37:22 < Dark_Shikari> there's no magic way to do that?
   2010-11-23 23:37:24 < Dark_Shikari> *that!
   2010-11-23 23:37:28 < Dark_Shikari> because they're not data type sizes
   2010-11-23 23:37:34 < Dark_Shikari> i.e. it's not 0 and 65535
   2010-11-23 23:37:35 < Dark_Shikari> or 0 and 255
   2010-11-23 23:37:50 < Dark_Shikari> so here's what you do
   2010-11-23 23:37:58 < Jumpyshoes> bleh, true
   2010-11-23 23:38:05 < Dark_Shikari> pmaxsw myval, {0}
   2010-11-23 23:38:13 < Dark_Shikari> pminsw myval, {MAX_PIXEL}
   2010-11-23 23:38:17 < Dark_Shikari> where {0} is pw_0
   2010-11-23 23:38:23 < Dark_Shikari> and max_pixel is pw_max
   2010-11-23 23:38:33 < Dark_Shikari> which is defined as times 8 ((BIT_DEPTH<<1)-1)
   2010-11-23 23:38:37 < Dark_Shikari> or pw_pixelmax
   2010-11-23 23:38:39 < Dark_Shikari> or something descriptive
   2010-11-23 23:39:00 < Dark_Shikari> also, pb_0 will (obviously) serve as a good pw_0/.
   2010-11-23 23:39:06 < Jumpyshoes> there's already a pw_pixel_max, but it's times 8
   2010-11-23 23:39:11 < Dark_Shikari> That's what you need
   2010-11-23 23:39:16 < Dark_Shikari> use it
   2010-11-23 23:39:17 < Jumpyshoes> oh right, i have 8 of them
   2010-11-23 23:39:31 < pengvado> there'as also a macro CLIPW
   2010-11-23 23:39:37 < Dark_Shikari> Oh, nice
   2010-11-23 23:39:38 < Jumpyshoes> o, can i use that?
   2010-11-23 23:39:57 < Dark_Shikari> pengvado: so, why do we need 32-bit dct coefficients for 10-bit?  I just did a dct between min pixel value and max pixel value, and checkasm still passed
   2010-11-23 23:40:03 < Dark_Shikari> Or is it because of idct scaling factors?
   2010-11-23 23:40:15 < Dark_Shikari> i.e. I assume I'm missing sometihng
   2010-11-23 23:40:16 < Dark_Shikari> Jumpyshoes: go check it out
   2010-11-23 23:40:23 < Dark_Shikari> it's probably already used for exactly this purpose!
   2010-11-23 23:40:53 < Jumpyshoes> yea
   2010-11-23 23:41:02 < Jumpyshoes> does exactly what you pasted
   2010-11-23 23:41:33 < Jumpyshoes> should i use pb_0 or can i just use 0?
   2010-11-23 23:41:57 < Jumpyshoes> or i guess i could define a pw_pixel_min
   2010-11-23 23:41:58 < Dark_Shikari> if you already have a zero register, use it
   2010-11-23 23:42:05 < Dark_Shikari> guess what, you do
   2010-11-23 23:42:18 < Dark_Shikari> m7
   2010-11-23 23:42:24 < Jumpyshoes> right, xor'd it up top
   2010-11-23 23:42:40 < Jumpyshoes> CLIPW dctcoeffreg1, m7, pw_pixel_max ;m7 = 0
   2010-11-23 23:42:40 < Jumpyshoes> CLIPW dctcoeffreg3, m7, pw_pixel_max
   2010-11-23 23:42:50 < Dark_Shikari> load pw_pixel_max into a register to avoid loading it twice
   2010-11-23 23:43:42 < Jumpyshoes> movq tmp1, pw_pixel_max
   2010-11-23 23:43:43 < Jumpyshoes> CLIPW dctcoeffreg1, m7, tmp1 ;m7 = 0
   2010-11-23 23:43:43 < Jumpyshoes> CLIPW dctcoeffreg3, m7, tmp1
   2010-11-23 23:44:00 < Dark_Shikari> yes
   2010-11-23 23:44:25 < Jumpyshoes> okay, now i need to store it
   2010-11-23 23:44:50 < Dark_Shikari> movq outputrow1, dctcoeffreg1
   2010-11-23 23:44:54 < Dark_Shikari> movhps outputrow1, dctcoeffreg1
   2010-11-23 23:44:56 < Dark_Shikari> etc
   2010-11-23 23:44:58 < Dark_Shikari> er
   2010-11-23 23:45:01 < Dark_Shikari> movhps outputrow2, dctcoeffreg1
   2010-11-23 23:45:06 < Dark_Shikari> where outputrow1 is a memory pointer, etc
   2010-11-23 23:45:45 < Jumpyshoes> oh, that is handy
   2010-11-23 23:45:53 < Dark_Shikari> movq and movhps work in both directions
   2010-11-23 23:45:54 < Dark_Shikari> loading and storing
   2010-11-23 23:46:01 < j-b> reid_: pong
   2010-11-23 23:46:50 < Jumpyshoes> movq [r0+0*FDEC_STRIDE], dctcoeffreg1
   2010-11-23 23:46:50 < Jumpyshoes> movhps [r0+4*FDEC_STRIDE], dctcoeffreg1
   2010-11-23 23:46:50 < Jumpyshoes> movq [r0+8*FDEC_STRIDE], dctcoeffreg3
   2010-11-23 23:46:50 < Jumpyshoes> movhps [r0+12*FDEC_STRIDE], dctcoeffreg3
   2010-11-23 23:46:59 < Dark_Shikari> think about where you're outputting
   2010-11-23 23:47:08 < Dark_Shikari> and look at the low bit depth version.
   2010-11-23 23:47:35 < Jumpyshoes> oh right, you're adding the FDEC_STRIDE
   2010-11-23 23:47:54 < Jumpyshoes> bleh, dinner, bbl
   2010-11-23 23:48:00 < Dark_Shikari> damn east coasters
   2010-11-23 23:48:12 < Jumpyshoes> but i just need to change it to 0,1,2,3?
   2010-11-23 23:53:06 < Dark_Shikari> yes
   --- Day changed Wed Nov 24 2010
   2010-11-24 00:02:55 < pengvado> Dark_Shikari: I don't know why your test passes.
   2010-11-24 00:03:42 < pengvado> fdct8's dc is the sum of 2^6 samples, each of which is an 11 bit different between two pixels. total: 17 bits.
   2010-11-24 00:04:00 < pengvado> and I think some of the ac coefs have another bit of expansion.
   2010-11-24 00:04:55 < pengvado> do we need to generate some maximal edge cases, like we do for hadamard?
   2010-11-24 00:05:03 < Dark_Shikari> I think that would be a good idea
   2010-11-24 00:06:51 < pengvado> btw, some of the butterfly passes could still be 16bit
   2010-11-24 00:07:36 < Dark_Shikari> yeah probably
   2010-11-24 00:17:24 < Dark_Shikari> (patches welcome)
   2010-11-24 00:22:08 < Dark_Shikari> Jumpyshoes: does it pass checkasm yet? =p
   2010-11-24 00:22:44 < rfw> Dark_Shikari: i'm sorta not regretting deleting everything now
   2010-11-24 00:22:49 < Dark_Shikari> lol
   2010-11-24 00:22:59 < rfw> fixed all the weird ass conventions i had before
   2010-11-24 00:23:07 < Dark_Shikari> "I told you so"
   2010-11-24 00:23:10 < rfw> lol
   2010-11-24 00:23:16 < rfw> should i delete it again when i finish this :D
   2010-11-24 00:23:18 < Dark_Shikari> Now commit early and often!
   2010-11-24 00:23:20 < Dark_Shikari> and push too
   2010-11-24 00:23:25 < rfw> Total 14 (delta 6), reused 0 (delta 0)
   2010-11-24 00:23:26 < rfw> To git@github.com:rofflwaffls/digress.git
   2010-11-24 00:23:26 < rfw>    2ee921b..12af40a  master -> master
   2010-11-24 00:23:28 < rfw> :D
   2010-11-24 00:23:56 < Dark_Shikari> I have saved another poor soul from data loss despair with github!
   2010-11-24 00:24:11 < rfw> i usually do commit everything to github
   2010-11-24 00:24:14 < rfw> not sure why i didn't with this
   2010-11-24 00:26:39 < espes> Dark_Shikari: So like, I requested that GCI task.
   2010-11-24 00:26:46 < Dark_Shikari> which one?
   2010-11-24 00:26:51 < espes> Dark_Shikari: filter.
   2010-11-24 00:26:57 < Dark_Shikari> That task is repeatable
   2010-11-24 00:27:08 < Dark_Shikari> i.e. if you say you want to do it, you can go do it, no problem
   2010-11-24 00:27:22 < Dark_Shikari> I'll go accept you, which filter do you want to do?
   2010-11-24 00:27:48 < Dark_Shikari> j-b: please approve my added duplicates of the filter task
   2010-11-24 00:28:00 < espes> Dark_Shikari: I was thinking something basic. 2xsai maybe.
   2010-11-24 00:28:31 < Dark_Shikari> we already have a resizer, though "interesting" resizing algorithms might be, well, interesting
   2010-11-24 00:28:53 < espes> Dark_Shikari: The justification is that you do have tasvideos linked from your homepage :P
   2010-11-24 00:28:53 < Dark_Shikari> hq2x/3x/4x might be interesting, though if I recall correctly those are written in pure asm and thus extremely scary
   2010-11-24 00:28:58 < Dark_Shikari> tasvideos?
   2010-11-24 00:29:13 < Dark_Shikari> Oh, wow, that list hasn't been updated in a mlilion years
   2010-11-24 00:29:14 < espes> Dark_Shikari: Video game speed runs.
   2010-11-24 00:29:15 < Dark_Shikari> I guess they are listed
   2010-11-24 00:29:40 < Dark_Shikari> well, it is fitting, considering that my x264 demos page consists almost entirely of video game clips
   2010-11-24 00:29:43 < Dark_Shikari> e.g. http://x264.nl/developers/Dark_Shikari/Flash/extra.html
   2010-11-24 00:30:52 < espes> Dark_Shikari: besides, it's easy enough to rip 2xsai out of mplayer.
   2010-11-24 00:31:16 < Dark_Shikari> didn't even know mplayer did
   2010-11-24 00:31:37 < Dark_Shikari> sounds cool enough, I'll go for that
   2010-11-24 00:31:45 < espes> Dark_Shikari: sweet.
   2010-11-24 00:31:48 < Dark_Shikari> just keep in mind...
   2010-11-24 00:31:55 < Dark_Shikari> all x264 tasks must go through pengvado
   2010-11-24 00:31:59 < Dark_Shikari> that is, he must approve your code
   2010-11-24 00:32:10 < Dark_Shikari> which means you must pass the code review =p
   2010-11-24 00:32:37 < pengvado> and pengvado generally disapproves of forking libavfilter
   2010-11-24 00:33:18 < Dark_Shikari> good point.
   2010-11-24 00:33:35 < kemuri-_9> hmm someone's doing a filter?
   2010-11-24 00:33:36 < Dark_Shikari> actually, pengvado, why didn't you say that earlier? =p
   2010-11-24 00:33:56 < pengvado> didn't I say it enough times, whenever anyone has proposed to add any filter to x264?
   2010-11-24 00:34:06 < Dark_Shikari> You never reviewed any filters.
   2010-11-24 00:34:14 < Dark_Shikari> pad, hqdn3d, etc are sitting around unreviewed
   2010-11-24 00:34:36 < Dark_Shikari> I'd be fine with 2xsai being ported to libavfilter though!
   2010-11-24 00:34:48 < Dark_Shikari> as long as someone writes an interface to transparently access libavfilter filters in x264
   2010-11-24 00:34:52 < Dark_Shikari> but someone can do that later
   2010-11-24 00:35:27 < Dark_Shikari> pengvado: I'd really like you to say something certain here on this topic
   2010-11-24 00:35:33 < pengvado> ok, so I only complained about yadif and h1dn3d
   2010-11-24 00:35:44 < Dark_Shikari> like "I don't want any more filters in x264"
   2010-11-24 00:35:50 < Dark_Shikari> or "I won't review any more filters in x264, but you can commit them"
   2010-11-24 00:35:59 < Dark_Shikari> or "let's just stuff everything in libavfilter and dump the ones in x264"
   2010-11-24 00:36:13 < pengvado> let's just stuff everything in libavfilter
   2010-11-24 00:36:16 < Dark_Shikari> for espes, it doesn't really matter -- x264 or libavfilter are both easy enough
   2010-11-24 00:36:40 < kemuri-_9> <_<
   2010-11-24 00:36:41 < Dark_Shikari> ok, good, we'll swap the tasks over to libavfilter then
   2010-11-24 00:36:48 < Dark_Shikari> Should have said this 6 months ago, slowpoke.
   2010-11-24 00:37:32 < Dark_Shikari> now, pengvado, are you going to volunteer to do that?
   2010-11-24 00:37:36 < Dark_Shikari> because nobody else wants to.
   2010-11-24 00:37:49 < Dark_Shikari> that is, we have one primary problem: there is no depth filter in libavfilter
   2010-11-24 00:37:51 < Dark_Shikari> and will probably never be
   2010-11-24 00:37:56 < Dark_Shikari> and we need that filter no matter what
   2010-11-24 00:38:25 < Dark_Shikari> so we need at least some of the x264 filter chain at some point.
   2010-11-24 00:38:44 < pengvado> never will be because libav* doesn't support anything other than 8 and 16bit?
   2010-11-24 00:38:51 < Dark_Shikari> yes
   2010-11-24 00:39:06 < Dark_Shikari> and there are 100 bikesheds between here and that being reality
   2010-11-24 00:39:11  * checkers waits for "I wrote a patch for that in 2006"
   2010-11-24 00:39:38 < kierank> ffmpeg - "there's a patch for that"
   2010-11-24 00:40:07 < rfw> http://code.google.com/p/soc/source/detail?r=57762a491b i don't think i trust google any more
   2010-11-24 00:40:08 < Dark_Shikari> so I'd like a straightforward statement of what you want us to do, and what part you'll take in it
   2010-11-24 00:40:14 < kemuri-_9> so what all filters are there for libavfilter atm?
   2010-11-24 00:40:19 < Dark_Shikari> kemuri-_9: a lot
   2010-11-24 00:40:28 < Dark_Shikari> rfw: OH GOD
   2010-11-24 00:40:32 < Dark_Shikari> homebrew time/date code
   2010-11-24 00:40:33 < Dark_Shikari> AGHAGHAHSDLFKJASDLFKJ
   2010-11-24 00:40:46 < kierank> and they say google is nih?
   2010-11-24 00:41:03 < rfw> lolol
   2010-11-24 00:41:32 < rfw> god i think i should go out for a walk
   2010-11-24 00:41:35 < kierank> there was something from google where they accidently used memset instead of memcpy
   2010-11-24 00:41:41 < Dark_Shikari> lol what
   2010-11-24 00:41:52 < pengvado> bleh, so keep the depth filter, and anything else that can't be merged into libavfilter short of really forking it.
   2010-11-24 00:42:19 < Jumpyshoes> bleh, still doesn't pass checkasm
   2010-11-24 00:42:19 < pengvado> any filter that *is* already in libavfilter, or could be developed there instead of here, gets a wrapper instead of a paste
   2010-11-24 00:42:27 < Dark_Shikari> pengvado: wait wait
   2010-11-24 00:42:30 < Dark_Shikari> should we wrap INDIVIDUAL filters
   2010-11-24 00:42:31 < Dark_Shikari> or LIBAVFILTER?
   2010-11-24 00:42:49 < Dark_Shikari> Jumpyshoes: pastebin the code
   2010-11-24 00:43:47 < Jumpyshoes> >We are currently upgrading our software, we will return in a few minutes.
   2010-11-24 00:43:49 < Jumpyshoes> hohohoho
   2010-11-24 00:43:57 < Dark_Shikari> use a different pastebin
   2010-11-24 00:44:14 < pengvado> you mean because if we use libavfilter's filterchain generation code, then it would support only libavfilter?
   2010-11-24 00:44:30 < Dark_Shikari> no I'm just asking whether or not we should keep our filterchain code.
   2010-11-24 00:44:36 < espes> Jumpyshoes: codepad
   2010-11-24 00:44:37 < Dark_Shikari> or whether we should wrap each filter separately
   2010-11-24 00:44:57 < pengvado> does ours do anything that libavfilter doesn't and won't?
   2010-11-24 00:45:03 < Dark_Shikari> I don't know.
   2010-11-24 00:45:06 < Dark_Shikari> Ask kemuri-_9
   2010-11-24 00:45:25 < kemuri-_9> i don't know enough about libavfilter to say anything on that
   2010-11-24 00:46:01 < Kovensky> though when the filtering system thing was started libavfilter was still vaporware
   2010-11-24 00:46:07 < Kovensky> isn't it still vaporware, or is it getting somewhere now?
   2010-11-24 00:46:13 < Dark_Shikari> no, it works
   2010-11-24 00:46:19 < Jumpyshoes> http://privatepaste.com/2ebbfd4a33
   2010-11-24 00:46:46 < Dark_Shikari> Jumpyshoes: 1) replace m7 with m6
   2010-11-24 00:46:49 < Dark_Shikari> 2) replace 2,2 with 2,2,7
   2010-11-24 00:47:18 < Jumpyshoes> should i xor out m6 too then?
   2010-11-24 00:47:24 < Dark_Shikari> yes, I mean replace all instances
   2010-11-24 00:47:29 < Dark_Shikari> this won't affect correctness
   2010-11-24 00:47:30 < Jumpyshoes> kk
   2010-11-24 00:48:09 < bcoudurier> hi guys
   2010-11-24 00:48:10 < pengvado> verdict: getting rid of duplicate code is good, but O(1) code for filterchain generation is less important than all of the individual filters
   2010-11-24 00:48:11  * Dark_Shikari summons bcoudurier 
   2010-11-24 00:48:41 < Dark_Shikari> Jumpyshoes: looks largely right.  this means it's debugging time ;)
   2010-11-24 00:48:58 < Jumpyshoes> sigh
   2010-11-24 00:49:09 < Dark_Shikari> see TEST_IDCT in checkasm.c
   2010-11-24 00:49:16 < Dark_Shikari>         if( memcmp( pbuf3, pbuf4, 32*32 * sizeof(pixel) ) ) \
   2010-11-24 00:49:22 < Dark_Shikari> before that line, print out the contents of pbuf3 and pbuf4, and compare
   2010-11-24 00:49:42 < Dark_Shikari> this will help you find your ug
   2010-11-24 00:49:45 < Dark_Shikari> *bug
   2010-11-24 00:49:46 < Jumpyshoes> what are pbuf3 and pbuf4?
   2010-11-24 00:49:56 < Jumpyshoes> strings?
   2010-11-24 00:50:02 < Dark_Shikari> pixel buffers
   2010-11-24 00:50:04 < Dark_Shikari> just memory.
   2010-11-24 00:50:07 < Jumpyshoes> ah
   2010-11-24 00:50:28 < Jumpyshoes> how do i print just a block of memory?
   2010-11-24 00:50:35 < Dark_Shikari> pengvado: so this means....
   2010-11-24 00:50:37 < Dark_Shikari> Jumpyshoes:
   2010-11-24 00:50:49 < Dark_Shikari> oh yeah, and you should print this inside the if where it fails
   2010-11-24 00:50:52 < Dark_Shikari> so it only prints for the broken one
   2010-11-24 00:50:55 < Dark_Shikari> for( int y = 0; y < 4; y++ )
   2010-11-24 00:51:01 < Dark_Shikari> for( int x = 0; x < 4; x++ )
   2010-11-24 00:51:08  * kemuri-_9 sees a vf_scale and looks
   2010-11-24 00:51:23 < Dark_Shikari> printf("%d ",pbuf3[x+y*FEC_STRIDE])
   2010-11-24 00:51:25 < Dark_Shikari> *FDEC_STRIDE
   2010-11-24 00:51:28 < Dark_Shikari> plus whatever line breaks you need
   2010-11-24 00:53:37 < pengvado> if there is something that libavfilter's framework doesn't support, and bikeshedding prevents patching libavfilter, and I can't just commit it to libavfilter anyway, then I'll tolerate a duplicate filterchain generator
   2010-11-24 00:54:20 < Dark_Shikari> wrappers allows us to make the syntax less retarded while avoiding duplicating internal code
   2010-11-24 00:54:29 < Dark_Shikari> now, the real problem here is just one of getting people to implement things
   2010-11-24 00:54:36 < Dark_Shikari> without someone willing to do it, it won't happen
   2010-11-24 00:54:46 < Dark_Shikari> and I don't want to sit around for 1 year with a half-completed filter system
   2010-11-24 00:54:50 < Dark_Shikari> that half-duplicates half-code
   2010-11-24 00:54:52 < Dark_Shikari> in a half-assed manner
   2010-11-24 00:55:05 < Jumpyshoes> hrm, so the first row is right, everything from there dies
   2010-11-24 00:55:32 < Dark_Shikari> the exact way in which it's wrong is often useful.
   2010-11-24 00:55:46 < Dark_Shikari> *useful to know
   2010-11-24 00:56:05 < bcoudurier> pengvado, I'll personally fight against any bikeshedding
   2010-11-24 00:56:29 < Dark_Shikari> kemuri-_9 / J_Darnley since you're the people actually writing this stuff, I'd like to know your thoughts
   2010-11-24 00:56:39 < Dark_Shikari> you can get the 16-bit hqdn3d committed to libavfilter
   2010-11-24 00:56:51 < Jumpyshoes> http://privatepaste.com/b452d32e20 first row seems right, everything else seems to be random
   2010-11-24 00:57:08 < Dark_Shikari> Jumpyshoes: oh duh
   2010-11-24 00:57:11 < Dark_Shikari> 0*FDEC_STRIDE
   2010-11-24 00:57:13 < Dark_Shikari> 2*FDEC_STRIDE
   2010-11-24 00:57:14 < Dark_Shikari> 4*FDEC_STRIDE
   2010-11-24 00:57:16 < Dark_Shikari> not 0/1/2/3
   2010-11-24 00:57:20 < Dark_Shikari> because the pixels are 2 bytes each
   2010-11-24 00:57:24 < Jumpyshoes> derp
   2010-11-24 00:57:30 < Dark_Shikari> I should have caught that dmanit.
   2010-11-24 00:57:39 < Jumpyshoes> i shoulda too
   2010-11-24 00:57:45 < Jumpyshoes> i considered that for a very long time
   2010-11-24 00:57:51 < Jumpyshoes> when i was using the wrong STORE_DIFF
   2010-11-24 00:58:12 < Jumpyshoes> x264: All tests passed Yeah :)
   2010-11-24 00:58:19 < kemuri-_9> "AVFilterPad type. Only video supported now, hopefully someone will add audio in the future." <--- lol, this concept looks familiar
   2010-11-24 00:58:38 < pengvado> I didn't comment on it because I thought Dark_Shikari noticed the error and was socratically questioning Jumpyshoes
   2010-11-24 00:58:56 < Jumpyshoes> ;-;
   2010-11-24 00:59:13 < Dark_Shikari> LOL
   2010-11-24 00:59:16 < Kovensky> lol
   2010-11-24 00:59:34 < Kovensky> Dark_Shikari: loren.html?
   2010-11-24 00:59:42 < Dark_Shikari> ohdear.jpg
   2010-11-24 00:59:46 < Jumpyshoes> okay, should i macro-ize this, or leave it as is?
   2010-11-24 00:59:59 < Jumpyshoes> i feel like if i mess with it, it'll blow up beyond all repair and i will be sad
   2010-11-24 01:00:30 < Dark_Shikari> make a macro right above your function
   2010-11-24 01:00:32 < Dark_Shikari> called STORE_DIFFx2
   2010-11-24 01:00:45 < Dark_Shikari> it should do two rows worth
   2010-11-24 01:00:50 < Dark_Shikari> so then call it twice.
   2010-11-24 01:01:05 < Jumpyshoes> sigh, very well
   2010-11-24 01:01:13 < Dark_Shikari> You'll be writing your first macro!
   2010-11-24 01:01:36 < Jumpyshoes> i will!
   2010-11-24 01:02:48 < bcoudurier> kemuri-_9 audio is added right now
   2010-11-24 01:04:10 < kemuri-_9> I have no current problems with focusing filtering into libavfilter, it's just more difficult for me as i wrote the current filtering system for x264cli and now i have to learn a completely different one.
   2010-11-24 01:05:21 < Dark_Shikari> kemuri-_9: if you want we can keep the x264 filter chain and just outsource individual filters
   2010-11-24 01:05:25 < Dark_Shikari> the main issue is:
   2010-11-24 01:05:29 < Dark_Shikari> a) libavfilter is getting lots of free development with cool filters
   2010-11-24 01:05:41 < Dark_Shikari> b) bcoudurier has been yelling at me like a chicken with its head cut off
   2010-11-24 01:05:44 < Dark_Shikari> c) pengvado has spoken
   2010-11-24 01:06:12 < kierank> the downside is all the bikeshedding
   2010-11-24 01:06:43 < bcoudurier> I hear you
   2010-11-24 01:07:09 < bcoudurier> bikeshedding is terrible, I'll do something about it
   2010-11-24 01:07:20 < kemuri-_9> at the bare minimum i agree with using what's available in libavfilter in some form or fashion (whether we ditch the current system or wrap it), we'll have to discuss putting new filters into libavfilter as they come along and see if libavfilter will accept them or say 'gtfo'
   2010-11-24 01:07:49 < Dark_Shikari> so, bcoudurier, you can get people to help mentor for libavfilter?
   2010-11-24 01:07:54 < Dark_Shikari> if so, we'll also need them to mentor kemuri-_9 =p
   2010-11-24 01:08:01 < kemuri-_9> :<
   2010-11-24 01:08:05 < kemuri-_9> sadly
   2010-11-24 01:08:08 < kierank> and can the bitdepth problem be sorted out ;)
   2010-11-24 01:08:35 < Dark_Shikari> we're keeping the depth filter for now
   2010-11-24 01:08:40 < kierank> the advantage to the x264 filter system was it didn't try to be a jack of all trades
   2010-11-24 01:08:43 < Dark_Shikari> i.e. libavfilter will still do 8-bit and 16-bit
   2010-11-24 01:08:46 < Dark_Shikari> and not 10-bit
   2010-11-24 01:08:51 < Dark_Shikari> and the depth filter will convert for us
   2010-11-24 01:08:59 < Dark_Shikari> kierank: we can keep doing that, actually
   2010-11-24 01:09:02 < Dark_Shikari> if we just wrap filters
   2010-11-24 01:09:07 < Dark_Shikari> then the filters will only do what we let them do
   2010-11-24 01:09:50 < bcoudurier> yes, I can mentor as well, and we'll be glad to do so
   2010-11-24 01:09:59 < bcoudurier> kemuri, ask me any question
   2010-11-24 01:11:07 < kemuri-_9> the only current problem i see immediately is the csp difference between libavfilter and the x264cli filter system, e.g. x264cli recognizes some csps that libavfilter does not (and technically vice versa)
   2010-11-24 01:12:23 < kemuri-_9> bcoudurier: thanks i'll ask when the time comes, which is not largely now, i have other things i want to get done for x264 before really messing with libavfilter
   2010-11-24 01:12:41 < Dark_Shikari> bcoudurier: we do want to smuggle students into ffmpeg for GCI though
   2010-11-24 01:12:43 < Dark_Shikari> and that's really near term
   2010-11-24 01:12:48 < Dark_Shikari> GCI literally just started and I got fucking flooded today
   2010-11-24 01:13:37 < kemuri-_9> how's that going to work, ffmpeg didn't get accepted by GCI right?
   2010-11-24 01:13:52 < Dark_Shikari> exactly
   2010-11-24 01:13:56 < Dark_Shikari> and we want video filters in x264
   2010-11-24 01:13:56 < rfw> i assume it's something like "hay kid wanna work in ffmpeg"
   2010-11-24 01:14:06 < Dark_Shikari> so everyone who "does a filter" for x264
   2010-11-24 01:14:09 < Dark_Shikari> will instead port to libavfilter!
   2010-11-24 01:14:11 < Dark_Shikari> problem solved.
   2010-11-24 01:14:19 < Dark_Shikari> trivial.
   2010-11-24 01:14:34 < Dark_Shikari> We intended to do this from the start -- the instant ffmpeg wasn't accepted, we were going to add Videolan/x264 tasks that were just to work on ffmpeg.
   2010-11-24 01:14:37 < Dark_Shikari> It's perfectly legit =p
   2010-11-24 01:14:49 < rfw> apart from the fact it's not videolan? :D
   2010-11-24 01:14:51 < kemuri-_9> seems like cheating the system but not like i a real voice in the issue
   2010-11-24 01:14:58 < kemuri-_9> i have a*
   2010-11-24 01:15:00 < kierank> boo hoo
   2010-11-24 01:15:02 < kierank> google is so sad
   2010-11-24 01:15:04 < Dark_Shikari> videolan uses ffmpeg
   2010-11-24 01:15:04 < kierank> ;)
   2010-11-24 01:15:06 < Dark_Shikari> x264 uses ffmpeg
   2010-11-24 01:15:08 < Dark_Shikari> I think it's legit
   2010-11-24 01:15:09 < Dark_Shikari> =p
   2010-11-24 01:15:14 < rfw> yes but ffmpeg isn't part of videolan :3
   2010-11-24 01:15:28 < Dark_Shikari> It might as well be, videolan is going to host ffmpeg's source now
   2010-11-24 01:15:29 < kierank> Dark_Shikari: I think it's legit
   2010-11-24 01:15:34 < kierank> x264 needs filters
   2010-11-24 01:15:35 < Dark_Shikari> they're moving to git, and videolan will host it
   2010-11-24 01:15:41 < rfw> ah
   2010-11-24 01:15:49 < kierank> we decide that we're going to use libavfilter because of duplicated work
   2010-11-24 01:15:50 < rfw> all hail git \o/
   2010-11-24 01:15:52 < kierank> that's it
   2010-11-24 01:15:53 < Dark_Shikari> kierank: yup
   2010-11-24 01:16:03 < Dark_Shikari> seems fine to me.
   2010-11-24 01:17:36 < rfw> after writing so many finally clauses i think i see why people use finally
   2010-11-24 01:17:51 < Dark_Shikari> you should have started that sentence with "finally"
   2010-11-24 01:18:04 < rfw> s/after/finally after/
   2010-11-24 01:18:09 < rfw> problem solved
   2010-11-24 01:18:50 < rfw> now how did i do my bisection again
   2010-11-24 01:18:55 < Dark_Shikari> magic
   2010-11-24 01:19:09 < rfw> i hate magic :(
   2010-11-24 01:20:16 < Jumpyshoes> Dark_Shikari, I AM DONE
   2010-11-24 01:20:30 < Dark_Shikari> woohoooo
   2010-11-24 01:20:35 < Dark_Shikari> now I just have to harass irock to fix his shit
   2010-11-24 01:20:40 < JEEBsv> lol
   2010-11-24 01:20:43 < Jumpyshoes> now what do i do
   2010-11-24 01:20:46 < Dark_Shikari> and harass pengvado to make a checkasm test that demosntrates that irock's shit is broken
   2010-11-24 01:20:50 < Dark_Shikari> Jumpyshoes: post your patch!
   2010-11-24 01:21:00 < Jumpyshoes> do a diff?
   2010-11-24 01:21:07 < Dark_Shikari> yes
   2010-11-24 01:21:17 < Dark_Shikari> then I will need from you three things!
   2010-11-24 01:21:49 < Jumpyshoes> ?
   2010-11-24 01:21:50 < Dark_Shikari> Your name, your email, and a response to the thing I send you via email!
   2010-11-24 01:22:18 < kemuri-_9> CLA powar
   2010-11-24 01:22:24 < Jumpyshoes> i should probably test the 8-bit
   2010-11-24 01:22:31 < Jumpyshoes> to make sure i didn't massively f something else up
   2010-11-24 01:22:49 < Dark_Shikari> Yup, of course
   2010-11-24 01:22:52 < Dark_Shikari> and post the patch so I can review it!
   2010-11-24 01:22:57 < Dark_Shikari> I will nitpick it in minor ways!
   2010-11-24 01:23:01 < Dark_Shikari> lol
   2010-11-24 01:24:07 < Jumpyshoes> after i test 8-bit i'll post
   2010-11-24 01:25:15 < Jumpyshoes> great
   2010-11-24 01:25:27 < Jumpyshoes> http://pastebin.com/nzybLAmG inb4 i get my ass handed to me
   2010-11-24 01:26:11 < Dark_Shikari> email sent
   2010-11-24 01:26:17 < Dark_Shikari> now for review!
   2010-11-24 01:26:51 < Dark_Shikari> 266/269/271: drop the extra spaces
   2010-11-24 01:27:03 < Dark_Shikari> in that whole macro, align everything so that the commas are aligned
   2010-11-24 01:27:08 < Dark_Shikari> 272: extra spaces, etc
   2010-11-24 01:27:14 < Dark_Shikari> 293 has extra spaces too
   2010-11-24 01:27:23 < Dark_Shikari> does your editor have weird tabbing or something?
   2010-11-24 01:27:27 < Dark_Shikari> fyi we use 4-space tabs
   2010-11-24 01:27:30 < Jumpyshoes> oh, yea
   2010-11-24 01:27:31 < Dark_Shikari> 306-307: pointless change
   2010-11-24 01:27:33 < Jumpyshoes> notepad++ defaults to single tab
   2010-11-24 01:27:47 < Dark_Shikari> fix that, and find all your tabs and fix them
   2010-11-24 01:27:51 < Dark_Shikari> 595: pointless change
   2010-11-24 01:27:55 < Dark_Shikari> ok, first pass done.
   2010-11-24 01:27:57 < Dark_Shikari> fix those and post it again
   2010-11-24 01:28:00 < Jumpyshoes> kk
   2010-11-24 01:28:50 < Jumpyshoes> oh btw
   2010-11-24 01:28:52 < Dark_Shikari> ?
   2010-11-24 01:28:54 < Jumpyshoes> i don't think this is an updated verion of x264
   2010-11-24 01:29:00 < Dark_Shikari> what do you mean
   2010-11-24 01:29:00 < espes> Dark_Shikari: so, what, am I still writing an x264 filter?
   2010-11-24 01:29:05 < Jumpyshoes> since i pulled 17xx and didn't bother to pull again
   2010-11-24 01:29:10 < Dark_Shikari> espes: you'll be writing a libavfilter filter -- much the same thing
   2010-11-24 01:29:14 < Dark_Shikari> Jumpyshoes: ok, here's how you do this
   2010-11-24 01:29:16 < espes> Dark_Shikari: right.
   2010-11-24 01:29:17 < Dark_Shikari> git commit -a
   2010-11-24 01:29:21 < Dark_Shikari> <type in your commit message, etc, etc>
   2010-11-24 01:29:24 < Dark_Shikari> git pull --rebase
   2010-11-24 01:29:26 < Dark_Shikari> now you have the latest version
   2010-11-24 01:29:33 < Dark_Shikari> then, to modify your commit, git commit -a --amend
   2010-11-24 01:29:37 < Dark_Shikari> to make a diff
   2010-11-24 01:29:41 < Dark_Shikari> git format-patch HEAD~1 --stdout > file.
   2010-11-24 01:29:48 < Dark_Shikari> you can also add your authorship to the patch
   2010-11-24 01:30:05 < Dark_Shikari> by adding --author="My Name <myemail@email.com>" to git commit
   2010-11-24 01:30:10 < Dark_Shikari> which will list your name on it
   2010-11-24 01:30:41 < Dark_Shikari> espes: bcoudurier here is responsible for getting someone to help you with this.  he's a cool french dude.
   2010-11-24 01:31:03 < espes> Dark_Shikari: ehh, I think libavfilter already supports loading libmpcodec filters, so it'll already be available. :\
   2010-11-24 01:31:24 < astrange> it doesn't
   2010-11-24 01:31:39 < Jumpyshoes> out of curiosity, why is ftp://ftp.videolan.org/pub/videolan/x264/snapshots/ dead?
   2010-11-24 01:32:15 < Dark_Shikari> Jumpyshoes: blame j-b
   2010-11-24 01:32:16 < Dark_Shikari> it's all j-b's fault
   2010-11-24 01:32:22 < astrange> a lot of libmpcodec filters are a mess anyway (timestamps are broken, only x86 is supported properly, no code reviews since forever)
   2010-11-24 01:32:32 < Dark_Shikari> Yeah, we want to move libmpcodecs into libavfilter anyways
   2010-11-24 01:32:38 < Dark_Shikari> libmpcodecs is part of mplayer and therefore rather dead
   2010-11-24 01:32:46 < Jumpyshoes> i don't actually know what i did in the useless changes
   2010-11-24 01:32:56 < Dark_Shikari> Jumpyshoes: shit happens, we do it too
   2010-11-24 01:33:09 < espes> Ok, so I move the filter from libmpcodec to libavfilter and make the code not suck.
   2010-11-24 01:33:14 < Dark_Shikari> Basically that's it.
   2010-11-24 01:33:20 < Dark_Shikari> And 4 points per filter.
   2010-11-24 01:33:40 < Dark_Shikari> Pick your favorites.
   2010-11-24 01:40:07 < Jumpyshoes> oh damn, my diff doesn't show anything anymor
   2010-11-24 01:40:07 < Jumpyshoes> e
   2010-11-24 01:40:51 < JEEBsv> you committed it?
   2010-11-24 01:41:05 < JEEBsv> then git format-patch HEAD~1 if it's just one commit
   2010-11-24 01:41:57 < Dark_Shikari> brb, I'm going to grab dinner
   2010-11-24 01:42:00 < Jumpyshoes> i mean, all my changes are committed already, so diff isn't finding anything <_<
   2010-11-24 01:42:06 < Jumpyshoes> or something
   2010-11-24 01:42:10 < astrange> http://pastebin.com/EdLuGCN7 those are the useful filters, i think
   2010-11-24 01:42:12 < Dark_Shikari> use format-patch
   2010-11-24 01:42:15 < Dark_Shikari> espes: ^
   2010-11-24 01:42:27 < astrange> actually ass is the most useful filter. but i don't think you could do that one
   2010-11-24 01:42:31 < Dark_Shikari> lol
   2010-11-24 01:42:31 < JEEBsv> Jumpyshoes: point on HEAD~1 (or other number depending on how many commits)
   2010-11-24 01:43:01 < JEEBsv> thus, git format-patch HEAD~1 will produce you one patch :3 (or the stdout way)
   2010-11-24 01:43:13 < JEEBsv> if you have more commits, f.ex. three -- HEAD~3
   2010-11-24 01:43:33 < espes> astrange: I'm told gradfun doesn't really work as a preprocessing filter...
   2010-11-24 01:43:44 < espes> (At least that's the note in the mplayer's implementation)
   2010-11-24 01:43:47 < Jumpyshoes> oh, so i actually have two commits
   2010-11-24 01:44:00 < Jumpyshoes> how do i compare my current with two commits ago?
   2010-11-24 01:44:19 < astrange> it sometimes works on bad inputs that spp/pp leave blocks on, but yes
   2010-11-24 01:44:22 < JEEBsv> git diff HEAD~2 ?
   2010-11-24 01:44:31 < Jumpyshoes> that gives 2 patches
   2010-11-24 01:44:38 < Jumpyshoes> so D_S can't see my changes
   2010-11-24 01:44:53 < JEEBsv> use the stdout way of format-patch
   2010-11-24 01:45:02 < JEEBsv> and thus concat it into one
   2010-11-24 01:45:10 < Jumpyshoes> ah
   2010-11-24 01:45:15 < Jumpyshoes> thanks
   2010-11-24 01:46:27 < espes> astrange: isn't colorspace conversion already done by the scale filter?
   2010-11-24 01:47:12 < Jumpyshoes> Dark_Shikari: http://pastebin.com/YASKQLHV
   2010-11-24 01:47:32 < espes> But if you think shelling out to swscale isn't really optimal :\
   2010-11-24 01:48:10 < astrange> nope, the issue is ignored. but that wouldn't be a bad idea
   2010-11-24 01:51:22 < JEEBsv> espes: gradfun has its uses even before encoding :) Just that it indeed needs more bits. Thus if the player can fix the banding, it's better of course.
   2010-11-24 01:53:39 < Jumpyshoes> speaking of filters
   2010-11-24 01:53:49 < Jumpyshoes> whatever happened to halomaker3000deluxe
   2010-11-24 01:54:14 < JEEBsv> lol
   2010-11-24 01:54:42 < rfw> python's documentation is quite questionable in places
   2010-11-24 01:54:47 < rfw> parser.add_option("-q", "--quiet",
   2010-11-24 01:54:47 < rfw>                   action="store_false", dest="verbose",
   2010-11-24 01:54:47 < rfw>                   help="be vewwy quiet (I'm hunting wabbits)")
   2010-11-24 01:54:52 < rfw> i mean, what.
   2010-11-24 01:55:23 < Jumpyshoes> i eat rabbits
   2010-11-24 01:55:58 < rfw> lol
   2010-11-24 01:56:07 < Jumpyshoes> i have actually eaten a rabbit before
   2010-11-24 01:56:19 < rfw> same
   2010-11-24 01:56:48 < rfw> Dark_Shikari: i think i'm finished (lolagain)
   2010-11-24 01:56:55 < rfw> do i have to implement linear revisions again
   2010-11-24 01:57:45 < JEEBsv> Jumpyshoes: I think they made a new filter adding pretty fabulous rainbows on #darkhold IIRC
   2010-11-24 01:58:06 < Jumpyshoes> what
   2010-11-24 01:58:14 < Jumpyshoes> HM3KD WITH RAINBOWS?
   2010-11-24 01:58:18 < Jumpyshoes> WHERE THE FUCK CAN I FIND THIS?
   2010-11-24 01:58:32 < rfw> i wrote an hlsl shader that rainbowed everything
   2010-11-24 01:58:41 < JEEBsv> You'll have to ask on #darkhold , I don't remember who wrote it atm
   2010-11-24 01:58:59 < Jumpyshoes> darn
   2010-11-24 01:59:00 < Jumpyshoes> this rizon?
   2010-11-24 01:59:07 < JEEBsv> yah, rizon
   2010-11-24 01:59:08 < rfw> why are we all on rizon
   2010-11-24 01:59:25 < rfw> half of this channel is on rizon
   2010-11-24 01:59:27 < rfw> :(
   2010-11-24 02:05:21 < Dark_Shikari> espes: gradfun2db WOULD be useful as a preprocessing filter with x264's 10-bit
   2010-11-24 02:05:36 < Dark_Shikari> testing has shown this
   2010-11-24 02:05:54 < Dark_Shikari> Jumpyshoes: you need to merge your patches
   2010-11-24 02:05:59 < Dark_Shikari> you inadvertantly made two local commits instead of one
   2010-11-24 02:06:01 < Jumpyshoes> how do i do that?
   2010-11-24 02:06:04 < Dark_Shikari> if you do git rebase -i HEAD~2
   2010-11-24 02:06:06 < Jumpyshoes> oh
   2010-11-24 02:06:10 < Dark_Shikari> you can change one of your commits to "squash" from "pick"
   2010-11-24 02:06:15 < Dark_Shikari> and it will squash the commits together
   2010-11-24 02:06:22 < Dark_Shikari> remember, to edit a commit, use --amend
   2010-11-24 02:06:56 < rfw> almost rm -rf'd digress there
   2010-11-24 02:06:57 < rfw> whoops
   2010-11-24 02:07:17 < Dark_Shikari> you should be banned from using rm
   2010-11-24 02:07:27 < rfw> lol
   2010-11-24 02:07:30 < rfw> well i'm on windows
   2010-11-24 02:07:34 < rfw> so del /s /q works too
   2010-11-24 02:07:44 < Dark_Shikari> don't use that either
   2010-11-24 02:08:02 < rfw> well i think i'm done
   2010-11-24 02:08:07 < JEEBsv>  /s /q isn't even easy to write :/
   2010-11-24 02:08:12 < Dark_Shikari> linear revisions? =p
   2010-11-24 02:08:16 < rfw> do i have to
   2010-11-24 02:08:17 < rfw> ;_;
   2010-11-24 02:08:23 < Dark_Shikari> ok then don't
   2010-11-24 02:08:28 < rfw> \o/
   2010-11-24 02:08:29 < Dark_Shikari> format-patch please :)
   2010-11-24 02:08:33 < Dark_Shikari> don't forget to git add
   2010-11-24 02:08:57 < rfw> hold on
   2010-11-24 02:09:01 < rfw> let me write a setuptools package
   2010-11-24 02:09:26 < Jumpyshoes> wait, how do i merge commits?
   2010-11-24 02:09:31 < rfw> git merge?
   2010-11-24 02:09:33 < Dark_Shikari> use git rebase -i as I said
   2010-11-24 02:09:38 < Dark_Shikari> and replace "pick" for one with "squash"
   2010-11-24 02:09:41 < Dark_Shikari> read the info it gives you
   2010-11-24 02:09:43 < Dark_Shikari> also, git help is your friend
   2010-11-24 02:09:52 < Dark_Shikari> git rebase -i HEAD~2 will let you modify the last 2 commits
   2010-11-24 02:09:56 < Dark_Shikari> one of the ways to modify them is squashing
   2010-11-24 02:10:01 < rfw> my git --help launches a help browser, except it doesn't
   2010-11-24 02:10:22 < Dark_Shikari> git help commandname
   2010-11-24 02:10:24 < Dark_Shikari> git help rebase
   2010-11-24 02:10:29 < Dark_Shikari> git help help
   2010-11-24 02:13:33 < rfw> whoops
   2010-11-24 02:13:38 < rfw> i filled my directory with .patch files
   2010-11-24 02:13:45 < rfw> there we go
   2010-11-24 02:13:48 < rfw> where do i submit this?
   2010-11-24 02:13:59 < Dark_Shikari> pastebin
   2010-11-24 02:14:11 < rfw> oh you wanted it in tools, right?
   2010-11-24 02:14:15 < Dark_Shikari> yes
   2010-11-24 02:14:22 < rfw> ah let me fix that
   2010-11-24 02:15:49 < Jumpyshoes> how do i resume an interactive git rebase?
   2010-11-24 02:16:21 < kemuri-_9> git rebase --continue
   2010-11-24 02:16:49 < rfw> http://pastebin.com/zLbbE2KL
   2010-11-24 02:17:27 < Dark_Shikari> rfw: does that include digress?
   2010-11-24 02:17:30 < rfw> oh
   2010-11-24 02:17:30 < rfw> no
   2010-11-24 02:17:36 < rfw> but that's on my github repo
   2010-11-24 02:17:36 < Dark_Shikari> well it won't run without it, will it?
   2010-11-24 02:17:41 < JEEBsv> lol
   2010-11-24 02:17:42 < Dark_Shikari> =p
   2010-11-24 02:17:45 < rfw> so
   2010-11-24 02:17:48 < rfw> put that in tools too?
   2010-11-24 02:17:50 < Dark_Shikari> I guess?
   2010-11-24 02:17:54 < rfw> heh
   2010-11-24 02:18:01 < rfw> am i going to have to include python
   2010-11-24 02:18:05 < rfw> and glibc :p
   2010-11-24 02:18:54 < Dark_Shikari> lol
   2010-11-24 02:18:59 < Dark_Shikari> digress isn't something you can install with apt-get =p
   2010-11-24 02:19:30 < Jumpyshoes> http://pastebin.com/GBSUtExQ
   2010-11-24 02:20:37 < rfw> maybe i should do a debian task next
   2010-11-24 02:20:41 < rfw> and include it in their apt repositories
   2010-11-24 02:20:42 < rfw> :D
   2010-11-24 02:21:14 < rfw> http://pastebin.com/Atb7j4DV
   2010-11-24 02:22:05 < Dark_Shikari> Jumpyshoes: in your STORE_DIFFx2, the , should all be vertically aligned
   2010-11-24 02:22:07 < Dark_Shikari> the first , in each line, that is
   2010-11-24 02:22:15 < Dark_Shikari> so add spaces as necessary
   2010-11-24 02:22:16 < Dark_Shikari> e.g.
   2010-11-24 02:22:21 < Dark_Shikari> packssdw %1, %2
   2010-11-24 02:22:24 < Jumpyshoes> oh right
   2010-11-24 02:22:26 < Dark_Shikari> movq     %3, %4
   2010-11-24 02:22:46 < Dark_Shikari> junk spaces are still around on line 306
   2010-11-24 02:22:57 < Dark_Shikari> 304 line break is needless
   2010-11-24 02:23:05 < Dark_Shikari> other than that lgtm
   2010-11-24 02:23:26 < Jumpyshoes> kk
   2010-11-24 02:25:53 < rfw> actually Dark_Shikari
   2010-11-24 02:25:59 < rfw> can't i add my repo as a submodule
   2010-11-24 02:26:18 < Dark_Shikari> I would really rather not do that.
   2010-11-24 02:26:23 < rfw> i guess
   2010-11-24 02:26:25 < Dark_Shikari> pengvado has the final word though
   2010-11-24 02:26:32 < Dark_Shikari> actually yeah, pengvado, can you comment on this in general?
   2010-11-24 02:26:37 < Dark_Shikari> python regression test script of magic
   2010-11-24 02:27:23 < pengvado> you mean comment on the magic part, or the python?
   2010-11-24 02:28:17 < Dark_Shikari> lol
   2010-11-24 02:28:25 < Dark_Shikari> python isn't magic?
   2010-11-24 02:28:56 < rfw> now to delete every file recovery tool i installed
   2010-11-24 02:29:13 < Dark_Shikari> lol
   2010-11-24 02:29:19 < pengvado> I don't see an "import magic", so no
   2010-11-24 02:29:47 < rfw> i should've probably called it magic, then
   2010-11-24 02:30:04 < Dark_Shikari> pengvado: seriously though
   2010-11-24 02:30:20 < Dark_Shikari> topics like "can we just dump this in tools/"
   2010-11-24 02:32:08 < pengvado> I haven't been following the featurelist, but my general comment on "can we just dump a regression tester in tools/" is "yes"
   2010-11-24 02:32:21 < Dark_Shikari> pengvado: any particular features you want to make sure are in there?
   2010-11-24 02:32:26 < Dark_Shikari> since I imagine you might want to use it too
   2010-11-24 02:33:24 < Jumpyshoes> http://pastebin.com/CEAfyzMd okay, tested w/ 8 and 10 bit
   2010-11-24 02:35:13 < Dark_Shikari> er
   2010-11-24 02:35:15 < Dark_Shikari> you're pxoring m7
   2010-11-24 02:35:21 < Dark_Shikari> an then using m6?
   2010-11-24 02:36:13 < Jumpyshoes> well, pxor was used in the other function
   2010-11-24 02:36:24 < Dark_Shikari> you're pxoring m7
   2010-11-24 02:36:25 < Jumpyshoes> oh wait
   2010-11-24 02:36:26 < Dark_Shikari> you never use m7 again
   2010-11-24 02:36:26 < Jumpyshoes> you're right
   2010-11-24 02:36:27 < Jumpyshoes> i am
   2010-11-24 02:36:49 < Jumpyshoes> yea, i can get rid of that
   2010-11-24 02:36:53 < Dark_Shikari> I'll fix it locally
   2010-11-24 02:36:54 < Jumpyshoes> the dangers of copoy pasta
   2010-11-24 02:37:44 < Dark_Shikari> aha
   2010-11-24 02:37:46 < Dark_Shikari> your patch fails to apply
   2010-11-24 02:37:48 < Dark_Shikari> trailing whitespace
   2010-11-24 02:37:52 < Dark_Shikari> lines 294, 297, 298, 299
   2010-11-24 02:38:47 < Jumpyshoes> wait, what?
   2010-11-24 02:38:57 < Dark_Shikari> whitespace at the end of lines
   2010-11-24 02:39:04 < Dark_Shikari> git yells about them when I try to apply your patch
   2010-11-24 02:39:11 < Jumpyshoes> oh
   2010-11-24 02:39:14 < Jumpyshoes> you can't do that?
   2010-11-24 02:39:23 < Dark_Shikari> I guess I could edit the patch manually ok
   2010-11-24 02:39:29 < Jumpyshoes> sorry, i didn't know
   2010-11-24 02:40:25 < kemuri-_9> notepad++ > textfx edit > trim trailing whitespace  <--- works wonders
   2010-11-24 02:41:56 < Dark_Shikari> Jumpyshoes:
   2010-11-24 02:41:59 < Dark_Shikari> original function: 188 cycles
   2010-11-24 02:42:00 < Dark_Shikari> yours: 30
   2010-11-24 02:42:13 < pengvado> kemuri-_9: does it parse diffs and not strip syntactically significant trailing whitespace?
   2010-11-24 02:42:28 < Jumpyshoes> :O?
   2010-11-24 02:42:29 < Dark_Shikari> pengvado: I think he meant on the code
   2010-11-24 02:42:30 < Dark_Shikari> =p
   2010-11-24 02:42:33 < Dark_Shikari> not the diff
   2010-11-24 02:42:35 < Jumpyshoes> so speedup of about 6x?
   2010-11-24 02:42:38 < Dark_Shikari> yes, for that function
   2010-11-24 02:42:53 < Jumpyshoes> woah, that's cool
   2010-11-24 02:43:31 < Dark_Shikari> http://pastebin.com/e0aa966g
   2010-11-24 02:43:33 < kemuri-_9> yeah, on the code - should do it before making diffs/commits to catch where you might've gotten careless
   2010-11-24 02:43:35 < Dark_Shikari> that's the final version with commit message
   2010-11-24 02:43:44 < Dark_Shikari> I'll handle any more changes pengvado wants to make before we push it
   2010-11-24 02:43:49 < astrange> s/^ +$//g
   2010-11-24 02:43:58 < astrange> take out the ^
   2010-11-24 02:44:09 < Jumpyshoes> woah, i'm the first GCI dude?
   2010-11-24 02:44:14 < Dark_Shikari> The first to finish yes
   2010-11-24 02:44:19 < pengvado> Dark_Shikari, rfw: vague wishlist: report whether output did or did not change (distinct from whether it changed enough to visibly affect bitrate/psnr). and the vaguer part: what if it's supposed to change some configurations and not others?
   2010-11-24 02:44:19 < Jumpyshoes> :O
   2010-11-24 02:44:22 < Jumpyshoes> i should sign up
   2010-11-24 02:45:04 < Jumpyshoes> Dark_Shikari, so i just take a code an asm func task on the page?
   2010-11-24 02:45:17 < Dark_Shikari> you didn't take one?  lol
   2010-11-24 02:45:19 < Dark_Shikari> go take one then
   2010-11-24 02:45:20 < Jumpyshoes> nope
   2010-11-24 02:45:42 < Jumpyshoes> what in the world is melange? cause it's fricking slow
   2010-11-24 02:46:06 < Dark_Shikari> Shit.
   2010-11-24 02:46:07 < Dark_Shikari> That's what it is.
   2010-11-24 02:46:26 < Jumpyshoes> sigh
   2010-11-24 02:46:34 < pengvado> Jumpyshoes: 319: prototypes of highdepth-aware functions should use dctcoef* and pixel*
   2010-11-24 02:46:34 < Jumpyshoes> using shitty open source to promote open source
   2010-11-24 02:46:37 < Jumpyshoes> good way to go
   2010-11-24 02:46:48 < Dark_Shikari> ah yes
   2010-11-24 02:46:56 < rfw> Dark_Shikari: what do you mean by the second part
   2010-11-24 02:46:58 < Dark_Shikari> pengvado: wait.  what?
   2010-11-24 02:47:01 < Jumpyshoes> ?
   2010-11-24 02:47:05 < Dark_Shikari> I don't think we've done that so far
   2010-11-24 02:47:15 < Dark_Shikari> since the asm functions only support one version at a time
   2010-11-24 02:47:25 < Jumpyshoes> oops, Dark_Shikari, can you add another asm func task?
   2010-11-24 02:47:29 < Jumpyshoes> i think both are taken
   2010-11-24 02:47:50 < Dark_Shikari> I think we'll have to wait for j-b to show up
   2010-11-24 02:47:53 < Dark_Shikari> yeah they're getting taken really fast
   2010-11-24 02:47:55 < Dark_Shikari> I'll have to go spam them
   2010-11-24 02:48:14 < Dark_Shikari> pengvado: it seems this wasn't done for anything else in dct.h.  what do you want to do?
   2010-11-24 02:48:45 < pengvado> in dct.h I see 3 functions with both versions and a bunch of 8bit-only
   2010-11-24 02:49:17 < Dark_Shikari> ah, I see
   2010-11-24 02:49:17 < Dark_Shikari> ok
   2010-11-24 02:49:31 < Dark_Shikari> but the function only has one version
   2010-11-24 02:49:33 < Dark_Shikari> it doesn't exist for 8-bit
   2010-11-24 02:49:37 < Dark_Shikari> does it make sense to have it be "templated" then?
   2010-11-24 02:49:50 < pengvado> hmm, do we want to use the prototypes to keep track of which functions have which versions, or change everything once and for all to dctcoef/pixel so that it doesn't have to change again with each patch to implement a few functions?
   2010-11-24 02:50:04 < Dark_Shikari> I like the first idea
   2010-11-24 02:50:21 < pengvado> ok, then leave it
   2010-11-24 02:51:02 < pengvado> 319: vertical align
   2010-11-24 02:52:07 < Dark_Shikari> how so?  just the [16]?
   2010-11-24 02:52:13 < Dark_Shikari> the rest is impossible to align without shifting all the others
   2010-11-24 02:52:39 < Dark_Shikari> Jumpyshoes: also, feel free to watch, this is how code reviews work =p
   2010-11-24 02:52:47 < Jumpyshoes> yea, i am
   2010-11-24 02:52:56 < pengvado> shifting the paren would make more match up
   2010-11-24 02:52:57 < Jumpyshoes> i feel sorta bad <_<
   2010-11-24 02:53:05 < Jumpyshoes> so many mistakes
   2010-11-24 02:53:13 < Dark_Shikari> Jumpyshoes: this is how it starts for everyone
   2010-11-24 02:53:21 < Dark_Shikari> even _my_ patches get 250 nitpicks before committing
   2010-11-24 02:53:26 < Dark_Shikari> this is how we make good code
   2010-11-24 02:53:29 < Dark_Shikari> we bitch about each others'
   2010-11-24 02:53:34 < Jumpyshoes> haha
   2010-11-24 02:53:35 < Dark_Shikari> pengvado: you mean shifting all of them?  or what
   2010-11-24 02:53:53 < pengvado> just the new one
   2010-11-24 02:54:12 < Dark_Shikari> so
   2010-11-24 02:54:13 < Dark_Shikari> void x264_add4x4_idct_mmx       ( uint8_t *p_dst, int16_t dct    [16] );
   2010-11-24 02:54:13 < Dark_Shikari> void x264_add4x4_idct_sse2     ( uint16_t *p_dst, int32_t dct    [16] );
   2010-11-24 02:54:14 < Dark_Shikari> ?
   2010-11-24 02:54:16 < pengvado> yes
   2010-11-24 02:54:19 < Dark_Shikari> ok
   2010-11-24 02:54:21 < Dark_Shikari> done
   2010-11-24 02:54:56 < Dark_Shikari> espes: claim accepted
   2010-11-24 02:55:02 < Dark_Shikari> fuck melange
   2010-11-24 02:55:22 < Jumpyshoes> so whenever the claims come out
   2010-11-24 02:55:39 < pengvado> if I'm not holding Jumpyshoes responsible for optimizing arithmetic width since I haven't written that test yet, then patch ok
   2010-11-24 02:55:51 < Dark_Shikari> pengvado: isn't that only possible with fdct?
   2010-11-24 02:56:03 < Dark_Shikari> or is there a stage that it's possible with in idct?
   2010-11-24 02:56:09 < Dark_Shikari> and yeah, I think that's reasonable
   2010-11-24 02:56:17 < Dark_Shikari> I mean, the fdct is clearly _broken_ now, so...
   2010-11-24 02:56:52 < pengvado> hmm, idct inputs should fit well within 16bit, but they're a 32bit type since pre-quant coefs need 32bit, so it's at least inconvenient
   2010-11-24 02:57:07 < Dark_Shikari> why would idct inputs fit within 16-bit if dct outputs won't?
   2010-11-24 02:58:00 < pengvado> because quant rescales things? at least I think it does.
   2010-11-24 02:58:06 < Dark_Shikari> by that large a margin?  I'm not sure
   2010-11-24 03:00:01 < rfw> x264.c: In function ‘help’: x264.c:351: error: ‘X264_VERSION’ undeclared (first use in this function)
   2010-11-24 03:00:05 < rfw> the hell
   2010-11-24 03:00:18 < Dark_Shikari> configure failed
   2010-11-24 03:00:19 < Dark_Shikari> or something
   2010-11-24 03:00:22 < Dark_Shikari> X264_VERSION gets written by configure
   2010-11-24 03:00:35 < Dark_Shikari> into config.h
   2010-11-24 03:00:40 < Dark_Shikari> pengvado: oh, another thing I wanted to bring up
   2010-11-24 03:00:44 < pengvado> oh, my bad. I was counting bits of expansion, assuming that if iddct expands things by 7 bits and is >>6 then it must have pretty small inputs. but that's wrong. it just means that it's syntactically possible to write a bitstream where idct is very very clipped, and even if it isn't there's no way to know which of the dct coefs that magnitude is in.
   2010-11-24 03:00:56 < rfw> huh that's funny
   2010-11-24 03:01:01 < rfw> it didn't catch the return code
   2010-11-24 03:01:14 < Dark_Shikari> a customer has requested that ffmpeg be able to link to a commercial x264
   2010-11-24 03:01:18 < Dark_Shikari> while ffmpeg remains LGPL
   2010-11-24 03:01:21 < Dark_Shikari> this of course makes sense.
   2010-11-24 03:01:30 < Dark_Shikari> But this requires that ffmpeg configure KNOW that x264 is commercially licensed, and not GPL.
   2010-11-24 03:01:41 < Dark_Shikari> I considered an installed x264_config.h, similar to ffmpeg's.
   2010-11-24 03:01:45 < Dark_Shikari> What do you think should be done?
   2010-11-24 03:02:35 < rfw> oh lol
   2010-11-24 03:02:36 < rfw> windows encoding
   2010-11-24 03:02:50 < rfw> i swear i turned autocrlf off too
   2010-11-24 03:04:29 < Jumpyshoes> Dark_Shikari, is my patch okay, or do i need to do what pengvado said?
   2010-11-24 03:04:53 < pengvado> patch ok
   2010-11-24 03:04:58 < Dark_Shikari> you're good
   2010-11-24 03:05:04 < Jumpyshoes> o
   2010-11-24 03:05:04 < Jumpyshoes> yay
   2010-11-24 03:05:31 < pengvado> I can't think of any way better than x264_config.h
   2010-11-24 03:05:43 < Dark_Shikari> is there anything else we should move to x264_config.h?
   2010-11-24 03:05:44 < Dark_Shikari> bit depth?
   2010-11-24 03:05:58 < pengvado> of course people will install an x264_config.h of one configuration and a binary of another
   2010-11-24 03:06:19 < pengvado> yes
   2010-11-24 03:06:23 < Dark_Shikari> the problem is that if you rely on an API call to check license
   2010-11-24 03:06:29 < Dark_Shikari> it breaks cross-compiling
   2010-11-24 03:06:31 < Dark_Shikari> so this leaves us two options
   2010-11-24 03:06:33 < Dark_Shikari> x264_config.h
   2010-11-24 03:06:39 < Dark_Shikari> or API call + runtime check in ffmpeg if LGPL is on
   2010-11-24 03:07:08 < pengvado> or x264_config.h + runtime check for consistency
   2010-11-24 03:07:42 < Dark_Shikari> so both bit depth and license will have APIs, *plus* config.h entries?
   2010-11-24 03:08:02 < Dark_Shikari> bit_depth is a variable instead of a function call, should license be a variable too, or should we make both function calls?
   2010-11-24 03:11:48 < pengvado> otoh, mismatched license doesn't cause segfaults, so maybe that doesn't need a consistency check
   2010-11-24 03:11:52 < pengvado> bitdepth does though
   2010-11-24 03:13:37 < Jumpyshoes> Dark_Shikari, if my other patch is good, can i claim dct4x4dc_mmx ?
   2010-11-24 03:13:43 < Dark_Shikari> Jumpyshoes: sure.
   2010-11-24 03:13:46 < Jumpyshoes> cool
   2010-11-24 03:14:18 < Dark_Shikari> important thing to note about that
   2010-11-24 03:14:24 < Dark_Shikari> That function used to only use 16-bit math
   2010-11-24 03:14:29 < Dark_Shikari> and thus looked very similar to all the other nearby functions
   2010-11-24 03:14:40 < Dark_Shikari> however, we found that if the input was all black for one input, and all white for the other
   2010-11-24 03:14:43 < Dark_Shikari> i.e. 00000 vs 255 255 255
   2010-11-24 03:14:47 < Dark_Shikari> it overflowed
   2010-11-24 03:14:54 < Dark_Shikari> so it emulates one extra bit of precision: see SUMSUB_17BIT
   2010-11-24 03:14:59 < Dark_Shikari> However... you're doing it in 32-bit.
   2010-11-24 03:15:01 < Dark_Shikari> So you don't need that.
   2010-11-24 03:15:04 < Jumpyshoes> yea
   2010-11-24 03:15:27 < Jumpyshoes> also, what is     movq   m7, [pw_8000] ; convert to unsigned and back, so that pavgw works          supposed to do, m7 isn' t used in the function
   2010-11-24 03:15:34 < Jumpyshoes> oh yes it is
   2010-11-24 03:15:37 < Jumpyshoes> i'm blind <_<
   2010-11-24 03:15:51 < Dark_Shikari> You should go view the git history for that file
   2010-11-24 03:15:53 < Dark_Shikari> and find were it was changed
   2010-11-24 03:15:56 < Dark_Shikari> and use the old version as you reference.
   2010-11-24 03:16:01 < Dark_Shikari> *your
   2010-11-24 03:16:06 < Dark_Shikari> It will be more applicable.
   2010-11-24 03:16:20 < Jumpyshoes> oh, okay
   2010-11-24 03:16:23 < Dark_Shikari> The 17bit, convert to unsigned, etc are pure hacks to quickly emulate the extra bit.
   2010-11-24 03:17:55  * pengvado sleeps
   2010-11-24 03:20:13 < rfw> Dark_Shikari: so what else am i going to need
   2010-11-24 03:24:07 < Dark_Shikari> rfw: link to the latest patch again?
   2010-11-24 03:24:21 < rfw> um hold on
   2010-11-24 03:24:26 < rfw> i changed a few weird things
   2010-11-24 03:24:29 < Dark_Shikari> I will locally commit it, but it'll need to go through two tests before it's done:
   2010-11-24 03:24:46 < Dark_Shikari> 1) I'll have to use it and be satisfied (along with a few other devs, like bugmaster and pengvado)
   2010-11-24 03:24:51 < Dark_Shikari> 2) pengvado's code review
   2010-11-24 03:24:55 < Dark_Shikari> of course, if pengvado isn't interested in python
   2010-11-24 03:24:58 < Dark_Shikari> he might just say "ok"
   2010-11-24 03:25:08 < Dark_Shikari> because it's not part of the encoder, standards are probably lower.
   2010-11-24 03:25:16 < Dark_Shikari> i.e. functioning is more important than being pretty
   2010-11-24 03:26:00 < Jumpyshoes> Dark_Shikari, do you have an idea when the tasks will come up?
   2010-11-24 03:26:09 < Dark_Shikari> when j-b wakes up
   2010-11-24 03:26:21 < Dark_Shikari> he's in france, so do the math
   2010-11-24 03:26:33 < JEEBsv> ~3AM in France now I'd guess
   2010-11-24 03:26:48 < Jumpyshoes> ah, okay
   2010-11-24 03:27:02 < rfw> Dark_Shikari: does that mean pengvado is perl supremacist like Kovensky
   2010-11-24 03:27:44 < Dark_Shikari> maybe.
   2010-11-24 03:27:47 < Dark_Shikari> I don't relaly know
   2010-11-24 03:27:54 < Dark_Shikari> there are many theories.
   2010-11-24 03:28:01 < rfw> http://pastebin.com/nDgwpk6S
   2010-11-24 03:28:02 < Dark_Shikari> some say that he's an alien
   2010-11-24 03:28:20 < rfw> what exactly is a pengvado
   2010-11-24 03:28:45 < JEEBsv> Nobody knows for sure. Only one thing is sure... they fork()
   2010-11-24 03:28:59 < Dark_Shikari> My guess is a youkai of some sort.
   2010-11-24 03:29:18 < Dark_Shikari> Doesn't like sunlight, has thought processes alien to a typical human... seems a perfect match.
   2010-11-24 03:29:22 < rfw> does he have a funny hat
   2010-11-24 03:29:59 < Dark_Shikari> well, everyone knows that youkai that hide out in human society don't wear their funny hats in public.
   2010-11-24 03:30:18 < rfw> :(
   2010-11-24 03:33:58 < Jumpyshoes> was HADAMARD4_1D phased out or something?
   2010-11-24 03:34:20 < Dark_Shikari> No, that change was made because HADAMARD4_1D didn't keep the necessary precision
   2010-11-24 03:34:34 < Jumpyshoes> i mean, i can't find it
   2010-11-24 03:34:38 < Dark_Shikari> oh
   2010-11-24 03:34:55 < Dark_Shikari> I think it was, yeah
   2010-11-24 03:35:03 < Jumpyshoes> just cause?
   2010-11-24 03:35:06 < Dark_Shikari> wow, holger has gone missing
   2010-11-24 03:35:13 < Jumpyshoes> or because of precision issues
   2010-11-24 03:35:23 < Jumpyshoes> cause i think i can bring it back for 32-bit... maybe
   2010-11-24 03:35:24 < Dark_Shikari> I'm guessing it relates to holger's changes
   2010-11-24 03:35:30 < Jumpyshoes> ah, okay
   2010-11-24 03:35:32 < Dark_Shikari> no, you just need WALSH4_1D
   2010-11-24 03:35:35 < Jumpyshoes> i'll bug him tomorrow or somethin
   2010-11-24 03:35:36 < Jumpyshoes> g
   2010-11-24 03:35:38 < Dark_Shikari>     SUMSUB_BADC w, m1, m0, m3, m2, m4
   2010-11-24 03:35:38 < Dark_Shikari>     SWAP 0, 1
   2010-11-24 03:35:38 < Dark_Shikari>     SWAP 2, 3
   2010-11-24 03:35:38 < Dark_Shikari>     SUMSUB_17BIT 0,2,4,7
   2010-11-24 03:35:38 < Dark_Shikari>     SUMSUB_17BIT 1,3,5,7
   2010-11-24 03:35:41 < Dark_Shikari> these lines replace a
   2010-11-24 03:35:44 < Dark_Shikari>     WALSH4_1D  0,1,2,3,4
   2010-11-24 03:35:48 < Dark_Shikari> You don't need HADAMARD
   2010-11-24 03:35:57 < Dark_Shikari> we renamed it to WALSH, I think, because it was a more accurate name
   2010-11-24 03:36:07 < Dark_Shikari> as it's a walsh-ordered transform
   2010-11-24 03:36:10 < Jumpyshoes> oh, so HADAMARD4_1D is WALSH4_1D?
   2010-11-24 03:36:16 < Jumpyshoes> (taking a look at the older revision)
   2010-11-24 03:37:15 < Dark_Shikari> I think so
   2010-11-24 03:37:25 < Dark_Shikari> anyways just look at the current code and mentally replace the thing I said above
   2010-11-24 03:37:28 < Dark_Shikari> with WALSH4_1D
   2010-11-24 03:37:36 < Dark_Shikari> It's basically that.
   2010-11-24 03:37:42 < Jumpyshoes> ah
   2010-11-24 03:40:36 < darkbringer> rfw, i'm not a developer, but would not it be better not to hardcode akiyo_qcif everywhere? I mean it is quite possible that some people would want to use different clips for testing.
   2010-11-24 03:40:48 < Dark_Shikari> Yeah, that.
   2010-11-24 03:40:52 < rfw> oh
   2010-11-24 03:40:54 < Dark_Shikari> it should be a cli argument
   2010-11-24 03:40:58 < rfw> cirno.tiff
   2010-11-24 03:41:00 < JEEBsv> Yes, indeed
   2010-11-24 03:41:08  * JEEBsv pats (9)-rfw
   2010-11-24 03:41:35 < Dark_Shikari> well next time I make a stupid mistake I can be dar(9)shikari
   2010-11-24 03:43:14 < Jumpyshoes> oh yea, one last question
   2010-11-24 03:43:28 < Jumpyshoes> when do revisions usually go up? i'm too lazy to commit and change everything
   2010-11-24 03:43:32 < Jumpyshoes> so i want to pull the latest one
   2010-11-24 03:43:50 < Dark_Shikari> we make a big push every 1-2 weeks
   2010-11-24 03:43:57 < Dark_Shikari> it depends how many changes there are, and how urgent they are
   2010-11-24 03:44:05 < Dark_Shikari> along with the push comes out a newsletter documenting the changes
   2010-11-24 03:44:12 < Dark_Shikari> pushes usually contain 8-24 commits
   2010-11-24 03:44:18 < Jumpyshoes> ah, okay
   2010-11-24 03:44:21 < Dark_Shikari> there may also be bugfix pushes soon after if bugs come up
   2010-11-24 03:44:24 < Dark_Shikari> these usually contain 1-5 commits
   2010-11-24 03:44:24 < Jumpyshoes> so i guess i'll work on it now
   2010-11-24 03:44:49 < Dark_Shikari> it's not really an issue though, asm changes rarely have any conflicts with anything else
   2010-11-24 03:45:22 < reid_> Dark_Shikari: what is the relation between  VLC and x264?
   2010-11-24 03:45:29 < Jumpyshoes> oh, i guess that's true
   2010-11-24 03:45:30 < JEEBsv> reid_: same host
   2010-11-24 03:45:42 < Dark_Shikari> reid_: Videolan is a big organization that hosts a lot of projects
   2010-11-24 03:45:42 < JEEBsv> and under the same videolan umbrella in GSoC etc.
   2010-11-24 03:45:46 < Dark_Shikari> those projects include VLC and x264
   2010-11-24 03:46:08 < Dark_Shikari> So "Videolan" gets accepted to Google Code-In
   2010-11-24 03:46:13 < Dark_Shikari> which means that any Videolan project can submit tasks
   2010-11-24 03:46:27 < Dark_Shikari> such as VLC, Videolan itself (website, etc), VLMC, x264, etc
   2010-11-24 03:46:45 < reid_> is x264 an application or more like a library?
   2010-11-24 03:46:50 < JEEBsv> both
   2010-11-24 03:46:51 < darkbringer> both
   2010-11-24 03:46:59 < Dark_Shikari> both
   2010-11-24 03:47:04 < JEEBsv> very strong command line app, as well as a highly versatile library
   2010-11-24 03:47:14 < Dark_Shikari> x264cli and libx264 as they're called
   2010-11-24 03:48:08 < Dark_Shikari> JEEBsv: yes, it's very strong, it can leap tall buildings in a single bound and make DC 40 fort saves
   2010-11-24 03:48:22 < JEEBsv> haha
   2010-11-24 03:49:37 < reid_> I ask because i'm looking at the filtering system.
   2010-11-24 03:50:42 < Jumpyshoes> i need a better computer
   2010-11-24 03:50:54 < Dark_Shikari> reid_: the filtering task has changed slightly on decree from our BDFL
   2010-11-24 03:50:59 < Jumpyshoes> this laptop is hot and x264 compiles too slowly
   2010-11-24 03:51:00 < Dark_Shikari> it's now porting new filters into libavfilter ;)
   2010-11-24 03:51:07 < Dark_Shikari> Which we'll then use from x264
   2010-11-24 03:51:10 < reid_> Jumpyshoes: celeron ftw!
   2010-11-24 03:51:17 < Jumpyshoes> oh
   2010-11-24 03:51:20 < Jumpyshoes> i have an i5
   2010-11-24 03:51:22 < Jumpyshoes> won a laptop
   2010-11-24 03:51:32 < Dark_Shikari> >x264 compiles too slowly
   2010-11-24 03:51:33 < Dark_Shikari> make -j8
   2010-11-24 03:51:35 < Dark_Shikari> problem solved
   2010-11-24 03:51:41 < Jumpyshoes> what?
   2010-11-24 03:51:45 < reid_> you cant get too much better that i5.
   2010-11-24 03:51:52 < Jumpyshoes> oh yes you can
   2010-11-24 03:51:58 < Dark_Shikari> I have a 1.6ghz i7
   2010-11-24 03:51:59 < Dark_Shikari> it's fast enough
   2010-11-24 03:52:03 < Jumpyshoes> i used a $3000 computer over the summer
   2010-11-24 03:52:04 < Sean_McG> you can get a 16-way Xeon
   2010-11-24 03:52:07  * Sean_McG lollerblades
   2010-11-24 03:52:15 < Jumpyshoes> i miss the days when i could open vs2010 in half a second
   2010-11-24 03:52:18 < Jumpyshoes> instead of two minutes
   2010-11-24 03:52:27 < Dark_Shikari> yes, that's called "time stop"
   2010-11-24 03:52:37 < Dark_Shikari> And unless you're a 9th level sorc/wizard, or Sakuya, you can't do that.
   2010-11-24 03:52:41 < Dark_Shikari> er, 9th spell level
   2010-11-24 03:52:43 < Jumpyshoes> it had an SSD
   2010-11-24 03:52:46 < reid_> Sean_McG: in a laptop?
   2010-11-24 03:52:49 < Dark_Shikari> Oh, that's the other way to do it.
   2010-11-24 03:52:53 < Sean_McG> reid_: hrm, no.
   2010-11-24 03:52:56 < Jumpyshoes> yea
   2010-11-24 03:52:57 < Jumpyshoes> i love SSDs

`Category:x264 <Category:x264>`__
