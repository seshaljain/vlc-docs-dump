{\| align="right" \| \__TOC_\_ \|} <!-- really should skip MDC in the
toc, but how? -->

= MDC, the missing manual =

This page contains some hard-won but still incomplete information that
the boys at mozilla conveniently forget to tell you and that may be
useful for developing mozilla plugins (such as our vlc plugin).

== General structure == Netscape Plugin Application Programming
Interface (NPAPI) conforming plugins have a number of entry points that
vary across platforms a bit in number and precise function per entry
point. Those entry points together must mainly do two things: One) tell
the browser what MIME-type(s) this plugin supports, and two) setup two
function pointer tables.

The first table contains pointers to functions inside the browser that
the plugin may call. This table apparently must be copied to local
storage, but I haven't found why. The table necessairily will end up as
a global for the plugin so it may as well be a statically allocated
global, though there is a shutdown entry point to clean up any dynamic
allocations after the last instance is destroyed.

The second table contains pointers to functions the plugin exports to
the browser to call. The browser will create a new instance by calling
the new function pointer for each place in a webpage that the plugin is
needed, and all the other functions will be called with a reference to
such an instance.

Enabling script interaction with the plugin should be done using the
"NPAPI scripting extensions". This can be done by exporting the desired
scripting interfaces through implementing NPObject derivates.

<blockquote>"And we've completely removed support for XPCOM plugins from
Mozilla 1.9.2 (Firefox 3.6).<br>&mdash;<cite>Benjamin Smedberg <!--
<benjamin@smedbergs.us> in
<E8idnZax4IVPNOTXnZ2dnUVZ_gednZ2d@mozilla.org> --> posting in
mozilla.dev.tech.plugins on news.mozilla.org</cite></blockquote>

"XPCOM plugins" may or may not be different from "xulrunner extensions".
Clarification needed.

== development ==

Apparently only a few files are really needed for developing plugins.
According to
[http://colonelpanic.net/2009/05/building-a-firefox-plugin-part-two/
this guy] only 12 files:

-  jni.h
-  jni_md.h
-  jri.h
-  jritypes.h
-  jri_md.h
-  npapi.h
-  npruntime.h
-  nptypes.h
-  npupp.h
-  obsolete/protypes.h
-  prcpucfg.h
-  prtypes.h

So far only two actual includes seem sufficient:

<pre><nowiki> #include <npapi.h> #include <npupp.h> </nowiki></pre>

=== GetValue === The NS_GetValue entry point and the getvalue function
table pointer apparently may point to the same function as long as it
can deal with NULL instance references.

== Compiling ==

Compiling a plugin is a bit sparsely documented but the gist seems to be
to use <code>pkg-config mozilla-plugin</code> and to add a few choice
flags. Thus on linux I have (which may or may not be correct):

<pre><nowiki> PKGCONFIG=pkg-config MOZILLA_PLUGIN_CFLAGS=`$(PKGCONFIG)
--cflags mozilla-plugin\` MOZILLA_PLUGIN_LIBS=`$(PKGCONFIG) --libs
mozilla-plugin\`

CXXFLAGS+=-fno-rtti -fno-exceptions -Wl,-z,defs -shared -O2 -g -DXP_UNIX
-DMOZILLA_STRICT_API $(MOZILLA_PLUGIN_CFLAGS) LDFLAGS+= -shared
-Wl,-Bsymbolic $(MOZILLA_PLUGIN_LIBS)

npplugin.so: npplugin.o
   $(CXX) $(LDFLAGS) $< -o $@

npplugin.o: npplugin.cpp

</nowiki></pre>

== debugging ==

One way to get more useful output out of nspr-based browsers (firefox,
epiphany at least) is to set two environment variables:

   export NSPR_LOG_FILE NSPR_LOG_MODULES NSPR_LOG_FILE=path/to/log/file
   NSPR_LOG_MODULES=modulename:level,modulename:level

However, I have failed to find a comprehensive list of modules to choose
from. &nbsp;<code>all:5</code> works but is perhaps a bit too verbose.
The default for NSPR_LOG_FILE appears to be stderr. On windows the
special ''WinDebug'' which redirects to OutputDebugString().

=== NSPR_LOG_MODULES === {\| class="wikitable" -\| all \| enable all log
modules sync \| enable unbuffered logging timestamp \| prefix log
messages with an UTC timestamp (NSPR 4.8 or later) bufsize'':size'' \|
set the log buffer size nsNativeModuleLoader \| xulrunner/XPCOM
component loading nsHttp \| What the http layer is up to
nsSocketTransport \| Socket stuff nsHostResolver \| DNS queries mime \|
rowspan=6-\| imap nntp smtp pop3 ldap nsRDFService \| RDF service
nsXULTemplateBuilder \| template rule network construction and
subsequent use InMemoryDataSource \| Assert(), Unassert(),
HasAssertion(), etc. for most datasources. nsComponentManager \| XPCOM,
clarification needed MCD \| autoconfig? HelperAppService \| ''save as''
related? negotiateauth \| Found in modauthkerb documentation Plugin \|
rowspan=3\| plugin related. Apparently verbosity goes up to 9? PluginNPP
PluginNPN \|}

== Using ==

The exported JavaScript API is documented in the
[[Documentation:WebPlugin]] page. It is the same for the Mozilla-plugin
and the [[ActiveX/HTML|ActiveX]] component.

[[Category:Coding]][[Category:Building]]
