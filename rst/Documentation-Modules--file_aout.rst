.. raw:: mediawiki

   {{Module|name=afile|type=Audio output|description=Audio output to write to a file}}

Shortcuts for this module include ``audiofile`` and ``afile``.

Options
-------

.. raw:: mediawiki

   {{Option
   |name=audiofile-file
   |value=string
   |default=audiofile.wav
   |description=File to which the audio samples will be written to ("-" for stdout)
   }}

.. raw:: mediawiki

   {{Option
   |name=audiofile-format
   |select={u8,s16,float32,spdif}
   |default=s16
   |description=Output format
   }}

.. raw:: mediawiki

   {{Option
   |name=audiofile-channels
   |value=integer
   |min=0
   |max=6
   |default=0
   |description=By default (0), all the channels of the incoming will be saved but you can restrict the number of channels here
   }}

.. raw:: mediawiki

   {{Option
   |name=audiofile-wav
   |value=boolean
   |description=Instead of writing a raw file, you can add a WAV header to the file
   |default=enabled
   }}

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/audio_output/file.c}}

.. raw:: mediawiki

   {{Documentation}}
