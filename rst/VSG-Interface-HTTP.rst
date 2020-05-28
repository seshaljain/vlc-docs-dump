How To Start VLC Server with http Interface
-------------------------------------------

| VLC ships with a little HTTP server integrated. It is used both to stream using HTTP, and for the HTTP remote control interface.
| **Step 1: VLC Server Preferences Settings**

Set up the http interface details in the VLC server application: Open VLC, then select Tools > Preferences. In the bottom left corner of the window, under "Show settings", click "All".

-  In the left hand menu click on the + button next to Interface. This will display three choices. Control interfaces, Hotkeys settings, and Main Interfaces. Click "Main Interfaces". Select "HTTP remote control interface".
-  Click on the plus button next to "Main interfaces". This will display four settings HTTP, Qt, RC, Skins. Click on HTTP to display the "HTTP remote control interface" settings.
-  Host address: Enter the port number that you want to use. Default is 8080.
-  Source directory: If you have installed VLC in a different folder than the default, enter path\to\VLC\\http.
-  If you are NOT using handlers or SSL certificates the setup is complete.
-  Click on the Save button in the lower right hand of the window.
-  If needed, edit the .hosts file in the vlc/http directory. By default only "localhost" is allowed, edit to enable other hosts.
-  Exit and restart VLC

| 
| **Step 2: Command Line Startup**

The VLC appplication can be run in a server or client environment. For complicated video and audio streaming on a LAN, one should consider dedicating a machine to act as the VLC server.

To start the VLC application in a server mode with the http interface automatically set, use the following command line in your desktop shortcut. This assumes the default location for installation was selected.

::

   "C:\Program Files\VideoLAN\VLC\vlc.exe" --extraintf http --intf wx

| 
| **Step 3: Testing the Interface**

From another computer, connect to the VLC server computer using your browser to the URL

http://server_ip_address:8080, such as http://192.168.0.186:8080

The Main VLC Interface page will be displayed,

| See `Web Interface <Web_Interface>`__ for additional information.
| 
