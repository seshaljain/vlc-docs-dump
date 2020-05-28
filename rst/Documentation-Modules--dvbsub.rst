.. raw:: mediawiki

   {{Module|name=dvbsub|type=Subtitles|first_version=0.8.0|description=[[DVB subtitles]] decoder/encoder}}

.. raw:: mediawiki

   {{Clear}}

There are notes in the source code:

.. code:: c

   /*****************************************************************************
    * Preamble
    *
    * FIXME:
    * DVB subtitles coded as strings of characters are not handled correctly.
    * The character codes in the string should actually be indexes referring to a
    * character table identified in the subtitle descriptor.
    *
    * The spec is quite vague in this area, but what is meant is perhaps that it
    * refers to the character index in the codepage belonging to the language
    * specified in the subtitle descriptor. Potentially it's designed for widechar
    * (but not for UTF-*) codepages.
    *****************************************************************************/

and

.. code:: c

   /*****************************************************************************
    * Notes on DDS (Display Definition Segment)
    * -----------------------------------------
    * DDS (Display Definition Segment) tells the decoder how the subtitle image
    * relates to the video image.
    * For SD, the subtitle image is always considered to be for display at
    * 720x576 (although it's assumed that for NTSC, this is 720x480, this
    * is not documented well) Also, for SD, the subtitle image is drawn 'on
    * the glass' (i.e. after video scaling, letterbox, etc.)
    * For 'HD' (subs marked type 0x14/0x24 in PSI), a DDS must be present,
    * and the subs area is drawn onto the video area (scales if necessary).
    * The DDS tells the decoder what resolution the subtitle images were
    * intended for, and hence how to scale the subtitle images for a
    * particular video size
    * i.e. if HD video is presented as letterbox, the subs will be in the
    * same place on the video as if the video was presented on an HD set
    * indeed, if the HD video was pillarboxed by the decoder, the subs may
    * be cut off as well as the video. The intent here is that the subs can
    * be placed accurately on the video - something which was missed in the
    * original spec.
    *
    * A DDS may also specify a window - this is where the subs images are moved so that the (0,0)
    * origin of decode is offset.
    ********************************************************************************************/

Options
-------

.. raw:: mediawiki

   {{Option
   |name=dvbsub-position<span id="dvbsub-position"></span>
   |value=integer
   |select={ 0, 1, 2, 4, 8, 5, 6, 9, 10 }
   |description=Subpicture position<sup>('''[[#appendix_dvbsub-position|key]]''')</sup>
   }}

.. raw:: mediawiki

   {{Option
   |name=dvbsub-x
   |value=integer
   |default=-1
   |description=X coordinate of the rendered subtitle
   }}

.. raw:: mediawiki

   {{Option
   |name=dvbsub-y
   |value=integer
   |default=-1
   |description=Y coordinate of the rendered subtitle
   }}

Encoder
~~~~~~~

.. raw:: mediawiki

   {{Option
   |name=sout-dvbsub-x
   |value=integer
   |default=-1
   |description=X coordinate of the encoded subtitle
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-dvbsub-y
   |value=integer
   |default=-1
   |description=Y coordinate of the encoded subtitle
   }}

.. raw:: mediawiki

   {{Clear}}

Appendix
--------

.. raw:: html

   <div class="plainlist">

-  ^ `--dvbsub-position <#dvbsub-position>`__\ 

.. raw:: html

   </div>

.. raw:: mediawiki

   {{Alignment mapping}}

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/codec/dvbsub.c}}

.. raw:: mediawiki

   {{Documentation footer}}
