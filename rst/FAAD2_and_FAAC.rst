.. raw:: mediawiki

   {{Website|FAAD2 and FAAC|https://www.audiocoding.com}}

.. raw:: mediawiki

   {{FOSS}}

**FAAD2** or **Freeware Advanced Audio Decoder** is a project for *decoding* `AAC <AAC>`__ in `MPEG-4 <MPEG-4>`__ and `MPEG-2 <MPEG-2>`__.

**FAAC** or **Freeware Advanced Audio Codec** is a project for *encoding* AAC in MPEG-4 and MPEG-2.

Both projects are released under the GPLv2, making them `open-source <open-source>`__.\ `† <#Note>`__ SourceForge hosts `Git <Git>`__ (source code) for both components, and there are respective GitHub mirrors. SourceForge also hosts binaries (executable code) for Windows (``*.exe``) and Linux (``*.tar.gz``).

.. raw:: mediawiki

   {{VLC}}

uses the FAAD2 `library <library>`__, libfaad, in the module; but VLC no longer uses the FAAC library, libfaac.

Note
----

\ `† <#Note-backlink>`__\  When audiocoding.com says it supports DRM, it does not mean `Digital Restrictions Management <Digital_Restrictions_Management>`__ but rather *Digital Radio Mondiale*. Supporting Digital Restrictions Management might (arguably) cast doubt on whether the project is truly open-source.

Links
-----

-  `Audiocoding.com <https://www.audiocoding.com/>`__

   -  `FAAD2 page <https://www.audiocoding.com/faad2.html>`__
   -  `FAAC page <https://www.audiocoding.com/faac.html>`__

-  `SourceForge - FAAC project <https://sourceforge.net/projects/faac/>`__

   -  `FAAD2 Git <https://sourceforge.net/p/faac/faad2/ci/master/tree/>`__ (`GitHub mirror <https://github.com/knik0/faad2>`__)
   -  `FAAC Git <https://sourceforge.net/p/faac/faac/ci/master/tree/>`__ (`GitHub mirror <https://github.com/knik0/faac>`__)

-  `Git commit search for faac in VLC <https://git.videolan.org/?p=vlc.git&a=search&h=HEAD&st=commit&s=faac>`__

   -  

      .. raw:: mediawiki

         {{Commitdiff|869c2e414e1bb954a2ed4f881c87ffe0f103f209|l=contribs: disable libfaac on Darwin (as part of ffmpeg) as it considered nonfree now}}

   -  

      .. raw:: mediawiki

         {{Commitdiff|b381e4a4c9b3b8031fe0af7a6620ceea34ddd13d|l=Contrib: remove faac from ffmpeg. Without this, ffmpeg refuses to build due to licensing problems.}}

   -  

      .. raw:: mediawiki

         {{Commitdiff|34ba8bd409b16a33353b2240330b405c970b0f7c|l=Faac is NOT compatible with VLC. Too bad for your AAC encoding, but, well.}}

`Category:Third parties <Category:Third_parties>`__
