{{Notesection link]])</sup></small> was
[https://git.videolan.org/?p\ {{=}}vlc.git;a{{=}}commitdiff;h{{=}}55280fa62cb68b71767778c56250352b4840b69a
renamed to avahi.c] and
[https://git.videolan.org/?p\ {{=}}vlc.git;a{{=}}commitdiff;h{{=}}1baae638b5759ff092c7977ab17185975f7e6524
bonjour.m was created].}}

None of these modules have options.

== Services discovery == {{Moduletype=Services discoveryos=macOS, tvOS,
iOSBonjour]] Network Discoverysc2=bonjour}} {{Clear}}

=== Renderer discovery === {{Moduletype=Renderer discoveryos=macOS,
tvOS, iOSBonjour]] Renderer Discoverysc2=bonjour_renderer}}

{{Clear}}

The {{Commitdiffl=introduction of this probe}} contains a note: <pre>
Add a bonjour renderer submodule to the bonjour service discovery
module, so it can discover chromecast renderers (for now) and others in
the future. There is still some work needed to make it detect chromecast
capabilities correctly and to not hardcode it to chromecast. (See the
TODO comment) </pre> The TODO comment in the same commit:
<syntaxhighlight lang="c"> // TODO: Detect rendered capabilities and
adapt to work with not just chromecast </syntaxhighlight>

{{Clear}}

== Services discovery (avahi) == {{Moduletype=Services
discoveryos=LinuxZeroconf]] servicessc2=avahi}}

{{Clear}}

=== Renderer discovery (avahi) === {{Moduletype=Renderer
discoveryos=LinuxAvahi]]
[[wikipedia:Zeroconfsc=mdns_renderer|sc2=avahi_renderer}}

The {{Commitdiffl=introduction of this probe}} was not announced; it was
experimental. A stable version
[https://git.videolan.org/?p=vlc.git;a=blob;f=NEWS;h=a90762a649d5bb2b8eba03a68163c10f459c6426;hb=HEAD#l63
is upcoming] (currently scheduled for 4.0.0-dev).

{{Clear}}

== Source code == bonjour.m: \*
{{VLCSourceFilep=vlc/vlc-0.8.gitmodules/services_discovery/avahi.c}}

{{Documentation}}
