{{howto|To use {{VLC}} with a Creative brand remote control on Windows
XP}} This guide describes the steps required to configure Creative brand
remotes that come with Creative sound cards to work with VLC.

This should be compatible with any Creative brand sound card and remote.
Creative Remote Center is the application that recieves and passes
remote commands to other applications, and it is therefore necessary to
install and run. It translates key presses on the remote into
application commands through the use of key files. Exact keymap settings
are not given because they vary by remote model and how the VLC hotkeys
are mapped.

== Open (your remote).RCI file == From the installation directory of
Creative Remote Center, navigate to <code>/Rc/RCRx</code>.

There will probably be several files with the '''.rci''' file extension.
Open the one that matches the model number of your remote with any text
editor such as Notepad.

Each set of four lines represent one button recognized by the remote.
There are two values you will need for each button:
<code>MMCDEvent</code> number, and <code>KeyName</code>.

<pre> [RCKeyCode########] A button on the remote control. MMCDEvent=####
The code sent by the remote when that button is pressed.
KeyName=''String'' Identifies the button pressed. OneShot=# Send
multiple signals while button is held down (volume, for instance) or
just a single button press signal. </pre>

== Create <code>wxWindowClassNR.key</code> file == Creative Remote
Center sends application commands from the remote through key files. If
there is a key file with the same name as the window that currently has
focus, Remote Center will be able to send commands to it.

VLC uses <code>wxWindowClassNR</code> as the main application window.
Create a key file with that name in order to control it with Remote
Center.

From the Creative Remote Center install directory, navigate to
<code>/Rc/KeyMap</code> and create a file called
<code>wxWindowClassNR.key</code>. This file will contain the keymap to
control VLC. It will look like a windows registry file, but just open it
with a text editor.

== Make the file header == The first seven lines of every key file is
nearly identical. Only the second line is important. It identifies which
window this key file is going to control. It should be identical to the
name of the file.

Copy and paste this into the beginning of the <code>wxWindowClassNR.key
file</code>:

<pre> [RC Key Map Information] Name=wxWindowClassNR Version=1.30
By=Creative Technology Ltd. Company=Creative Technology Ltd.
Copyright=Copyright (C) 2001 Creative Technology Ltd. All Rights
Reserved. Comments= </pre>

== Keymap entries == The next section of the key file will be keymap
entries.

Keymap format: <pre> [KeyEvent####] #### corresponds to an MMCDEvent
number in the .RCI file. KeyName=''String'' ''String'' is displayed via
the Remote Center On Screen Display when you press the button.
Notification=# # can be one of several values, but for our purposes
should be -1 or possibly 2. Details later. KeyEventRemap=## ## is a
value that corresponds to the keyboard key you want the button mapped
to. </pre>

<pre> Notification values: -1 - Sends the KeyEventRemap value to the
window that has focus. ASCII decimal format. 2 - Sends the KeyEventRemap
value to the highlighted window. non-ASCII format. {3,4,5} - Used in the
Default.key key file. Don't use these! </pre>

Use <code>Notification=-1</code> for simple keyboard keys that have an
ASCII representation.<br> Use <code>Notification=2</code> for key
combinations involving '''Ctrl''', '''Alt''', and '''Shift'''. Not all
of the non-ASCII codes are known because Creative has not released the
information, however some people have worked on discovering the values.
[http://forums.creative.com/creativelabs/board/message?board.id=soundblaster&message.id=87188#M87188
A partial list of notification=2 codes].

A full keymap entry will look like this: <pre> [KeyEvent6906]
KeyName=Kill All Humans Notification=-1 KeyEventRemap=32 </pre>

This entry maps the ''6'' button on a remote (MMCDEvent 6906) to the
keyboard key ''Space Bar'' (ASCII 32) and displays '''Kill All Humans'''
(key name) when using VLC.

Whether that does anything in VLC depends on if the space bar is
configured to do anything in VLC. If fullscreen mode is mapped to the
''space bar'', then pressing the ''6'' on the remote would toggle
fullscreen mode and display '''Kill All Humans'''.

== Map entries to the key file == From VLC, open the preferences and
look at the Hotkey settings. For the commands you want to map to the
remote, look up the Hotkey's ASCII representation or (for complex
commands) <code>notification=2</code> representation.

For each button you want to map, follow the keymap format. Not hard, but
probably the most tedious step.

== <code>VLC DirectX.key</code> file == Create an identical keymap file
to <code>wxWindowClassNR.key</code> and name it <code>VLC
DirectX.key</code>. Change the second line in the file to <code>Name=VLC
DirectX</code>.

This file ensures control of VLC when in fullscreen mode. This second
file enables control of the fullscreen window. The fullscreen window has
focus instead of the main application window while in fullscreen mode.
This prevents control of the main application window with the remote.

== Final Note == The method outlined here is useful for control of any
application with a Creative brand remote. The only requirement is that
you know the internal window name. I used Spy++ to get the window class
names for VLC (<code>wxWindowClassNR</code> and <code>VLC
DirectX</code>) and it's easy enough to get the names for any others.

== Update! == In version 0.9.8a, and maybe earlier, the window class
name has been changed to <code>VLC</code>, so you should replace every
instance of <code>wxWindowClassNR</code> with <code>VLC</code>.
<code>VLC DirectX</code> has remained the same, though.

== See also == [http://forum.videolan.org/viewtopic.php?t=31022 Original
post on VideoLAN Forum]<br>
[http://forums.creative.com/creativelabs/board/message?board.id=soundblaster&message.id=41756
Creative Labs Soundblaster Forum thread]

[[Category:Control VLC]]
