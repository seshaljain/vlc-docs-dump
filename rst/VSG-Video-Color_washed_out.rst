= Video Colors are washed out =

When using nVidia cards or improper output settings, with {{VLC}} on
[[Windows]], sometimes the black levels are not correct, and dark
regions in the image appear as gray. The image is washed-out or milky,
like in the following screenshots:

[[Image:Vadrouille snapshot 235.jpgcenterColors wrong]]
[[Image:Vadrouille snapshot 255.jpgcenterColors right]]

= Solution Using the nVidia Control Pannel =

To fix this issue:

*go to the nVidia Control panel&nbsp;*\ change color range from
''limited (16-235)'' to ''full dynamic range (0-255)''&nbsp; \*restart
VLC

[[Image:Nvidia-Panel.jpgcenter|600px]]

Some versions of the nVidia Control Pannel do not present this setting.
You can also try to "Reset to defaults" from the upper right corner.

= Alternate Solutions =

-  Tools -> Settings -> Video and try the following, in the order of
   decreasing playback performance:
-  Switch to DirectX(DirectDraw) - recommended setting for Windows XP,
   incompatible with Vista Aero interface
-  If that does not work, Disable Hardware YUV->RGB conversions
-  If that does not work, try Windows GDI video output (worst
   performance)

After each change you need to restart the player (not just the
playback).

{{VSG}}
