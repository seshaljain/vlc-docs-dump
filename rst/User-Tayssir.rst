Hi, I'm using VLC to record meetings of a pretty large city council. A moderator uses a GUI (written in Common Lisp) to record who is speaking and manage their political party speaking times. This information goes to a server and it asks VLC to overlay a speaker name and maybe a logo. The video goes out both streaming and to file.

This is all automated.

Right now I have a problem, since sometimes the video should cut to a logo, and the audio stopped. The video is no problem, but I'm not so hot at writing audio filters (because of insignificant C experience), so stopping the audio is a problem. With dionoea's kindly advice, I'm trying to solve this with with bridge-in (formerly part of Mosaic). Hope it interacts well with the stream filters I'm chaining together; the chain length is like 4 or 5.
