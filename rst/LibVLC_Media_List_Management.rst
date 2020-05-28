{{Lowercase}} {{Example code}} == Global Description of the available
objects == The atomic item that represent a media that you can play is a
'''libvlc_media''' in [[libVLC]].

A '''media_list''' is an object that contains several ''libvlc_media''.
You can add items to that media_list.

You can play a media_list using a '''media_list_player'''.

== A media descriptor can contain a media list == A playlist downloaded
from Google video has a corresponding ''libvlc_media''. This
''libvlc_media'' has several subitems. You can access them through
libvlc_media_subitems() which returns a media_list.

This explains how a media_list can be hierarchical. To browse it you'll
use libvlc_media_list_hierarchy_view(). To view the all the item without
hierarchy use libvlc_media_list_flat_view().

== Sample Code == <syntaxhighlight lang="c"> void
play_media(libvlc_instance_t \*vlc, libvlc_drawable_t window) {

   libvlc_media_list_t *ml; libvlc_media_list_player_t*\ mlp;
   libvlc_media_player_t *mp; libvlc_media_t*\ md1, \*md2;

   ml = libvlc_media_list_new(vlc);

   md1 = libvlc_media_new_path(vlc, "http://mycool.com/movie1.avi"); md2
   = libvlc_media_new_path(vlc, "http://mycool.com/movie2.avi");

   libvlc_media_list_add_media(ml, md1); libvlc_media_list_add_media(ml,
   md2);

   libvlc_media_release(md1); libvlc_media_release(md2);

   mlp = libvlc_media_list_player_new(vlc);

   mp = libvlc_media_player_new(vlc);

   /\* Use our media list \*/
   libvlc_media_list_player_set_media_list(mlp, ml);

   /\* Use a given media player \*/
   libvlc_media_list_player_set_media_player(mlp, p_mp);

   /\* Get our media instance to use our window \*/
   libvlc_media_player_set_drawable(mlp, window);

   /\* Play \*/ libvlc_media_list_player_play(mlp);

   /\* Let it play forever \*/ while(1) sleep(300);

..

   }

</syntaxhighlight>

[[Category:libVLC]]
