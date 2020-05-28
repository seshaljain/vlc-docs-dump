{{Moduletype=Visualization|description=Visualizer filter}}

For the option <code>--effect-fft-window</code> the values for
<var>window_list</var> originate from
{{VLCSourceFile|modules/visualization/window_presets.h}}.

The code claims <code>--spect-color</code> must be within 1 &le;
<var>x</var> &le; 127 but no checks seem to be performed.

The options <code>--visual-nbbands</code>, <code>--visual-separ</code>,
<code>--visual-amp</code> and <code>--spect-nbbands</code> have been
obsolete since VLC 1.0.0.

This module has a single shortcut: <code>visualizer</code> (specifically
with a <samp>z</samp>).

== Options == {{Option value=string description=A list of visual effect,
separated by commas name=effects-width default=800 name=effects-height
default=500 name=effect-fft-window default=flat
select={none,hann,flattop,blackmanharris,kaiser} }} {{Option value=float
description=The parameter alpha for the Kaiser window. Increasing alpha
increases the main-lobe width and decreases the side-lobe amplitude }}

=== Spectrum analyser === {{Option value=boolean description=Show 80
bands instead of 20 }} {{Option value=boolean description=Draw peaks in
the analyzer }}

=== Spectrometer === {{Option value=boolean description=Enable the
"flat" spectrum analyzer in the spectrometer }} {{Option value=boolean
description=Draw the base of the bands }} {{Option value=integer
description=Defines radius size in pixels, of base of bands (beginning)
}} {{Option value=integer min=1 description=Determines how many sections
of spectrum will exist }} {{Option value=integer
description=[[YUV]]-Color cube shifting across the V-plane ( 0 - 127 )
}} {{Option value=boolean description=Draw bands in the spectrometer }}
{{Option value=boolean description=Show 80 bands instead of 20 }}
{{Option value=integer description=Number of blank pixels between bands
}} {{Option value=integer description=This is a coefficient that
modifies the height of the bands }} {{Option value=boolean
description=Draw peaks in the analyzer }} {{Option value=integer
description='''''Additions or subtractions of pixels''''' on the peak
width }} {{Option value=integer description='''''Total pixel height'''''
of the peak items }}

== Screenshots == Click thumbnails for larger images and author
attribution. <gallery> File:Spectrum visualization.pngSpectrometer
</gallery>

== Source code == \*
{{VLCSourceFile|modules/visualization/visual/visual.c}}

{{Documentation footer}}
