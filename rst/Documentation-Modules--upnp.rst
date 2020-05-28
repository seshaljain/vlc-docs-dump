| Prior to VLC 2.0.0 the `UPnP <wikipedia:UPnP>`__ module had 2 files: upnp_cc (for `CyberLink <wikipedia:CyberLink>`__) and upnp_intel (for `Intel <wikipedia:Intel_Corporation>`__).
| The upnp_cc file was and the upnp_intel file was to upnp.

 upnp.cpp
--------

.. raw:: mediawiki

   {{Module|name=upnp|type=Services discovery|first_version=0.8.4|description=[[wikipedia:Universal Plug'n'Play|Universal Plug'n'Play]]|sc=none}}

When VLC is compiled with UPNP support, you will still need to enable UPNP service discovery:

-  either on command line via $ vlc --services-discovery upnp_intel
-  or in the playlist menu: File/Service discovery/UPNP

Then discovered UPNP servers will be listed on the playlist.

Options
~~~~~~~

Note the spelling difference: it is option satip-channe\ **l**\ ist and satip-channe\ **ll**\ ist-url.

upnp
~~~~

.. _options-1:

Options
^^^^^^^

None.

upnp_renderer
~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Module|name=upnp_renderer|type=Renderer discovery|description=UPnP Renderer Discovery|sc=upnp_renderer}}

.. _options-2:

Options
^^^^^^^

None.

 upnp_cc.cpp
-----------

.. raw:: mediawiki

   {{Module|name=UPnP|type=Services discovery|last_version=1.1.?|description=Universal Plug'n'Play|sc=none}}

.. _options-3:

Options
~~~~~~~

None.

Source code
-----------

Current:

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/services_discovery/upnp.cpp}}

Former:

-  

   .. raw:: mediawiki

      {{VLCSourceFile|p=vlc/vlc-0.8.git|modules/services_discovery/upnp_cc.cpp}}

-  

   .. raw:: mediawiki

      {{VLCSourceFile|p=vlc/vlc-0.9.git|modules/services_discovery/upnp_cc.cpp}}

-  

   .. raw:: mediawiki

      {{VLCSourceFile|p=vlc/vlc-1.0.git|modules/services_discovery/upnp_cc.cpp}}

-  

   .. raw:: mediawiki

      {{VLCSourceFile|p=vlc/vlc-1.1.git|modules/services_discovery/upnp_cc.cpp}}

-  

   .. raw:: mediawiki

      {{VLCSourceFile|p=vlc/vlc-0.8.git|modules/services_discovery/upnp_intel.cpp}}

-  

   .. raw:: mediawiki

      {{VLCSourceFile|p=vlc/vlc-0.9.git|modules/services_discovery/upnp_intel.cpp}}

-  

   .. raw:: mediawiki

      {{VLCSourceFile|p=vlc/vlc-1.0.git|modules/services_discovery/upnp_intel.cpp}}

-  

   .. raw:: mediawiki

      {{VLCSourceFile|p=vlc/vlc-1.1.git|modules/services_discovery/upnp_intel.cpp}}

Appendix
--------

**For the option**\ ```--satip-channelist`` <#satip-channelist>`__\ **:**

=========== ==== ============ ============ ============ ================ =========== ===========
Option name Auto ASTRA_19_2E  ASTRA_28_2E  ASTRA_23_5E  MasterList       ServerList  CustomList
=========== ==== ============ ============ ============ ================ =========== ===========
Meaning     Auto Astra 19.2°E Astra 28.2°E Astra 23.5°E SAT>IP Main List Device List Custom List
=========== ==== ============ ============ ============ ================ =========== ===========

.. raw:: mediawiki

   {{Documentation}}

.. raw:: mediawiki

   {{DEFAULTSORT:{{#titleparts:{{PAGENAME}}|0|2}}

\|noerror}}
