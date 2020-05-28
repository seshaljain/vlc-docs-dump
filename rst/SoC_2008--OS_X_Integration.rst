.. raw:: mediawiki

   {{SoCProject|year=2008|student=[[User:dudiak|Eric Dudiak]]|mentor=[[User:Fkuehne|Felix Paul Kühne]]}}

Mac OS X (Leopard) Integration
==============================

Abstract
--------

Unlike Windows and Linux, Mac OS X does not offer much in terms of alternatives to its built-in QuickTime media player. VLC media player represents the only Mac media player with significant support for various media formats and a tight integration with the OS, including a "Mac-like" user interface. As it is the only full, viable alternative to QuickTime on the Mac OS X platform, it is important that it stay current with various Mac technologies to offer users a comprehensive option for media playback.

Aspects of tighter Mac OS X integration:

-  Quick Look Generator for Leopard (to generate thumbnails and full media previews from the Finder)
-  Making most common preferences accessible in a Mac-style preference window organized with icon tabs across the top such as in Safari and Mail.
-  Moving the Readme document and other help resources into a HelpViewer HTML document to allow better help searching in Leopard.
-  Improvements in steaming server wizard to be more in-line with other Mac wizards and easier to use for personal streaming between Macs.
-  Add better support for package files that contain media VLC can play, such as iMovie Projects and EyeTV recordings.
-  Update the VLC file icons to the 512 by 512 size for Leopard.

Detailed Description
--------------------

This project will use the libraries provided by Apple for creating a Quick Look Generator. Due to various restrictions placed on these by Apple, the method for generating the live preview may use the mozilla plugin if no better alternative can be found. Creating these enhancements will require a combination of C and Objective-C. The Quick Look function should generate a thumbnail when simply browsing the Finder or viewing with CoverFlow and should provide full playback when the spacebar is pressed (which actually opens the Quick View). For those not familiar with the details of Mac OS X, Apple provides very specific models for Human-Computer Interaction (HCI) defined in documents on their `developer site <http://developer.apple.com>`__. In addition to providing the Quick Look functionality, I will be attempting to bring VLC more in line with these usability guidelines. This will include updating the preferences window to have a more Mac OS X feel and organization to it for at least the most fundamental set of preferences (with the rest to be accessible in the traditional way). I will also be moving some of the documentation into HelpViewer format to allow easy searching of it directly from the menu bar in Leopard. Also, I will be designing a new Streaming/Transcoding Wizard that better matches the Mac OS X wizard look and feel, such as the in the Bluetooth Setup Assistant or Network Setup Assistant. The new icons should look more like other modern Mac OS X file icons since the current ones more closely resemble icons found in the Mac OS X Public Beta. These new icons should be included for several of the formats that are newer to VLC (and were not supported when the old icons were made) and should differentiate between types (audio vs. video) in the icon style.

Development Plan
----------------

-  Research both Apple and community documentation on Quick Look Generators.
-  Attempt to create a simple, dynamic Quick Look Generator to test the ability to create such generators.
-  Failing that, create a simple Quick Look Generator that uses a custom WebKit plugin.
-  Move to developing a Quick Look Generator for VLC that uses whichever method was more successful.
-  Create Quick Look Generator that plays at least one VLC media format (no controls yet, just basic playback).
-  Add support for additional formats.
-  Add thumbnail generation for supported formats.
-  Add basic playback controls (play/pause, possibly mute and scrubber)
-  If ahead of schedule, add support for displaying relevant metadata, such as ID3 tags for MP3 files.
-  Create new Mac OS X icon files.
-  Evaluate icons/Quick View with community and sample end users.
-  Work on new Mac OS X interface
-  Perform think aloud evaluation on prototype.
-  Refine prototype.
-  Build fully functional version in VLC.

Weekly Schedule
---------------

| This schedule only includes coding plans for about a month going forward because I will have to asses what has been completed of my plan for each week before planning additional weeks. It does, however, include all known conflicts for the entire period.
| **Week 1 (May 26 – May 30)**
| \*Review Apple documentation for Quick Look development

