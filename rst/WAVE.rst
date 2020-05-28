{{muxencoder=y}}

'''WAVE''' is a way of storing audio, which is normally
[[raw|uncompressed]]. It is based on [[RIFF]]. Note that wav isn't a
streamable audio format, so you can only stream it using [[RTP]] (to
stream it otherwise, transcode it to something that's streamable).

== Accepted audio codecs == \* [[dummy]]: Uncompressed audio of various
types, based on storing integer values of the amplitude of the sound
(see [[wikipedia:PCM|PCM]]). \* [[fl32]]: Floating point 32-bit
uncompressed audio, also based on PCM but allowing the values to be
stored as floating point data types. This can give better quality audio
when the sound becomes quiet.

== Converting to WAVE ==

The command-line for [[convert]]ing any readable input file to a WAVE
audio file is the following:

   {{%}} {{font colourvlc}} -I dummy -vv {{font colour"input.mp3"}}
   --sout=#transcode{acodec={{font colours16l}},channels=2,ab={{font
   colour128}},samplerate=44100}:standard{access=file,mux=wav,dst={{font
   colour"output.wav"}}} vlc://quit

Where on Windows you need to add installation directory in front of
{{font colourvlc}} (by default {{font colour{{Path to VLCdir=y}}}}).

As {{font colouraudio codec (acodec)}} you can specify one of the above
mentioned ones. The [[bitrate]] of the output file is specified by the
{{font colourab}} parameter.

== Source code == {{fileoutput muxer}} {{fileinput demuxer}}
