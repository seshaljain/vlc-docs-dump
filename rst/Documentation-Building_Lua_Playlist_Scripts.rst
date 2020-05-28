.. raw:: mediawiki

   {{Example code}}

.. raw:: mediawiki

   {{RightMenu|Documentation TOC}}

Introduction
------------

Starting with version 0.9.0, VLC gives you the possible to implement your own playlist loading modules easily. Such modules can do stuff like:

-  *URL translation*: You give it the youtube webpage URL and VLC starts playing the corresponding video;
-  *Text playlist parsing*: You use some custom text playlist format.

Lua playlist scripts shipped with VLC are stored in the following directory:

-  C:\Program Files\VideoLAN\VLC\lua\playlist\\ on Windows;
-  VLC.app/Contents/MacOS/share/lua/playlist/ on Mac OS X;
-  /usr/share/vlc/lua/playlist/ on Linux.

You can add your own Lua playlist scripts in this directory or in your VLC's preferences folder "lua/playlist" subdirectory on Windows or Mac OS X and in your local VLC shared data folder on Linux (~/.local/share/vlc/lua/playlist).

Simple Examples
---------------

URL translation
~~~~~~~~~~~~~~~

What we want to do
^^^^^^^^^^^^^^^^^^

Let's say that we want VLC to open Google Video links automatically. Google Video pages have URLs like

``http://video.google.com/videoplay?docid=-5784010886294950089``

to the URL of the corresponding Google Video Playlist file which is

``http://video.google.com/videogvp?docid=-5784010886294950089``

Probe
^^^^^

The Lua script is going to be made of 2 functions. The first one is the **probe()** function. This function tells VLC if the Lua script should be used (function returns true) or not (function returns false). Here it would look like:

.. code:: lua

    function probe()
        if vlc.access ~= "http"
        then
            return false
        end
        if string.match( vlc.path, "video.google.com/videoplay" )
        then
            return true
        else
            return false
        end
    end

Lets analyse that function step by step. First we check that VLC is using HTTP. If it isn't (for example it's reading a file off your hard drive or a DVD), we don't want to trigger the Google Video URL translation. The **vlc** Lua object provides **vlc.access** which should be equal to string **"http"**. Then we check that the URL is a Google Video page. This is easily done by trying to find the **"video.google.com/videoplay"** string in **vlc.path**.

Note that the same function can be written as

.. code:: lua

    function probe()
        return vlc.access == "http" and string.match( vlc.path, "video.google.com/videoplay" )
    end

Parse
^^^^^

If the **probe()** function returns true, VLC will use the **parse()** to ask for the new playlist item(s) which need to be added.

.. code:: lua

    function parse()
        item = {}
        item.path = "http://" .. string.gsub( vlc.path, "videoplay", "videogvp" )
        item.name = "Some Google video playlist"
        return { item }
    end

We create a new playlist item (a Lua table). We set the item's path to the appropriate string: 1/ we prepend "http://" since the **vlc.path** string doesn't include that part of the original URL and 2/ we replace "videoplay" by "videogvp".

We also set the new playlist item's name to "Some Google video playlist".

We then return the new playlist to VLC (a Lua table which basically represents a list of items).

A shorter version would be:

.. code:: lua

    function parse()
        return { { path = "http://" .. string.gsub( vlc.path, "videoplay", "videogvp" ); name = "Some Google video playlist" } }
    end

Saving that to a file
^^^^^^^^^^^^^^^^^^^^^

