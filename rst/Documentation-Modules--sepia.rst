{{Moduletype=Video filterdescription=Gives video a warmer tone by
applying sepia effect}}

== Options == {{Option value=integer min=0 description=Intensity of
sepia effect }}

== Examples ==
   {{%}} --video-filter "sepia" video.ogv {{%}} --video-filter
   "sepia{intensity=100}" video.ogv

== Source code == \* {{VLCSourceFile|modules/video_filter/sepia.c}}

{{Documentation footer}}
