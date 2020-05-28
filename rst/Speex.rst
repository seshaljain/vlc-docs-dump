.. raw:: mediawiki

   {{Codec audio|mod=speex|encoder=y|id=spx|for=[[Ogg]]}}

.. raw:: mediawiki

   {{Website|Speex|https://www.speex.org/}}

.. raw:: mediawiki

   {{Xiph|Speex}}

.. raw:: mediawiki

   {{Open}}

**Speex** is a deprecated speech-oriented audio codec designed for use over packet networks (e.g. `HTTP <HTTP>`__, local network use) and `VoIP <VoIP>`__ applications. As of 2013, Speex.org recommends parties consider `Opus <Opus>`__ instead, calling the Opus codec superior.

It supports `compression <compression>`__ in a `lossy <lossy>`__ way. It uses `CELP <CELP>`__ (Code Excited Linear Prediction) to compress, meaning it takes advantage of the frequency patterns of human speech to efficiently compress data; this also means harmonics that do not follow this pattern will perform poorly (e.g. electronic music). has supported decoding and encoding Speex since version 0.7.0.

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/codec/speex.c}}
