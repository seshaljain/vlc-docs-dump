Here you can find my VLC related notes and ideas. It's primarily for me
so that I don't forget things. ;D

== Deutsche Übersetzung == Media Kontextmenü: *"Wiedergabe mit VLC" =>
"Mit VLC wiedergeben"*"Zur VLC's Wiedergabeliste hinzufügen" => "Zu
VLC-Wiedergabeliste hinzufügen"

Menüs: *Extras->"Vollbildsteuerung" => "Vollbild" (wie
Firefox)*\ Medien->"Advanced open file" => "" ('''NICHT ÜBERSETZT''')

In Goldeneye: *"Systray-Icon" => "Kontrolleisten-Icon anzeigen"
(Pidgin)*"Audio aktivieren" => "Audioausgabe aktivieren" *"Video
aktivieren" => "Videoausgabe aktivieren"*"Vollbild" (Im einfachen Modus;
"Vollbildausgabe" im Alle-Modus) => "Im Vollbildmodus starten"
\*"Beschleunigte Videoausgabe (Overlay)" (im einfachen Modus;
"Videoausgabe überlagern" im Alle-Modus) => "Videoausgabe beschleunigen
(Overlay benutzen)"

== Misc. == Menus: *Extras->"Media info", Extras->"Codec info"*\ \*
Duplicate functionality: First one already allows for switching to
second one '''[DUP]''' *Media->"Open file", Media->"Advanced open
file"*\ \* Duplicate functionality: Second one always opens as file
selection dialogue, which is exactly what the first one provides
'''[DUP]'''

== TODO == \* <s>Think about applying for [[SoC 2008]]. [[SoC
2008#Fullscreen_Controller|Fullscreen Controller]] looks tasty!</s>
Gone! Resort to wiki editing :-( \* <s>Read ''C++ Primer''</s> Bad
choice; read TC++PL instead \* Get and read ''C++ GUI Programming with
Qt 4'' \*\* Ha! Free version
[http://www.qtrac.eu/C++-GUI-Programming-with-Qt-4-1st-ed.zip here].

=== Fullscreen controller polishing === Style the fullscreen controller
with [http://doc.trolltech.com/4.4/stylesheet.html Qt Style Sheet] to
make it look more like
[http://download.videolan.org/vlc/screenshots/0.8.6/VLC-mac-Fullscreen.jpg
the one on OS X]. \* Supports: \*\*
[http://doc.trolltech.com/4.4/stylesheet-examples.html#customizing-a-qpushbutton-using-the-box-model
Round corners] \*\* Transparency (specify <tt>background-color</tt> as a
rgba color) \*\* More things to ponder on?

Alternative: Use a
[http://web.archive.org/web/20080410001552/http://trolltech.com/products/qt/addon/solutions/catalog/4/Widgets/qtpiemenu/
pie menu]!

=== Improve translation process === Get in touch with the polish
translators what the heck
[http://translate.sourceforge.net/wiki/decathlon/mainpage?redirect=1
Pootle] is good for. '''[DONE!]''' :''Nice, but Problem is that you
can't export to one file without help from the admin.'' '''''Is this
still the case?''''' --[[User:Materthron|materthron]] 17:58, 4 January
2009 (CET)

Migrate to [http://www.transifex.net/ Transifex]?
