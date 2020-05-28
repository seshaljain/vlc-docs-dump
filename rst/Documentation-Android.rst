------ Work in progress ------

Here is the documentation of the Android port of VLC media player.

Preliminary Notes
-----------------

VLC for Android is a little different from VLC on desktops. In some ways, you can do more; in other ways, you can do less. VLC for Android only does media playback. Active streaming or file / stream to file conversations are not supported for usability and performance reasons. This walk-through does only include screenshots of a phone interface for size reasons. However, all features are also available on tablets with a similar appearance.

| 
| == Feature Overview ==

========================================================= ================== ================== ================== ================== ================== ==================
Feature                                                   Version 1.0        Version 1.6        Version 2.0        Version 2.5        Version 3.0        Version 3.1
========================================================= ================== ================== ================== ================== ================== ==================
Opening Network Streams                                   .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{No}}             {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}
UPnP discovery and streaming                              .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{No}}             {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}
Plex server discovery and streaming                       .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{No}}             {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}
Password-protected Plex shares                            .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{No}}             {{No}}             {{No}}             {{No}}             {{No}}             {{No}}
Downloads from UPnP multimedia servers                    .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{No}}             {{No}}             {{No}}             {{No}}             {{No}}             {{No}}
FTP discovery, streaming                                  .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{No}}             {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}
Store FTP server bookmarks                                .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{No}}             {{No}}             {{No}}             {{Yes}}            {{Yes}}            {{Yes}}
Audio Playback via Connector Cables                       .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}
Video Playback via Connector Cables                       .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}
Subtitles playback                                        .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}
Subtitles Font Customization                              .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{No}}             {{No}}             {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}
Closed Caption playback                                   .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}
Teletext subtitles playback                               .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{No}}             {{No}}             {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}
Multi-track audio handling                                .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{No}}             {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}
Video Filtering incl. Screen Brightness                   .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{No}}             {{No}}             {{No}}             {{No}}             {{No}}             {{No}}
Video Cropping and Aspect Ratio variation                 .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}
Deinterlacing                                             .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}
Playback Speed control                                    .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}
Audio/Subtitles delay control                             .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{No}}             {{No}}             {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}
Repeated playback                                         .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}
Gestures based playback control                           .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}
Playback of Audio-only media (mp3, m4a, flac, …)          .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}
Audio Playback in Background                              .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}
Video Playback in Background                              .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}
Playback timer                                            .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}
Chapter & title selection                                 .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{No}}             {{No}}             {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}
10-band equalizer                                         .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}
Playback UI Lock                                          .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}
Smart Media Library sorting for audio albums and TV shows .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}
Media Library Search                                      .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{No}}             {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}
Passcode Lock                                             .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{No}}             {{No}}             {{No}}             {{No}}             {{No}}             {{No}}
Voice search support                                      .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{No}}             {{No}}             {{No}}             {{Yes}}            {{Yes}}            {{Yes}}
Voice actions support                                     .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{No}}             {{No}}             {{No}}             {{No}}             {{No}}             {{No}}
Organize media in folders                                 .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{No}}             {{No}}             {{No}}             {{No}}             {{No}}             {{No}}
Use folders as playlists                                  .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{No}}             {{No}}             {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}
Loop playlists                                            .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}
Playback control through headphones or lock screen        .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}
Mediasession support (Wear, TV, etc…)                     .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{No}}             {{No}}             {{Partial}}        {{Yes}}            {{Yes}}            {{Yes}}
Playback is paused when headphones are unplugged          .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}
WiFi upload and HTTP downloads in background              .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{No}}             {{No}}             {{No}}             {{No}}             {{No}}             {{No}}
Support for password protected HTTP streams               .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{No}}             {{No}}             {{No}}             {{No}}             {{No}}             {{No}}
Sharing files with further apps                           .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{No}}             {{No}}             {{No}}             {{No}}             {{No}}             {{No}}
Custom vlc:// protocol                                    .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{No}}             {{No}}             {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}
Support for x-callback-url                                .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{No}}             {{No}}             {{No}}             {{No}}             {{No}}             {{Yes}}
Action mode                                               .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{No}}             {{No}}             {{No}}             {{Yes}}            {{Yes}}            {{Yes}}
Android TV                                                .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{No}}             {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}
Picture-in-Picture                                        .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{No}}             {{No}}             {{Partial}}        {{Yes}}            {{Yes}}            {{Yes}}
ChromeOS support                                          .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{No}}             {{ARC}}            {{ARC}}            {{Yes}}            {{Yes}}            {{Yes}}
Android Auto                                              .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{No}}             {{No}}             {{No}}             {{Yes}}            {{No}}             {{Yes}}
Sorting                                                   .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{No}}             {{No}}             {{Partial}}        {{Yes}}            {{Yes}}            {{Yes}}
360° videos                                               .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{No}}             {{No}}             {{No}}             {{Yes}}            {{Yes}}            {{Yes}}
DayNight mode                                             .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{No}}             {{No}}             {{No}}             {{Yes}}            {{Yes}}            {{Yes}}
Chromecast                                                .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{No}}             {{No}}             {{No}}             {{No}}             {{Yes}}            {{Yes}}
Equalizer custom presets                                  .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{No}}             {{No}}             {{No}}             {{No}}             {{Yes}}            {{Yes}}
Audio boost                                               .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{No}}             {{No}}             {{No}}             {{No}}             {{Yes}}            {{Yes}}
Android 2.1 support                                       .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{Yes}}            {{Yes}}            {{No}}             {{No}}             {{No}}             {{No}}
Android 2.2 support                                       .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{Yes}}            {{Yes}}            {{Yes}}            {{No}}             {{No}}             {{No}}
Android 2.3 support                                       .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}            {{No}}
Android 6 (Runtime permissions)                           .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{No}}             {{No}}             {{Yes}}            {{Yes}}            {{Yes}}            {{Yes}}
Android 8 support                                         .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                                                        
                                                             {{No}}             {{No}}             {{No}}             {{Partial}}        {{Partial}}        {{Yes}}
