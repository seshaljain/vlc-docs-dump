.. raw:: mediawiki

   {{Back to|Hacker Guide}}

Description
-----------

An audio output module is used to pass decoded audio frames to the audio output hardware. Normally, the audio frames contain an integral number of audio samples coded linearly, i.e. `PCM <wikipedia:Pulse-code_modulation>`__. However, to address the need for digital audio pass-through, the audio output may also receive coded audio frames encapsulated as `S/PDIF <wikipedia:S/PDIF>`__ packets.

This describes the fourth version of the audio output layer, found in `VLC <VLC>`__ version 1.2.0. Versions 0.5.0 to 1.1.x were based on a partly similar but nevertheless incompatible interface known as aout3.

Writing an audio output module
------------------------------

For more details on writing modules in general, see `{{#rel2abs:../How To Write a Module}} <{{#rel2abs:../How_To_Write_a_Module}}>`__. An audio output module should be declared with the correct capability and category as follows:

.. code:: c

    set_capability("audio output", 60)
    set_category(CAT_AUDIO)
    set_subcategory(SUBCAT_AUDIO_AOUT)
    set_callbacks(Open, Close)

(Note: The callbacks name can be different. We use Open() and Close() in this example.)

Instances of an audio output module should store their private internal state (if any) as an aout_sys_t structure:

.. code:: c

    struct aout_sys_t
    {
        /* ... */
    };

Priority
~~~~~~~~

Unless a specific module has been provisioned in the VLC preferences, or specified through the --aout command line parameter, `LibVLC <LibVLC>`__ will try to each audio output module in order of decreasing priority until one succeeds. As usual modules with a priority of zero will never be probed unless configured explicitly.

Thus, on `Linux <Linux>`__ for instance, the `PulseAudio <Documentation:Modules/pulse>`__ module has a higher priority than the `ALSA <Documentation:Modules/alsa>`__ one, and the `OSS <Documentation:Modules/oss>`__ module has the smallest (non-zero) priority. The file audio output has zero priority and will not be used normally. This is so that VLC uses PulseAudio if available, otherwise ALSA, otherwise OSS.

Initialization
--------------

The audio output will be probed and initialized with the typical Open() callback. The audio output should check the input audio format in audio_output_t.format:

.. code:: c

    static int Open (vlc_object_t *obj)
    {
        audio_output_t *aout = (audio_output_t *)obj;
        aout_sys_t *sys;
        
        /* Check input format */
        vlc_fourcc_t format = aout->format.i_format;
        unsigned samplerate = aout->format.i_rate;
        unsigned channels = aout_FormatNbChannels(&aout->format);
        
        /* Initialize audio subsystem */ 
        sys = malloc (sizeof (*sys));
        if (unlikely(sys == NULL))
            return VLC_ENOMEM;
        /* ... */
        if (failure)
        {
            free (sys);
            return VLC_EGENERIC;
        }
        
        /* Adjust format to stereo */
        aout->format.i_original_channels =
        aout->format.i_physical_channels = AOUT_CHAN_LEFT|AOUT_CHAN_RIGHT;
        /* aout->format.i_format = VLC_CODEC_S16N; */
        /* aout->format.i_rate = 48000; */
        
        /* Setup callbacks */
        aout->sys = sys;
        aout->pf_play = Play;
        aout->pf_pause = Pause;
        aout->pf_flush = Flush;
        aout_VolumeSoftInit (aout);
        return VLC_SUCCESS;
    }

When done, the audio output module will be deinitialized:

.. code:: c

    static void Close (vlc_object_t *obj)
    {
        audio_output_t *aout = (audio_output_t)obj;
        aout_sys_t *sys = aout->sys;
        
        /* Deinitialize */
        /* ... */
        
        free (sys);
    }

Audio format
~~~~~~~~~~~~

The initial format when Open() starts, is usually VLC_CODEC_FL32 (float) on desktop systems, but not always. All formats are implicitly channel-interleaved. Uninterleaved audio is never used. For instance, stereo audio is ordered as:

-  first left channel value,
-  first right channel value,
-  second left channel value,
-  second right channel value,
-  etc.

Currently, the following formats are supported:

