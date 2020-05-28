.. raw:: mediawiki

   {{Module|name=dshow|type=Access demux|first_version=0.7.0|os=Windows|description=[[wikipedia:DirectShow|DirectShow]] input}}

Options
-------

.. raw:: mediawiki

   {{Option
   |name=dshow-vdev
   |value=string
   |default=NULL
   |description=Name of the video device that will be used by the DirectShow plugin. If you don't specify anything, the default device will be used
   }}

.. raw:: mediawiki

   {{Option
   |name=dshow-adev
   |value=string
   |default=NULL
   |description=Name of the audio device that will be used by the DirectShow plugin. If you don't specify anything, the default device will be used
   }}

.. raw:: mediawiki

   {{Option
   |name=dshow-size
   |value=string
   |default=NULL
   |description=Size of the video that will be displayed by the DirectShow plugin. If you don't specify anything the default size for your device will be used. You can specify a standard size (cif, d1, ...) or <width>x<height>
   }}

.. raw:: mediawiki

   {{Option
   |name=dshow-aspect-ratio
   |value=string
   |default=4:3
   |description=Define input picture [[aspect ratio]] to use. Default is 4:3
   }}

.. raw:: mediawiki

   {{Option
   |name=dshow-chroma
   |value=string
   |default=NULL
   |description=Force the DirectShow video input to use a specific chroma format (eg. [[I420]] (default), RV24, etc.)
   }}

.. raw:: mediawiki

   {{Option
   |name=dshow-fps
   |value=float
   |default=0.0f
   |description=Force the DirectShow video input to use a specific [[frame rate]] (eg. 0 means default, 25, 29.97, 50, 59.94, etc.)
   }}

.. raw:: mediawiki

   {{Option
   |name=dshow-config
   |value=boolean
   |default=disabled
   |description=Show the properties dialog of the selected device before starting the stream
   }}

.. raw:: mediawiki

   {{Option
   |name=dshow-tuner
   |value=boolean
   |default=disabled
   |description=Show the tuner properties [channel selection] page
   }}

.. raw:: mediawiki

   {{Option
   |name=dshow-tuner-channel
   |value=integer
   |default=0
   |description=Set the TV channel the tuner will set to (0 means default)
   }}

.. raw:: mediawiki

   {{Option
   |name=dshow-tuner-country
   |value=integer
   |default=0
   |description=Set the tuner country code that establishes the current channel-to-frequency mapping (0 means default)
   }}

.. raw:: mediawiki

   {{Option
   |name=dshow-tuner-input
   |value=integer
   |default=0
   |select={0,1,2}
   |description=Select the tuner input type (Default/Cable/Antenna)
   }}

.. raw:: mediawiki

   {{Option
   |name=dshow-video-input
   |value=integer
   |default=-1
   |description=Select the video input source, such as composite, s-video, or tuner. Since these settings are hardware-specific, you should find good settings in the "Device config" area, and use those numbers here. -1 means that settings will not be changed
   }}

.. raw:: mediawiki

   {{Option
   |name=dshow-video-output
   |value=integer
   |default=-1
   |description=Select the video output type. See the "video input" option
   }}

.. raw:: mediawiki

   {{Option
   |name=dshow-audio-input
   |value=integer
   |default=-1
   |description=Select the audio input source. See the "video input" option
   }}

.. raw:: mediawiki

   {{Option
   |name=dshow-audio-output
   |value=integer
   |default=-1
   |description=Select the audio output type. See the "video input" option
   }}

.. raw:: mediawiki

   {{Option
   |name=dshow-amtuner-mode
   |value=integer
   |default=<var>AMTUNER_MODE_TV</var>
   |select={0,1,2,3,4}
   |description=AM Tuner mode. Can be one of Default (0), TV (1), AM Radio (2), FM Radio (3) or DSS (4)
   }}

.. raw:: mediawiki

   {{Option
   |name=dshow-audio-channels
   |value=integer
   |default=0
   |description=Select audio input format with the given number of audio channels (if non 0)
   }}

.. raw:: mediawiki

   {{Option
   |name=dshow-audio-samplerate
   |value=integer
   |default=0
   |description=Select audio input format with the given [[sample rate]] (if non 0)
   }}

.. raw:: mediawiki

   {{Option
   |name=dshow-audio-bitspersample
   |value=integer
   |default=0
   |description=Select audio input format with the given bits/sample (if non 0)
   }}

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/access/dshow/dshow.cpp}}

-  

   .. raw:: mediawiki

      {{VLCSourceFolder|modules/access/dshow}}

.. raw:: mediawiki

   {{Documentation footer}}
