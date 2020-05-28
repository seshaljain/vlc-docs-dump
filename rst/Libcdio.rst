.. raw:: mediawiki

   {{website|libcdio|http://www.gnu.org/software/libcdio/}}

The **Compact Disc Input and Control Library** (libcdio) encapsulates CD-ROM reading and control. The libcdio package contains a library which encapsulates CD-ROM reading and control. Applications wishing to be oblivious of the OS- and device-dependent properties of a CD-ROM can use this library.

Some support for on-disk CD-image types like CDRWIN's BIN/CUE format, cdrdao's TOC format, and Nero's NRG format is available. Therefore, applications that use this library also have the ability to read on-disk CD images as though they were CDs.

A library for working with ISO-9660 filesystems (libiso9660) is included. A generic interface for issuing MMC (multimedia commands) is also part of the libcdio library.

A library for working with UDF filesystems (libudf) is included, although this is not fully complete.

The cdparanoia library and cdparanoia command are included making this the only single-source cdparanoia that works on FreeBSD, cygwin, Solaris, BSDI as well as GNU/Linux.

The core library is in C however there are libraries/modules are available in C++, Perl, Python and Ruby.

`Category:Libraries <Category:Libraries>`__
