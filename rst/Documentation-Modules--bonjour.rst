.. raw:: mediawiki

   {{Note|Past versions of VLC may refer to a different module as bonjour:<br />with VLC 3.0.0 the old bonjour.c module<small><sup class{{=}}

"noprint">(`section link <#Services_discovery_(avahi)>`__) was [https://git.videolan.org/?p\ {{=}}vlc.git;a{{=}}commitdiff;h{{=}}55280fa62cb68b71767778c56250352b4840b69a renamed to avahi.c] and [https://git.videolan.org/?p\ {{=}}vlc.git;a{{=}}commitdiff;h{{=}}1baae638b5759ff092c7977ab17185975f7e6524 bonjour.m was created].}}

None of these modules have options.

Services discovery
------------------

.. raw:: mediawiki

   {{Module|name=bonjour.m|type=Services discovery|first_version=3.0.0|os=macOS, tvOS, iOS|description=[[wikipedia:Bonjour (software)|Bonjour]] Network Discovery|sc=mdns|sc2=bonjour}}

.. raw:: mediawiki

   {{Clear}}

Renderer discovery
~~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Module|name=bonjour.m|type=Renderer discovery|first_version=3.0.0|os=macOS, tvOS, iOS|description=[[wikipedia:Bonjour (software)|Bonjour]] Renderer Discovery|sc=mdns_renderer|sc2=bonjour_renderer}}

.. raw:: mediawiki

   {{Clear}}

The contains a note:

::

   Add a bonjour renderer submodule to the bonjour service discovery
   module, so it can discover chromecast renderers (for now) and others
   in the future.
   There is still some work needed to make it detect chromecast
   capabilities correctly and to not hardcode it to chromecast.
   (See the TODO comment)

The TODO comment in the same commit:

.. code:: c

   // TODO: Detect rendered capabilities and adapt to work with not just chromecast

.. raw:: mediawiki

   {{Clear}}

Services discovery (avahi)
--------------------------

.. raw:: mediawiki

   {{Module|name=avahi.c|type=Services discovery|first_version=0.8.4|os=Linux|description=[[wikipedia:Zeroconf|Zeroconf]] services|sc=mdns|sc2=avahi}}

.. raw:: mediawiki

   {{Clear}}

Renderer discovery (avahi)
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Module|name=avahi_renderer.c|type=Renderer discovery|first_version=1.0.4|os=Linux|description=[[wikipedia:Avahi (software)|Avahi]] [[wikipedia:Zeroconf|Zeroconf]] renderer Discovery|sc=mdns_renderer|sc2=avahi_renderer}}

The was not announced; it was experimental. A stable version `is upcoming <https://git.videolan.org/?p=vlc.git;a=blob;f=NEWS;h=a90762a649d5bb2b8eba03a68163c10f459c6426;hb=HEAD#l63>`__ (currently scheduled for 4.0.0-dev).

.. raw:: mediawiki

   {{Clear}}

Source code
-----------

bonjour.m:

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/services_discovery/bonjour.m}}

bonjour.c/avahi.c:

-  

   .. raw:: mediawiki

      {{VLCSourceFile|p=vlc/vlc-0.8.git|modules/services_discovery/bonjour.c}}

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/services_discovery/avahi.c}}

.. raw:: mediawiki

   {{Documentation}}
