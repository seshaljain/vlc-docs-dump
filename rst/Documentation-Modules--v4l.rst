{{moduletype=Access demuxos=Linux|description=Video 4 Linux input}}

== Help Output ==

Each of these options can be used as commandline flags individually as
shown below or as such:
v4l:///dev/video:norm=secam:frequency=543250:size=640x480:channel=0:adev=/dev/dsp:audio=0
where you can see that /dev/video refers to vdev, and the rest line up
with the flags below less the prefix --v4l-.

Video4Linux input (v4l)
   --v4l-caching <integer> Caching value in ms
      Caching value for V4L captures. This value should be set in
      milliseconds.

   --v4l-vdev <string> Video device name
      Name of the video device to use. If you don't specify anything, no
      video device will be used.

   --v4l-adev <string> Audio device name
      Name of the audio device to use. If you don't specify anything, no
      audio device will be used.

   --v4l-chroma <string> Video input chroma format
      Force the Video4Linux video device to use a specific chroma format
      (eg. I420 (default), RV24, etc.)

   --v4l-fps <float> Framerate
      Framerate to capture, if applicable (-1 for autodetect).

   --v4l-samplerate <integer> Samplerate
      Samplerate of the captured audio stream, in Hz (eg: 11025, 22050,
      44100)

   --v4l-channel <integer> Channel
      Channel of the card to use (Usually, 0 = tuner, 1 = composite, 2 =
      svideo).

   --v4l-tuner <integer> Tuner
      Tuner to use, if there are several ones.

   --v4l-norm {3 (Automatic), 2 (SECAM), 0 (PAL), 1 (NTSC)}
      Norm

   ..

      Norm of the stream (Automatic, SECAM, PAL, or NTSC).

   --v4l-frequency <integer> Frequency
      Frequency to capture (in kHz), if applicable.

   --v4l-audio <integer> Audio Channel
      Audio Channel to use, if there are several audio inputs.

   --v4l-stereo, --no-v4l-stereo
      Stereo (default enabled)

   ..

      Capture the audio stream in stereo. (default enabled)

   --v4l-width <integer> Width
      Width of the stream to capture (-1 for autodetect).

   --v4l-height <integer> Height
      Height of the stream to capture (-1 for autodetect).

   --v4l-brightness <integer> Brightness
      Brightness of the video input.

   --v4l-colour <integer> Color
      Color of the video input.

   --v4l-hue <integer> Hue
      Hue of the video input.

   --v4l-contrast <integer> Contrast
      Contrast of the video input.

   --v4l-mjpeg, --no-v4l-mjpeg
      MJPEG (default disabled)

   ..

      Set this option if the capture device outputs MJPEG (default
      disabled)

   --v4l-decimation <integer> Decimation
      Decimation level for MJPEG streams

   --v4l-quality <integer> Quality
      Quality of the stream.

[[Category:GNU/Linux]]
