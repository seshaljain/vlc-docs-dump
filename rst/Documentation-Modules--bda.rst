.. raw:: mediawiki

   {{Module|name=bda|type=Access|first_version=0.9.0|last_version=1.1.?|os=Windows|description=DirectShow [[wikipedia:Broadcast Driver Architecture|BDA]] input}}

This module was superseded by sometime between 1.1 and 2.0.

The `options for this module were conditional <wikipedia:C_preprocessor#Conditional_compilation>`__ upon the presence of either macro ``WIN32`` (Windows 32-bit) or ``WINCE`` (Windows CE), indicating that the target was a Windows system:

.. code:: c

   # if defined(WIN32) || defined(WINCE)
    // Condition: Windows
   # else
    // Condition: Other
   # endif

Shortcuts to this module were ```dvb`` <dvb>`__, ``dvb-s``, ``dvbs``, ``qpsk``, ``satellite``, ``dvb-c``, ``dvbc``, ``qam``, ``cable``, ``dvbt``, ``dvb-t``, ``ofdm``, ``terrestrial``, ``atsc`` and ``usdigital``.

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFolder|p=vlc/vlc-1.1.git|modules/access/bda}}

-  

   .. raw:: mediawiki

      {{VLCSourceFile|p=vlc/vlc-1.1.git|a=blob|modules/access/bda/bda.c}}

.. raw:: mediawiki

   {{Documentation}}
