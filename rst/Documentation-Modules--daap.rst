This module provided compatibility in accessing [[iTunes]] shares. It was removed with the note:
   - Remove broken daap plugin (unmaintained <abbr title="with respect to">wrt</abbr> VLC API changes, relies on
      an unmaintained library, probably unable to read content from new
      itunes, ...). Implementations exist in rhythmbox, xmms2 and
      daap-sharp, we should see if a proper lib exists or if we could
      make one

The library it depended upon was
[https://linux.die.net/man/3/libopendaap libopendaap].

== Services discovery == {{Moduletype=Services
discoverylast_version=0.9.?DAAP]] shares|sc=none}}

=== Options === None. {{Clear}}

=== Access === {{Moduletype=Accesslast_version=0.9.?DAAP]]
access|sc=none}}

==== Options ==== None. {{Clear}}

== Source code == \*
[https://git.videolan.org/?p=vlc/vlc-0.8.git;a=commitdiff;h=024fa1c48391bdcff9f3ca3f19f8ebb03a6db1f8
&#x5B;024fa1c48391bdcff9f3ca3f19f8ebb03a6db1f8&#x5D;] (introduction) \*
{{VLCSourceFilemodules/services_discovery/daap.c}} \*
[https://git.videolan.org/?p=vlc/vlc-0.9.git;a=commitdiff;h=0900f11014557ea895a290d2c1518d739f97a8b6
&#x5B;0900f11014557ea895a290d2c1518d739f97a8b6&#x5D;] (removal)

{{Documentation}}
