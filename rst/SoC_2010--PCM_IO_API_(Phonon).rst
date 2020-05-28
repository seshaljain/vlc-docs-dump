.. raw:: mediawiki

   {{SoCProject|year=2010|student=[[User:Mforney|Michael Forney]]|mentor=Jean-Baptiste Kempf}}

Abstract
--------

Design a fully featured PCM I/O API for Phonon, and provide an implementation for the Phonon-VLC backend and one other (either Xine or GStreamer). This API will allow developers to capture PCM data from devices like a sound card, or to play back raw audio from memory, or elsewhere. This will provide some important missing features in Phonon, and open the door for many applications waiting to make use of an API like this.

Timeline
--------

======================== ================================================== ===========
Date                     Description                                        Status
======================== ================================================== ===========
April 26th - May 23rd    Planning, API design                               Completed
May 24th - June 7th      API implementation in Phonon                       In progress
June 8th - July 4th      Add support for API to VLC backend                 Not started
July 5th - July 25th     Add support for other backend (probably GStreamer) Not started
July 26th - August 1st   Code finalization                                  Not started
August 2nd - August 9th  Finish documentation                               Not started
August 9th - August 16th Cleanup                                            Not started
======================== ================================================== ===========

Repositories
------------

-  Phonon: git://gitorious.org/~tridactyla/phonon/tridactyla-phonon.git
-  Phonon-VLC: git://gitorious.org/~tridactyla/phonon/tridactyla-phonon-vlc.git

.. raw:: mediawiki

   {{GSoC}}
