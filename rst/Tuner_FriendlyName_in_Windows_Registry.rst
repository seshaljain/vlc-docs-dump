.. raw:: mediawiki

   {{Example code}}

Note that the following config will require you putting your tuner's `MAC addresses <wikipedia:MAC_address>`__ in place of the two I'm using. This is more for reference. Please be *very* careful when editing anything in ``HKLM\System\CurrentControlSet``.

Tuners_FriendlyName.reg:
------------------------

.. code:: reg

     Windows Registry Editor Version 5.00
     
     ;; This file is for two external Motorola DCH-3200 Tuners operating via firewire. The MAC address of the firewire
     ;; interface on the tuner is in the ##?#AVC key name in reverse word order.
     ;;
     ;;    Ex:   MAC '''0023A3FFFE542D31'''
     ;;          ##?#AVC#MOTOROLA&DCH-3200&TYP_5&ID_0#'''312D54FEFFA32300'''#
     ;;
     ;; Furthermore, There are 4 classes associated with each Tuner/Panel:
     ;;
     ;;    Ex:   {65e8773d-8f56-11d0-a3b9-00a0c9223196}
     ;;    Ex:   {65e8773e-8f56-11d0-a3b9-00a0c9223196}
     ;;    Ex:   {6994ad05-93ef-11d0-a3cc-00a0c9223196}
     ;;    Ex:   {cc7bfb41-f175-11d1-a392-00e0291f3959}
     ;;
     ;;
     ;; So you could in escence generate your own configuration if you know the classes assocated with the equiptment. I believe all video
     ;; capture devices are stored in these 4 classes reguardless of manufacturer. I could be wrong though. It's almost as if the tree's 
     ;; content in Device manager for Imaging Devices is determined based on the content of these classes.
     ;;
     ;; Renaming the FriendlyName allows us to isolate the control and capture of video via VLC on an endless amount of multiple tuners.
     
     
     [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\DeviceClasses\{65e8773d-8f56-11d0-a3b9-00a0c9223196}\##?#AVC#MOTOROLA&DCH-3200&TYP_5&ID_0#312D54FEFFA32300#{65e8773d-8f56-11d0-a3b9-00a0c9223196}\#GLOBAL\Device Parameters]
     "FriendlyName"="Motorola DCH-3200 Tuner 1"
     [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\DeviceClasses\{65e8773e-8f56-11d0-a3b9-00a0c9223196}\##?#AVC#MOTOROLA&DCH-3200&TYP_5&ID_0#312D54FEFFA32300#{65e8773e-8f56-11d0-a3b9-00a0c9223196}\#GLOBAL\Device Parameters]
     "FriendlyName"="Motorola DCH-3200 Tuner 1"
     [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\DeviceClasses\{6994ad05-93ef-11d0-a3cc-00a0c9223196}\##?#AVC#MOTOROLA&DCH-3200&TYP_5&ID_0#312D54FEFFA32300#{6994ad05-93ef-11d0-a3cc-00a0c9223196}\#GLOBAL\Device Parameters]
     "FriendlyName"="Motorola DCH-3200 Tuner 1"
     [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\DeviceClasses\{cc7bfb41-f175-11d1-a392-00e0291f3959}\##?#AVC#MOTOROLA&DCH-3200&TYP_5&ID_0#312D54FEFFA32300#{cc7bfb41-f175-11d1-a392-00e0291f3959}\#GLOBAL\Device Parameters]
     "FriendlyName"="Motorola DCH-3200 Tuner 1"
     
     [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\DeviceClasses\{65e8773d-8f56-11d0-a3b9-00a0c9223196}\##?#AVC#MOTOROLA&DCH-3200&TYP_5&ID_0#CA200BFEFFA32300#{65e8773d-8f56-11d0-a3b9-00a0c9223196}\#GLOBAL\Device Parameters]
     "FriendlyName"="Motorola DCH-3200 Tuner 2"
     [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\DeviceClasses\{65e8773e-8f56-11d0-a3b9-00a0c9223196}\##?#AVC#MOTOROLA&DCH-3200&TYP_5&ID_0#CA200BFEFFA32300#{65e8773e-8f56-11d0-a3b9-00a0c9223196}\#GLOBAL\Device Parameters]
     "FriendlyName"="Motorola DCH-3200 Tuner 2"
     [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\DeviceClasses\{6994ad05-93ef-11d0-a3cc-00a0c9223196}\##?#AVC#MOTOROLA&DCH-3200&TYP_5&ID_0#CA200BFEFFA32300#{6994ad05-93ef-11d0-a3cc-00a0c9223196}\#GLOBAL\Device Parameters]
     "FriendlyName"="Motorola DCH-3200 Tuner 2"
     [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\DeviceClasses\{cc7bfb41-f175-11d1-a392-00e0291f3959}\##?#AVC#MOTOROLA&DCH-3200&TYP_5&ID_0#CA200BFEFFA32300#{cc7bfb41-f175-11d1-a392-00e0291f3959}\#GLOBAL\Device Parameters]
     "FriendlyName"="Motorola DCH-3200 Tuner 2"
     
     [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\DeviceClasses\{cc7bfb41-f175-11d1-a392-00e0291f3959}\##?#AVC#MOTOROLA&DCH-3200&TYP_9&ID_0#312D54FEFFA32300#{cc7bfb41-f175-11d1-a392-00e0291f3959}\#GLOBAL\Device Parameters]
     "FriendlyName"="Motorola DCH-3200 Panel 1"
     [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\DeviceClasses\{65e8773d-8f56-11d0-a3b9-00a0c9223196}\##?#AVC#MOTOROLA&DCH-3200&TYP_9&ID_0#312D54FEFFA32300#{65e8773d-8f56-11d0-a3b9-00a0c9223196}\#GLOBAL\Device Parameters]
     "FriendlyName"="Motorola DCH-3200 Panel 1"
     [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\DeviceClasses\{65e8773e-8f56-11d0-a3b9-00a0c9223196}\##?#AVC#MOTOROLA&DCH-3200&TYP_9&ID_0#312D54FEFFA32300#{65e8773e-8f56-11d0-a3b9-00a0c9223196}\#GLOBAL\Device Parameters]
     "FriendlyName"="Motorola DCH-3200 Panel 1"
     [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\DeviceClasses\{6994ad05-93ef-11d0-a3cc-00a0c9223196}\##?#AVC#MOTOROLA&DCH-3200&TYP_9&ID_0#312D54FEFFA32300#{6994ad05-93ef-11d0-a3cc-00a0c9223196}\#GLOBAL\Device Parameters]
     "FriendlyName"="Motorola DCH-3200 Panel 1"
     
     [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\DeviceClasses\{cc7bfb41-f175-11d1-a392-00e0291f3959}\##?#AVC#MOTOROLA&DCH-3200&TYP_9&ID_0#CA200BFEFFA32300#{cc7bfb41-f175-11d1-a392-00e0291f3959}\#GLOBAL\Device Parameters]
     "FriendlyName"="Motorola DCH-3200 Panel 2"
     [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\DeviceClasses\{65e8773d-8f56-11d0-a3b9-00a0c9223196}\##?#AVC#MOTOROLA&DCH-3200&TYP_9&ID_0#CA200BFEFFA32300#{65e8773d-8f56-11d0-a3b9-00a0c9223196}\#GLOBAL\Device Parameters]
     "FriendlyName"="Motorola DCH-3200 Panel 2"
     [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\DeviceClasses\{65e8773e-8f56-11d0-a3b9-00a0c9223196}\##?#AVC#MOTOROLA&DCH-3200&TYP_9&ID_0#CA200BFEFFA32300#{65e8773e-8f56-11d0-a3b9-00a0c9223196}\#GLOBAL\Device Parameters]
     "FriendlyName"="Motorola DCH-3200 Panel 2"
     [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\DeviceClasses\{6994ad05-93ef-11d0-a3cc-00a0c9223196}\##?#AVC#MOTOROLA&DCH-3200&TYP_9&ID_0#CA200BFEFFA32300#{6994ad05-93ef-11d0-a3cc-00a0c9223196}\#GLOBAL\Device Parameters]
     "FriendlyName"="Motorola DCH-3200 Panel 2"

`Category:Windows <Category:Windows>`__
