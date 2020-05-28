== Install MSysGit == Take latest on
https://github.com/msysgit/msysgit/releases/

And follow installation. It should be straightforward.

== Install TortoiseGit == Take the
[http://download.tortoisegit.org/tgit/ latest 32-bit version] -
currently
http://download.tortoisegit.org/tgit/1.8.9.0/TortoiseGit-1.8.9.0-32bit.msi

Start and follow installation until success. You may need to point where
MSysGit is after installation (point it to the bin/ folder).

== Checkout a project == Open explorer, create a folder named VideoLAN.

Enter it.

Right click, select ''Git Clone'' and enter one of the VideoLAN project.

In the URL text box fill in the following:
"http://git.videolan.org/git/x264.git"

Accept and wait.

For more information including access using http only, see the [[Git]]
page.

== Cygwin git issue == '''Note for Windows users using
[http://www.cygwin.com Cygwin] (linux-like build environment):'''

Applies to:

   Windows XP Service Pack 2 with Security Update '''KB925902'''
   installed Windows XP Service Pack 3

There is a problem on Windows XP (and possibly on other Microsoft
Operating Systems) with 'git clone' which aborts unexpectedly with a
Cygwin error during the 'checking out files' (reproducable every time
and at the same percentage) at the end of the clone procedure:

   $ 2 [main] git 4012 D:cygwinbingit.exe:
      \**\* fatal error - '''could not load shell32, Win32 error 487'''

This has been verified (May 22, 2008) against the currently available
Cygwin 1.5.25-12 with git package versions 1.5.5.1-1 and 1.5.4-1 and is
a generic problem which also affects cloning from other git repositories
(although x264.git seems unaffected).

The issue is referred to in the mail archives of the Cygwin project
mailing list here [http://sourceware.org/ml/cygwin/2007-07/msg00858.html
Git error on Cygwin].

By eliminating the impossible, whatever remained, however improbable, it
is the following Windows Security Update (April 3, 2007) which is
actually the cause of the Cygwin issue:
[http://www.microsoft.com/technet/security/bulletin/ms07-017.mspx
Microsoft Security Bulletin MS07-017 - Vulnerabilities in GDI Could
Allow Remote Code Execution (925902)]

Even though the same Security Update applies to the following systems,
these are reported not to be affected:

   Windows Vista Service Pack 1 Windows 2003 Server Standard Service
   Pack 2

''It is possible to get 'git clone' working again on the affected
systems by removing the Security Update (KB925902) but this is obviously
not recommended for security reasons.''

---

To use git with Cygwin (for WinXP) do this:

[Start][Run] and type "cmd".

Change to the directory where you desire to download x264 to:

cd c:ffmpeg-SVN

If you have installed Cygwin in the standard location then type this:

C:ffmpeg-SVN>c:cygwinbingit clone http://git.videolan.org/vlc/x264.git

Initialized empty Git repository in
/cygdrive/c/ffmpeg-SVN/x264/.git/<br> remote: Generating pack...<br>
remote: Done counting 6710 objects.<br> remote: Deltifying 6710
objects...<br> remote: 100% (6710/6710) done<br> remote: Total 6710
(delta 5345), reused 156 (delta 123) :<br> Receiving objects: 100%
(6710/6710), 1.63 MiB \| 25 KiB/s, done.<br> Resolving deltas: 100%
(5345/5345), done.<br>

You can use Cygwin's git under the DOS shell but if you try the same
command under the Cygwin (Bash) shell you get an error message.

---

[[Category:Building]] [[Category:Windows]]
