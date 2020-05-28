== Python bindings == The bindings feature:

-  Complete coverage of the libvlc API, since it is automatically
   generated from the include files.
-  No compilation hassles: the generated module is pure python.
-  [https://www.olivieraubert.net/vlc/python-ctypes/doc/ API
   documentation].

=== Download === The preferred install method is through PyPI:

   pip install python-vlc

or (if you are using python3):

   pip3 install python-vlc

You can also download the
[https://git.videolan.org/?p=vlc/bindings/python.git;a=tree;f=generated;b=HEAD
vlc.py] module from the Git repository. It only depends on ctypes
(standard module in python >= 2.5). Put the module in some place
accessible by python (either next to your application, or in a directory
from sys.path).

Alternatively, you can generate it by yourself using the generate.py
program and accompanying files in the vlc source tree (see
[https://git.videolan.org/?p=vlc/bindings/python.git;a=tree]).

Note that this only installs the python module itself, which depends on
the availability of the libvlc libraries. You must also install VLC
itself to get these libraries.

=== Usage === The vlc.py file also contains a runnable example player
application (see code at the end of the file, starting from the line
<code>if \__name_\_ == '__main__'</code>).

A set of helper examples
[https://git.videolan.org/?p=vlc/bindings/python.git;a=tree;f=examples;hb=HEAD
examples] provide a pyGtk, a pyQt and a pyWx player to ease integration.

There is also a
[https://git.videolan.org/?p=vlc/bindings/python.git;a=blob_plain;f=README.rst
README]

Note: you must install VLC before using it through Python.

=== Projects using this binding ===
https://code.google.com/p/movie-content-editor/ See also
[[LibVLC_Users]]

=== FAQ === ==== Win32 initialization ==== When initializing
<code>vlc.Instance()</code> with no parameter, it tries to guess the
location of the modules. However, if you pass any argument to
<code>vlc.Instance()</code>, you will need to supply the appropriate
<kbd>--plugin-path=/path/to/the/modules</kbd> yourself.

==See also== \* [[Old Python bindings]] - The old, obsolete python
bindings that are no longer used and since then removed. Kept only for
historical interest.

[[Category:Bindings]]
