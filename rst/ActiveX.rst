{{Example code}}

The [[Windows]] build of VLC includes an (optionaly installed)
'''ActiveX control'''. The ActiveX control enables VLC to be embedded in
web browsers and third-party applications.

==Important== The API described in this page only reflects VLC ActiveX
controls prior to 0.8.5.1. This API will be removed soon.

'''It is {{font colournot advised}} to use this JS API any longer.'''

Please use the VLC ActiveX v2 interface as described in the new
[[Documentation:WebPlugin|documentation]].

The new JS API interface is exactly the same for Internet Explorer,
Mozilla/Firefox and Safari. Thus easing the maintenance and developing
of webpages for the VLC browser plugins.

==Properties== <!--NOTE TO EDITORS! PLEASE LEAVE THE SYNTAX AS VB (6 or
98, not .net or 2005). IF NEEDED, WE SHOULD CREATE A SEPERATE SECTION
FOR EACH LANGUAGE/VARIANT AND LINK TO IT. --> The ActiveX control
includes the following properties: {\| '''''type'''''
'''''description''''' Length get - Returns the count of items in the
playlist playlistIndex \| Returns the index of the current item in the
playlist. AutoLoop get/set -Boolean Determines if the player should
start playing a new file/playlist immediately upon being loaded. Volume
get/set -String Presumably returns the MRL of the currently loaded
file.<!-- readme says "initial MRL in playlist" --> Time get/set
-Boolean show/hide control viewport<!-- from readme --> Playing get
-'real' Playback position within current MRL, scaled from 0.0 to 1.0.
Live feed returns 0.0 VersionInfo get } Note: In Visual Basic, type
"Long" should be used for properties listed with type "Integer".

==Methods== The ActiveX control includes the following methods
(functions): {\| '''''type''''' '''''syntax ([[wikipedia:Visual
Basic-method controlname.setVariable name as String, value getVariable
Returns the contents of a variable that is defined in libvlc.c -method
controlname.pause play Plays as in the normal player, if a clip is not
loaded, does nothing. -method controlname.playFaster playSlower Makes
the currently playing clip play slower. -method controlname.stop shuttle
Moves the playback position a specified number of seconds in either
direction. -method controlname.playlistClear playlistNext Goes to next
item in the playlist -method controlname.playlistPrev addTarget Adds a
uri to the current playlist or replaces the current playlist with the
uri. -method controlname.toggleMute fullscreen Toggles between
fullscreen and non-fullscreen modes. }

==Options== The <code>addTarget</code> method accepts most of the
command line options; including, but not limited to, the following :
*<code>:audio-track=''index''</code>*\ <code>:vout-filter=''output-filter''</code>
(<code>deinterlace</code> for example)
\*<code>:deinterlace-mode=''mode''</code> (<code>linear</code> for
example)

==Samples== \*[[ActiveX/Delphi|Delphi Implementation]]

-  [[ActiveX/HTML|HTML Implementation]]

==Installing== ===Introduction===

VideoLAN is not a good source for the installation of VLC through an
ActiveX control. At some point, Microsoft Internet Explorer stopped
allowing the installation of ActiveX controls unless: \* they were
signed to associate the software vendor's name with the file containing
the ActiveX control, or \* they resided in an "trusted site" (from the
user's perspective, running Internet Explorer) The second option is only
feasible where both server and client infrastructure are managed under
the same umbrella, i.e. where the server providing the ActiveX control
can be declared "trusted". This is not feasible in the open web. In a
web configuration, a [http://en.wikipedia.org/wiki/Certificate_authority
Certificate Authority] needs to digitally sign the ActiveX control. This
comes at a cost which the VideoLAN project is not able to bear. The
solution is to create one's own ActiveX control distribution, which in
turn can be digitally signed by a Certificate Authority of your choice,
if necessary.

===Creating an VLC ActiveX Distribution=== The following requisites are
required: \* CABSDK by Microsoft to create a
[http://en.wikipedia.org/wiki/Cabinet_%28file_format%29 Cabinet File]
(.cab-file) containing the relevant ActiveX control and VLC files. MSDN
has [http://msdn2.microsoft.com/en-us/library/aa751974.aspx a good
description how to package an ActiveX Control], including a link to the
CABSDK download page. \* The .cab-file is a special form of a .zip file,
consisting of: \*\* axvlc.inf - The INF file, which would be called
manifest in the modern age \*\* axvlc.dll - ActiveX DLL which bootstraps
the VLC setup file \*\* vlc-0.8.6e-win32.exe - VLC setup file (refer to
your version)

I am using the following code in the INF file: <syntaxhighlight
lang="ini"> ; Version number and signature of INF file. ; [version]
signature="$CHICAGO$" AdvancedINF=2.0

[Add.Code] vlc-0.8.6e-win32.exe axvlc.dll=axvlc.dll

[axvlc.dll] FileVersion=0,8,6,0
clsid={9BE31822-FDAD-461B-AD51-BE1D1C159921} RegisterServer=no
hook=nsiinstaller

[vlc-0.8.6e-win32.exe] FileVersion=0,8,6,0 file-win32-x86=thiscab

[nsiinstaller] run=%EXTRACT_DIR%vlc-0.8.6e-win32.exe </syntaxhighlight>
Again, refer to your version of VLC.

You can extract axvlc.dll from the binary distribution of VLC. This is a
zip file on VideoLAN's download page, version 0.8.6.e
[http://downloads.videolan.org/pub/videolan/vlc/0.8.6e/win32/vlc-0.8.6e-win32.zip
here].

The regular VLC setup file is the "featured" download on VideoLAN's main
page; a copy resides in the same directory as axvlc.dll, the VLC setup
file of version 0.8.6.e
[http://downloads.videolan.org/pub/videolan/vlc/0.8.6e/win32/vlc-0.8.6e-win32.exe
here].

With CABSDK installed and the three components in place, you can create
the .cab-file using the CABARC tool from Microsoft's CABSDK, using the
following command from a command prompt:

   {{Prompt|cmd}} CABARC.EXE N axvlc.cab axvlc.inf axvlc.dll
   vlc-0.8.6e-win32.exe

This assumes the [[wikipedia:Path (computing)|PATH]] has been set to
CABARC.EXE's directory. If you need to sign the .cab-file, you need to
use the -s switch to allocate space for your digital certificate.

===.cab-file Integration=== The .cab file is integrated as described in
the [[#Samples|samples above]], using the <OBJECT> element in the case
of HTML, for example. When the ActiveX Control is called for the first
time, i.e. prior to VLC installation through any means, the setup
program should start up. Unfortunately, users have to click through a
few dialogs, "allow blocked contents" or deal with other inconveniences,
depending on your configuration and the user's security settings of
Internet Explorer. The user must have proper rights to install VLC on
the user's computer; identical to a regular installation of VLC as
required by the VLC setup program.

==See Also== \* {{VLCSourceFilelabel=Official ReadMe}}

[[Category:Development‏‎]]
