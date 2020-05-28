.. raw:: mediawiki

   {{RightMenu|documentation streaming howto toc}}

Note: This is possible under GNU/Linux only.

Install the libraw1394 and libavc1394
-------------------------------------

If you want to be able to stream from a DV camcorder, then you need to install the libraries libraw1394 and libavc1394:

-  if you use a Fedora Core distribution then you just need to install the libraries using:

| ``% ``\ **``yum``\ ````\ ``update``**
| ``% '''yum install libraw1394 libavc1394'``

-  if you want to install the libraries from the source then you must download them from the `libraw1394 <http://www.linux1394.org/>`__ and `libavc1394 <http://sourceforge.net/projects/libavc1394>`__ from their projects website.

-  if you have a distribution that uses `udev <http://kernel.org/pub/linux/utils/kernel/hotplug>`__, then you must add/change the following line to the file 50-udev.rules in your /etc/udev/rules.d directory.

| ``% ``\ **``vi``\ ````\ ``/etc/udev/rules.d/50-udev.rules``**
| ``# IEEE1394 (firewire) devices (must be before raw devices below)``
| ``KERNEL=="raw1394",              NAME="%k"``
| ``KERNEL=="dv1394",               NAME="dv1394/%k"``
| ``KERNEL=="video1394*",           NAME="video1394/%n"``

The following sections assume that you have a working linux installation with the IEEE 1394 (Firewire) libraries installed, either manually from the source code or through your distributions upgrade mechanism.

Stream with DV
--------------

Connect the DV camcorder with a Firewire cable to your computer, and check the creation of the file **/dev/raw1394**.

Run VLC with the following in one command line:

| ``% '''vlc -vvv dv/rawdv:///dev/raw1394 --dv-caching 10000 --sout``
| ``'#transcode{vcodec=WMV2,vb=512,scale=1,acodec=mp3,ab=192,channels=2,fps=25.0}:``
| ``std{access=mmsh,mux=asfh,url=:8080}' '''``

where:

-  **dv/rawdv://** is the DV input and **/dev/raw1394** the device file,
-  **dv-caching** is the delay is milliseconds (ms) (start with a high value, 10s or so, and lower it later),
-  **sout** is the stream output chain that is used to stream the DV camcorder as a multimedia stream over the network. The **transcode** syntax is explained in the chapter about transcoding. The example as given above generates a multimedia stream that is compatible with Windows Media Player,
-  **sout-transcode-fps** is the number of pictures per second **25.0** that the transcode module should generate of the requested audio/video codec.

.. raw:: mediawiki

   {{Documentation}}
