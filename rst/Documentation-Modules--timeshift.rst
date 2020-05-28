{{Moduletype=Access filterlast_version=0.9.9|description=enable
timeshifting on live streams}}

This access filter will enable timeshifting on live streams. The user
will thus be able to pause the stream. Buffered data will be stored in
memory for short periods and on the hard drive afterwards.

<font color="red">''' \*\* Warning : the following documentation is
deprecated \*\* '''

It is now in the VLC core. </font>

== Options == {{Option value=integer description=Size of temporary files
in MB }}

{{Option value=string \|description=Directory where temporary files will
be stored. }}

{{Option default=disabled \|description=Force use of the timeshift
module even if the underlying access claims that it can pause }}

== Example ==
   % '''vlc --access-filter timeshift <some live stream>'''

{{Documentation footer}}
