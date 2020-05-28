A character encoding describes how to interpret data outside the very
limited range of ASCII.<br /> It is recommended to use '''UTF-8'''
(Unicode) for maximum portability.

Incorrect character encodings render text obviously wrong,
misinterpreting a single multi-byte character as several ASCII
characters. For example, compare {{VLCSourceFile|AUTHORS}} versus
[https://git.videolan.org/?p=vlc.git;a=blob_plain;f=AUTHORS;hb=HEAD
AUTHORS without UTF-8 support]. Character encodings are particularly
important for [[subtitles]] and configuration files.

Windows Notepad defaults to Windows-1252\* for all new documents
([https://www.bleepingcomputer.com/news/microsoft/windows-10-notepad-is-getting-better-utf-8-encoding-support/
though this might be getting better]) leading to potential
misinterpretation by other programs. To save a Notepad document in UTF-8
hit <kbd>Ctrl+Shift+S</kbd> to bring up a dialogue or use a free
third-party editor like [https://notepad-plus-plus.org/ Notepad++].

<small><nowiki>*</nowiki> Windows might incorrectly call Windows-1252
''ANSI''</small>

[[Category:Glossary]]
