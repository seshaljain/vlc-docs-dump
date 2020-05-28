<noinclude>== Options (dummy section) ==</noinclude> {{Option
value=integer max=255 description=If there is more than one digital
broadcasting adapter, the adapter number must be selected. Numbering
starts from zero. }} {{Option value=integer max=255 description=If the
adapter provides multiple independent tuner devices, the device number
must be selected. Numbering starts from zero. }} {{Option value=boolean
description=Only useful programs are normally demultiplexed from the
transponder. This option will disable demultiplexing and receive all
programs. }} {{Option value=integer max=107999999 description=TV
channels are grouped by transponder (a.k.a. multiplex) on a given
frequency. This is required to tune the receiver. }} {{Option
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
name=dvb-voltage min=0 default=13 name=dvb-high-voltage default=false
name=dvb-lnb-low min=0 default=0 name=dvb-lnb-high min=0 default=0
name=dvb-lnb-switch min=0 default=11700000 name=dvb-satno select={ 0, 1,
2, 3, 4 } description=If the satellite receiver is connected to multiple
low noise block-downconverters (LNB) through a DiSEqC 1.0 switch, the
correct LNB can be selected (1 to 4). If there is no switch, this
parameter should be 0. }} {{Option value=integer default=0 name=dvb-tone
select={ -1, 0, 1 } description=A continuous tone at 22kHz can be sent
on the cable. This normally selects the higher frequency band from a
universal LNB. }}<noinclude>

{{Documentation}}

</noinclude>
