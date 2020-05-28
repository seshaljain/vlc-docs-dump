.. raw:: mediawiki

   {{howto|set specific brightness or contrast for a file}}

| First open Command Prompt/cmd.exe. A quick way of doing this is to go to:
| **Start** >> **Run**. Then enter "**cmd**" and press Enter/OK.
| **Assuming you have VLC installed, to do it in one line, you can do something like:**

::

       C:\Program Files\VideoLAN\VLC\vlc.exe [options] FILE

Where [options] are the `command line <command_line>`__ parameters and FILE is the location of the file you wish to play.

| 
| **For a two-line method, which is potentially faster for doing multiple instances etc.:**

::

   cd C:\Program Files\VideoLAN\VLC
   vlc [options] FILE

| 
| **The commandline parameters for image properties are as follows:**

::

   Image properties filter
         --contrast &lt;float&gt;         Image contrast (0-2)
         --brightness &lt;float&gt;       Image brightness (0-2)
         --hue &lt;integer&gt;            Image hue (0-360)
         --saturation &lt;float&gt;       Image saturation (0-3)
         --gamma &lt;float&gt;            Image gamma (0-10)
         --brightness-threshold, --no-brightness-threshold
                                    Brightness threshold (default disabled)

| 
| **The image adjust filter needs to be enabled so use:**

::

    --video-filter adjust

| To enable it.
| **Here is an example:**

::

    vlc --video-filter adjust --brightness 1.8 --contrast 1.5 FILE

| 
| 

.. raw:: mediawiki

   {{DEFAULTSORT:Contrast}}
