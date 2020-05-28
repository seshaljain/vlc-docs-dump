==easy discuss/talk here==

-  Welcome ! [[User:J-b|jb]] 10:44, 19 February 2008 (CET)
-  Will attend the dev days 08 (on Saturday) :)

==TODO list==

=== Wiki Pages ===

\* [[Trac]] or [[Bug Tracker]] explanation (account validation, etc)
\*\* @see [[Report_bugs]] [[VLC_report]]

\* Backtraces with those chapters (for now, inside [[debug]] page) \*\*
What backtraces are **\* Rely on accurate release/commit ID** get
backtraces **\* Requirements**\ \* Basic use of [[gdb]] to debug {{VLC}}
**\* Windows gdb how to**\ \* libvlc and web plugins debug how to \*\*
How to embed backtraces in (trac, wiki, IRC, emails) \*\* links (gdb,
[[Report bugs]], etc) \* NB: asked page: "-enable-[[debug]]"

=== global===

(the newest the upper) {\| class="wikitable" ! Category !! Actions !!
States !! comment feature \|\| add a "ts-pid-pmt=pid" CLI option \|\|
{{no}} \|| To easily support streams without PAT, etc doc \|\| improve
[[Win32Compile]] to add NSI chapter \|\| {{no}} devel \|\| don't fail in
NSI (Windows installer generation) when a feature is disabled \|\|
{{ok}} \|\| to be tested and proposed doc \|\| update [[OSXCompile]]
page (from discuss at least) \|\| maybe won't do devel \|\| compile for
MacOS X \|\| maybe won't do documentation \|\| webplugin HTML params
\|\| {{no}} priv \|\| Understand fetch, pull, merge, branch under Git|\|
{{ok}} feature \|\| enable fullscreen control on web plugins \|\| {{no}}
feature \|\| allow hiding control toolbar (for mozplug X11) \|\| {{ok}}
test \|\| Test activeX API \|\| {{partial}} test \|\| Test mozplug API
\|\| {{Partial}} test \|\| List APIs for ActiveX \|\| {{no}} test \|\|
List APIs for mozplug \|\| {{Ok}} devel \|\| Suscrib to the MailingList
and the Wiki (create account...) \|\| {{yes}} devel \|\| Suscrib to the
Google group (vlc-mozplug-friends) \|\| {{yes}} devel \|\| Go to the IRC
channel (#videolan) \|\| {{yes}} devel \|\| Build the latest git version
of VLC (0.9) (windows & debian Etch) \|\| {{yes}} \|}

==clipboard/reminder==

===public clipboard=== ''Feel free to past some links you seems
interesting for me.''

'' not yet seen :'' ----''seen :''

===private clipboard===

\*irc, to avoid sec policy <xtophe> --security-policy=1

-  [[HowTo_Integrate_VLC_plugin_in_your_webpage]]
-  [[Documentation:Play_HowTo/Advanced_Use_of_VLC#The_Mozilla_plugin]]

..

   ./include/vlc_messages.h:148:#define msg_Dbg( p_this, ... ) msg_Dbg(
   p_libvlc, COPYRIGHT_MESSAGE ); msg_Dbg( p_libvlc, "libvlc was
   configured with %s", CONFIGURE_LINE );

   msg_Info( p_this, ... ) msg_Err( p_this, ... ) msg_Warn( p_this, ...
   ) msg_Dbg( p_this, ... )

== ideas ==

Isn't madness the origin of our lives?

\* '''bash completion''' config for VLC command line :p \*\* something
exists in extra/ for zsh completion. \*\* begin from a docbok to
generate a man page t \* stable '''unit-tests for web plugins'''
(Javascript?) usable in command-line ''(doesn't have the "how" yet in
mind)'' \* environment to help using '''automated git bissect''',
"pluggable" to webplugins unit-test CLI ''(wahoo yeah, dreaming :) )''
\* (low) '''split file sout''' parameter (roll files with an index and a
max time/size for each chunk) \* on mozplug X11, conditional embedded
controls (play, pause, ..): done, optionnal now.