To make that script available to VLC, simply create a new something.lua file in one of the directories listed in the introduction (You should also remove the googlevideo.lua file shipped with VLC to make sure that it isn't used instead of your new script).

Text Playlist Parsing
~~~~~~~~~~~~~~~~~~~~~

In the previous example we translated a URL to another URL. This new URL redirects VLC to a Google Video Playlist which is basically a text file. This file needs to be read to get the final video's true URL. Here's what such a file would look like if you were to open it with a text editor:

::

   # download the free Google Video Player from http://video.google.com/
   gvp_version:1.1
   url:http://vp.video.google.com/videodownload?version=0&secureurl=uQAAAAznrU3q0BdxTkn_lLSpVJQ4a4JBDFAc5V8lB5OXXPqJ6Dts-Hq5Ll-2dIgeBIDGN1ZAMv65MMP0Zu5cwbIrgAhinWRNl-UtZCU4CgPpnYrR5IwLCk-sEXjs4o89dTT8MQxWcSo3lFPKulC0_TT9L0EW_IyANloBjyoEld5KGkcXdUTtXvj1TmaRh5Yvq4zIfxmYPQ4fehJY6rucnqMQLm8NTD32NvVpSp1bJ06ub_YJgDz4Nic-_qpW0rnFReSyrQ&sigh=zy8gMs8AhAM0Hv3N1PR7djz3m2I&begin=0&len=72640&docid=-5784010886294950089
   docid:-5784010886294950089
   duration:72640
   title:Penguins go for a stroll
   description:African penguins caught a breath of fresh air as they were out for a stroll through Tokyo's aquarium. Ikebukuro Sunshine Aquarium offer spectators a chance to get a closer encounter with penguins as they are taken for a walk through the aquariums compound.
   description:
   description:During the parade the penguins were separated from spectators, mainly children, by portable fences on wheels which were pushed by the zookeepers. The fence ensures they don't run away and also prevents them from biting spectators. 
   description:
   description:"I came up with this idea to let people get a close look at penguins walking." said Keeper Masahiro Tomiyama, adding only penguins born and raised at the aquarium can walk outside their cage without feeling stressed by all the attention.
   description:
   description:Reuters 16094/06
   description:Keywords: animals, cute, sweet, funny, ITN Source.

.. _probe-1:

Probe
^^^^^

The first thing we need to worry about is making sure that the file we're playing is a Google Video Playlist (GVP) file. We could rely on the URL, but that would prevent playing GVP files from our hard drive. Fortunately, the file's contents, especially the "gvp_version:" string seem specific to GVP files. We'll thus try reading a bunch of characters from the beginning of the file and look for the "gvp_version:" string.

.. code:: lua

    function probe()
        return string.match( vlc.peek( 512 ), "gvp_version:" )
    end

The **vlc.peek(** ** **)** function asks VLC to return the first characters. If the string "gvp_version:" isn't found in a file's first 512 characters, we're almost 100% sure that it's not a valid GVP file.

.. _parse-1:

Parse
^^^^^

We now need to read information from the file to create our new playlist item. A simple version would only fetch the URL:

.. code:: lua

    function parse()
        item = {}
        while true
        do
            line = vlc.readline()
            if not line
            then
                break
            end
            if string.match( line, "^url:" )
            then
                item.path = string.sub( line, 5 )
            end
        end
        return { item }
    end

We read all the file's lines using the **vlc.readline()** function. If we encounter the line starting with **"url:"** (*string.match( line, "url:" )* would match lines containing "url:", while *string.match( line, "^url:" )* only matches those starting with "url:"), we use that as our new item's path.

If vlc.readline() returns nil, this means that we've finished reading the file so we break out of the while loop and return our new playlist.

This simple **parse()** function unfortunately discards all the other useful meta information available in the GVP file. Lets try to use it:

.. code:: lua

    function parse()
        item = {}
        while true
        do
            line = vlc.readline()
            if not line
            then
                break
            end
            if string.match( line, "^url:" )
            then
                item.path = string.sub( line, 5 )
            elseif string.match( line, "^title:" )
            then
                item.name = string.sub( line, 7 )
            elseif string.match( line, "^duration:" )
            then
                item.duration = string.sub( line, 10 ) / 1000
            elseif string.match( line, "^description:" )
            then
                if item.description
                then
                    item.description = item.description .. "\n" .. string.sub( line, 13 )
                else
                    item.description = string.sub( line, 13 )
                end
            end
        end
        return { item }
    end

Getting the video's title works like the URL parameter. The duration is a bit more tricky. GVP uses times in milliseconds while VLC wants a time in seconds. We thus have to divide it by 1000. For the description, it works like the URL and title parameters except that a GVP file can have more than one description parameter. If we read more than one parameter we thus concatenate the different description lines.

Reference
---------

Information about the VLC Lua scripts is available in your VLC installation in the lua subdirectory.

-  `Global VLC Lua README <http://www.videolan.org/developers/vlc/share/lua/README.txt>`__
-  `Playlist script specific README <http://www.videolan.org/developers/vlc/share/lua/playlist/README.txt>`__

Scripts shipped with VLC
------------------------

Scripts for popular playlist formats and video websites are available in the default VLC installer:

-  dailymotion.lua: URL translation for Daily Motion video pages;
-  googlevideo.lua: URL translation for Google Video video pages;
-  metacafe.lua: URL translation for metacafe video pages and flash player;
-  youtube.lua: URL translation for YouTube video pages and flash player (including fullscreen video URLs);
-  youtube_hompage.lua: Parse YouTube homepage and browse page.

Useful links
------------

-  `Lua 5.1 reference manual <http://www.lua.org/manual/5.1/>`__
-  `Lua tutorials <http://lua-users.org/wiki/TutorialDirectory>`__

.. raw:: mediawiki

   {{Documentation}}

`Category:Playlist <Category:Playlist>`__
