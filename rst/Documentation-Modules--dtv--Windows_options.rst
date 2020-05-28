== Options (dummy section) ==

Terrestrial reception parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: mediawiki

   {{Option
   |name=dvb-bandwidth
   |value=integer
   |select={ 0, 10, 8, 7, 6, 5, 2 }
   |default=0
   |description=Bandwidth (MHz)
   }}

.. raw:: mediawiki

   {{Option
   |name=dvb-transmission
   |value=integer
   |select={ -1, 1, 2, 4, 8, 16, 32 }
   |default=0
   |description=Transmission mode
   }}

.. raw:: mediawiki

   {{Option
   |name=dvb-guard
   |value=string
   |select={ "1/128", "1/32", "1/16", "19/256", "1/8", "19/128", "1/4" }
   |default=""
   |description=Guard interval
   }}

DVB-T reception parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: mediawiki

   {{Option
   |name=dvb-code-rate-hp
   |value=string
   |select={ "", "0", "1/2", "3/5", "2/3", "3/4", "4/5", "5/6", "6/7", "7/8", "8/9", "9/10" }
   |default=""
   |description=The code rate for Forward Error Correction can be specified.
   }}

.. raw:: mediawiki

   {{Option
   |name=dvb-code-rate-lp
   |value=string
   |select={ "", "0", "1/2", "3/5", "2/3", "3/4", "4/5", "5/6", "6/7", "7/8", "8/9", "9/10" }
   |default=""
   |description=The code rate for Forward Error Correction can be specified.
   }}

.. raw:: mediawiki

   {{Option
   |name=dvb-hierarchy
   |value=integer
   |select={ -1, 0, 1, 2, 4 }
   |default=-1
   |description=Hierarchy mode
   }}

.. raw:: mediawiki

   {{Option
   |name=dvb-plp-id
   |value=integer
   |min=0
   |max=255
   |default=0
   |description=DVB-T2 Physical Layer Pipe
   }}

ISDB-T reception parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: mediawiki

   {{Option
   |name=dvb-a-modulation
   |value=string
   |select={ "", "QAM", "16QAM", "32QAM", "64QAM", "128QAM", "256QAM", "8VSB", "16VSB", "QPSK", "DQPSK", "8PSK", "16APSK", "32APSK" }
   |default=NULL
   |description=The digital signal can be modulated according with different constellations (depending on the delivery system). If the demodulator cannot detect the constellation automatically, it needs to be configured manually.
   }}

.. raw:: mediawiki

   {{Option
   |name=dvb-a-fec
   |value=string
   |select={ "", "0", "1/2", "3/5", "2/3", "3/4", "4/5", "5/6", "6/7", "7/8", "8/9", "9/10" }
   |default=NULL
   |description=The code rate for Forward Error Correction can be specified.
   }}

.. raw:: mediawiki

   {{Option
   |name=dvb-a-count
   |value=integer
   |min=0
   |max=13
   |default=0
   |description=Layer A segments count
   }}

.. raw:: mediawiki

   {{Option
   |name=dvb-a-interleaving
   |value=integer
   |min=0
   |max=3
   |default=0
   |description=Layer A time interleaving
   }}

.. raw:: mediawiki

   {{Option
   |name=dvb-b-modulation
   |value=string
   |select={ "", "QAM", "16QAM", "32QAM", "64QAM", "128QAM", "256QAM", "8VSB", "16VSB", "QPSK", "DQPSK", "8PSK", "16APSK", "32APSK" }
   |default=NULL
   |description=The digital signal can be modulated according with different constellations (depending on the delivery system). If the demodulator cannot detect the constellation automatically, it needs to be configured manually.
   }}

.. raw:: mediawiki

   {{Option
   |name=dvb-b-fec
   |value=string
   |select={ "", "0", "1/2", "3/5", "2/3", "3/4", "4/5", "5/6", "6/7", "7/8", "8/9", "9/10" }
   |default=NULL
   |description=The code rate for Forward Error Correction can be specified.
   }}

.. raw:: mediawiki

   {{Option
   |name=dvb-b-count
   |value=integer
   |min=0
   |max=13
   |default=0
   |description=Layer B segments count
   }}

.. raw:: mediawiki

   {{Option
   |name=dvb-b-interleaving
   |value=integer
   |min=0
   |max=3
   |default=0
   |description=Layer B time interleaving
   }}

.. raw:: mediawiki

   {{Option
   |name=dvb-c-modulation
   |value=string
   |select={ "", "QAM", "16QAM", "32QAM", "64QAM", "128QAM", "256QAM", "8VSB", "16VSB", "QPSK", "DQPSK", "8PSK", "16APSK", "32APSK" }
   |default=NULL
   |description=The digital signal can be modulated according with different constellations (depending on the delivery system). If the demodulator cannot detect the constellation automatically, it needs to be configured manually.
   }}

.. raw:: mediawiki

   {{Option
   |name=dvb-c-fec
   |value=string
   |select={ "", "0", "1/2", "3/5", "2/3", "3/4", "4/5", "5/6", "6/7", "7/8", "8/9", "9/10" }
   |default=NULL
   |description=The code rate for Forward Error Correction can be specified.
   }}

