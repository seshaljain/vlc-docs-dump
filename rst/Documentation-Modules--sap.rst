{{Moduletype=Services discoverydescription=Network streams ([[SAP]])}}
This module will listen on [[port]] 9875 for SAP announcements. The
option <code>--sap-timeshift</code> has been deprecated since 1.0.0
(redundant). Options <code>--sap-ipv4</code> and <code>--sap-ipv6</code>
have been deprecated since 2.0.0.

== Options == {{Option value=string description=The SAP module normally
chooses itself the right addresses to listen to. However, you can
specify a specific address }} {{Option value=integer description=Delay
after which SAP items get deleted if no new announcement is received }}
{{Option value=boolean live555}}" (RTP/RTSP) module name=sap-strict
description=When this is set, the SAP parser will discard some
non-compliant announcements \|default=disabled }}

== Sub-module == {{Moduletype=Services discoverysc=sdp}}

=== Options === None. {{Clear}}

== Source code == \* {{VLCSourceFile|modules/services_discovery/sap.c}}

{{Documentation}}
