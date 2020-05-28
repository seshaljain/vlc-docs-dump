{{Moduletype=Access filterdescription=toggle recording incoming data to
disk}}

This access filter will enable recording incoming data to disk when the
user presses the <kbd>r</kbd> key. Note that this is very unlikely to
work for sources using an encapsulation method other than ts.

== Options == {{Option value=string description=Directory where recorded
that will be stored. }}

== Example ==
   % '''vlc --access-filter record <some udp ts stream>'''

: VLC will toggle recording when you press the <kbd>r</kbd> hotkey.

{{Documentation footer}}