========================================================= ================== ================== ================== ================== ================== ==================

Installation
------------

There are many ways to install VLC on Android. This may be because you have a non-ARMv7 or x86 processor or do not wish to use the Play Store for whatever reason.

From the Play Store (recommended)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The normal way, for ARMv7 (and above) and x86 processors only. Don't know your processor? Don't worry, if you can download it, you have a compatible ARMv7 or an x86 processor.

   https://play.google.com/store/apps/details?id=org.videolan.vlc

| 

From the F-Droid Repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~

| The F-Droid repository (https://f-droid.org) is a completely FOSS (Free and Open Source Software) equivalent to the Google Play Store. The F-Droid Repository and all apps within it are provided completely free of charge and licensed under open source licenses. The F-Droid repository can be downloaded directly from their website. The "Unknown Sources" setting must be turned on for Android devices (typically located in Settings -> Security) in order to install repositories other than the Google Play Store.

From VideoLAN
~~~~~~~~~~~~~

If you can't download from the Play Store or just want to install the VLC .apk by yourself, follow these steps:

#. Go to Android Settings → Security → Device Administration → Enable 'Unknown Sources'
#. Go to our download server, preferably from your device: http://get.videolan.org/vlc-android/\ /
#. Choose your processor architecture (ARMv7 or Intel x86) and grab the .apk file.
#. Click on the .apk you just downloaded and install it.

Don't really know your processor architecture? Try both... it's not very clever, but it's harmless.

None of the two work? It is possible that you have an older processor with the ARMv6 architecture. The solution for now is to install a Nightly Build release. See below.

| Still doesn't work? Really? Well, then you must have an exotic processor... Contact us, on the `Android forum <http://forum.videolan.org/viewforum.php?f=35>`__ or directly at videolan.mobile@gmail.com.

Be a Beta tester or try a Beta release
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You want want to know the future of VLC for Android? You want to help us and/or test if your issue is already fixed for the next release ?

Be a Beta tester
^^^^^^^^^^^^^^^^

Just follow this link `Be a Beta tester <https://play.google.com/apps/testing/org.videolan.vlc>`__

Soon, Beta release will automatically install on our device.

Try a Beta release
^^^^^^^^^^^^^^^^^^

You don't want to be a Beta Tester but just try a Beta ? Follow these steps :

#. Go to Android Settings → Security → Device Administration → Enable 'Unknown Sources'
#. Go to our server, preferably from your device, : http://get.videolan.org/testing/android/\ /
#. Choose your processor architecture (ARMv7, ARMv8, x86...)
   Don't really know your processor architecture? Try both... it's not very clever, but it's harmless
#. Download the chosen .apk on your device
#. Click on the .apk you just download and install it.

| 

Install a Nightly Build
~~~~~~~~~~~~~~~~~~~~~~~

You fear nothing and want our very last works on VLC ? Or you have an ARMv6 Processor and want VLC? Follow these steps:

#. Go to Android Settings → Security → Device Administration → Enable 'Unknown Sources'
#. Go to our server, preferably from your device: http://nightlies.videolan.org/
#. Choose your processor architecture (ARMv7, ARMv8, x86...)
#. Grab the latest .apk
#. Click on the .apk you just download and install it.

You may experience some weird issues but generally, it works fine. If not, please try an older nightly release, and contact us.

| 

Interface
---------

At first start, VLC scans all your device to find all your media files. This is the main interface after the scan :

============================ ======================================== ==========================================================
.. figure:: Android_Main.jpg ========================= ============== ========================== ===============================
   :alt: Android_Main.jpg    .. figure:: caption_1.png Show Menu      .. figure:: caption_6.png  Video browser view
   :width: 550px                :alt: caption_1.png                      :alt: caption_6.png    
   :height: 550px               :width: 40px                             :width: 40px           
                                :height: 40px                            :height: 40px          
   Android_Main.jpg                                                                             
                                caption_1.png                            caption_6.png          
                             .. figure:: caption_2.png Video view     .. figure:: caption_7.png  Search a specific media
                                :alt: caption_2.png                      :alt: caption_7.png    
                                :width: 40px                             :width: 40px           
                                :height: 40px                            :height: 40px          
                                                                                                
                                caption_2.png                            caption_7.png          
                             .. figure:: caption_3.png Audio view     .. figure:: caption_8.png  Open network MRL
                                :alt: caption_3.png                      :alt: caption_8.png    
                                :width: 40px                             :width: 40px           
                                :height: 40px                            :height: 40px          
                                                                                                
                                caption_3.png                            caption_8.png          
                             .. figure:: caption_4.png Directory view .. figure:: caption_9.png  Load last playlist
                                :alt: caption_4.png                      :alt: caption_9.png    
                                :width: 40px                             :width: 40px           
                                :height: 40px                            :height: 40px          
                                                                                                
                                caption_4.png                            caption_9.png          
                             .. figure:: caption_5.png History view   .. figure:: caption_10.png | More actions :
                                :alt: caption_5.png                      :alt: caption_10.png    | \* Sort by name or length
                                :width: 40px                             :width: 40px            | \* Refresh your media library
                                :height: 40px                            :height: 40px           | \* Equalizer
                                                                                                 | \* Preferences
                                caption_5.png                            caption_10.png          | \* About VLC
                             ========================= ============== ========================== ===============================
============================ ======================================== ==========================================================

| 

Playing Video
-------------

Video browser view
~~~~~~~~~~~~~~~~~~

This view displays all your videos present in your device, or in the directories you have specified (see Preferences). To play one, just click on it, like the video |caption_1.png|.

Note the difference with the video |caption_2.png| which is a group of videos : VLC automatically groups your videos with the 4 same starting letters.

==================================== ============================================
.. figure:: Android_VideoBrowser.jpg ========================= ==================
   :alt: Android_VideoBrowser.jpg    .. figure:: caption_1.png A Video
   :width: 550px                        :alt: caption_1.png   
   :height: 550px                       :width: 40px          
                                        :height: 40px         
   Android_VideoBrowser.jpg                                   
                                        caption_1.png         
                                     .. figure:: caption_2.png A group of videos.
                                        :alt: caption_2.png   
                                        :width: 40px          
                                        :height: 40px         
                                                              
                                        caption_2.png         
                                     ========================= ==================
==================================== ============================================

| 

Video playback interface
~~~~~~~~~~~~~~~~~~~~~~~~

============================================= ========================================== ======================================================
.. figure:: Android_VideoPlayer_Interface.jpg ========================= ================ ========================== ===========================
   :alt: Android_VideoPlayer_Interface.jpg    .. figure:: caption_1.png Video title      .. figure:: caption_7.png  Video menu (for DVD iso)
   :width: 550px                                 :alt: caption_1.png                        :alt: caption_7.png    
   :height: 550px                                :width: 40px                               :width: 40px           
                                                 :height: 40px                              :height: 40px          
   Android_VideoPlayer_Interface.jpg                                                                               
                                                 caption_1.png                              caption_7.png          
                                              .. figure:: caption_2.png Battery and time .. figure:: caption_8.png  Lock screen
                                                 :alt: caption_2.png                        :alt: caption_8.png    
                                                 :width: 40px                               :width: 40px           
                                                 :height: 40px                              :height: 40px          
                                                                                                                   
                                                 caption_2.png                              caption_8.png          
                                              .. figure:: caption_3.png Play / Pause     .. figure:: caption_9.png  Elapsed time
                                                 :alt: caption_3.png                        :alt: caption_9.png    
                                                 :width: 40px                               :width: 40px           
                                                 :height: 40px                              :height: 40px          
                                                                                                                   
                                                 caption_3.png                              caption_9.png          
                                              .. figure:: caption_4.png Aspect ratio     .. figure:: caption_10.png Seek bar
                                                 :alt: caption_4.png                        :alt: caption_10.png   
                                                 :width: 40px                               :width: 40px           
                                                 :height: 40px                              :height: 40px          
                                                                                                                   
                                                 caption_4.png                              caption_10.png         
                                              .. figure:: caption_5.png Audio tracks     .. figure:: caption_11.png Total time / Remaining time
                                                 :alt: caption_5.png                        :alt: caption_11.png   
                                                 :width: 40px                               :width: 40px           
                                                 :height: 40px                              :height: 40px          
                                                                                                                   
                                                 caption_5.png                              caption_11.png         
                                              .. figure:: caption_6.png Subtitles tracks .. figure:: caption_12.png Advanced Options
                                                 :alt: caption_6.png                        :alt: caption_12.png   
                                                 :width: 40px                               :width: 40px            -  Playback Speed
                                                 :height: 40px                              :height: 40px           -  Sleep timer
                                                                                                                    -  Jump to specific time
                                                 caption_6.png                              caption_12.png          -  Add subtitle
                                              ========================= ================ ========================== ===========================
============================================= ========================================== ======================================================

Some precisions:

-  You can change audio and/or subtitle track if there are any. If not, these icons won't be displayed.
-  The Video Menu icon is only displayed for iso video (a DVD iso for example)

| 

Video playback gesture
~~~~~~~~~~~~~~~~~~~~~~

=========================================== ===========================================
.. figure:: Android_VideoPlayer_Gesture.jpg ========================= =================
   :alt: Android_VideoPlayer_Gesture.jpg    .. figure:: caption_1.png Adjust Brightness
   :width: 550px                               :alt: caption_1.png   
   :height: 550px                              :width: 40px          
                                               :height: 40px         
   Android_VideoPlayer_Gesture.jpg                                   
                                               caption_1.png         
                                            .. figure:: caption_2.png Adjust Volume
                                               :alt: caption_2.png   
                                               :width: 40px          
                                               :height: 40px         
                                                                     
                                               caption_2.png         
                                            .. figure:: caption_3.png Quick search
                                               :alt: caption_3.png   
                                               :width: 40px          
                                               :height: 40px         
                                                                     
                                               caption_3.png         
                                            ========================= =================
=========================================== ===========================================

| 

Playing Audio
-------------

TODO

-  You can change the time display to remaining time (e.g. -1:30 for 1:30 minutes remaining) in the audio player by tapping on the current time label in the left.

Settings
--------

See Also
--------

| `AndroidFAQ <AndroidFAQ>`__
| `Android Checklist <Android_Checklist>`__
| `Android Player Intents <Android_Player_Intents>`__
| `Android Report bugs <Android_Report_bugs>`__

`\* <Category:Android>`__

.. |caption_1.png| image:: caption_1.png
   :width: 30px
   :height: 30px
.. |caption_2.png| image:: caption_2.png
   :width: 30px
   :height: 30px