================ ====================== =================== ========== ====================== ================
FOURCC           Description            `C Type <C_Type>`__ Endianness On entry               On return
================ ====================== =================== ========== ====================== ================
VLC_CODEC_FL32   Single precision       float               Native     With FPU               Allowed
VLC_CODEC_FI32   Fixed-point            int32_t             Native     Without FPU            Forbidden
VLC_CODEC_S16N   Signed 16-bits         int16_t             Native     Without FPU            Allowed
VLC_CODEC_F32L   Single precision       float               Little     With little endian FPU Allowed
VLC_CODEC_F32B   Single precision       float               Big        With big endian FPU    Allowed
VLC_CODEC_F64L   Double precision       double              Little     Never                  Allowed
VLC_CODEC_F64B   Double precision       double              Big        Never                  Allowed
VLC_CODEC_S16L   Signed 16-bits         int16_t             Little     Without FPU            Allowed
VLC_CODEC_S16B   Signed 16-bits         int16_t             Big        Without FPU            Allowed
VLC_CODEC_S24L   Signed 24-bits         N/A                 Little     Never                  Allowed
VLC_CODEC_S24B   Signed 24-bits         N/A                 Big        Never                  Allowed
VLC_CODEC_S32L   Signed 32-bits         int32_t             Little     Never                  Allowed
VLC_CODEC_S32B   Signed 32-bits         int32_t             Big        Never                  Allowed
VLC_CODEC_A52    AC-3 / Dolby           Non-linear          N/A        A52 input              Forbidden
VLC_CODEC_DTS    DTS Coherent Acoustics Non-linear          N/A        DTS input              Forbidden
VLC_CODEC_MPGA   MPEG 2 Audio           Non-linear          N/A        MPEG input             Forbidden
VLC_CODEC_SPDIFL S/PDIF                 uint16_t            Little     Never                  Allowed (S/PDIF)
VLC_CODEC_SPDIFB S/PDIF                 uint16_t            Big        Never                  Allowed (S/PDIF)
================ ====================== =================== ========== ====================== ================

The "on entry" column indicates in which situation (if any), the format may be presented by the LibVLC core to the audio output Open() callback. The "on return" column determines if the format is supported for actual output.

If the returned format differs from the one specified by LibVLC core upon entry, then LibVLC will insert any required conversion filter automatically. So **do not convert manually** in the output module!

S/PDIF
^^^^^^

If **and only if** the format on entry is non-linear, the audio output module can enable digital pass-through mode. To do so, it must set the audio output format to VLC_CODEC_SPDIFL (or VLC_CODEC_SPDIFB). If on the contrary pass-through is not to be used, then the format must be set to a linear FOURCC, usually VLC_CODEC_FL32 or VLC_CODEC_S16N.

Convenience aliases
^^^^^^^^^^^^^^^^^^^

VLC_CODEC_FL32 is an alias for VLC_CODEC_F32L or VLC_CODEC_F32B depending on architecture endianness. The full list of convenience native endianness FOURCC is

-  VLC_CODEC_FL32 (float)
-  VLC_CODEC_FL64 (double)
-  VLC_CODEC_S32N (int32_t)
-  VLC_CODEC_S24N (N/A)
-  VLC_CODEC_S16N (int16_t)
-  VLC_CODEC_U16N (uint16_t)

Sample rate and channels
~~~~~~~~~~~~~~~~~~~~~~~~

The sample rate is the sample rate that comes from the decoder or the audio filters, so is the channel mapping.

If possible, it is recommended that the audio output uses a format as close to the input as possible. This is to conversion and loss of quality. Nevertheless, it is often necessary to use different a output format due to hardware limitation:

-  resample if the aout->format.i_rate is modified,
-  remix the channels if aout->format.i_physical_channels and/or aout->format.i_original_channels are modified,
-  convert the sample format is aout->format.i_format is modified.

Warning
~~~~~~~

Beware that the Open() callback **must not change** aout->format until it is absolutely certain to return VLC_SUCCESS (0). If it were to change the format and then return an initialization failure, subsequent modules would get corrupt information about the input format!

Playback
--------

Implementation of the audio_output_t.pf_play callback is mandatory. The LibVLC core will invoke the callback once per audio data block:

.. code:: c

    static void Play (audio_output_t *aout, block_t *block)
    {
        const void *data = block->p_buffer; /* Pointer to audio data */
        size_t datalen = block->i_buffer; /* Byte size of audio data */
        unsigned samples = block->i_nb_samples; /* Number of samples in the block */
        /* NOTE: For linear formats:
          datalen = samples * channels * aout_FormatBitsPerSample(&aout->format) */
        
        /* Queue the block in some platform-speific buffer */
        /* ... */
        
        block_Release (block); /* release memory */
    }

The number of samples in an audio block depends on the particular audio decoder, input format. It might also be altered by some audio filters.

In the example above, the block is destroyed synchronously, but this is not mandatory. block_Release() is thread-safe. If you need to retain the audio data longer, you may call block_Release() later asynchronously.

Lip synchronization
~~~~~~~~~~~~~~~~~~~

Each block has a timestamp and a duration. In most cases, the timestamp will be equal to the sum of previous block's timestamp and the previous block's length. The timestamp and duration are expressed in microseconds. If the sample rate is not a divisor of 1000000, the LibVLC core will automatically adjust the length so that rounding errors do not cause long term drift.

.. code:: c

        /* Time the sample should be physically rendered: */
        mtime_t pts = block->i_pts;
        /* Current time */
        mtime_t now = mdate();
        /* Block duration */
        mtime_t length = block->i_length;
        
        /* Estimate hardware latency */
        /* ... */
        
        /* Report timing to LibVLC core */
        aout_TimeReport (aout, block->i_pts - latency);

