{{See alsoVSG:ResetPrefs}} <gallery> File:ToolsPreferences-Windows
8.pngalt= File:Preferences-Windows 8.pngalt= File:Vlcmenu preferences
osx.pngalt= </gallery>

You can edit settings for VLC by navigating to the menu toolbar,
selecting Tools, and selecting Preferences (or by pressing
<kbd>Ctrl+P</kbd>). \* To save your preferences, click Save. \* To show
more options, switch the ''Show settings'' radio button to ''All''.

=== Configuration File ===

The preferences stated in the options are stored in a configuration
file. There is one configuration file per user, stored at: \* ''Unix,
Linux and BSD:'' <code>~/.config/vlc/vlcrc</code> since 0.9. Before it
was: <code>~/.vlc/vlcrc</code> \* ''macOS:''
<code>~/Library/Preferences/org.videolan.vlc/vlcrc</code> \*
''Windows:'' <code>%appdata%vlcvlcrc</code> is generic and is expanded
to: \*\* ''Windows 95/98/ME:'' <code>C:WindowsApplication
Datavlcvlcrc</code> \*\* ''Windows NT/2000/XP:'' <code>C:Documents and
Settings<username>Application Datavlcvlcrc</code> \*\* ''Windows
Vista/7/8/10:'' <code>C:Users<username>AppDataRoamingvlcvlcrc</code> \*
When used from the command line, sometimes there are unintended
conflicts with settings in the config file; to ignore the config file,
use: <code>--ignore-config</code>

==Your Preferences== To view/change your Wiki preferences go
[[Special:Preferences|here]].

[[Category:Documentation]]
