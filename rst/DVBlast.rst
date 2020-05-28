What is it?
-----------

DVBlast is a streaming solution to stream multiple channels of TV to a network. A DVB-Card (terrestrial, cable, satellite) or an ASI-Input-Card from `Computer Modules <http://www.computermodules.com/>`__ is needed to provide input to DVBlast. Thanks to videocompression and *some magic* one frequency (so called "transponder" can hold multiple TV-channels. So if your DVB-device is tuned to one frequecy, the whole so called "bouquet" could be used by applications like DVBlast. More information can be found on `videolan.org server <http://www.videolan.org/projects/dvblast.html>`__.

Get it
------

First place to get it: `videolan.org server <http://www.videolan.org/projects/dvblast.html>`__. You have to compile it from source and you will need to install libdvbpsi in order to make it work. You could also use your package manager. On Ubuntu-based systems you could use *sudo apt-get install dvblast* for example.

Using it
--------

First of all you have to know how channels and bouquets are organized it your DVB-source. A could thing to start with is wscan, which could output you a channels.conf, including a list of frequencies to be tuned to and channels on a frequency´s bouquet. Easiest way to use it is to create a config file, which could look like this one:

root@streamdev-01:~# cat freeHD.conf

239.255.0.1:1234 1 11100

239.255.0.2:1234 1 11110

239.255.0.3:1234 1 11120

First is the multicast-IP (and :port), which is causing DVBlast to "blast" everything into the whole network. Be aware, that some soho-routers/APs and switches have severe problems with the many packets DVBlast generates and sends. My AVM Fritz!Box is rebooting as long as I have DVBlast running the above config file (which broadcasts three HD-streams simultaneously). Call "dvblast -c freeHD.conf" in a Kabel Deutschland, Hamburg-based environment for this to work.

More to come, I will extend these explanations. --`Kakohari <User:Kakohari>`__ 07:09, 13 September 2011 (UTC)

`Category:VideoLAN projects <Category:VideoLAN_projects>`__
