\__NOTOC_\_

| The **Image** demuxer is responsible for opening most image file formats in .
| Though the module is capable of handling `JPEGs <JPEG>`__, the module handles them as of VLC 2.2.0, so they can be encoded and decoded by the same `module <module>`__. The modules handle `SVGs <SVG>`__.

Supported formats:

.. raw:: html

   <div class="col6">

-  `PNG <#PNG>`__\ :sup:`†`
-  `XCF <#XCF>`__
-  `GIF <#GIF>`__
-  `TIFF <#TIFF>`__
-  `LBM <#ILBM>`__
-  `PCX <#PCX>`__
-  `Targa <#Targa>`__
-  `MxPEG <MxPEG>`__
-  `BMP <#BMP>`__
-  `PNM <#PNM>`__
-  `WebP <#WebP>`__
-  `BPG <#BPG>`__

.. raw:: html

   </div>

:sup:`†` Encoding is supported for given format

Formats
-------

PNG
~~~

.. raw:: mediawiki

   {{Wikipedia|Portable Network Graphics}}

PNG is an acronym for portable network graphics. It was historically preferred over `GIFs <#GIF>`__ for its unencumbered license, and though GIF is now free PNG is still used out of habit. It supports a wider range of transparency than GIF and stores virtually no metadata. PNG, because it is `lossless <lossless>`__, is generally larger in size than a `JPG <JPG>`__ and somewhat smaller than a GIF.

XCF
~~~

.. raw:: mediawiki

   {{Wikipedia|XCF (file format)}}

`Run-length encoded <RLE>`__ image format. Used by `GIMP <wikipedia:GNU_Image_Manipulation_Program>`__.

GIF
~~~

.. raw:: mediawiki

   {{Wikipedia|GIF}}

GIF is an acronym for Graphics Interchange Format. It is a versatile image type that is `lossless <lossless>`__ and supports animation and `compression <compression>`__.

TIFF
~~~~

.. raw:: mediawiki

   {{Wikipedia|TIFF}}

TIFF is an acronym for Tagged Image File Format. It is a container that allows the storage of information alongside the image. It supports `lossless <lossless>`__ `compression <compression>`__.

ILBM
~~~~

.. raw:: mediawiki

   {{Website|ILBM|on=AmigaOS Wiki|https://wiki.amigaos.net/wiki/ILBM_IFF_Interleaved_Bitmap}}

A format originating on `Amiga computers <wikipedia:Amiga>`__. May appear in games from the 1980s and 1990s.

PCX
~~~

.. raw:: mediawiki

   {{Wikipedia|PCX}}

A bitmap image format developed by the ZSoft Corporation and used by MS-DOS, it is now considered deprecated.

Targa
~~~~~

.. raw:: mediawiki

   {{Wikipedia|Truevision TGA}}

Truevision TGA, also called TARGA and TGA, is a raster graphics file format.

BMP
~~~

This is a simple bitmap format that is widely supported in graphic editing programs. Microsoft developed the specification and uses it for Windows: Paint can export in this format, and BMP files can be set directly as desktop wallpapers.

PNM
~~~

.. raw:: mediawiki

   {{Wikipedia|Netbpm format}}

The Portable Anymap Format (PNM) refers to any of a set of formats designed for portability by the Netbpm project: PPM, PGM, and PBM.

WebP
~~~~

.. raw:: mediawiki

   {{Wikipedia|WebP}}

A raster graphics file format developed by `On2 <On2>`__, acquired by Google. It is derived from the `VP8 <VP8>`__ format, and a "sister project" of `WebM <WebM>`__. WebP supports both `lossy <lossy>`__ and `lossless <lossless>`__ compression. Its claims of outperforming other image file formats have been challenged.

BPG
~~~

.. raw:: mediawiki

   {{Website|BPG|https://bellard.org/bpg/}}

Better Portable Graphics (BPG) was introduced in 2014 as a more efficient replacement for `JPEG <JPEG>`__, based on the technology behind `HEVC <HEVC>`__.
