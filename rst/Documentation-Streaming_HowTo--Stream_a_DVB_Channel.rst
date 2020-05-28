.. raw:: mediawiki

   {{RightMenu|documentation streaming howto toc}}

Note: This is possible under GNU/Linux only.

Install the DVB drivers
-----------------------

If you want to be able to stream from a DVB card (a satellite card or a digital terrestial TV card), you need to install the DVB drivers:

-  if you use a Linux 2.6.x kernel, you just need to select the right modules in your kernel configuration.
-  if you use a dvb-card Technisat SkyStar2 rev. 2.8, you must download the latest release of the DVB drivers from the `DVB-S(S2) drivers for Linux <http://mercurial.intuxication.org/hg/s2-liplianin/>`__.
-  if you are using a Linux 2.4.x kernel, you must download the latest release of the DVB drivers from the `DVB drivers download page <http://www.linuxtv.org/download/dvb/>`__ of the `LinuxTV <http://www.linuxtv.org/>`__ Project.

The following sections assume that you have a working linux-dvb installation, either from stock kernel 2.6 or from kernel 2.4 with DVB patches. If you have any problem with the linux-dvb drivers, please report the problem to the maintainers of the drivers, not to us. Thanks.

Stream with VLS
---------------

Note: VLS is currently deprecated and hasn't been maintained for years. It is strongly advised to use VLC instead, which now supports the same features as VLS, and many more. The only advantage of VLS is to support the dvbrc file syntax, and it requires a bit less CPU horsepower. However, we do not support VLS any longer.

Put a **.dvbrc** file containing the DVB channels (satellite or digital terrestial TV channels) you want to stream in your home directory (some are provided in the *libdvb* tarball for the satellite channels).

Run VLS with the following command line:

``% ``\ **``vls``\ ````\ ``-vv``\ ````\ ``-d``\ ````\ **\ ```udp:192.168.0.42`` <udp:192.168.0.42>`__\ **\ ````\ **\ ```dvb:"EUROSPORT`` <dvb:%22EUROSPORT>`__\ **\ ``"``\ ````\ ``--ttl``\ ````\ ``12``**

where:

-  **"EUROSPORT"** is the channel you want to stream as written in your **~/.dvbrc** file,
-  **192.168.0.42** is either:

   -  the IP address of the machine you want to unicast to;
   -  or the DNS name the machine you want to unicast to;
   -  or a multicast IP address.

-  **12** is the value of the TTL (Time To Live) of your IP packets (which means that the stream will be able to cross 11 routers).

Stream with VLC
---------------

Note: VLC has many more features than VLS. First you can use the advanced stream output options such as transcoding and all kinds of output supports. Second VLC can take advantage of the Common Interface supported by some DVB adapters to descramble one or several services. Currently released versions of VLC only support the low-level API so some adapters won't work (budget-ci cards work, twinhan doesn't). Some CAM modules aren't compatible with some DVB cards, check the linux-dvb documentation for more information. So-called "professional" CAM modules are able to descramble up to twelve services, whereas customer-oriented modules are often limited to one or two services unless otherwise specified.

VLC must be compiled with --enable-dvb and you need the linux-dvb headers installed in your system. An example command-line is as follows:

| ``% ``\ **``vlc``\ ````\ ``-vvv``\ ````\ ``--color``\ ````\ ``--ttl``\ ````\ ``12``\ ````\ ``--ts-es-id-pid``\ ````\ ``--programs=8508,8505``\ ````\ ``dvb:``\ ````\ ``\``**
| ``  ``\ **``--dvb-frequency=11739000``\ ````\ ``--dvb-srate=27500000``\ ````\ ``--dvb-voltage=13``\ ````\ ``\``**
| ``  ``\ **``--sout-standard-access=udp``\ ````\ ``--sout-standard-mux=ts``\ ````\ ``--sout``\ ````\ ``\``**
| `` ''' '#duplicate{dst=std{dst=address1},select="program=8508",dst=std{dst=address2},select="program=8505"}' '''``

The example above shows the minimum set of options needed to stream out two services. Here is a list of frontend options, depending on the frontend type:

