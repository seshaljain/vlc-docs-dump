{{Moduletype=Accessdescription=[[MMS]] inputsc2=mmshsc4=mmsu}}

Handles Microsoft Media Server [[UDP]], [[TCP]] and [[HTTP]] variants,
including the ability to open mms:// and mmsh:// [[MRL]]s.

In the source code for mms module it says:
   -  NOTES:
   -  MMSProtocole documentation found at
      <nowiki>http://get.to/sdp\ </nowiki>

get.to/sdp is now located at sdp.ppona.com. This document is pertinent:
([http://sdp.ppona.com/zipfiles/MMSprotocol.pdf MMSprotocol.pdf] or
[https://archive.today/QClst archived copy]) <!-- DoesItReallyMatter
says: Why do I say sdp.ppona.com when get.to/sdp redirects (as of April
2019) to mediadiscovery.net? The whole thing looks to me disreputable
and mediadiscovery.net says nothing of the MMS protocol.

When I traced it with the Internet Archive:
https://web.archive.org/web/20011114142105/http://get.to/sdp redirects
to
https://web.archive.org/web/20011105142315/http://freespace.virgin.net/sdpman.sdp/
https://web.archive.org/web/20040611223803/http://freespace.virgin.net/sdpman.sdp/
announced it moved to http://sdp.ppona.com Additionally, get.to/sdp is
visible in the screenshot:
http://sdp.ppona.com/readme/readme.html#anchor21312 --> == Options ==
{{Option value=integer name=mms-all description=Force selection of all
streams }} {{Option value=integer description=Select the stream with the
maximum [[bitrate]] under this limit }} {{Option value=string
description=HTTP proxy for the HTTP MMS variant.
<code><nowiki>http://%5Buser\ [:password]@]proxy.example.com:</nowiki>[[port]]/</code>
}}

== Source code == \* {{VLCSourceFoldermodules/access/mms/mms.c}} (main
file) \* {{VLCSourceFilemodules/access/mms/mmstu.c}} (MMS over TCP or
UDP)

{{Stub}}

{{Documentation footer}}
