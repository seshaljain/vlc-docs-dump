{{Moduletype=Access filterdescription=limit incoming bandwidth}}

== Options == {{Option value=integer description=The bandwidth module
will drop any data in excess of that many bytes per seconds }}

== Example ==
   % '''vlc --access-filter bandwidth --access-bandwidth 131072 <some
   url>'''

: Will limit incoming data to 128 kBytes/second (128*1024 Bytes/second).

{{Stub}}

{{Documentation footer}}
