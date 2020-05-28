.. raw:: mediawiki

   {{RightMenu|Documentation TOC}}

There are VLC binaries available for the many `OSes <OS>`__, but not for all supported ones. If there are no binaries for your OS or if you want to change the default settings, you can compile VLC from `source <GetTheSource>`__.

|Windows_logo2.jpg| Windows
---------------------------

95, 98, ME
~~~~~~~~~~

You can install VLC on Windows 95, 98, or ME operating systems by using `KernelEx <http://kernelex.sourceforge.net/wiki/Main_Page>`__.

2000, XP, Vista, 7, 8, 10
~~~~~~~~~~~~~~~~~~~~~~~~~

Recommended
^^^^^^^^^^^

The normal and recommended way to install VLC on a Windows operating system is via the installer package.

**Step 0: Download and launch the installer**

Download the installer package from the `VLC download page for Windows <https://www.videolan.org/vlc/download-windows.html>`__. After you download the installer package, double click on the file to begin the install process. If you're using Windows Vista, 7, 8 or 10 and have UAC (User Account Control) enabled, the operating system may prompt you to grant VLC administrator permissions. Click **Yes** to continue the installation process.

**Step 1: Select an installer language**

Before you can continue, you must select the language that you want the installer to use to display information to you. After you select a language, click **OK**.

.. figure:: Step-1-select-language.png
   :alt: Step-1-select-language.png

   Step-1-select-language.png

**Step 2: Review the Welcome screen**

The VLC installer recommends that you close all other applications before continuing the installation process. When you're ready to proceed with the installation process, click **Next**.

.. figure:: Step-2-welcome.png
   :alt: Step-2-welcome.png

   Step-2-welcome.png

**Step 3: Read License agreement**

Read the Terms of Service. Once you're done reading, click **Next**.

.. figure:: Step-3-licence.png
   :alt: Step-3-licence.png

   Step-3-licence.png

**Step 4: Select components**

Use this menu to customize your install. Choose all of the components you wish to install and whether you want VLC to be your default media player or not. Once you are done, click **Next**.

.. figure:: Step-4-components.png
   :alt: Step-4-components.png

   Step-4-components.png

**Step 5: Pick a location**

Click **Browse...** to choose the destination installation folder. After you've identified the desired folder, click **Install**.

.. figure:: Step-5-install-location.png
   :alt: Step-5-install-location.png

   Step-5-install-location.png

**Step 6: Now installing**

Wait as VLC is installed on your machine. It shouldn't take too long. Then click "Show details" to see more information about the progress of the installation.

.. figure:: Step-6-installing.png
   :alt: Step-6-installing.png

   Step-6-installing.png

**Step 7: Installation complete**

Once installation is complete, you may choose to run VLC or read VLC's release notes. Click **Finish** to complete the installation process and close the installer.

.. figure:: Step-7-completed.png
   :alt: Step-7-completed.png

   Step-7-completed.png

Alternative
^^^^^^^^^^^

If you want to perform an unattended (or silent) installation of VLC, you can do so via a `command-line interface <command-line_interface>`__. Type in "*filename*" /L="*languagecode*" /S. For example, the English installation would look something like **vlc-2.0.1-win32.exe /L=1033 /S**.

**PowerShell**

Installing VLC using PowerShell is as easy.

.. figure:: Step-8-silent-installation-ps.png
   :alt: Step-8-silent-installation-ps.png
   :width: 669px

   Step-8-silent-installation-ps.png

**Command Prompt**

You can also install VLC using the command prompt.

.. figure:: Step-9-silent-installation-cmd.png
   :alt: Step-9-silent-installation-cmd.png

   Step-9-silent-installation-cmd.png

|Applelogo.jpg| macOS
---------------------

#. Download the macOS package from the `VLC macOS download page <https://www.videolan.org/vlc/download-macosx.html>`__.
#. Double-click on the icon of the package: an icon will appear on your Desktop, right beside your drives.
#. Open it and drag the VLC application from the resulting window to the place where you want to install it (it should be **/Applications**).

Note: You may need to delete older versions of VLC on your computer before you can successfully install the latest version.

Linux
-----

|Debian-logo.jpg| Debian
~~~~~~~~~~~~~~~~~~~~~~~~

Download page: https://www.videolan.org/vlc/download-debian.html

**A standard install without libdvdcss:**

| \ `` apt-get update``
| \ `` apt-get install vlc ``\ 

Or search for ``vlc`` with the graphical package manager you like best. It should be in the main Debian repository in the section *Video software*. Additional plugins are available and most require manual selection, e.g. ``vlc-plugin-access-extra``, ``vlc-plugin-notify`` and ``vlc-plugin-jack``.

**For a standard install with libdvdcss:**

A simple install of the `libdvdcss <libdvdcss>`__ package can be found here: https://download.videolan.org/debian/stable/, but for future bug fixes add the following lines to your **/etc/apt/sources.list**:

.. code:: apt_sources

    deb https://download.videolan.org/debian/stable stable main
    deb-src https://download.videolan.org/debian/stable stable main

Then:

| \ `` apt-get update``
| \ `` apt-get install vlc libdvdcss2 ``\ 

This will allow you to decrypt `DVDs <DVD>`__.

|Ubuntulogo.png| Ubuntu
^^^^^^^^^^^^^^^^^^^^^^^

