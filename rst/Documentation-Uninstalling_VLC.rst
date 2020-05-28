.. raw:: mediawiki

   {{RightMenu|Documentation TOC}}

Windows |Windows-logo.jpg|
--------------------------

You can uninstall VLC from *Add/Remove Programs* (*Programs and Features* in Windows 7) located in the *Control Panel*. Search for VLC media player and right click, then select "Uninstall/Change". Follow the prompts to finish the uninstallation.

.. figure:: Remvlc.jpg
   :alt: centre
   :width: 600px
   :height: 422px

   centre

Alternatively, you can browse to VLC's installation directory (for a typical install, go to your *C: Drive* and look for Program Files (if 64-bit, Program Files (x86) )→VideoLAN→VLC and double-click on the *uninstall* link and follow the prompts to uninstall.

.. figure:: Winunvlc.png
   :alt: centre
   :width: 600px
   :height: 422px

   centre

macOS |Applelogo.jpg|
---------------------

Drag the VLC application to your trash can. You can also remove the configuration file and the cache files in **~/Library/Preferences/VLC/**. There is an AppleScript on the disk-image which lets you do this automatically.

If that did not work, you can double-click on the *Applications* icon. This will bring up a list of all applications on your Mac. Scroll through the list of Applications, then press and hold the *Ctrl* button to bring up a table of options and actions. Click on "move to trash".

Finally, if the previous processes failed, you can try downloading a third-party uninstaller program to uninstall it, such as `AppCleaner <http://www.macupdate.com/app/mac/25276/appcleaner>`__.

.. figure:: Appcleaner.png
   :alt: Appcleaner.png
   :width: 300px
   :height: 200px

   Appcleaner.png

Linux
-----

Debian |Debian.png|
~~~~~~~~~~~~~~~~~~~

Remove the packages that you installed:

``# ``\ **``apt-get``\ ````\ ``remove``\ ````\ ``--purge``\ ````\ ``vlc``\ ````\ ``libdvdcss2``**

Ubuntu |Ubuntulogo.png|
^^^^^^^^^^^^^^^^^^^^^^^

Remove *VLC Media Player* by entering this command in the Terminal.

``$ ''' sudo apt-get remove vlc '''``

Or you can also search *VLC* in the *Ubuntu Software Center* and click on *Remove* to uninstall it.

.. figure:: Ubunvlc.png
   :alt: Ubunvlc.png
   :width: 550px
   :height: 500px

   Ubunvlc.png

Red Hat and SuSE |Redhat.jpg|\ |Suse-Logo.png|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Uninstall the RPM packages that you installed:

``# ``\ **``rpm``\ ````\ ``-e``\ ````\ ``vlc-version``\ ````\ ``vlc-mad-version``\ ````\ ``wxvlc-version``\ ````\ ``libdvdcss2-version``\ ````\ ``libdvdpsi1-version``**

Compiled the sources by yourself
--------------------------------

Go to the directory containing VLC sources and execute

``# ``\ **``make``\ ````\ ``uninstall``**

You can then remove the VLC sources.

.. raw:: mediawiki

   {{Documentation}}

.. |Windows-logo.jpg| image:: Windows-logo.jpg
   :width: 40px
   :height: 40px
.. |Applelogo.jpg| image:: Applelogo.jpg
   :width: 40px
   :height: 40px
.. |Debian.png| image:: Debian.png
   :width: 40px
   :height: 40px
.. |Ubuntulogo.png| image:: Ubuntulogo.png
   :width: 45px
   :height: 45px
.. |Redhat.jpg| image:: Redhat.jpg
   :width: 40px
   :height: 40px
.. |Suse-Logo.png| image:: Suse-Logo.png
   :width: 35px
   :height: 35px
