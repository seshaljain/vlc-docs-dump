{{howto|Make your Video Files playable on an Play-Yan Micro}}

A Play-Yan Micro is a Nintendo peripheral for Nintendo portable game
devices. See [https://www.nintendo.co.jp/n08/play_yan_micro/index.html
Nintendo's official page (Japanese)] for more info.

(The rest of the page follow the format/tone set by the Ipod howto
article.)

To play on this device, the file you copy to it needs to be of the
correct format. This format is summarised below: {\| \| Video Codec \|
'''mp4v''' Audio Codec \| '''mp4a''' ([[MP4 audio]]), '''aac'''
([[AAC]]) [[Container]] \| '''mp4''' ([[MPEG-4-\| Size \| 240x174 \|}

To make the video the correct size, you can edit the [[preferences]], or
run vlc from a [[command prompt]]. For Windows, make a batch file as
shown:

<!-- The correct language is "winbatch" but the and : characters are
misinterpreted. --> <syntaxhighlight lang="dos"> set
INPUT=V:mediasample.avi set OUTPUT=V:transcode outputsample.mp4 set
VLC=F:appVideoLANVLCvlc.exe %VLC% "%INPUT%"
:sout=#transcode{vcodec=mp4v,vb=1024,scale=1,acodec=mp4a,audio-sync}:std{access=file,mux=mp4,url="%OUTPUT%"}
--sout-transcode-width=240 --sout-transcode-height=176
--aspect-ratio=16:9 </syntaxhighlight>

Fill in the input and output filenames. (FIXME: Aspect Ratio does not
seem to be working){{Check}}

Note: Some videos can be transcoded, some can't. This info is still a
work in progress.
