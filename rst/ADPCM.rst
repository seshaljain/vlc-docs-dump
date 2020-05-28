\__FORCETOC_\_ **ADPCM** or **Adaptive Differential PCM** is a variant of `PCM <PCM>`__.

FourCC
------

This codec is known by the following `FourCCs <FourCC>`__. The ones in hex code (e.g. ``ms 0x00 0x02``) `cannot be represented conventionally <wikipedia:Control_character>`__. Omit any spaces when typing (e.g. [``xa  ``] is just ``xa``):

=========================== ==================
Internal name               FourCC
=========================== ==================
VLC_CODEC_ADPCM_4XM         [``4xma``]
VLC_CODEC_ADPCM_EA          [``ADEA``]
VLC_CODEC_ADPCM_XA          [``xa  ``]
VLC_CODEC_ADPCM_ADX         [``adx ``]
VLC_CODEC_ADPCM_IMA_WS      [``AIWS``]
VLC_CODEC_ADPCM_G722        [``g722``]
VLC_CODEC_ADPCM_G726        [``g726``]
VLC_CODEC_ADPCM_SWF         [``SWFa``]
VLC_CODEC_ADPCM_MS          [``ms 0x00 0x02``]
VLC_CODEC_ADPCM_IMA_WAV     [``ms 0x00 0x11``]
VLC_CODEC_ADPCM_IMA_AMV     [``imav``]
VLC_CODEC_ADPCM_IMA_QT      [``ima4``]
VLC_CODEC_ADPCM_YAMAHA      [``ms 0x00 0x20``]
VLC_CODEC_ADPCM_DK3         [``ms 0x00 0x62``]
VLC_CODEC_ADPCM_DK4         [``ms 0x00 0x61``]
VLC_CODEC_ADPCM_CREATIVE    [``ms 0x00 0xC0``]
VLC_CODEC_ADPCM_SBPRO_2     [``ms 0x00 0xC2``]
VLC_CODEC_ADPCM_SBPRO_3     [``ms 0x00 0xC3``]
VLC_CODEC_ADPCM_SBPRO_4     [``ms 0x00 0xC4``]
VLC_CODEC_ADPCM_THP         [``THPA``]
VLC_CODEC_ADPCM_XA_EA       [``XAJ0``]
VLC_CODEC_ADPCM_IMA_EA_SEAD [``SEAD``]
VLC_CODEC_ADPCM_EA_R1       [``EAR1``]
VLC_CODEC_ADPCM_IMA_APC     [``AIPC``]
=========================== ==================

Source code
-----------

.. raw:: mediawiki

   {{file|modules/codec/adpcm.c|audio codec}}

.. raw:: mediawiki

   {{file|include/vlc_fourcc.h|FourCC definitions - you will have to search for <code>ADPCM</code>}}
