<noinclude>== Options (dummy section) ==</noinclude> {{Option
value=integer description=If there is more than one digital broadcasting
adapter, the adapter number must be selected. Numbering starts from
zero. }} {{Option value=string description=Unique network name in the
System Tuning Spaces }} {{Option value=string description=Create unique
name in the System Tuning Spaces }} {{Option value=integer max=107999999
description=TV channels are grouped by transponder (a.k.a. multiplex) on
a given frequency. This is required to tune the receiver. }} {{Option
value=integer default=-1 \|description=If the demodulator cannot detect
spectral inversion correctly, it needs to be configured manually. }}

==== Terrestrial reception parameters ==== {{Option value=integer
default=0 name=dvb-transmission select={ -1, 1, 2, 4, 8, 16, 32 }
description=Transmission mode }} {{Option value=string default=""
\|description=Guard interval }}

==== DVB-T reception parameters ==== {{Option value=string default=""
name=dvb-code-rate-lp select={ "", "0", "1/2", "3/5", "2/3", "3/4",
"4/5", "5/6", "6/7", "7/8", "8/9", "9/10" } description=The code rate
for Forward Error Correction can be specified. }} {{Option value=integer
default=-1 name=dvb-plp-id min=0 default=0 \|description=DVB-T2 Physical
Layer Pipe }}

==== ISDB-T reception parameters ==== {{Option value=string default=NULL
name=dvb-a-fec select={ "", "0", "1/2", "3/5", "2/3", "3/4", "4/5",
"5/6", "6/7", "7/8", "8/9", "9/10" } description=The code rate for
Forward Error Correction can be specified. }} {{Option value=integer
max=13 description=Layer A segments count }} {{Option value=integer
max=3 description=Layer A time interleaving }} {{Option value=string
default=NULL name=dvb-b-fec select={ "", "0", "1/2", "3/5", "2/3",
"3/4", "4/5", "5/6", "6/7", "7/8", "8/9", "9/10" } description=The code
rate for Forward Error Correction can be specified. }} {{Option
value=integer max=13 description=Layer B segments count }} {{Option
value=integer max=3 description=Layer B time interleaving }} {{Option
value=string default=NULL name=dvb-c-fec select={ "", "0", "1/2", "3/5",
"2/3", "3/4", "4/5", "5/6", "6/7", "7/8", "8/9", "9/10" }
description=The code rate for Forward Error Correction can be specified.
}} {{Option value=integer max=13 description=Layer C segments count }}
{{Option value=integer max=3 description=Layer C time interleaving }}

==== Cable and satellite reception parameters ==== {{Option value=string
default=NULL name=dvb-srate min=0 default=0 name=dvb-fec select={ "",
"0", "1/2", "3/5", "2/3", "3/4", "4/5", "5/6", "6/7", "7/8", "8/9",
"9/10" } description=The code rate for Forward Error Correction can be
specified. }}

==== DVB-S2 parameters ==== {{Option value=integer max=255
description=Stream identifier }} {{Option value=integer default=-1
name=dvb-rolloff select={ -1, 35, 20, 25 } description=Roll-off factor
}}

==== ISDB-S parameters ==== {{Option value=integer max=0xffff
description=Transport stream ID }}

==== Satellite equipment control ==== {{Option value=string default=""
name=dvb-voltage min=0 default=13 name=dvb-lnb-low min=0 default=0
name=dvb-lnb-high min=0 default=0 name=dvb-lnb-switch min=0
default=11700000 name=dvb-network-id default=0 name=dvb-azimuth
default=0 name=dvb-elevation default=0 name=dvb-longitude default=0
name=dvb-range default="" \|description=Satellite range code as defined
by manufacturer e.g. DISEqC switch code }}

==== ATSC reception parameters ==== {{Option value=integer
description=Major channel }} {{Option value=integer description=ATSC
minor channel }} {{Option value=integer description=Physical channel
}}<noinclude>

{{Documentation}}

</noinclude>
