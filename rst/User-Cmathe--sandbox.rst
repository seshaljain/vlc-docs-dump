====Subtitle Object====

readonly properties

\*'''vlc.subtitle.count''': (supported in vlc version >= 1.1.0) returns
the number of subtitle available.

read/write properties

\*'''vlc.subtitle.track''': (supported in vlc version >= 1.1.0) get and
set the subtitle track to show on the video screen. The property takes
an integer as input value [1..65535]. If subtitle track is set to 0, the
subtitles will be disabled. If set to a value outside the current
subtitle tracks range, then it will return -1 and display an error
message.

methods

\*'''vlc.subtitle.description(int i)''': (supported in vlc version >=
1.1.0) give the i-th subtitle name. 0 correspond to disable and 1 to the
first subtitle.

====Video object====

readonly properties

\*''none''

read/write properties

-  ''none''

methods

*'''vlc.video.deinterlaceEnable("my_mode")''': (supported in vlc version
>= 1.1.0) enable deinterlacing with my_mode. You can enable it with
"blend", "bob", "discard", "linear", "mean" or "x" mode. Enabling too
soon deinterlacing may cause some problems. You have to wait that all
variable are available before enabling
it.*'''vlc.video.deinterlaceDisable()''': (supported in vlc version >=
1.1.0) disable deinterlacing.

=====Marquee Object=====

readonly properties

-  ''none''

read/write properties

-  ''none''

methods *'''vlc.video.marquee.enable()''': (supported in vlc version >=
1.1.0) enable marquee filter*'''vlc.video.marquee.disable()''':
(supported in vlc version >= 1.1.0) disable marque filter
*'''vlc.video.marquee.text("my text")''': (supported in vlc version >=
1.1.0) display my text on the screen*'''vlc.video.marquee.color(int
val)''': (supported in vlc version >= 1.1.0) change the text color. val
is the new color to use (WHITE=0x000000, BLACK=0xFFFFFF, RED=0xFF0000,
GREEN=0x00FF00, BLUE=0x0000FF...). *'''vlc.video.marquee.opacity(int
val)''': (supported in vlc version >= 1.1.0) change the text opacity,
val is defined from 0 (completely transparent) to 255 (completely
opaque).*'''vlc.video.marquee.position(int val)''': (supported in vlc
version >= 1.1.0) change the text position (CENTER=0, LEFT=1, RIGHT=2,
TOP=4, TOP-LEFT=5, TOP-RIGHT=6, BOTTOM=8, BOTTOM-LEFT=9,
BOTTOM_RIGHT=10) *'''vlc.video.marquee.refresh(int val)''': (supported
in vlc version >= 1.1.0) change the marquee refresh
period.*'''vlc.video.marquee.size(int val)''': (supported in vlc version
>= 1.1.0) val define the new size for the text displayed on the screen.
If the text is bigger than the screen then the text is not displayed.
*'''vlc.video.marquee.timeout(int val)''': (supported in vlc version >=
1.1.0) change the timeout value. val is defined in ms, but 0 value
correspond to unlimited.*'''vlc.video.marquee.x(int val)''': (supported
in vlc version >= 1.1.0) change text abscissa.
\*'''vlc.video.marquee.y(int val)''': (supported in vlc version >=
1.1.0) change text ordinate.

Some problems may happen (option like color or text will not be applyed)
because of the VLC asynchronous functioning. To avoid it, after enabling
marquee, you have to wait a little time before changing an option. But
it should be fixed by the new vout implementation.

====Audio object====

readonly properties \*'''vlc.audio.count''': (supported in vlc version
>= 1.1.0) returns the number of audio track available.

methods \*'''vlc.audio.description(int i)''': (supported in vlc version
>= 1.1.0) give the i-th audio track name. 0 corresponds to disable and 1
to the first audio track.

=====Equalizer object=====

readonly properties

-  ''none''

read/write properties \*'''vlc.audio.equalizer.preset''': (supported in
vlc version >= 1.1.0) set an equalizer preset.

methods *'''vlc.audio.equalizer.enable()''': (supported in vlc version
>= 1.1.0) enable equalizer.*'''vlc.audio.equalizer.disable()''':
(supported in vlc version >= 1.1.0) disable equalizer.
*'''vlc.audio.equalizer.presetName(int i)''': (supported in vlc version
>= 1.1.0) give the i-th preset name.*'''vlc.audio.equalizer.getBand(int
i)''': (supported in vlc version >= 1.1.0) if i is an int value from 0
to 9 it returns a double corresponding to the i-th band value. If i
value is -1 it returns a double corresponding to the preamp value, and
if i value is -2 it gives the number of band.
\*'''vlc.audio.equalizer.setBand(int i, double amp)''': (supported in
vlc version >= 1.1.0) set amp as new value (from -20dB to 20dB) of the
i-th band (-1 for the preamp, from 0 to 9 for the 60 Hz to 16 kHz band).
