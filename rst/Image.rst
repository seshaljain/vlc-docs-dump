{{muxencoder=n}}

The '''Image''' demuxer is responsible for opening most image file
formats in {{VLC}}.<br /> Though the {{docmodjpeg}} module handles them
as of VLC 2.2.0, so they can be encoded and decoded by the same
[[module]]. The {{docmod|svg}} modules handle [[SVG]]s.

Supported formats: <div class="col6"> \* [[#PNGXCF]] \* [[#GIFTIFF]] \*
[[#ILBMPCX]] \* [[#TargaBMP]] \* [[#PNMWebP]] \* [[#BPG|BPG]] </div>
<sup>&dagger;</sup> Encoding is supported for given format

== Formats == === PNG === {{WikipediaGIF]]s for its unencumbered
license, and though GIF is now free PNG is still used out of habit. It
supports a wider range of transparency than GIF and stores virtually no
metadata. PNG, because it is [[lossless]], is generally larger in size
than a [[JPG]] and somewhat smaller than a GIF.

=== XCF === {{WikipediaRun-length encoded]] image format. Used by
[[wikipedia:GNU Image Manipulation Program|GIMP]].

=== GIF === {{Wikipedia|GIF}} GIF is an acronym for Graphics Interchange
Format. It is a versatile image type that is [[lossless]] and supports
animation and [[compression]].

=== TIFF === {{Wikipedia|TIFF}} TIFF is an acronym for Tagged Image File
Format. It is a container that allows the storage of information
alongside the image. It supports [[lossless]] [[compression]].

=== ILBM === {{Websiteon=AmigaOS WikiAmiga computers]]. May appear in
games from the 1980s and 1990s.

=== PCX === {{Wikipedia|PCX}} A bitmap image format developed by the
ZSoft Corporation and used by MS-DOS, it is now considered deprecated.

=== Targa === {{Wikipedia|Truevision TGA}} Truevision TGA, also called
TARGA and TGA, is a raster graphics file format.

=== BMP === This is a simple bitmap format that is widely supported in
graphic editing programs. Microsoft developed the specification and uses
it for Windows: Paint can export in this format, and BMP files can be
set directly as desktop wallpapers.

=== PNM === {{Wikipedia|Netbpm format}} The Portable Anymap Format (PNM)
refers to any of a set of formats designed for portability by the Netbpm
project: PPM, PGM, and PBM.

=== WebP === {{Wikipedia|WebP}} A raster graphics file format developed
by [[On2]], acquired by Google. It is derived from the [[VP8]] format,
and a "sister project" of [[WebM]]. WebP supports both [[lossy]] and
[[lossless]] compression. Its claims of outperforming other image file
formats have been challenged.

=== BPG === {{Websitehttps://bellard.org/bpg/}} Better Portable Graphics
(BPG) was introduced in 2014 as a more efficient replacement for
[[JPEG]], based on the technology behind [[HEVC]].
