It is not said in which directory are images saved if image output
enabled. : Default is to save them in the current directory (unless you
change the --image-out-prefix option's value to something like
"/a/b/img" which will make it save in directory /a/b/). Feel free to
update the description in the article. [[User:Dionoea|Dionoea]] 10:37, 7
September 2007 (CEST)

Regarding cloning the output. Is ''-clone-vout-filter=...'' correct, or
should it be ''-clone-vout=...''? The former gives an error for me
(Windows XP). I needed to get the video to output on both monitors on a
dual display system. To get it to work (without getting blank windows
rather than video) I had to set the DirectX module to output to DISPLAY2
and then set ''--clone-vout=vout_directx,opengl''.
[[User:Gushie|Gushie]] 16:47, 17 October 2007 (CEST)
