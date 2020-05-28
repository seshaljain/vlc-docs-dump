I've had some difficulty getting the Python bindings to VLC operating on Mac OSX 10.6 but finally found a workaround. The difficulty is that when operating on a Mac, the bindings will only operate properly using a 32 bit Python. On Mac OS 10.6 the default Python is version 2.6.1 which operates as a 64 bit python by default. This leads to a variety of errors depending on the circumstances but generally you will get vlc.py reporting 'image not found'.

The workaround is to force Python 2.6.1 to 32 bit architecture. This can be done on a temporary basis with the commands:

``   % export VERSIONER_PYTHON_PREFER_32_BIT=yes # Bourne-like shells``

or

``   % setenv VERSIONER_PYTHON_PREFER_32_BIT yes # C-like shells``

You can also make the change semi-permanent with the command:

``   % defaults write com.apple.versioner.python Prefer-32-Bit -bool yes``

(both of these pages are from the OSX man page for Python). The vlc.py bindings will then operate correctly with the universal executable and the 32 bit executable which are available from the main download page for Macs.

I'd like to include this information on the main wiki page as it took me a couple of days to work it out. As to the larger question of getting vlc.py operating with a 64 bit Python, I'm currently clueless as I haven't been able to get a build operating yet. I do know there's no inherent problem with 64 bit python and ctypes as I've written my own library and loaded it.
