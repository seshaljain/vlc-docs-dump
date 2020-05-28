LibVLC was switched to UTF-8 internally sometime in 2005, and it's now getting kind of usable again. Still, there's been quite many changes throughout 2006, so let's summarise.

Overview
--------

As a general rules, all character strings passed to LibVLC should be in UTF-8. This includes, but is far from limited to the playlist, and all the *chain* from the input/access to the outputs. We pretty much needed Unicode anyway; the only options were UTF-8 and wide char. We picked UTF-8 because, as disruptive as it has been, it remains much less disruptive than wide characters. Also wide characters means different things on different platforms (e.g. UCS2LE on old Windows, UTF-16LE on modern Windows, UTF-32 on glibc), are a pain to use in POSIX environment (including Mac OS X and Linux which most of the devs are using), and might have needed lots of libc replacements ``wc*`` functions on some platforms.

Historical approach
-------------------

The original approach has been to rely on ``ToLocale``, ``FromLocale`` and ``LocaleFree`` (and ``ToLocaleDup``, ``FromLocaleDup`` and ``free``) whenever a character string in the OS native representation was needed. It turned out to be a big mistake on Windows, which uses no less than three different representations internally: UTF-16 in the kernel and file system (Unicode/wide), ACP (ANSI Code Page) which is a locale-dependant 8-bit character set (CP1252 in the West), and even "OEM" (cp437 in the US, cp850 in Western Europe). Unfortunately, (To|From)Locale were using ACP, which prevents usage of Unicode code points outside the range of the local charset, while the filesystem and native Win32 supports them. This means VLC cannot *reach* some files.

Current approach
----------------

So we now have a comprehensive (but not fully yet) set of higher-level wrappers that accept UTF-8 character string to represent filenames, or text to be output to the console. At the time of writing, trunk includes:

-  utf8_open, utf8_fopen, utf8_stat, utf8_lstat, utf8_mkdir, utf8_opendir, utf8_readdir, utf8_scandir for file system operation,

-  utf8_fprintf, utf8_vfprintf for console output (or actually output in any file which needs local charset).

All of these functions behave like their non "utf8_"-prefixed equivalent with the exception that they expect UTF-8 character strings.

We also have EnsureUTF8 that forces a string into UTF-8 (replaces invalid character sequences with '?') and IsUTF8 that checks if the string is valid UTF-8 (returns NULL if not). These are useful when reading UTF-8 from untrusted sources, such as the network, before injecting the data into VLC.

Backward compatibility note
~~~~~~~~~~~~~~~~~~~~~~~~~~~

ToLocale and FromLocale should NEVER be used for filesystem operations anymore, except on code that is not aimed at Windows. And even then it's better to use wrappers; for instance, Mac OS X has some conversion logic for its directory listing. When using the Win32 API manually, always use the Unicode version (the one ending with 'W' instead of 'A'). If you need to convert to UTF-8 for use in LibVLC, you can use FromWide (Win32 only!). Of course, it's better to resort to the wrappers otherwise you always need a specific Windows implementations. Please refer to the various pieces of code using Win32 SHFolderGetPath() for reference implementations.

Now for the good (?) news: in trunk, the only parts that still use the ``*Locale`` LibVLC APIs are:

-  GnomeVFS (pretty much dead and not aimed at Win32 anyway),
-  GnuTLS (no support from GnuTLS library),
-  skins2,
-  WxWidgets (only on non-Win32 and being phased out)

However I have only checked the core and plugins, so there might be problems with browser plugins and bindings. Also, if you intend to write new plugins, please keep this in mind.

Automatic charset detection
---------------------------

In addition to this, I remind you that we now have the GetFallbackEncoding() API that returns the ANSI code page used by Windows for the given locale, to be passed to iconv. For instance, if your system is configured to run in German, it returns "CP1252". This is convenient when handling subtitles or various kind of texts that are typically aimed at Windows users.

Adapted from a `vlc-devel <vlc-devel>`__ post by `Courmisch <User:Courmisch>`__ (December 2006).

`Category:libVLC <Category:libVLC>`__
