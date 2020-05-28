{{howto|set specific brightness or contrast for a file}}

First open Command Prompt/cmd.exe. A quick way of doing this is to go
to:<br>'''Start''' &gt;&gt; '''Run'''. Then enter "'''cmd'''" and press
Enter/OK.<br>

<br>

'''Assuming you have VLC installed, to do it in one line, you can do
something like:'''<br> <pre> C:Program FilesVideoLANVLCvlc.exe [options]
FILE

</pre> Where [options] are the [[command line]] parameters and FILE is
the location of the file you wish to play.

<br>

'''For a two-line method, which is potentially faster for doing multiple
instances etc.:'''<br> <pre>cd C:Program FilesVideoLANVLC vlc [options]
FILE </pre> <br>

'''The commandline parameters for image properties are as
follows:'''<br> <pre>Image properties filter --contrast &lt;float&gt;
Image contrast (0-2) --brightness &lt;float&gt; Image brightness (0-2)
--hue &lt;integer&gt; Image hue (0-360) --saturation &lt;float&gt; Image
saturation (0-3) --gamma &lt;float&gt; Image gamma (0-10)
--brightness-threshold, --no-brightness-threshold Brightness threshold
(default disabled) </pre> <br>

'''The image adjust filter needs to be enabled so use:'''<br> <pre>
--video-filter adjust </pre> To enable it.<br>

<br>

'''Here is an example:'''<br> <pre> vlc --video-filter adjust
--brightness 1.8 --contrast 1.5 FILE </pre> <br>

<br>

<br>

{{VSG}}

{{DEFAULTSORT:Contrast}}
