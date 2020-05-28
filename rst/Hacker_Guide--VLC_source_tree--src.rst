Note: Data taken verbatim from the API. To get an overview see `{{#rel2abs:..}} <{{#rel2abs:..}}>`__.

**libvlccore** is the core part of VLC. It is the heart of VLC, powering the `LibVLC <LibVLC>`__ library and providing the internal infrastructure for a lot of functionality such as stream access, audio and video output, plugin handling, a thread system. All the libvlccore source files are located in the directory and its subdirectories:

======================================== ==============================================================================================================================================================================================
Directory Name                           Directory Explanation
======================================== ==============================================================================================================================================================================================
.. raw:: mediawiki                       Configuration code specific to VLC on `Android <Android>`__.
                                        
   {{VLCSourceFolder|src/android}}      
.. raw:: mediawiki                       initializes the audio mixer, ie. finds the right playing frequency, and then resamples audio frames received from the decoder(s).
                                        
   {{VLCSourceFolder|src/audio_output}} 
.. raw:: mediawiki                       Contains code to parse command line arguments and vlcrc files.
                                        
   {{VLCSourceFolder|src/config}}       
.. raw:: mediawiki                       Configuration code specific to VLC on Mac OS X.
                                        
   {{VLCSourceFolder|src/darwin}}       
.. raw:: mediawiki                       Some extra functions to complement the C library.
                                        
   {{VLCSourceFolder|src/extras}}       
.. raw:: mediawiki                       Opens an input module, reads packets, parses them and passes reconstituted elementary streams to the decoder(s).
                                        
   {{VLCSourceFolder|src/input}}        
.. raw:: mediawiki                       Contains code for user interaction such as key presses and device ejection.
                                        
   {{VLCSourceFolder|src/interface}}    
.. raw:: mediawiki                       Miscellaneous utilities used in other parts of VLC, such as the thread system, the message queue, the object lookup system, the `variable system <Hacker_Guide/Variables>`__ or CPU detection.
                                        
   {{VLCSourceFolder|src/misc}}         
.. raw:: mediawiki                       Contains the mechanism of the modules/plugin system.
                                        
   {{VLCSourceFolder|src/modules}}      
.. raw:: mediawiki                       Contains code related to network access.
                                        
   {{VLCSourceFolder|src/network}}      
.. raw:: mediawiki                       Configuration code specific to VLC on OS/2.
                                        
   {{VLCSourceFolder|src/os2}}          
.. raw:: mediawiki                       Manages playlist interaction such as stop, play, next, or random playback.
                                        
   {{VLCSourceFolder|src/playlist}}     
.. raw:: mediawiki                       Configuration code specific to VLC on POSIX.
                                        
   {{VLCSourceFolder|src/posix}}        
.. raw:: mediawiki                       Initializes stream output muxers and encoders to enable `streaming <streaming>`__ with VLC.
                                        
   {{VLCSourceFolder|src/stream_output}}
src/symbian                              Configuration code specific to VLC on Symbian.
.. raw:: mediawiki                       The short VLC test suite.
                                        
   {{VLCSourceFolder|src/test}}         
.. raw:: mediawiki                       Contains text-related functions, like character encodings, `Unicode <Unicode>`__, and IDNs.
                                        
   {{VLCSourceFolder|src/text}}         
.. raw:: mediawiki                       initializes the video display, gets all pictures and subpictures (ie. subtitles) from the decoder(s), optionally converts them to another format (such as YUV to RGB), and displays them.
                                        
   {{VLCSourceFolder|src/video_output}} 
.. raw:: mediawiki                       Configuration code specific to VLC on `Windows <Windows>`__
                                        
   {{VLCSourceFolder|src/win32}}        
======================================== ==============================================================================================================================================================================================

.. raw:: mediawiki

   {{Hacker Guide}}

`Category:Building <Category:Building>`__
