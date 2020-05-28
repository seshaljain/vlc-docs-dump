{{Moduletype=Services
discoverylast_version=1.1.13description=[[wikipedia:HAL
(software)sc=none}}

This module was removed because it is no longer needed; it was used on
\*nix systems before the advent of [[wikipedia:udev|udev]]. {{Clear}}

It was removed with this note: <pre> HAL is officially deprecated. The
new udev discs module provide the same functionality in VLC. Moreover,
the plugin was waking up the CPU at regular intervals. Last,
InitDeviceValues seemed to cause problems with wrong disc paths being
saved to vlcrc for some people </pre>

== Options == None.

== Source code == \*
[https://git.videolan.org/?p=vlc/vlc-0.8.git;a=blob;f=modules/services_discovery/hal.c;h=9ee9e9aa659dfa5f283b28cc971eab622a7c9052;hb=8b61d4ef6120a68ea9e4dd3865d6a35d11965e2c
&#x5B;9ee9e9aa659dfa5f283b28cc971eab622a7c9052&#x5D;] (introduction) \*
{{VLCSourceFilemodules/services_discovery/hal.c}} \*
{{VLCSourceFilemodules/services_discovery/hal.c}} \*
{{VLCSourceFilemodules/services_discovery/hal.c}} \*
[https://git.videolan.org/?p=vlc/vlc-1.1.git;a=commitdiff;h=0565b5c2e5062b41e6e1d2b441724899bfdcf38d
&#x5B;0565b5c2e5062b41e6e1d2b441724899bfdcf38d&#x5D;] (removal)

== External links == \* [https://freedesktop.org/wiki/Software/hal/
freedesktop.org - hal]

{{Documentation}}
