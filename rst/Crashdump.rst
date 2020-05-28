<!--Dummy edit--> :''See [[Report_bugs#Mac_OS_X_users|here]] for macOS
information'' '''crashdump''' is the file VLC's Windows builds generate
when VLC crashes. It is stored to '''%appdata%vlc''' folder and its
content can be send to VLC server during next startup if you want that.
Content of the file is something like this: <syntaxhighlight lang="ini">
[version] OS=6.0.6002.2.Service Pack 2 VLC=1.1.2 The Luggage

[exceptions] c0000005 at 6861e792

[context] EDI:00000000 ESI:0257c840 EBX:0000001e EDX:00000008
ECX:00000018 EAX:ffffffe0 EBP:02f8cb00 EIP:6861e792 ESP:02f8cad8

[stacktrace] #EIPmodule 6861e792C:softavlc-1.1.2libvlccore.dll
6861cbfaC:softavlc-1.1.2pluginslibhotkeys_plugin.dll
686567dbC:softavlc-1.1.2libvlccore.dll
68648dc5C:softavlc-1.1.2libvlccore.dll
68656b3eC:softavlc-1.1.2pluginslibqt4_plugin.dll
641faa20C:softavlc-1.1.2pluginslibqt4_plugin.dll
641d3a24C:softavlc-1.1.2pluginslibqt4_plugin.dll
6466f260C:softavlc-1.1.2pluginslibqt4_plugin.dll
645e1255C:softavlc-1.1.2pluginslibqt4_plugin.dll
7789fd72C:Windowssystem32USER32.dll 778a018dC:Windowssystem32USER32.dll
6470c1adC:softavlc-1.1.2pluginslibqt4_plugin.dll
646feca6C:softavlc-1.1.2pluginslibqt4_plugin.dll
646704c3C:softavlc-1.1.2pluginslibqt4_plugin.dll
6866127aC:Windowssystem32msvcrt.dll
764a26b3C:Windowssystem32kernel32.dll 779e19bbC:Windowssystem32ntdll.dll
</syntaxhighlight>

'''It is a good idea to send crashdumps with encryption.''' Otherwise
attackers can snoop and learn about any software vulnerabilities. For
example, the metadata in the short crashdump above show 32-bit Windows
Vista SP2 VLC 1.1.2 Qt Interface on what seems to be a Finnish locale.
This information, combined with possibly more information, can make for
an effective attack by compiling lists of vulnerabilities against 32-bit
systems, Vista systems, VLC 1.1.2, etc. To guard against this: \* For
forum posts, email and bug reports you can use [[HTTPS]] (look for a
green lock icon in the URL bar) \* For file send operations, this means
[[FTPS]] if available

[[Category:Glossary]]
