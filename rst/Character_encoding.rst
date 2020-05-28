| A character encoding describes how to interpret data outside the very limited range of ASCII.
| It is recommended to use **UTF-8** (Unicode) for maximum portability.

Incorrect character encodings render text obviously wrong, misinterpreting a single multi-byte character as several ASCII characters. For example, compare versus `AUTHORS without UTF-8 support <https://git.videolan.org/?p=vlc.git;a=blob_plain;f=AUTHORS;hb=HEAD>`__. Character encodings are particularly important for `subtitles <subtitles>`__ and configuration files.

Windows Notepad defaults to Windows-1252\* for all new documents (`though this might be getting better <https://www.bleepingcomputer.com/news/microsoft/windows-10-notepad-is-getting-better-utf-8-encoding-support/>`__) leading to potential misinterpretation by other programs. To save a Notepad document in UTF-8 hit Ctrl+Shift+S to bring up a dialogue or use a free third-party editor like `Notepad++ <https://notepad-plus-plus.org/>`__.

\* Windows might incorrectly call Windows-1252 *ANSI*\ 

`Category:Glossary <Category:Glossary>`__
