.. raw:: mediawiki

   {{Module|name=opensles|type=Audio output|description=OpenSLES audio output|os=Android|first_version=2.1}}

Introduction
------------

This is the latest audio output module found on the `Android <Android>`__ platform. It offers better lipsync than the AudioTrack modules.

Sometimes, however, on recent Android platforms an `Android bug <https://trac.videolan.org/vlc/ticket/9325>`__ might prevent it from functioning well, so in that case trying out the AudioTrack (Java) audio output may be recommended.

Options
-------

None.

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/audio_output/opensles_android.c}}

`Category:Android <Category:Android>`__
