TODO
----

-  weird to begin with a 3rd level title (very often a second level) (=== instead of ==?)
-  Does the wiki preference link and VLC preference files should be merged in the same page?
-  --`Thannoy <User:Thannoy>`__ 15:31, 29 September 2008 (CEST)

 Playback States
---------------

Saving State
~~~~~~~~~~~~

We have different settings and options per media and per Application in the clients. The settings should behave the same across all of Platforms. This document tries to formulate a guideline on how to persist these states

What states need to be considered for persistance?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

============================ ================== ================== ==================
State/Setting                Media              Application        has Default
============================ ================== ================== ==================
Repeat                       .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                  
                                {{No}}             {{Yes}}            {{No}}
Playback speed               .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                  
                                {{Yes}}            {{No}}             {{Yes}}
Shuffle                      .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                  
                                {{No}}             {{Yes}}            {{No}}
Audio/Video track            .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                  
                                {{Yes}}            {{No}}             {{No}}
Aspect Ratio                 .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                  
                                {{Yes}}            {{No}}             {{No}}
Audio/Video sync             .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                  
                                {{Yes}}            {{No}}             {{Yes}}
Equalizer                    .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                  
                                {{No}}             {{Yes}}            {{No}}
Subtitle sync                .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                  
                                {{Yes}}            {{No}}             {{Yes}}
last played media            .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                  
                                {{No}}             {{Yes}}            {{No}}
play as audio                .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                  
                                {{No}}             {{Yes}}            {{No}}
Current renderer             .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                  
                                {{No}}             {{Yes}}            {{No}}
Current position in playlist .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                  
                                {{No}}             {{Yes}}            {{No}}
============================ ================== ================== ==================

has Default: means that there is a general value and can be changed in the settings or somewhere in the application

Application: means that it is application wide one state

Media: just a state per media

Reasoning
^^^^^^^^^

Playback Speed
''''''''''''''

If you watch conference videos you might want to double the speed. Persisting this across the Application when you change it on one Media item and applying it to the next might be confusing and unwanted. Instead there should be a default playback speed that can be set. Up for discussion is still if it should be a checkmark next to the playback speed control like [x] always apply or if it should be somewhere hidden in the settings. On Android Devices we also detect the medium, like Podcast or Audiobook to set a different playback speed automatically.

Audio Video sync, subtitle sync
'''''''''''''''''''''''''''''''

For bluetooth headsets some users want a default delay to make up for the delay experienced due to bluetooth connectivity
