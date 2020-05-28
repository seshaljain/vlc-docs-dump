Note: Data taken verbatim from the API. To get an overview see
[[{{#rel2abs:..}}]].

'''libvlccore''' is the core part of VLC. It is the heart of VLC,
powering the [[LibVLC]] library and providing the internal
infrastructure for a lot of functionality such as stream access, audio
and video output, plugin handling, a thread system. All the libvlccore
source files are located in the {{VLCSourceFolder|src}} directory and
its subdirectories:

{\| class="wikitable"

\|-! Directory Name ! Directory Explanation

{{VLCSourceFolderConfiguration code specific to VLC on [[Android]].
{{VLCSourceFolderinitializes the audio mixer, ie. finds the right
playing frequency, and then resamples audio frames received from the
decoder(s). {{VLCSourceFolderContains code to parse command line
arguments and vlcrc files. {{VLCSourceFolderConfiguration code specific
to VLC on Mac OS X. {{VLCSourceFolderSome extra functions to complement
the C library. {{VLCSourceFolderOpens an input module, reads packets,
parses them and passes reconstituted elementary streams to the
decoder(s). {{VLCSourceFolderContains code for user interaction such as
key presses and device ejection. {{VLCSourceFolderMiscellaneous
utilities used in other parts of VLC, such as the thread system, the
message queue, the object lookup system, the [[Hacker
Guide/Variables-src/modules}} -src/network}} -src/os2}} -src/playlist}}
-src/posix}} -src/stream_output}} -Configuration code specific to VLC on
Symbian. {{VLCSourceFolderThe short VLC test suite.
{{VLCSourceFolderContains text-related functions, like character
encodings, [[Unicode]], and IDNs. {{VLCSourceFolderinitializes the video
display, gets all pictures and subpictures (ie. subtitles) from the
decoder(s), optionally converts them to another format (such as YUV to
RGB), and displays them. {{VLCSourceFolderConfiguration code specific to
VLC on [[Windows]] \|}

{{Hacker Guide}} [[Category:Building]]
