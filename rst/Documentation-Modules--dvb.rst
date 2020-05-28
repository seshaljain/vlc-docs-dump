.. raw:: mediawiki

   {{See also|Documentation:Modules/dtv}}

.. raw:: mediawiki

   {{Module|name=dvb|type=Access|first_version=0.6.2|os=Linux|description=[[DVB]] input with [[v4l2]] support|sc=dvb}}

Shortcuts:

-  ``dvb`` (Generic name)

   -  ``dvb-s``, ``qpsk``, ``satellite`` (Satellite)
   -  ``dvb-c``, ``cable`` (Cable)
   -  ``dvb-t``, ``terrestrial`` (Terrestrial)

Options
-------

.. raw:: mediawiki

   {{Option
   |name=dvb-probe
   |value=boolean
   |default=enabled
   |description=Some [[DVB]] cards do not like to be probed for their capabilities, you can disable this feature if you experience some trouble.
   }}

.. raw:: mediawiki

   {{Option
   |name=dvb-satellite
   |value=string
   |default=NULL
   |description=Filename of config file in share/dvb/dvb-s.
   }}

.. raw:: mediawiki

   {{Option
   |name=dvb-scanlist
   |value=string
   |default=NULL
   |description=Filename containing initial scan tuning data.
   }}

.. raw:: mediawiki

   {{Option
   |name=dvb-scan-nit
   |value=boolean
   |default=enabled
   |description=Use NIT for scanning services
   }}

See also
--------

-  

   .. raw:: mediawiki

      {{docmod|dvbsub}}

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/access/dvb/access.c}}

   (main file)

-  

   .. raw:: mediawiki

      {{VLCSourceFolder|modules/access/dvb}}

   (folder)

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/demux/playlist/dvb.c}}

   (LinuxTV channels list, part of )

.. raw:: mediawiki

   {{Documentation}}
