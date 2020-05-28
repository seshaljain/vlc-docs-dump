:''For the former module, see [[Documentation:Modules/crop]]''
{{Moduletype=Video filterdescription=Video [[crop]]ping filter}}

== Options == === Crop === <onlyinclude>{{Option value=integer
max=<var>INT_MAX</var> name=croppadd-cropbottom min=0 description=Pixels
to crop from bottom }} {{Option value=integer max=<var>INT_MAX</var>
name=croppadd-cropright min=0 description=Pixels to crop from right
}}</onlyinclude> === Padd === <onlyinclude>{{Option value=integer
max=<var>INT_MAX</var> name=croppadd-paddbottom min=0 description=Pixels
to add to bottom }} {{Option value=integer max=<var>INT_MAX</var>
name=croppadd-paddright min=0 description=Pixels to add to right
}}</onlyinclude>

== Source code == \* {{VLCSourceFile|modules/video_filter/croppadd.c}}

{{Documentation}}
