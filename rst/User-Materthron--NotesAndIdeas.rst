Here you can find my VLC related notes and ideas. It's primarily for me so that I don't forget things. ;D

Deutsche Übersetzung
--------------------

Media Kontextmenü:

-  "Wiedergabe mit VLC" => "Mit VLC wiedergeben"
-  "Zur VLC's Wiedergabeliste hinzufügen" => "Zu VLC-Wiedergabeliste hinzufügen"

Menüs:

-  Extras->"Vollbildsteuerung" => "Vollbild" (wie Firefox)
-  Medien->"Advanced open file" => "" (**NICHT ÜBERSETZT**)

In Goldeneye:

-  "Systray-Icon" => "Kontrolleisten-Icon anzeigen" (Pidgin)
-  "Audio aktivieren" => "Audioausgabe aktivieren"
-  "Video aktivieren" => "Videoausgabe aktivieren"
-  "Vollbild" (Im einfachen Modus; "Vollbildausgabe" im Alle-Modus) => "Im Vollbildmodus starten"
-  "Beschleunigte Videoausgabe (Overlay)" (im einfachen Modus; "Videoausgabe überlagern" im Alle-Modus) => "Videoausgabe beschleunigen (Overlay benutzen)"

Misc.
-----

Menus:

-  Extras->"Media info", Extras->"Codec info"

   -  Duplicate functionality: First one already allows for switching to second one **[DUP]**

-  Media->"Open file", Media->"Advanced open file"

   -  Duplicate functionality: Second one always opens as file selection dialogue, which is exactly what the first one provides **[DUP]**

TODO
----

-  Think about applying for `SoC 2008 <SoC_2008>`__. `Fullscreen Controller <SoC_2008#Fullscreen_Controller>`__ looks tasty! Gone! Resort to wiki editing :-(
-  Read *C++ Primer*\  Bad choice; read TC++PL instead
-  Get and read *C++ GUI Programming with Qt 4*

   -  Ha! Free version `here <http://www.qtrac.eu/C++-GUI-Programming-with-Qt-4-1st-ed.zip>`__.

Fullscreen controller polishing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Style the fullscreen controller with `Qt Style Sheet <http://doc.trolltech.com/4.4/stylesheet.html>`__ to make it look more like `the one on OS X <http://download.videolan.org/vlc/screenshots/0.8.6/VLC-mac-Fullscreen.jpg>`__.

-  Supports:

   -  `Round corners <http://doc.trolltech.com/4.4/stylesheet-examples.html#customizing-a-qpushbutton-using-the-box-model>`__
   -  Transparency (specify ``background-color`` as a rgba color)
   -  More things to ponder on?

Alternative: Use a `pie menu <http://web.archive.org/web/20080410001552/http://trolltech.com/products/qt/addon/solutions/catalog/4/Widgets/qtpiemenu/>`__!

Improve translation process
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get in touch with the polish translators what the heck `Pootle <http://translate.sourceforge.net/wiki/decathlon/mainpage?redirect=1>`__ is good for. **[DONE!]**

   *Nice, but Problem is that you can't export to one file without help from the admin.*

**Is this still the case?** --`materthron <User:Materthron>`__ 17:58, 4 January 2009 (CET)

Migrate to `Transifex <http://www.transifex.net/>`__?
