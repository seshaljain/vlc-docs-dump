{{Howto|extract audio from a video}} The following example shows how to
extract audio (<code>file.mp3</code>) from a working video file
(<code>file.ts</code>) via [[command-line]]: vlc file.ts --no-sout-video
--sout '#std{mux=raw,dst=file.mp3}'

The following example will prevent the GUI from appearing and converts
the audio to .wav:

   vlc -I dummy --sout
   "#transcode{acodec=s16l,channels=2}:std{access=file,mux=wav,dst=OUTFILE.wav}"
   INFILE.mp4 vlc://quit

With this, you can [[VLC HowTo/Transcode multiple videos|build scripts
to mass-convert multiple files]], for example in Bash (Linux, Mac OS X)
to convert all files ending in lowercase "mp4" you would use:

   for i in \*mp4; do vlc -I dummy --sout
   "#transcode{acodec=s16l,channels=2}:std{access=file,mux=wav,dst=$i.wav}"
   "$i" vlc://quit; done

==See also== \* article ''[[Extract audio]]''
