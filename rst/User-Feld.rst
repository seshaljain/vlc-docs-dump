Hi, my name is Feld.

== Problem: Cannot keep settings for capture device ==

I am using version 0.8.5 of VLC with the wxWindows interface. The
computer/OS is an Athlon 64 running Windows XP Home. The capture device
is a CompUSA "High Speed USB Video Grabber" which according to the
drivers and to VLC is a "USB 2820 device".

My problem is that the capture device appears to output in a strange
aspect ratio. (The software that came with the device, ULead Video
Studio 7 SE Basic, appears to be capturing from the device in a 950x480
aspect.)

I have found how to get normal-aspect video to play on the screen:
#''File''->''Open Capture Device'' #:I get the ''Open'' dialog, on the
''DirectShow'' tab. #Press the ''Refresh list'' button across from
''Video device name'' #:In a few moments, "USB 2820 Device" appears.
#Select ''USB 2820 Device'' #Press ''Advanced options'' button #:Get
''Advanced options (DirectShow input)'' dialog #Check ''Device
properties'' checkbox #Click ''OK'' on ''Advanced options (DirectShow
input)'' dialog #Click ''OK'' on ''Open'' dialog #:Get ''Properties''
dialog with tabs ''Video Decoder'', ''Video Proc Amp'', and ''Video
Image'' tabs. On ''Video Decoder'' tab: #:\ *''Video Standard'' is set
to "NTSC_M" #:* ''Signal Detected'' is 1 #:\* ''Lines detected'' is 525
#:\* ''VCR Input'' is unchecked. #Click ''OK'' on ''Properties'' dialog
with ''Video Decoder'', ''Video Proc Amp'', and ''Video Image'' tabs.
#:Get ''Properties'' dialog with single ''Stream Format'' tab. Panes are
''Video Format'' and ''Compression''; on ''Video Format'' pane: #:\*
''Video Standard'' is set to "NTSC_M" (unchangable here) #:\* ''Frame
Rate'' is "30.000" #:\* ''Flip Horizontal'' is greyed out #:\* ''Color
Space / Compression'' is set to ''I420'' #:\* ''Output Size'' says the
default is "640x480" but is always "352x240" when this dialog first
appears. #Click ''Apply'' and ''OK'' #:Get ''Properties'' dialog with
single ''Crossbar'' tab. Panes are ''Input'' and ''Output''. #Click
''OK''. #:Video from capture device now appears on screen in a normal
aspect ratio.

This works to get video onto the screen, but I would like to use VLC to
save the video I'm capturing to file. I can't seem to do this, because
if I try to set up a transcoding chain with the input from the capture
device, I have no way of changing the Output Size to the 640x480 it
should be.
