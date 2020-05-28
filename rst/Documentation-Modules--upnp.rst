Prior to VLC 2.0.0 the [[wikipedia:UPnPCyberLink]]) and upnp_intel (for
[[wikipedia:Intel
Corporation63751e5aef7dc2ef5098df0df8bdca07849d8fd515e31aa8a7a30df086bb31422b750dcbd632dfae|l=renamed}}
to upnp.

== <span id="upnp_intel"></span> upnp.cpp == {{Moduletype=Services
discoverydescription=[[wikipedia:Universal Plug'n'Playsc=none}} When VLC
is compiled with UPNP support, you will still need{{Check|for=May no
longer be necessary?}} to enable UPNP service discovery: \* either on
command line via $ vlc --services-discovery upnp_intel \* or in the
playlist menu: File/Service discovery/UPNP

Then discovered UPNP servers will be listed on the playlist.

=== Options === Note the spelling difference: it is option
satip-channe'''l'''ist and satip-channe'''ll'''ist-url. {{Option
value=string { "Auto", "ASTRA_19_2E", "ASTRA_28_2E", "ASTRA_23_5E",
"MasterList", "ServerList", "CustomList" }]] description=Custom
SAT&gt;IP channel list URL }} {{Option value=string description=Custom
SAT&gt;IP channel list URL }} {{Clear}}

=== upnp === ==== Options ==== None. {{Clear}}

=== upnp_renderer === {{Moduletype=Renderer discoverysc=upnp_renderer}}

==== Options ==== None. {{Clear}}

<!-- Scheduled for 4.0.0-dev: === dlna === {{Moduletype=Stream output]]
stream output|sc=dlna}}

Note that <code>--sout-dlna-base_url</code> uses an underscore
<code>'''_'''</code> rather than a hyphen.

==== Options ==== {{Option value=string description=[[IP
addressname=sout-dlna-port default=NULL name=sout-dlna-http-port
default=7070 name=sout-dlna-video default=enabled
name=sout-dlna-base_url default=NULL name=sout-dlna-url default=NULL
\|description=The Url used to get the xml descriptor of the UPnP
Renderer }} {{Clear}}-->

== <span id="upnp_cc"></span> upnp_cc.cpp == {{Moduletype=Services
discoverydescription=Universal Plug'n'Play|sc=none}}

=== Options === None. {{Clear}}

== Source code == Current: \*
{{VLCSourceFilep=vlc/vlc-0.8.gitp=vlc/vlc-0.9.gitp=vlc/vlc-1.0.gitp=vlc/vlc-1.1.gitp=vlc/vlc-0.8.gitp=vlc/vlc-0.9.gitp=vlc/vlc-1.0.gitp=vlc/vlc-1.1.git|modules/services_discovery/upnp_intel.cpp}}

== Appendix == <span id="appendix_satip-channelist"></span> '''For the
option <code>[[#satip-channelist class="mw-datatable sortable" !
scope="row" \| Option name \| Auto \|\| ASTRA_19_2E \|\| ASTRA_28_2E
\|\| ASTRA_23_5E \|\| MasterList \|\| ServerList \|\| CustomList Meaning
\| Auto \|\| Astra 19.2°E \|\| Astra 28.2°E \|\| Astra 23.5°E \|\|
SAT&gt;IP Main List \|\| Device List \|\| Custom List \|}

{{Documentation}}

{{DEFAULTSORT:{{#titleparts:{{PAGENAME}}2}}|noerror}}<!-- Override
sortkey -->
