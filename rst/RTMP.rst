.. raw:: mediawiki

   {{protocol|RTMP|mod=avio}}

.. raw:: mediawiki

   {{wikipedia|Real Time Messaging Protocol}}

**Real Time Messaging Protocol** (**RTMP**) is a `protocol <protocol>`__ used by `Macromedia Flash <wikipedia:Macromedia_Flash>`__.

.. raw:: mediawiki

   {{clear}}

Compatibility
-------------

VLC supports RTMP and rtmp:// URLs as of version 1.1, through the `avio <Documentation:Modules/avio>`__ module via the libavformat library. In past versions, use of rtmpdump was required in conjunction with VLC, but that is no longer needed after VLC 1.1.x.

URL format
----------

The basic URL format is: rtmp://tcurl/app/playpath

Options
-------

Some options can be used in command line :

============= ===========
Option        Description
============= ===========
rtmp_pageurl 
rtmp_swfurl  
rtmp_swfvfy  
rtmp_live    
rtmp_playpath Playpath
rtmp_app      Application
rtmp_tcurl    ip[:port]
\            
============= ===========

Example
-------

Find the swfurl of the RTMP stream (if required), and place it in the appropriate location below:

``vlc ``\ ```rtmp://10.12.34.56/`` <rtmp://10.12.34.56/>`__\ `` --avio-options "{rtmp_swfurl=``\ ```http://path/to/the.swf`` <http://path/to/the.swf>`__\ ``}"``

See also
--------

-  `SoC_2009/RTMP_Flash_Streaming <SoC_2009/RTMP_Flash_Streaming>`__
-  http://www.osflash.org/rtmp_os

`Category:Protocols <Category:Protocols>`__
