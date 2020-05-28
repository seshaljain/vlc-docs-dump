   *Were you looking for the current module, ?*

The dirac demuxer will be removed. It has already been in 4.0.0-dev.

Demux
-----

.. raw:: mediawiki

   {{Module|name=dirac|type=Access demux|first_version=1.0.0|description=[[Dirac]] video demuxer|sc=dirac}}

Options
~~~~~~~

.. raw:: mediawiki

   {{Option
   |name=dirac-dts-offset
   |value=integer
   |default=0
   |description=Value to adjust dts by
   }}

.. raw:: mediawiki

   {{Clear}}

Mux
---

.. raw:: mediawiki

   {{Module|name=dirac|type=Muxer|first_version=0.8.2|last_version=2.1.6|description=[[Dirac]] video encoder using [https://sourceforge.net/projects/dirac/files/dirac-codec/ dirac-research library]|sc=none}}

A few notes (of no real importance as this is a removed module):

-  the option ``--sout-dirac-cpd`` is, unusually, a float with an integer range
-  the option ``--sout-dirac-me-combined`` is `dependent <wikipedia:Conditional_compilation>`__ on Dirac research version of at least 1.0.1
-  the options ``--sout-dirac-multi-quant`` and ``--sout-dirac-spartition`` are disabled when set to ``-1``. They have a code comment:

      /\* NB, unforunately vlc doesn't have a concept of 'don't care' \*/

-  the options ``--sout-dirac-mc-blk-xblen`` and ``--sout-dirac-mc-blk-yblen`` were originally aliases for ``--sout-dirac-mc-blk-width`` and ``--sout-dirac-mc-blk-height`` prior to 1.0.0

.. _options-1:

Options
~~~~~~~

.. raw:: mediawiki

   {{Option
   |name=sout-dirac-quality
   |value=float
   |default=5.5
   |min=0.
   |max=10.
   |description=If [[bitrate]]=0, use this value for constant quality
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-dirac-bitrate
   |value=integer
   |default=-1
   |min=-1
   |max=<var>INT_MAX</var>
   |description=A value > 0 (in kbps) enables constant bitrate mode
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-dirac-lossless
   |value=boolean
   |default=disabled
   |description=[[Lossless]] coding ignores bitrate and quality settings, allowing for perfect reproduction of the original
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-dirac-prefilter
   |value=string
   |select={none,cwm,rectlp,diaglp}
   |default=diaglp
   |description=Enable adaptive prefiltering: The options correspond to "none", "Centre Weighted Median", "Rectangular Linear Phase", "Diagonal Linear Phase"
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-dirac-prefilter-strength
   |value=integer
   |default=1
   |min=0
   |max=10
   |description=Higher value implies more prefiltering
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-dirac-chroma-fmt
   |value=string
   |select={420,422,444}
   |default=420
   |description=Picking [[chroma]] format will force a conversion of the video into that format: "[[4:2:0]]", "[[4:2:2]]" or "[[4:4:4]]"
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-dirac-l1-sep
   |value=integer
   |default=-1
   |min=-1
   |max=<var>INT_MAX</var>
   |description=Distance between ''[[P-frame]]s''
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-dirac-num-l1
   |value=integer
   |default=-1
   |min=-1
   |max=<var>INT_MAX</var>
   |description=Number of ''P-frames'' per [[GOP]]
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-dirac-coding-mode
   |value=string
   |select={auto,progressive,field}
   |default=auto
   |description=Field coding is where interlaced fields are coded seperately as opposed to a pseudo-progressive frame (auto - let encoder decide based upon input (Best), progressive - force coding frame as single picture, field - force coding frame as seperate interlaced fields)
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-dirac-mv-prec
   |value=string
   |select={1,1/2,1/4,1/8}
   |default=1/2
   |description=Motion vector precision in pels
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-dirac-mc-blk-width
   |value=integer
   |default=-1
   |min=-1
   |max=<var>INT_MAX</var>
   |description=Width of motion compensation blocks
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-dirac-mc-blk-height
   |value=integer
   |default=-1
   |min=-1
   |max=<var>INT_MAX</var>
   |description=Height of motion compensation blocks
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-dirac-mc-blk-overlap
   |value=integer
   |default=-1
   |min=-1
   |max=100
   |description=Amount (%) that each motion block should be overlapped by its neighbours
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-dirac-me-simple-search
   |value=string
   |default=""
   |description=(Not recommended) Perform a simple (non hierarchical block matching motion vector search with search range of &plusmn;<var>x</var>, &plusmn;<var>y</var>)
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-dirac-me-combined
   |value=boolean
   |default=enabled
   |description=Use chroma as part of the motion estimation process
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-dirac-dwt-intra
   |value=integer
   |default=-1
   |min=-1
   |max=6
   |description=Intra picture DWT filter
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-dirac-dwt-inter
   |value=integer
   |default=-1
   |min=-1
   |max=6
   |description=Inter picture DWT filter
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-dirac-dwt-depth
   |value=integer
   |default=-1
   |min=-1
   |max=4
   |description=Number of DWT iterations (Also known as DWT levels)
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-dirac-noac
   |value=boolean
   |default=disabled
   |description=Disable arithmetic coding&mdash;Use variable length codes instead, useful for very high bitrates
   }}

Advanced options
^^^^^^^^^^^^^^^^

.. raw:: mediawiki

   {{Option
   |name=sout-dirac-mc-blk-xblen
   |value=integer
   |default=-1
   |min=-1
   |max=<var>INT_MAX</var>
   |description=Total horizontal block length including overlaps
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-dirac-mc-blk-yblen
   |value=integer
   |default=-1
   |min=-1
   |max=<var>INT_MAX</var>
   |description=Total vertical block length including overlaps
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-dirac-multi-quant
   |value=integer
   |default=-1
   |min=-1
   |max=1
   |description=Enable multiple quantizers per subband (one per codeblock)
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-dirac-spartition
   |value=integer
   |default=-1
   |min=-1
   |max=1
   |description=Enable spatial partitioning
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-dirac-cpd
   |value=float
   |default=-1
   |min=-1
   |max=<var>INT_MAX</var>
   |description=cycles per degree
   }}

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|p=vlc/vlc-3.0.git|modules/demux/dirac.c}}

   (demux)

-  

   .. raw:: mediawiki

      {{VLCSourceFile|p=vlc/vlc-2.1.git|modules/codec/dirac.c}}

   (mux)

.. raw:: mediawiki

   {{Documentation}}