-  *common options*

   -  **dvb-adapter**: specifies the adapter to use in case you have several adapters in your machine (by default use adapter 0)
   -  **dvb-device**: specifies the name of the DVB device to use (should not be needed with a standard linux-dvb installation)
   -  **dvb-srate**: specifies the symbol rate of the modulated signal, in symbols/s
   -  **dvb-inversion**: specifies whether the signal is inverted or not (default is automatic detection)
   -  **dvb-budget-mode**: enters a special mode where all PIDs are retrieved by the driver; it should no longer be necessary as VLC should filter wanted PIDs

-  *satellite frontend (QPSK)*

   -  **dvb-frequency**: specifies the frequency to tune to in kHz; according to the frequency range, VLC auto-detects the band to use: S (2.5-2.7 GHz), C-lower (3.4-4.2 GHz), C-higher (4.5-4.8 GHz), Ku (10.7-13.25 GHz) or direct BIS frequency (0.95-2.15 GHz); it is mandatory to supply the **dvb-srate** option to satellite frontends
   -  **dvb-voltage**: specifies the voltage to apply on the IF; most LNBs behave differently when supplied with 13 V or 18 V; universal LNBs select vertical polarity with 13 V and horizontal with 18 V; you can also select 0 V if your LNB has another power supply (default is 13 V)
   -  **dvb-tone**: specifies whether to send a 22 kHz pulse tone to the LNB; universal LNBs switch to high-band when this pulse is sent; by default VLC automatically adopts the correct behaviour if the frequency supplied is in the Ku band (other bands do not need this)
   -  **dvb-fec**: specifies the code-rate to use for Forward Error Correction; type in the first number of the code-rate, for 2/3 use --dvb-rate=2, etc. (default is 9, meaning automatic detection)
   -  **dvb-high-voltage**: enables a special mode of the DVB adapter to compensate for the voltage loss in very long cables (AFAIK it is present in the API, but no DVB adapter actually implements it)
   -  **dvb-lnb-lof1, dvb-lnb-lof2, dvb-lnb-slof**: specifies the frequencies of the first and second local oscillators, and the frequency at which the 22 kHz pulse should be activated to enable the second oscillator; by default VLC uses the values for universal LNBs if the frequency supplied is in the Ku band (other bands do not need this)

-  *cable frontend (QAM)*

   -  **dvb-frequency**: specifies the frequency to tune to in Hz; it is mandatory to supply the **dvb-srate** option to cable frontends
   -  **dvb-modulation**: specifies the modulation of the analog signal; valid values are -1 (QPSK), 0 (automatic QAM, default), 16 (QAM16), 32 (QAM32), 64 (QAM64) 128 (QAM128), 256 (QAM256)

-  *terrestrial frontend (OFDM)*

   -  **dvb-frequency**: specifies the frequency to tune to in Hz; it is mandatory to supply the **dvb-bandwidth** option, all other parameters are optional
   -  **dvb-bandwidth**: specifies the bandwidth of the OFDM channel (6, 7 or 8 MHz depending on the country)
   -  **dvb-hierarchy**: specifies if the OFDM channel uses hierarchic information; allowed values are -1 (no hierarchy), 0 (automatic, default), 1, 2 and 4
   -  **dvb-code-rate-hp, dvb-code-rate-lp**: specifies the code-rate to use for higher and lower hierarchies respectively (default auto, same syntax as **dvb-fec**)
   -  **dvb-guard**: specifies the guard interval; valid values are 0 (automatic, default), 4 (1/4), 8 (1/8), 16 (1/16) and 32 (1/32)
   -  **dvb-transmission**: specifies the transmission mode; valid values are 0 (automatic, default), 2 (2K) and 8 (8K)

We also ought to explain the other non-dvb-specific options of the example command-line:

-  **ts-es-id-pid**: this option is necessary if you use the **#duplicate** stream output filter to split the multiplex in several outputs; there is no need to use **#duplicate** neither **ts-es-id-pid** if you have one program only
-  **programs, program, sout-all**: there are several ways of specifying the services to select (and optionally descramble):

   -  **programs**: used to specify one or serveral programs to select; VLC selects all known elementary streams of these programs; this is the currently recommended way
   -  **program**: used to specify one program to select; it differs from using **programs** with only one program in that this option only select the first audio stream, and no subtitle stream; it should be used if you plan to switch programs and audio with a GUI
   -  **sout-all**: tells VLC to select all programs; this is discouraged because of the extra CPU load needed to demultiplex unwanted programs, and because it is not compatible with CAM descrambling

-  The other options are standard stream output options and are described in the other chapters of this documentation.

.. raw:: mediawiki

   {{Documentation}}
