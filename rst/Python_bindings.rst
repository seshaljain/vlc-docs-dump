Python bindings
---------------

The bindings feature:

-  Complete coverage of the libvlc API, since it is automatically generated from the include files.
-  No compilation hassles: the generated module is pure python.
-  `API documentation <https://www.olivieraubert.net/vlc/python-ctypes/doc/>`__.

Download
~~~~~~~~

The preferred install method is through PyPI:

``pip install python-vlc``

or (if you are using python3):

``pip3 install python-vlc``

You can also download the `vlc.py <https://git.videolan.org/?p=vlc/bindings/python.git;a=tree;f=generated;b=HEAD>`__ module from the Git repository. It only depends on ctypes (standard module in python >= 2.5). Put the module in some place accessible by python (either next to your application, or in a directory from sys.path).

Alternatively, you can generate it by yourself using the generate.py program and accompanying files in the vlc source tree (see `1 <https://git.videolan.org/?p=vlc/bindings/python.git;a=tree>`__).

Note that this only installs the python module itself, which depends on the availability of the libvlc libraries. You must also install VLC itself to get these libraries.

Usage
~~~~~

The vlc.py file also contains a runnable example player application (see code at the end of the file, starting from the line ``if __name__ == '__main__'``).

A set of helper examples `examples <https://git.videolan.org/?p=vlc/bindings/python.git;a=tree;f=examples;hb=HEAD>`__ provide a pyGtk, a pyQt and a pyWx player to ease integration.

There is also a `README <https://git.videolan.org/?p=vlc/bindings/python.git;a=blob_plain;f=README.rst>`__

Note: you must install VLC before using it through Python.

Projects using this binding
~~~~~~~~~~~~~~~~~~~~~~~~~~~

https://code.google.com/p/movie-content-editor/ See also `LibVLC_Users <LibVLC_Users>`__

FAQ
~~~

Win32 initialization
^^^^^^^^^^^^^^^^^^^^

When initializing ``vlc.Instance()`` with no parameter, it tries to guess the location of the modules. However, if you pass any argument to ``vlc.Instance()``, you will need to supply the appropriate --plugin-path=/path/to/the/modules yourself.

See also
--------

-  `Old Python bindings <Old_Python_bindings>`__ - The old, obsolete python bindings that are no longer used and since then removed. Kept only for historical interest.

`Category:Bindings <Category:Bindings>`__
