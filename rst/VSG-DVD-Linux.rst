DVDs wont play in Linux
-----------------------

*This tip is only intended for Linux users who can't play any DVD.*

| 
| Maybe you don't have the **libdvdcss** package, which you need if you want to play DVDs with VLC.
| You can get the libdvdcss package `here <http://linux.softpedia.com/get/Programming/Libraries/libdvdcss-165.shtml>`__.

| 
| You can try to check about you have the access rights for your DVD player.
| Make sure you have access rigths to your DVD player. In linux, you can use chmod to edit access rights to your DVD block device: #chmod 666 /dev/dvd
| Here /dev/dvd is the device corresponding to your DVD drive.

| 
| Make sure VLC knows where your DVD drive is located (/dev/dvd usually).

Go to Settings>Preferences>Input/Codecs>General and under "Default devices" make sure your dvd drive path is entered in the "Default DVD" box.

| 
| When you go to open a DVD, you should see something like "dvd:///dev/dvd" as the media resource locator in the "Open:" box near the top of the Open dialog.
| 