.. raw:: mediawiki

   {{Option
   |name=dvb-c-count
   |value=integer
   |min=0
   |max=13
   |default=0
   |description=Layer C segments count
   }}

.. raw:: mediawiki

   {{Option
   |name=dvb-c-interleaving
   |value=integer
   |min=0
   |max=3
   |default=0
   |description=Layer C time interleaving
   }}

Cable and satellite reception parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: mediawiki

   {{Option
   |name=dvb-modulation
   |value=string
   |select={ "", "QAM", "16QAM", "32QAM", "64QAM", "128QAM", "256QAM", "8VSB", "16VSB", "QPSK", "DQPSK", "8PSK", "16APSK", "32APSK" }
   |default=NULL
   |description=The digital signal can be modulated according with different constellations (depending on the delivery system). If the demodulator cannot detect the constellation automatically, it needs to be configured manually.
   }}

.. raw:: mediawiki

   {{Option
   |name=dvb-srate
   |value=integer
   |min=0
   |max=UINT64_C(0xffffffff)
   |default=0
   |description=The symbol rate must be specified manually for some systems, notably DVB-C, DVB-S and DVB-S2.
   }}

.. raw:: mediawiki

   {{Option
   |name=dvb-fec
   |value=string
   |select={ "", "0", "1/2", "3/5", "2/3", "3/4", "4/5", "5/6", "6/7", "7/8", "8/9", "9/10" }
   |default=""
   |description=The code rate for Forward Error Correction can be specified.
   }}

DVB-S2 parameters
^^^^^^^^^^^^^^^^^

.. raw:: mediawiki

   {{Option
   |name=dvb-stream
   |value=integer
   |min=0
   |max=255
   |default=0
   |description=Stream identifier
   }}

.. raw:: mediawiki

   {{Option
   |name=dvb-pilot
   |value=integer
   |select={ -1, 0, 1 }
   |default=-1
   |description=Pilot
   }}

.. raw:: mediawiki

   {{Option
   |name=dvb-rolloff
   |value=integer
   |select={ -1, 35, 20, 25 }
   |default=-1
   |description=Roll-off factor
   }}

ISDB-S parameters
^^^^^^^^^^^^^^^^^

.. raw:: mediawiki

   {{Option
   |name=dvb-ts-id
   |value=integer
   |min=0
   |max=0xffff
   |default=0
   |description=Transport stream ID
   }}

Satellite equipment control
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: mediawiki

   {{Option
   |name=dvb-polarization
   |value=string
   |select={ "", "V", "H", "R", "L" }
   |default=""
   |description=To select the polarization of the transponder, a different voltage is normally applied to the low noise block-downconverter (LNB).
   }}

.. raw:: mediawiki

   {{Option
   |name=dvb-voltage
   |value=integer
   |min=0
   |max=18
   |default=13
   |description=""
   }}

.. raw:: mediawiki

   {{Option
   |name=dvb-lnb-low
   |value=integer
   |min=0
   |max=0x7fffffff
   |default=0
   |description=The downconverter (LNB) will subtract the local oscillator frequency from the satellite transmission frequency. The intermediate frequency (IF) on the RF cable is the result.
   }}

.. raw:: mediawiki

   {{Option
   |name=dvb-lnb-high
   |value=integer
   |min=0
   |max=0x7fffffff
   |default=0
   |description=The downconverter (LNB) will subtract the local oscillator frequency from the satellite transmission frequency. The intermediate frequency (IF) on the RF cable is the result.
   }}

.. raw:: mediawiki

   {{Option
   |name=dvb-lnb-switch
   |value=integer
   |min=0
   |max=0x7fffffff
   |default=11700000
   |description=If the satellite transmission frequency exceeds the switch frequency, the oscillator high frequency will be used as reference. Furthermore the automatic continuous 22kHz tone will be sent.
   }}

.. raw:: mediawiki

   {{Option
   |name=dvb-network-id
   |value=integer
   |default=0
   |description=Network identifier
   }}

.. raw:: mediawiki

   {{Option
   |name=dvb-azimuth
   |value=integer
   |default=0
   |description=Satellite azimuth in tenths of degree
   }}

.. raw:: mediawiki

   {{Option
   |name=dvb-elevation
   |value=integer
   |default=0
   |description=Satellite elevation in tenths of degree
   }}

.. raw:: mediawiki

   {{Option
   |name=dvb-longitude
   |value=integer
   |default=0
   |description=Satellite longitude in tenths of degree. West is negative.
   }}

.. raw:: mediawiki

   {{Option
   |name=dvb-range
   |value=string
   |default=""
   |description=Satellite range code as defined by manufacturer e.g. DISEqC switch code
   }}

ATSC reception parameters
^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: mediawiki

   {{Option
   |name=dvb-major-channel
   |value=integer
   |default=0
   |description=Major channel
   }}

.. raw:: mediawiki

   {{Option
   |name=dvb-minor-channel
   |value=integer
   |default=0
   |description=ATSC minor channel
   }}

.. raw:: mediawiki

   {{Option
   |name=dvb-physical-channel
   |value=integer
   |default=0
   |description=Physical channel
   }}

.. raw:: mediawiki

   {{Documentation}}


