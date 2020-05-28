This page will help you compile **VLC for WinRT**

Development Environment
-----------------------

To develop VLC for WinRT, you would need to have:

-  Windows 8.1
-  Visual Studio 2013 with Update 2 (or Update 3)
-  Windows 8.1 SDK (Recommended)
-  Latest version of `Git <Git>`__
-  Lots of patience :D

Get the source
--------------

You can clone the VLC for WinRT git repository

``git clone ``\ ```https://code.videolan.org/videolan/vlc-winrt.git`` <https://code.videolan.org/videolan/vlc-winrt.git>`__

Get libVLC source
-----------------

Packaged 7zip file
^^^^^^^^^^^^^^^^^^

You can download vlc.7z from `here <http://people.videolan.org/~hugo/vlc-Win32.7z>`__. Extract the contents of vlc.7z and copy the contents to vlc folder of winrt source code

Cross Compiling
^^^^^^^^^^^^^^^

If you feel adventurous, you can try cross-compiling libVLC for WinRT. Refer to the `README <https://code.videolan.org/videolan/vlc-winrt>`__ file in the source folder for more information

Build and Deploy
----------------

-  Open the VLC_WinRT solution in app/VLC_WINRT.sln
-  Open Package.appxmanifest, and generate a test certificate. More information can be found in the `README <https://code.videolan.org/videolan/vlc-winrt/blob/master/README>`__ file in the source folder
-  Click on Build Solution and then Deploy

Additional Notes
----------------

-  If building fails with lots of errors referring to Windows SDK headers, installing Windows 8.1 SDK usually helps
-  It helps to right click the specific project (eg: Windows 8.1 project ) and then click deploy rather than trying to deploy the whole solution

`Category:Building <Category:Building>`__ `Category:Mobile documentation <Category:Mobile_documentation>`__ `Category:Windows <Category:Windows>`__
