{{muxmod=es|encoder=n}}

DTS is a private company that develops audio formats, similar to Dolby.
The term "DTS" generally refers to DTS's digital surround audio
technology that is used widely on DVD-Video discs, just like Dolby's
Dolby Digital/AC3.

DTS differs from [[Dolby Digital]] in that it uses less compression and
has a lower bass extension, which allows it to produce a better sound
quality. DTS Stereo sounds almost identical to Dolby Surround.

== Codec info == DTS Coherent Acoustics is a perceptual audio codec. The
main technique used is a QMF filter together with Huffman, ADPCM and
vector quantization.

The DTS codec consists of a core and various extensions, that improve
quality.

=== DTS Extensions === \* Core: core components with core sub stream \*
XCh: DTS-ES backward compatible 6.1 extension :Adds an extra centre
surround channel, with 6.1->5.1 downmix embedded in the core stream
using default down-mix coefficients. \* X96: sampling frequency
extension up to 96 kHz :48kHz downsampled stream is embedded in the
core. \* XXCH: channel extension beyond 5.1 :Allows up to 32 additional
channels, with the 5.1 downmix embedded in the core stream. \* XBR:
Extended Bit Rate extension (>1.5Mbps) :Guaranteed to be compatible with
the DTS core \* XLL: Lossless extension :core and residual signal are
splitted. \* LBR: Low Bit Rate component

=== DTS Products === \* DTS-Core: 5.1 Primary audio stream core
component decoder \*\* Samples everywhere :) \* DTS-ES: Core + XCh, XXCh
support \*\*
http://streams.videolan.org/samples/A-codecs/DTS/dts/ES%206.1%20-%205.1%2016bit.dts
\*\*
http://streams.videolan.org/samples/A-codecs/DTS/dts/ES%206.1%2024bit.dts
\* DTS 96/24: Core + X96 Support (+ XBR?) \*\*
http://streams.videolan.org/samples/A-codecs/DTS/dts/96-24.dts \*\*
http://streams.videolan.org/samples/A-codecs/DTS/dts/chronos%20-%2096-24.dts
\* DTS-HD High Resolution Audio: Core + XCh + XBR support \*\*
http://streams.videolan.org/misc/DTS-HD/SpeakerID-DTS-HD-HRA.mkv \*\*
http://streams.videolan.org/samples/A-codecs/DTS/dts/Hi-Res%206.1%2024bit.dts
\* DTS-HD Master Audio: Core + XLL support \*\*
http://streams.videolan.org/samples//A-codecs/DTS/dts/Master%20Audio%207.1%2024bit.dts
\*\*
http://streams.videolan.org/samples//A-codecs/DTS/dts/Master%20Audio%205.1%2024bit.dts
\* DTS Express: LBR support

-  DTS-Broadcast, DTS Neo, DTS- Surround Sensation: unknown

== Samples == http://streams.videolan.org/samples/A-codecs/DTS/dts/

== Source code == {{filedecoder packetizer}}

[[Category:Companies]]
