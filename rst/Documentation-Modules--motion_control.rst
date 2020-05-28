{{Moduletype=Control interfaceos=Linux|description=motion control
interface}}

Use this control interface to rotate the video when moving a laptop
using HDAPS or AMS sensors.

== Options ==

{{Option default=enabled rotate]] video filter instead of the
[[Documentation:Modules/transform|transform]] video ouput filter to
rotate the video }}

== Examples == Using the [[Documentation:Modules/transformrotate]] video
filter (possible rotation angles theoretically range from -180° to
+180°, depending on your sensor): % '''vlc --control motion
--motion-use-rotate --video-filter rotate somevideo.avi'''

{{Documentation footer}}
