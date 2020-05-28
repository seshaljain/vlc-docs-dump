'''Jb,

I am new to VLC and trying to build it by following the procedure "How
to compile on Windows using Cygwin" and stuck at runing
"configure-vlc.sh" with the following message. Would you help ?

Sincerely, Junfang ''' ----------------$ ./configure-vlc.sh configure:
WARNING: unrecognized options: --with-caca-config-path configure:
WARNING: If you wanted to set the --build type, don't use --host.
configure: error: in \`/home/HNJ786/vlc': configure: error: C compiler
cannot create executables See \`config.log' for more details.
-----------------

== Mingw == Seriously, you really should use MingW to compile VLC.
[[User:J-b|jb]] 08:01, 23 April 2010 (UTC) ===========

-----------------------Jb,

Appreciate your prompt.

Sincerely, Junfang -----------------------

----------------------------------------------Jb,

By following "Win32CompileMSYSNew" it stuck at

   $ sh extras/package/win32/configure-msys.sh

with the following errors.

   checking for broken mingw-runtime... present configure: error: LibVLC
   requires mingw-runtime version 3.15 or higher!

Screen shot attached for your kind review.

Sincerely, Junfang

$ sh extras/package/win32/configure-msys.sh checking build system
type... i386-pc-linux-gnu checking host system type...
i586-pc-mingw32msvc checking for a BSD-compatible install...
/usr/bin/install -c checking whether build environment is sane... yes
checking for i586-mingw32msvc-strip... no checking for strip... strip
configure: WARNING: using cross tools not prefixed with host triplet
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p checking for
gawk... gawk checking whether make sets $(MAKE)... yes checking how to
create a ustar tar archive... gnutar checking whether to enable
maintainer-specific portions of Makefiles... yes checking for style of
include used by make... GNU checking for i586-mingw32msvc-gcc... gcc
checking whether the C compiler works... yes checking for C compiler
default output file name... a.exe checking for suffix of executables...
.exe checking whether we are cross compiling... yes checking for suffix
of object files... o checking whether we are using the GNU C compiler...
yes checking whether gcc accepts -g... yes checking for gcc option to
accept ISO C89... none needed checking dependency style of gcc... gcc3
checking for gcc option to accept ISO C99... -std=gnu99 checking how to
run the C preprocessor... gcc -std=gnu99 -E checking for grep that
handles long lines and -e... /usr/bin/grep checking for egrep...
/usr/bin/grep -E checking for ANSI C header files... yes checking for
sys/types.h... yes checking for sys/stat.h... yes checking for
stdlib.h... yes checking for string.h... yes checking for memory.h...
yes checking for strings.h... yes checking for inttypes.h... yes
checking for stdint.h... yes checking for unistd.h... yes checking
minix/config.h usability... no checking minix/config.h presence... no
checking for minix/config.h... no checking whether it is safe to define
\__EXTENSIONS__... yes checking whether gcc -std=gnu99 and cc understand
-c and -o together... yes checking whether we are using the GNU C++
compiler... yes checking whether g++ accepts -g... yes checking
dependency style of g++... gcc3 checking how to run the C
preprocessor... gcc -std=gnu99 -E checking for i586-mingw32msvc-gcc...
no checking for i586-mingw32msvc-objcc... no checking for
i586-mingw32msvc-objc... no checking for i586-mingw32msvc-cc... no
checking for i586-mingw32msvc-CC... no checking for gcc... gcc checking
whether we are using the GNU Objective C compiler... yes checking
whether gcc accepts -g... yes checking dependency style of gcc... gcc3
checking dependency style of gcc... (cached) gcc3 checking for egrep...
(cached) /usr/bin/grep -E checking whether make sets $(MAKE)... (cached)
yes checking dependency style of gcc -std=gnu99... gcc3 checking for
i586-mingw32msvc-ranlib... no checking for ranlib... ranlib checking for
i586-mingw32msvc-strip... strip checking for i586-mingw32msvc-ar... no
checking for ar... ar checking for i586-mingw32msvc-ld... no checking
for ld... ld checking for i586-mingw32msvc-dlltool... no checking for
dlltool... dlltool checking for an ANSI C-conforming const... yes
checking for inline... inline checking for C/C++ restrict keyword...
\__restrict checking for i586-mingw32msvc-windres... no checking for
windres... windres checking for i586-mingw32msvc-objcopy... no checking
for objcopy... objcopy checking for i586-mingw32msvc-peflags... no
checking for peflags... peflags checking for unix2dos... unix2dos
checking for i586-mingw32msvc-as... no checking for as... as checking
for i586-mingw32msvc-dlltool... dlltool checking for
i586-mingw32msvc-objdump... no checking for objdump... objdump checking
how to print strings... printf checking for a sed that does not truncate
output... /usr/bin/sed checking for fgrep... /usr/bin/grep -F checking
for ld used by gcc -std=gnu99... ld checking if the linker (ld) is GNU
ld... yes checking for BSD- or MS-compatible name lister (nm)... no
checking for i586-mingw32msvc-dumpbin... no checking for
i586-mingw32msvc-link... no checking for dumpbin... no checking for
link... link -dump checking the name lister (nm) interface... BSD nm
checking whether ln -s works... yes checking the maximum length of
command line arguments... 512 checking whether the shell understands
some XSI constructs... yes checking whether the shell understands
"+="... yes checking how to convert i386-pc-linux-gnu paths to
i586-pc-mingw32msvc format... func_nix_to_mingw_path_convert checking
for ld option to reload object files... -r checking for
i586-mingw32msvc-objdump... objdump checking how to recognize dependent
libraries... (cached) pass_all checking for i586-mingw32msvc-dlltool...
(cached) dlltool checking how to associate runtime and link libraries...
func_cygming_dll_for_imp lib checking for i586-mingw32msvc-ar... ar
checking for i586-mingw32msvc-strip... (cached) strip checking for
i586-mingw32msvc-ranlib... ranlib checking command to parse nm output
from gcc -std=gnu99 object... ok checking for dlfcn.h... yes checking
for objdir... .libs checking if gcc -std=gnu99 supports -fno-rtti
-fno-exceptions... no checking for gcc -std=gnu99 option to produce
PIC... -DDLL_EXPORT -DPIC checking if gcc -std=gnu99 PIC flag
-DDLL_EXPORT -DPIC works... yes checking if gcc -std=gnu99 static flag
-static works... no checking if gcc -std=gnu99 supports -c -o file.o...
yes checking if gcc -std=gnu99 supports -c -o file.o... (cached) yes
checking whether the gcc -std=gnu99 linker (ld) supports shared
libraries... yes

checking whether -lc should be explicitly linked in... yes checking
dynamic linker characteristics... Win32 ld.exe checking how to hardcode
library paths into programs... immediate checking whether stripping
libraries is possible... yes checking if libtool supports shared
libraries... yes checking whether to build shared libraries... yes
checking whether to build static libraries... no checking how to run the
C++ preprocessor... g++ -E checking for ld used by g++... ld checking if
the linker (ld) is GNU ld... yes checking whether the g++ linker (ld)
supports shared libraries... yes checking for g++ option to produce
PIC... -DDLL_EXPORT -DPIC checking if g++ PIC flag -DDLL_EXPORT -DPIC
works... yes checking if g++ static flag -static works... no checking if
g++ supports -c -o file.o... yes checking if g++ supports -c -o
file.o... (cached) yes checking whether the g++ linker (ld) supports
shared libraries... yes checking dynamic linker characteristics... Win32
ld.exe checking how to hardcode library paths into programs... immediate
checking whether NLS is requested... no checking for msgfmt...
/usr/bin/msgfmt checking for gmsgfmt... /usr/bin/msgfmt checking for
xgettext... /usr/bin/xgettext checking for msgmerge... /usr/bin/msgmerge
checking for ld used by GCC... ld checking if the linker (ld) is GNU
ld... yes checking for shared library run path origin... done checking
for CFPreferencesCopyAppValue... no checking for CFLocaleCopyCurrent...
no checking whether to use NLS... no checking for iconv... no, consider
installing GNU libiconv checking for broken mingw-runtime... present
configure: error: LibVLC requires mingw-runtime version 3.15 or higher!
------------------------------------------------------------------------
