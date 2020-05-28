The modular nature of allows you to do quite strange and unusual things with it. This page tries to list some funny and insane uses.

Caca and Goom
-------------

If you have vlc compiled with both caca and goom you can listen to music with `caca <caca>`__ rendering the output of `goom <goom>`__. That means you can show the visualisations from an audio file as colour ASCII art! Try something like this:

``{{$}} vlc --audio-visual goom --vout caca somemusic.mp3``

Likewise, if you would like to view a video file as colour ASCII art, try the following:

``{{$}} vlc --vout caca somevideo.avi``

Pipe data to VLC
----------------

You can pipe input from standard input to VLC, rather than open a file or stream. VLC accepts data this way if you use a dash as a filename, ie:

``{{$}} vlc -``

You can access a named pipe using fd://, ie:

``{{$}} vlc fd://nameofpipe ``

Syntax in VLM conf file:

``setup yourinput input fd://nameofpipe``

Piping passes the output of one program into the input of another. An example of this is using `cat <wikipedia:Cat_(Unix)>`__, which is part of GNU coreutils (ie, on \*nix systems). Cat displays the contents of a file to standard output (normally to the screen as text). In this case, we'll use the pipe character to redirect this into vlc's standard input, which will then be played. To wit,

``{{$}} cat file.mpg | vlc -``

All very sane (though pointless) so far: if you're looking for madness, read on. You can get input from anywhere. A good place to get input is `ffmpeg <ffmpeg>`__. Say you have a `.flv <.flv>`__ file (which VLC now supports from version 0.8.4a onwards) and you want to play it in vlc. You could use ffmpeg to `transcode <transcode>`__ it on the fly and pipe the output to vlc. The following command will do this:

``{{$}} ffmpeg -i 0.flv -f asf - | vlc -``

A longer version with all the options ffmpeg likes to have is:

``{{$}} ffmpeg -i 0.flv -vcodec mpeg4 -ac 1 -ab 64 -acodec mp2 -b 128 -f asf -s cif - | vlc -``

The advantage of this is that you don't have to make a new file (possibly 100s of MB in size). But you'll probably need a good computer. Plus, you wont have much control when playing it. You can pipe into ffmpeg too, so I suppose you could pass things along ffmpeg forever, transcoding it a million different ways, and ending up in vlc (please don't try that, your computer really wouldn't like it).

Encoding Lots of Files
----------------------

This command shows how to encode a whole directory of files in Linux, without your input. When complete, it'll show a message to say it is complete. It's a single command split over several lines (with \\)

.. code:: bash

    for A in *.avi; do \
    echo ************************* $A ********************* ;\
    vlc --sout-all "$A" :sout="#transcode{...}:\
    std{access=file,mux=avi,url=~/$A.avi}" \
    vlc://quit -I dummy ;\
    done ;\
    Xdialog --title 'Complete' --msgbox 'All done' 0 0;

Make sure you really understand this command before using it. It's also a good idea to make sure you've got the right options in the transcode bit, and that it'll transcode the right files. The output is sent to your home folder in this example.

`Category:How_To <Category:How_To>`__
