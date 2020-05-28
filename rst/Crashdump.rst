   *See*\ `here <Report_bugs#Mac_OS_X_users>`__\ *for macOS information*

**crashdump** is the file VLC's Windows builds generate when VLC crashes. It is stored to **%appdata%\vlc** folder and its content can be send to VLC server during next startup if you want that. Content of the file is something like this:

.. code:: ini

   [version]
   OS=6.0.6002.2.Service Pack 2
   VLC=1.1.2 The Luggage

   [exceptions]
   c0000005 at 6861e792

   [context]
   EDI:00000000
   ESI:0257c840
   EBX:0000001e
   EDX:00000008
   ECX:00000018
   EAX:ffffffe0
   EBP:02f8cb00
   EIP:6861e792
   ESP:02f8cad8

   [stacktrace]
   #EIP|base|module
   6861e792|C:\softa\vlc-1.1.2\libvlccore.dll
   6862fe8f|C:\softa\vlc-1.1.2\libvlccore.dll
   6861cbfa|C:\softa\vlc-1.1.2\libvlccore.dll
   70b62590|C:\softa\vlc-1.1.2\plugins\libhotkeys_plugin.dll
   686567db|C:\softa\vlc-1.1.2\libvlccore.dll
   68656b3e|C:\softa\vlc-1.1.2\libvlccore.dll
   68648dc5|C:\softa\vlc-1.1.2\libvlccore.dll
   686568a9|C:\softa\vlc-1.1.2\libvlccore.dll
   68656b3e|C:\softa\vlc-1.1.2\libvlccore.dll
   64032e5d|C:\softa\vlc-1.1.2\plugins\libqt4_plugin.dll
   641faa20|C:\softa\vlc-1.1.2\plugins\libqt4_plugin.dll
   6420f1f0|C:\softa\vlc-1.1.2\plugins\libqt4_plugin.dll
   641d3a24|C:\softa\vlc-1.1.2\plugins\libqt4_plugin.dll
   641dab80|C:\softa\vlc-1.1.2\plugins\libqt4_plugin.dll
   6466f260|C:\softa\vlc-1.1.2\plugins\libqt4_plugin.dll
   645df034|C:\softa\vlc-1.1.2\plugins\libqt4_plugin.dll
   645e1255|C:\softa\vlc-1.1.2\plugins\libqt4_plugin.dll
   644207fe|C:\softa\vlc-1.1.2\plugins\libqt4_plugin.dll
   7789fd72|C:\Windows\system32\USER32.dll
   7789fe4a|C:\Windows\system32\USER32.dll
   778a018d|C:\Windows\system32\USER32.dll
   778a022b|C:\Windows\system32\USER32.dll
   6470c1ad|C:\softa\vlc-1.1.2\plugins\libqt4_plugin.dll
   6441bb63|C:\softa\vlc-1.1.2\plugins\libqt4_plugin.dll
   646feca6|C:\softa\vlc-1.1.2\plugins\libqt4_plugin.dll
   646fee4b|C:\softa\vlc-1.1.2\plugins\libqt4_plugin.dll
   646704c3|C:\softa\vlc-1.1.2\plugins\libqt4_plugin.dll
   64023147|C:\softa\vlc-1.1.2\plugins\libqt4_plugin.dll
   6866127a|C:\softa\vlc-1.1.2\libvlccore.dll
   764a2599|C:\Windows\system32\msvcrt.dll
   764a26b3|C:\Windows\system32\msvcrt.dll
   765ad0e9|C:\Windows\system32\kernel32.dll
   779e19bb|C:\Windows\system32\ntdll.dll
   779e198e|C:\Windows\system32\ntdll.dll

**It is a good idea to send crashdumps with encryption.** Otherwise attackers can snoop and learn about any software vulnerabilities. For example, the metadata in the short crashdump above show 32-bit Windows Vista SP2 VLC 1.1.2 Qt Interface on what seems to be a Finnish locale. This information, combined with possibly more information, can make for an effective attack by compiling lists of vulnerabilities against 32-bit systems, Vista systems, VLC 1.1.2, etc. To guard against this:

-  For forum posts, email and bug reports you can use `HTTPS <HTTPS>`__ (look for a green lock icon in the URL bar)
-  For file send operations, this means `FTPS <FTPS>`__ if available

`Category:Glossary <Category:Glossary>`__
