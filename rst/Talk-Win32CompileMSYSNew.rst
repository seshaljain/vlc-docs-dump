The links to update autoconf, automake, and libtool seem incorrect -
they install into /usr/local and contain executables named with the
version number (as in 'autoconf-2.61'). The MSYS versions seem to work
better, as in: \*
http://sourceforge.net/projects/mingw/files/MSYS%20System%20Builder/autoconf-2.61-MSYS-1.0.11-1.tar.bz2/download
\*
http://sourceforge.net/projects/mingw/files/MSYS%20System%20Builder/automake-1.10-MSYS-1.0.11-1.tar.bz2/download
\*
http://sourceforge.net/projects/mingw/files/MSYS%20System%20Builder/libtool1.5-1.5.25a-20070701-MSYS-1.0.11-1.tar.bz2/download

--[[User:Mcross|Mcross]] 18:55, 20 July 2009 (UTC)

(Fixed)

When I installed msys, from the msys prompt, /usr/ is equivalent to
C:msys1.0, so wherever you see jb refer to /usr/win32/, I had to use
only /win32/

(noted)

I also needed to get and build a recent x264 snapshot (latest trunk
needs >0.76).

--Simonh 29 Sept 2009

\*'''Fix libtool search dirs''', seem incorrect.

--[[User:Diblo Dk|Diblo Dk]] 22:56, 14 June 2010 (UTC)

What looks incorrect? Did it cause failures? (I think it just looks odd
but is right) [[User:Rogerdpack|Rogerdpack]] 21:27, 21 September 2010
(UTC)
