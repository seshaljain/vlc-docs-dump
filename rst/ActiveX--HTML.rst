.. raw:: mediawiki

   {{howto| use the [[ActiveX]] control within a webpage|nosort=yes}}

.. raw:: mediawiki

   {{Example code}}

Embedding Activex using Javascript
----------------------------------

You can insert the `ActiveX <ActiveX>`__ control in your HTML pages like this :

.. code:: html4strict

     <OBJECT classid="clsid:9BE31822-FDAD-461B-AD51-BE1D1C159921"
        codebase="https://downloads.videolan.org/pub/videolan/contrib/win32/axvlc.cab"
           width="640" height="480" id="vlc" events="True">
     <param name="Src" value="" />
     <param name="ShowDisplay" value="True" />
     <param name="AutoLoop" value="False" />
     <param name="AutoPlay" value="False" />
     </OBJECT>

Then, using JavaScript, you can select another source, or change the audio track :

.. code:: javascript

     document.vlc.playlistClear();
     var options=[":audio-track=5"]; // select audio track 5 (=6th, 1st is 0)
     document.vlc.addTarget("...",options,2,0); // replace entry 0
     document.vlc.play();

See http://people.videolan.org/~damienf/plugin-0.8.6.html\ `(Internet Archive) <https://web.archive.org/web/20081218063905/http://people.videolan.org/~damienf/plugin-0.8.6.html>`__ for a complete demo.

Embedding ActiveX using m3u Playlists
-------------------------------------

Maybe a better to show VLC in an HTML Website is to use `m3u <m3u>`__ Playlists. It has got the advantage that users with turned-off JavaScript can also use this plugin, since ``document.vlc.addTarget()`` won't work with JavaScript turned off.

-  Step 1: Create the HTML website with the VLC-Object linked to the m3u playlist
-  Step 2: Create your m3u playlist with all options, save and upload it to your webspace.
-  Step 3 (optional): Create buttons and other objects to `control VLC <control_VLC>`__ (like ``document.vlc.play();``)

**Step 1: Creating the website to embed ActiveX Control**

.. code:: html4strict

    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Frameset//EN" "http://www.w3.org/TR/html4/frameset.dtd">
    < HTML >
      <BODY marginwidth="0" marginheight="0" topmargin="0" leftmargin="0">
        <OBJECT classid="clsid:E23FE9C6-778E-49D4-B537-38FCDE4887D8"
            codebase="https://downloads.videolan.org/pub/videolan/contrib/win32/axvlc.cab"
            width="400" height="300" id="vlc" events="True">
          <param name="Src" value="myplaylist.m3u" />
          <param name="ShowDisplay" value="True" />
          <param name="AutoLoop" value="True" />
          <param name="AutoPlay" value="True" />
          <param name="Volume" value="100">
        </OBJECT>
      </BODY>
    < /HTML >

You should modify the values of width, height and volume (0-100) fitting to your desires. If you don't know them, simply delete them (e.g. remove ``width="640"`` from the code).

**Step 2: Creating the m3u playlist**

Open Notepad, create your playlist and save it as 'myplaylist.m3u' for this example.

| ``#EXTM3U                                     // Required to identify this file as m3u file``
| ``#EXTVLCOPT--input-repeat=-1                 // repeat the following file/playlist``
| ``#EXTVLCOPT--http-reconnect=true             // required for a streaming-client to enable repeat``
| ``#EXTVLCOPT--any further parameter goes here // see also ``\ ```VLC``\ ````\ ``command-line``\ ````\ ``help`` <VLC_command-line_help>`__
| ``#EXTINF:0, Test Description                 // set the title for the following file shown in your playlist``
| ``video.mpg                                // the actual file to be displayed``

**Annotations:**

-  For actual looping of the entire playlist, the user has to have check 'Repeat all' under Preferences --> Playlist --> General
-  Mind that options have different names if you play a file locally or if you want to stream it (--sub-filter --> --s-filter)

**Mind the different Options-styles:**

| `` --option  A global option that is set for the duration of the program.``
| ``  -option  A single letter version of a global --option.``
| ``  :option  An option that only applies to the playlistitem directly before it``
| ``           and that overrides previous settings.``

Known Problems and how to solve them
------------------------------------

**Problem**

A know problem is, that the VLC-Plugin won't be displayed. Instead, you are asked whether you want to install the VLC-ActiveX-Component. "Don't install" cancels the installation and nothing happens. "Install" runs the usual VLC-Setup (mind to install the ActiveX-Plugin), but after reopening an HTML-page with the VLC-Plugin, it's the same situation as before.

**Solution**

-  Use the "other" ClassID in your HTML-Source as shown above:

:

.. code:: html4strict

    <OBJECT classid="clsid:9BE31822-FDAD-461B-AD51-BE1D1C159921" ...

-  You have to lower the security settings on your PC. **Do this at your own risk! Use**\ `Firefox <https://www.getfirefox.com>`__\ **to browse the web!**

-  In Internet Explorer select [Tools], [Internet Options]. The "Internet Options" window opens. Select the Tab "Advanced". Scroll down until you see the main point "Security".

-  Check the following entries:

   -  Allow active content to CDs to run on My Computer
   -  Allow active content to run in files on My Computer
   -  Allow software to run or install even if the signature is invalid

-  Instead of lowering security level, you can add the website address to the right security area.

See also
--------

-  `ActiveX/Delphi <ActiveX/Delphi>`__ for a Delphi implementation
-  `ActiveX <ActiveX>`__ for a description of ActiveX

`Category:Development‏‎ <Category:Development‏‎>`__
