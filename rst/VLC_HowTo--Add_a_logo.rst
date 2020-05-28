.. raw:: mediawiki

   {{howto|add a logo on your video using the logo filter}}

Idea
----

This How To just explains how to use the logo filter in order to add a logo on your videos, like a TV.

Local
~~~~~

``{{%}} vlc --sub-source logo --logo-file ``\ *``logo.png``*\ `` ``\ *``video.avi``*

Stream
~~~~~~

``{{%}} vlc --logo-file ``\ *``logo.png``*\ `` ``\ *``video.avi``*\ `` --sout "#transcode{vcodec=...,vb=...,sfilter=logo}:std{...}"``

Make sure you do not specify --sub-source logo, and that you specify a vcodec= value in the `transcode <transcode>`__ part.

Save the new video locally
~~~~~~~~~~~~~~~~~~~~~~~~~~

``{{%}} vlc --logo-file ``\ *``logo.png``*\ `` ``\ *``video.avi``*\ `` --sout "#transcode{vcodec=...,vb=...,sfilter=logo}:std{access=file,dst=``\ *``new_video.avi``*\ `` }``

Dynamically change logo using `RC <RC>`__, then send output to stream and local debugging display
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| ``{{%}} vlc -I rc --logo-file nonexistent_dummy.png --sout "#transcode{vcodec=...,vb=...,sfilter=logo}:duplicate{dst=display,dst=std{...}}"``
| ``# Once the program has started``
| ``add ``\ *``video.avi``*
| ``# If using VLC 0.8.6 or older:``
| ``logo-file ``\ *``logo.png``*
| ``# If using VLC 0.9.0 or newer (see NEWS for details about the new syntax):``
| ``@logo logo-file ``\ *``logo.png``*

This requires a ``--logo-file``, but for some reason it won't work if you specify "``--sub-source logo``". Nor does it apparently work if the ``transcode`` doesn't specify `````\ ``vcodec=`` <Codec#Video>`__.

A non-existent logo-file currently removes any logos from the video, and does not result in an error. Since you must specify one on the command-line, "``nonexistent_dummy.png``" was used.

Troubleshooting
---------------

My text doesn't look right! It's sort of pixellated or has artifacts.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sounds like a stretching or `deinterlacing <deinterlacing>`__ problem. One possible solution is to set your "``--aspect-ratio``" to the right setting. For instance, I got this when I ran VLC with "``-vvv``" (for verbose verbose verbose output—\ *note: only verbose verbose exists anymore*):

| ``[00000372] main video output debug: picture in 704x576 (0,0,704x576), chroma I420, ar 4:3, sar 12:11``
| ``[00000372] main video output debug: picture user 704x576 (0,0,704x576), chroma I420, ar 4:3, sar 12:11``
| ``[00000372] main video output debug: picture out 768x576 (0,0,768x576), chroma RV32, ar 4:3, sar 1:1``

Here, the input was 704x576 resolution and VLC outputted it to 768x576. My text was added before this stretching occurred, and so the text looked awful. Forcing it back to the normal resolution using "``--aspect-ratio 11:9``" worked. (Because 704/576 = 11:9.)

See also `Documentation:Modules/logo <Documentation:Modules/logo>`__.

Note also that setting the logo on the command line appears to be a "global" option and not available as stream specific.

.. raw:: mediawiki

   {{DEFAULTSORT:Logo|noerror}}