The audio output module is responsible for synchronization. aout_TimeReport() notifies the LibVLC of the effective current time of the audio output. The latency value must be obtained from the underlying audio subsystem; the details will vary depending on the subsystem. The time report will trigger upsampling or downsampling if desynchronization is above a certain threshold. That situation commonly occurs when the audio hardware clock and the input media timing do not have perfectly identical clock rates.

Use of aout_TimeReport() is optional. Some audio output modules implement their own mechanism to compensate desynchronization:

-  the PulseAudio output module asks the PulseAudio server to resample instead,
-  the file output module does not care about time synchronization at all.

However, for real audio outputs, some form of **synchronization is absolutely required**. Without it, there would be no lip synchronization when playing videos. Therefore sound output interfaces without any mechanism to estimate latency should be avoided (e.g. SDL audio, libao).

Pause / Resume
--------------

When playback is paused, the audio output needs to be notified so that it can mute the sound as soon as possible. To that end, the audio output module should provide the audio_output_t.pf_pause callback:

.. code:: c

    static void Pause (audio_output_t *aout, bool pause, mtime_t pts)
    {
        if (pause)
        {
            /* Pause playback immediately */
        }
        else
        {
            /* Resume playback from where it was paused previously */
        }
    }

This callback is optional, and can be NULL. If pause were not implemented, audio playback would continue until the underlying audio buffer underruns. This would sound *amateurish* especially when large caching buffers are used (VLC 1.2 allows up to 2 seconds).

Parameters
~~~~~~~~~~

The LibVLC core warrants that the *pause* boolean parameter is always toggled. It is always true the first time Pause() is invoked, always false the second time and so on. *pts* is the time the pause ro resume action was triggered; it should be in the *recent* past with respect to *mdate()*.

Note
~~~~

Resuming occurs when the input playback is resumed from paused state. This is totally unrelated to suspend and/or power management features exposed by some hardware. The audio output module is responsible for dealing with power management internally on its own.

Flush / Drain
-------------

When playback is stopped, pending audio buffers should be discarded as soon as possible. Conversely, when the end of a stream is reached, the audio buffers must be drained to avoid cropping. The optional audio_output_t.pf_flush callback deals with this:

.. code:: c

    static void Flush (audio_output_t *aout, bool wait)
    {
        if (wait)
        {
            /* Wait for buffers to be drained */
        }
        else
        {
            /* Flush (discard) buffers */
        }
    }

Volume management
-----------------

Depending on the capability of the underlying subsystem, LibVLC provides three modes of volume (amplification)

-  Software volume/amplification: the LibVLC core applies volume internally.
-  *Hardware* volume/amplification: the audio output applies volume by whatever means appropriate.
-  No volume/amplification.

For S/PDIF pass-through, software volume is evidently not supported.

The audio output module needs to select the correct volume management mode in the Open() callback. It should call one of the following functions:

-  aout_VolumeSoftInit(aout) for LibVLC software volume,
-  aout_VolumeHardInit(aout, VolumeSet) for "hardware" volume,
-  aout_VolumeNoneInit(aout) to turn off volume.

Hardware volume
~~~~~~~~~~~~~~~

When hardware mode is selected, LibVLC will invoke the following callback to change the volume:

.. code:: c

    static void VolumeSet(audio_output_t *aout, float volume, bool muted)
    {
        /* ...*/
    }

-  **aout** is the audio output instance.
-  **volume** is a float (0.0f = 0% volume, 1.0f = 100% volume, 2.0f = 200% volume).
-  **muted** is true if muted.

If the volume is modified asynchronously outside of LibVLC, the audio output module can notify LibVLC. This enables the VLC UI to show the correct value:

.. code:: c

    aout_VolumeHardSet(aout, volume, muted);

Mute
^^^^

The mute flag is independent from the volume. This allows the UI to separate the mute control from the saved volume level.

Output device selection
-----------------------

Run-time
~~~~~~~~

While audio is playing back, the user interface will look for an "audio-device" `VLC object variable <{{#rel2abs:../Variables}}>`__ on the audio_output_t object to hold the current output device and available output devices. If the variable does not exist, then the audio device selection will be grayed out.

Configuration
~~~~~~~~~~~~~

For persistent settings, and when audio is not playing, a normal configuration item should be declared in the plugin descriptor. Conventionally, the name is "XXX-audio-device" where XXX is the name of the output module, e.g. for `ALSA <ALSA>`__:

.. code:: c

        add_string ("alsa-audio-device", "default", N_("ALSA device"), NULL, false)
            change_string_list (alsa_devices, alsa_devices_text, NULL)

If however the underlying subsystem provides its own (per-application) settings, as is the case for `PulseAudio <PulseAudio>`__, there should not be any persistent configuration item. It would be redundant.

.. raw:: mediawiki

   {{Hacker_Guide}}

`Category:Pages to check <Category:Pages_to_check>`__
