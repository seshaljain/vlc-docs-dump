== Thoughts about SDI API ==

There are a number of manufacturers using V4L2, sometimes alongside
ALSA, to provide Linux drivers for their SDI cards. This causes a lot of
issues for professional users. There are a number of proprietary APIs
that provide a better interface for professional users. On the capture
side the issues can be described as follows:

-  Separate file descriptors for Audio/Video meaning sync must be
   performed with timestamps (if they exist; sometimes they don't). This
   is the most serious issue in a professional environment.
-  Timestamps are sometimes generated with the system clock and do not
   reflect the way audio is transported in SDI, nor precise nature of
   NTSC timestamps.
-  Impossible to select number of lines to capture per poll response
   (e.g x lines, one field, one frame)
-  Impossible to keep NTSC audio samples per video frame cadence, nor
   line number where audio starts
-  8 or 10-bit capture (though this is easy to solve in V4L2)
-  Signals when frames are dropped (so alternative signals can be sent)
-  An API for accessing VBI and HBI in 10-bit alongside the frame for
   things like Closed captions

Most of these issues are caused by the separation of
Audio/Video/Blanking so the two solutions in that area could be accurate
timestamps (using a 27mhz clock) or data returned multiplexed. Another
way of solving the issue would be to have an SDI "pixel format" and
userspace could parse the datastream itself as VLC does with the
Computermodules SD-SDI driver.

== SDI extension to V4L2 thoughts == Single SDI file descriptor. Open,
setup options (bit-depth etc), poll on descriptor with buffers to read
(or mmap if the data is large enough?).

Receive minimum of one line of data starting at EAV to subsequent EAV.
Either in v210 for 10-bit or UYVY for 8-bit. Userspace has the
responsibility of parsing the datastream (easily doable with a libsdi
component).

[[Category:Dev Discussions]]