Links: `Download page <https://www.videolan.org/vlc/download-ubuntu.html>`__ • Launchpad (`Source <https://launchpad.net/ubuntu/+source/vlc/>`__ • `Bugs sorted by most users <https://bugs.launchpad.net/ubuntu/+source/vlc/+bugs?field.searchtext=&orderby=-users_affected_count&search=Search&field.status%3Alist=NEW&field.status%3Alist=CONFIRMED&field.status%3Alist=TRIAGED&field.status%3Alist=INPROGRESS&field.status%3Alist=FIXCOMMITTED&field.status%3Alist=INCOMPLETE_WITH_RESPONSE&field.status%3Alist=INCOMPLETE_WITHOUT_RESPONSE&assignee_option=any&field.assignee=&field.bug_reporter=&field.bug_commenter=&field.subscriber=&field.tag=&field.tags_combinator=ANY&field.status_upstream-empty-marker=1&field.upstream_target=&field.has_cve.used=&field.omit_dupes.used=&field.omit_dupes=on&field.affects_me.used=&field.has_patch.used=&field.has_branches.used=&field.has_branches=on&field.has_no_branches.used=&field.has_no_branches=on&field.has_blueprints.used=&field.has_blueprints=on&field.has_no_blueprints.used=&field.has_no_blueprints=on>`__ • `Questions <https://answers.launchpad.net/ubuntu/+source/vlc>`__)

Launch the Ubuntu Software Center and go to **All Software → Sound & Video** then in search VLC Player. After it will come click on it and it will automatically install

You need to check that a universe mirror is listed in your **/etc/apt/sources.list** file.

| ``{{$}} sudo apt-get update``
| ``{{$}} sudo apt-get install vlc vlc-plugin-pulse mozilla-plugin-vlc``

As given by https://help.ubuntu.com/community/RestrictedFormats/PlayingDVDs:

``{{$}} sudo apt install libdvd-pkg && sudo dpkg-reconfigure libdvd-pkg``

will install a packaged version of `libdvdcss <libdvdcss>`__ without the need for third-party repos.

Red Hat
~~~~~~~

File:Redhat2.jpg%7Calt=Red Hat logo File:Centos.png%7Calt=CentOS logo

Adapted (annotated) from https://www.videolan.org/vlc/download-redhat.html:

Red Hat/CentOS/Scientific Linux have almost the same setups (they're all derived from Red Hat). Red Hat and derivatives have `different instructions <https://fedoraproject.org/wiki/EPEL#Quickstart>`__ if EPEL (Extra Packages for Enterprise Linux) is not set up. Red Hat Network (RHN) users should verify that they have enabled the *optionals* and *extras* channels for RHN subscriptions.

If you want to have DVD playback ability, you will need to install the libdvdcss package too (`source <https://www.videolan.org/vlc/download-redhat.html>`__).

For the latest version (up to the now-current version 3.0.6) use `RPM Fusion <https://rpmfusion.org/RPM%20Fusion>`__, otherwise VLC branches 2.0.x and 2.2.x are available: Red Hat/CentOS/Scientific Linux 7: (vlc-2.2.x – branch available for x86_64 architectures)

| ``{{$}}> su -``
| ``    #> yum install ``\ ```https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm`` <https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm>`__
| ``    #> yum install ``\ ```https://download1.rpmfusion.org/free/el/rpmfusion-free-release-7.noarch.rpm`` <https://download1.rpmfusion.org/free/el/rpmfusion-free-release-7.noarch.rpm>`__
| ``    #> yum install vlc``
| ``    #> yum install vlc-core             # (for minimal headless/server install)``
| ``    #> yum install python-vlc npapi-vlc # (optionals)``

Red Hat/CentOS/Scientific Linux 6: (vlc-2.0.x branch – available for i686 and x86_64 architectures)

| ``{{$}}> su -``
| ``    #> yum install ``\ ```https://dl.fedoraproject.org/pub/epel/epel-release-latest-6.noarch.rpm`` <https://dl.fedoraproject.org/pub/epel/epel-release-latest-6.noarch.rpm>`__
| ``    #> yum install ``\ ```https://download1.rpmfusion.org/free/el/rpmfusion-free-release-6.noarch.rpm`` <https://download1.rpmfusion.org/free/el/rpmfusion-free-release-6.noarch.rpm>`__
| ``    #> yum install vlc``
| ``    #> yum install vlc-core             # (for minimal headless/server install)``
| ``    #> yum install python-vlc npapi-vlc # (optionals)``

SUSE
~~~~

Download page: https://www.videolan.org/vlc/download-suse.html

FreeBSD
-------

Download page: https://www.videolan.org/vlc/download-freebsd.html

Install vlc from the packages collection:

\ `` pkg install vlc``

Compile the sources by yourself
-------------------------------

For more detailed information on compiling VLC, please see `Compile VLC <Compile_VLC>`__.

.. raw:: mediawiki

   {{Documentation}}

.. |Windows_logo2.jpg| image:: Windows_logo2.jpg
   :width: 100px
   :height: 100px
.. |Applelogo.jpg| image:: Applelogo.jpg
   :width: 100px
   :height: 100px
.. |Debian-logo.jpg| image:: Debian-logo.jpg
   :width: 100px
   :height: 100px
.. |Ubuntulogo.png| image:: Ubuntulogo.png
   :width: 100px
   :height: 100px
