{{See alsoname=smemfirst_version=1.1.0sc=smem}} {{Clear}}

There is a note in the source code: <syntaxhighlight lang="c">
/*************************************************************************\***\*
\* How to use
it**\ \***********************************************************************\*\ **\*
\* \* You should use this module in combination with the transcode
module, to get \* raw datas from it. This module does not make any
conversion at all, so you \* need to use the transcode module for this
purpose. \* \* For example, you can use smem as it : \*
--sout="#transcode{vcodec=RV24,acodec=s16l}:smem{smem-options}" \* \*
Into each lock function (audio and video), you will have all the
information \* you need to allocate a buffer, so that this module will
copy data in it. \* \* the video-data and audio-data pointers will be
passed to lock/unlock function
\***\ \****************************************************************************/
</syntaxhighlight>

== Options == {{Option value=string description=Address of the video
prerender callback function. This function will set the buffer where
render will be done. }} {{Option value=string description=Address of the
audio prerender callback function. This function will set the buffer
where render will be done. }} {{Option value=string description=Address
of the video postrender callback function. This function will be called
when the render is into the buffer. }} {{Option value=string
description=Address of the audio postrender callback function. This
function will be called when the render is into the buffer. }} {{Option
value=string description=Data for the video callback function. }}
{{Option value=string description=Data for the audio callback function.
}} {{Option value=boolean description=Time Synchronisation option for
output. If true, stream will render as usual, else it will be rendered
as fast as possible. }}

== Source code == \* {{VLCSourceFile|modules/stream_out/smem.c}}

{{Documentation}}
