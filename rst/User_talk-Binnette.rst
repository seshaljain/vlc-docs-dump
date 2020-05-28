List of tasks, I can do
-----------------------

Please, put here some task I can do in order to help VLC :

-  ...

List of task, I try to do
-------------------------

-  Reading info on VideoLAN wiki.
-  Reading `Mini_Projects <Mini_Projects>`__ and [http://trac.videolan.org/vlc/query?status=new&status=assigned&status=reopened&difficulty=easy&order=priority\ \` easy bugs]
-  trying compile vlc on Ubuntu, missing library libgcrypt but I have libgcrypt11

| binnette@NightShade:~/vlc_project/vlc$ ./bootstrap
| + ACLOCAL_ARGS=-I m4
| + test -d extras/contrib/bin
| + uname -s
| + test .Linux = .Darwin
| + pkg-config --version
| + PKGCONFIG=yes
| + export AUTOPOINT
| + test
| + AUTOPOINT=autopoint
| + autopoint --dry-run --force
| + AUTOPOINT=true
| + echo
| + set +x
| generating modules/**/Makefile.am
| ............................................................................
| + echo
| + echo
| + cp -f INSTALL INSTALL.git
| + autoreconf --install --force --verbose -I m4
| autoreconf: Entering directory \`.'
| autoreconf: running: true --force
| autoreconf: running: aclocal --force -I m4
| configure.ac:5219: warning: macro \`AM_PATH_LIBGCRYPT' not found in library
| autoreconf: configure.ac: tracing
| autoreconf: running: libtoolize --copy --force
| Putting files in AC_CONFIG_AUX_DIR, \`autotools'.
| configure.ac:5219: warning: macro \`AM_PATH_LIBGCRYPT' not found in library
| autoreconf: running: /usr/bin/autoconf --include=m4 --force
| configure.ac:5219: error: possibly undefined macro: AM_PATH_LIBGCRYPT
| If this token and others are legitimate, please use m4_pattern_allow.
| See the Autoconf documentation.
| autoreconf: /usr/bin/autoconf failed with exit status: 1
| Is there somebody, who can help me ? ^^

Hello, The wiki is not the place to ask for help. You'd better try on the forum or on vlc-devl @ videolan.org or on irc In your case it seems you're missing libgcrypt-dev