-  Review potential of VLCkit
-  Review potential of VLC WebKit plugin
-  Start building Quick Look Generator

*Completed:*

-  Review Apple documentation
-  Decided to start development with the VLC WebKit/Mozilla plugin
-  Started coding on the generator

| **Week 2 (June 2 – June 6)**
| \*Finish alpha Quick Look Generator for previews *Completed:*

-  Alpha not yet ready. Will continue work into week 3.

| **Week 3 (June 9 – June 13)**
| \*Add thumbnail support

-  Finish preview work from week 2.

*Completed:*

-  Created new icon files at 512x512 resolution

| **Week 4 (June 16 – June 20)**
| \*Refine controls/appearance for Quick Look.

-  Create new icons
-  Evaluate Quick Look and icons

*Completed:*

-  Made a quicklook preview by converting VLC files into QuickTime files

| **Week 5 (June 23 – June 27)**
| \*Start new interface design **Week 6 (June 30 – July 4)**
| \*Continue new interface prototype

-  Away Tuesday onward (still online, just unlikely able to work)

| **Week 7 (July 7 – July 11)**
| \*Arrive back on Tuesday (still online, just unlikely able to work)

-  Integrate new interface into existing VLC code
-  Midterm evalutation

| **Week 8 (July 14 – July 18)**
| \*Get playback working in new UI

-  Get basic controls working
-  Create additional new icons for interface

| **Week 9 (July 21 – July 25)**
| \*Set up sidebar/source bar to act as expected

-  Make resizing work correctly
-  Finish setting up controls

| **Week 10 (July 28 – August 1)**
| \*Fix drawing errors

-  Fix resize errors
-  Allow dragging by background
-  Fix/update git repository

| **Week 11 (August 4 – August 8)**
| \*Integrate playlist into new interface

-  Add content to sidebar/sourcebar

| **Week 12 (August 11 – August 15)**
| \*Wrap up coding **After August 15**
| \*August 16: Leave for California (Apple Cocoa Camp)

-  August 24: Leave for Sweden (Study Abroad Semester)
-  Final evaluation

Note: I will still be within contact after leaving for Sweden. Also, since this is past the end of coding date (August 11 week), I should not have any problems not having a work visa (although my student visa does allow me to work). I will still be able to complete the final evaluation before September 1.

New Icon Prototypes
-------------------

| **Current Icon:**
| http://www.dudiak.com/VLC-Icons/generic.png
| **New Icons at (reduced) 128 x 128 resolution:**
| http://www.dudiak.com/VLC-Icons/Sample.png
| These new icons are designed to better highlight the contents of files and better meet the Apple Interface Guidelines for document icons. These icons are also rendered at 512 x 512 to support Mac OS X Leopard's higher resolution icon standard and can be scaled larger if needed (all graphics are vectors). Furthermore, the use of six generic icons instead of one allows future formats to be easily added without the need for more icons. As current users of VLC for Mac OS X know, the "blank" icon is often used for more newly supported formats in VLC such as MKV, FLV, FLAC, and others. When adding a format, an icon that matches the type of file could be used to be more specific without needing to make an icon that says "FLAC" on it. That being said, I intend to create titled icons for the majority of currently-supported files, but will also include these six generic ones for future file support. Also, it should be noted that the more of these 512 x 512 icons included, the larger the VLC download will become as they are much larger than the current 128 x 128. These icons range from 96 KB to 276 KB when exported as apple .icns files. The full resolution versions can be seen `here <http://www.dudiak.com/VLC-Icons/>`__.
| *Please email me all comments at*\ dudiak@gmail.com\ *. Thanks!*

New Interface
-------------

| **July 29, 2008:**
| `First Prototype Functioning <http://www.dudiak.com/VLC-Icons/new_interface.mp4>`__
| **August 12, 2008:**
| `Feature Complete Version <http://www.dudiak.com/VLC-Icons/new_interface_2.mp4>`__
