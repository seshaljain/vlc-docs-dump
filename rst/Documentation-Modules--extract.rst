{{Moduletype=Video filterdescription=extract a color component from the
video}}

{{Option value=integer description=Color component to extract (0xRRGGBB)
}}

== Example == Extract the yellow component from a video: % '''vlc
--video-filter "extract{component=0xFFFF00}" somevideo.avi'''

== Typical use == You can create a live Andy Warhol display.

{{Stub}} {{Documentation footer}}
