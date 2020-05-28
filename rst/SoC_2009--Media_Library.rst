.. raw:: mediawiki

   {{SoCProject|year=2009|student=[[User:jetru|Srikanth Raju]]|mentor=[[User:J-Peg|Jean-Philippe Andre]]}}

Project Abstract
----------------

The project is about extending the Media Library(ML) for VLC Player. The media library will allow users to manage all their local and network media. The project will use the basic structure that already exists for the ML and will focus on extending the features. New features include Search, Smart playlists, Annotations and "Just play music".

Goals
-----

-  Basic: Add media files/folders to the library.
-  Live Folders: This will automatically scan folders for media additions. They will be automatically added to the ML. This feature already exists and requires some finetuning.
-  Search: Audio, Video, Streams and their metadata can be searched. Also, there is an advanced search that can allow searches on specific fields in the metadata.
-  Smart Playlists: A Smart playlist can be created from an "Advanced Search". Here you can specify some search and the result of this search can be stored in the playlist. The Smartness is that this type of playlist changes dynamically as the ML changes. Example: all audio between year 1970 and 1980 with rating > 4.
-  Bookmarks and Annotations:
-  Auto metadata fill: This will automatically fetch meta data information from external sources such as IMDB, Rotten Romatoes, AzLyrics(for lyrics), MusicBrainz, etc
-  Save file specific settings: VLC will remember if you played that screwed up video using some video filter/subtitle, etc. Next time the same media is opened, the settings are loaded from the ML. Ofcourse, there is a line to draw. This won't be very useful for volume, for example. No point setting low volume, if your sleeping roomate has to wake up everytime the track changes.
-  Podcasts and Services Discovery Integration: This will move all the services discovery features in VLC into the ML and complete the unified portal to accessing media! Notifications for these features will be improved.
-  "Just Play Music" Feature. Use information about what the user has been playing and likes(based on ratings) and find music that the user likes the best from his ML and play randomly.

Todo List
---------

============================ ================= ===========
What                         When              Status
============================ ================= ===========
Learn qt, git, bit of auto*. April 23 - May 16 Done
Off on a small vacation      May 16 - 23       yo!
QT Model Enhancement         May 23 - June 7   Not started
Just Play                    June 7 - June 14  Not started
Improve Live folders         May 23 - June 31  Not started
Search                       May 23 - June 31  Not started
Smart Playlists              May 23 - June 31  Not started
\                                             
============================ ================= ===========

Updates from me
---------------

My repo is at http://git.videolan.org/?p=vlc-jetru.git All ML work is done in branch "mlwork". --`Jetru <User:Jetru>`__ 05:18, 2 June 2009 (UTC)

Some changes in plans and lots of stuff to be decided and pipelined yet. Timelines are completely prospective. --`Jetru <User:Jetru>`__ 07:32, 16 May 2009 (CEST)

Writing minor patches to the existing ML. This should help me understand some stuff better. --`Jetru <User:Jetru>`__ 07:24, 7 May 2009 (CEST)

Back. Continuing studying stuff for vlc --`Jetru <User:Jetru>`__ 23:24, 29 April 2009 (CEST)

Traveling to the US. I'll be back online on Tuesday! --`Jetru <User:Jetru>`__ 08:34, 26 April 2009 (CEST)
