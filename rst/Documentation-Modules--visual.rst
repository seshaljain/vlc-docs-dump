.. raw:: mediawiki

   {{Module|name=visual|type=Visualization|description=Visualizer filter}}

For the option ``--effect-fft-window`` the values for window_list originate from .

The code claims ``--spect-color`` must be within 1 ≤ x ≤ 127 but no checks seem to be performed.

The options ``--visual-nbbands``, ``--visual-separ``, ``--visual-amp`` and ``--spect-nbbands`` have been obsolete since VLC 1.0.0.

This module has a single shortcut: ``visualizer`` (specifically with a z).

Options
-------

.. raw:: mediawiki

   {{Option
   |name=effects-list
   |value=string
   |default=spectrum
   |description=A list of visual effect, separated by commas
   |select={dummy,scope,spectrum,spectrometer,vuMeter}
   }}

.. raw:: mediawiki

   {{Option
   |name=effects-width
   |value=integer
   |default=800
   |description=The width of the effects video window, in pixels
   }}

.. raw:: mediawiki

   {{Option
   |name=effects-height
   |value=integer
   |default=500
   |description=The height of the effects video window, in pixels
   }}

.. raw:: mediawiki

   {{Option
   |name=effect-fft-window
   |value=string
   |default=flat
   |description=The type of FFT window to use for spectrum-based visualizations. Values correspond to "None", "Hann", "Flat Top", "Blackman-Harris", "Kaiser"
   |select={none,hann,flattop,blackmanharris,kaiser}
   }}

.. raw:: mediawiki

   {{Option
   |name=effect-kaiser-param
   |value=float
   |default=3.0f
   |description=The parameter alpha for the Kaiser window. Increasing alpha increases the main-lobe width and decreases the side-lobe amplitude
   }}

Spectrum analyser
~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Option
   |name=visual-80-bands
   |value=boolean
   |default=enabled
   |description=Show 80 bands instead of 20
   }}

.. raw:: mediawiki

   {{Option
   |name=visual-peaks
   |value=boolean
   |default=enabled
   |description=Draw peaks in the analyzer
   }}

Spectrometer
~~~~~~~~~~~~

.. raw:: mediawiki

   {{Option
   |name=spect-show-original
   |value=boolean
   |default=disabled
   |description=Enable the "flat" spectrum analyzer in the spectrometer
   }}

.. raw:: mediawiki

   {{Option
   |name=spect-show-base
   |value=boolean
   |default=enabled
   |description=Draw the base of the bands
   }}

.. raw:: mediawiki

   {{Option
   |name=spect-radius
   |value=integer
   |default=42
   |description=Defines radius size in pixels, of base of bands (beginning)
   }}

.. raw:: mediawiki

   {{Option
   |name=spect-sections
   |value=integer
   |default=3
   |min=1
   |max=<var>INT_MAX</var>
   |description=Determines how many sections of spectrum will exist
   }}

.. raw:: mediawiki

   {{Option
   |name=spect-color
   |value=integer
   |default=80
   |description=[[YUV]]-Color cube shifting across the V-plane ( 0 - 127 )
   }}

.. raw:: mediawiki

   {{Option
   |name=spect-show-bands
   |value=boolean
   |default=enabled
   |description=Draw bands in the spectrometer
   }}

.. raw:: mediawiki

   {{Option
   |name=spect-80-bands
   |value=boolean
   |default=enabled
   |description=Show 80 bands instead of 20
   }}

.. raw:: mediawiki

   {{Option
   |name=spect-separ
   |value=integer
   |default=1
   |description=Number of blank pixels between bands
   }}

.. raw:: mediawiki

   {{Option
   |name=spect-amp
   |value=integer
   |default=8
   |description=This is a coefficient that modifies the height of the bands
   }}

.. raw:: mediawiki

   {{Option
   |name=spect-show-peaks
   |value=boolean
   |default=enabled
   |description=Draw peaks in the analyzer
   }}

.. raw:: mediawiki

   {{Option
   |name=spect-peak-width
   |value=integer
   |default=61
   |description='''''Additions or subtractions of pixels''''' on the peak width
   }}

.. raw:: mediawiki

   {{Option
   |name=spect-peak-height
   |value=integer
   |default=1
   |description='''''Total pixel height''''' of the peak items
   }}

Screenshots
-----------

Click thumbnails for larger images and author attribution.

File:Spectrum visualization.png|Spectrum File:Spectrometer on Ubuntu.png|Spectrometer

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/visualization/visual/visual.c}}

.. raw:: mediawiki

   {{Documentation footer}}
