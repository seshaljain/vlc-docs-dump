{{historical}} == Installing VLC on Mandriva ==

To install the latest VLC packages, add the following sources for your
Mandriva version (you can use Easy urpmi for that):

   -  contrib from the core distribution;
   -  plf (Penguin Liberation Front) from the external add-ons.

Then install the required packages with urpmi:

   # urpmi libdvdplay0 wxvlc vlc-plugin-a52 vlc-plugin-ogg
   vlc-plugin-mad libmatroska0

You might also try to install libdvdcss2:

   # urpmi libdvdcss2

[[Category:GNU/Linux distros]] [[Category:Proposed deletion]]
