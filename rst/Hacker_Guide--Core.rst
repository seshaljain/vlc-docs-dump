.. raw:: mediawiki

   {{Back to|Hacker Guide}}

Introduction to libVLCcore
--------------------------

| The core of is called `libVLCcore <libVLCcore>`__.
| It manages the threads, the modules (codecs, demuxers, etc...), the modules' layers, the clocks, the playlist and all low-level control in VLC.
| For example, it is responsible for the synchronization management between all the audio, video and subtitle tracks.

| On top of libVLCcore, there is `libVLC <libVLC>`__ that allow external application builders to access to all features of the core.
| Modules are linked with libvlccore, to interact with the core.

**Modules are built against libvlccore. External applications are built against**\ `libVLC <libVLC>`__\ **.**

VLC Pipeline and Modularity
---------------------------

One of the main concepts in VLC is "**modularity**".

VLC is, in fact, a complete `multimedia framework <wikipedia:multimedia_framework>`__ (like DirectShow or GStreamer) where you can load and plug-in many modules dynamically, depending on the necessity.

| The core framework is used to do the "wiring" and the media processing, from input (files, network streams) to output (audio or video, on a screen or a network). It uses modules to do most of the work at every stage (various muxers, demuxers, decoders, filters and outputs).
| Even the interfaces are plugins for libVLC.

The modules in VLC
~~~~~~~~~~~~~~~~~~

So, VLC uses **modules** to do most of the work, at every stage of the pipeline. Modules are loaded accordingly at runtime depending on the necessity. (See `VLC Modules loading mechanism <Documentation:VLC_Modules_Loading>`__).

| Every module offers different features that will best suit a particular use-case or a particular environment.
| Besides, most portability of VLC results from writing `audio_output <{{#rel2abs:../Audio_Output}}>`__/`video_output <{{#rel2abs:../Video_Output}}>`__/`interface <{{#rel2abs:../Interfaces}}>`__ modules specific to the platform.

| **plugins** modules are loaded and unloaded dynamically by functions in .
| Modules can also be built directly into the application which uses libVLC, for instance when VLC is on an operating system that does not have support for dynamically loadable code. They are then called **builtins**.

In the `source code <{{#rel2abs:../VLC_source_tree}}>`__, modules are usually located inside the `modules/ subdirectory <{{#rel2abs:../Modules_source_tree}}>`__.

Thread management
-----------------

VLC is heavily multi-threaded.

| The single-threaded approach would have introduced too much complexity because decoder preemptibility and scheduling would then be a mastermind (for instance decoders and outputs have to be separated, otherwise it cannot be warrantied that a frame will be played at the exact presentation time).
| Multi-process approach wasn't chosen either, because multi-process decoders usually imply more overhead (problems of shared memory) and communication between processes is harder.

VLC's threading structure is modeled after POSIX threads (*pthread*). However, for portability reasons, VLC does not use ``pthread_*`` functions directly, but a similar custom set of APIs.

Threads (vlc_thread_t)
~~~~~~~~~~~~~~~~~~~~~~

``vlc_clone()``
   Creates a thread.
``vlc_join()``
   Waits for a thread to terminate and releases its resources

Mutual exclusion (vlc_mutex_t)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``vlc_mutex_init()``
   Creates a non-recursive mutex.
``vlc_mutex_init_recursive()``
   Creates a recursive mutex (discouraged).
``vlc_mutex_lock()``
   Locks a mutex, waiting if required.
``vlc_mutex_trylock()``
   Locks a mutex if it is not already locked, or returns an error otherwise.
``vlc_mutex_unlock()``
   Unlocks a mutex.
``vlc_mutex_destroy()``
   Destroys a mutex.

Condition variable (vlc_cond_t)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``vlc_cond_init()``
   Creates a condition variable using the monotonic clock (``mdate()``) for timeouts.
``vlc_cond_init_daytime()``
   Creates a condition variable using the realtime clock / wall clock for timeouts.
``vlc_cond_signal()``
   Signals one thread waiting on a condition variable.
``vlc_cond_broadcast()``
   Signals all threads waiting on a condition variable.
``vlc_cond_wait()``
   Waits for a condition variable to be signaled (can also wake up spuriously).
``vlc_cond_timedwait()``
   Waits for a condition variable to be signaled up to a certain timeout (can also wake up spuriously).
``vlc_cond_destroy()``
   Destroys a condition variable.

Misc
~~~~

VLC also has abstractions for slim read/write locks, spin locks, thread-specific variables, similar to POSIX threads.

Atomic variables
~~~~~~~~~~~~~~~~

Atomic variables are small ``(sizeof(void *))`` values that can be manipulated from multiple threads without locking. See ``include/vlc_atomic.h`` for the list of supported operations.

Synchronization
---------------

Another key feature of VLC is that decoding and playing are asynchronous: decoding is done by a decoder thread, playing is done by audio_output or video_output thread. The design goal is to ensure that an audio or video frame is played exactly at the right time, without blocking any of the decoder threads. This leads to a complex communication structure between the interface, the input, the decoders and the outputs.

Having several input and video_output threads reading multiple files at the same time is permitted, despite the fact that the current interface doesn't allow any way to do it (this is subject to change in the near future). Anyway the client has been written from the ground up with this in mind. This also implies that a non-reentrant library (including in particular liba52\ `See talk page <{{TALKPAGENAME}}>`__) cannot be used without using a global lock.

Presentation Time Stamps located in the system layer of the stream are passed to the decoders, and all resulting samples are dated accordingly. The output layers are supposed to play them at the right time. Dates are converted to microseconds, an absolute date is the number of microseconds since Epoch (Jan 1st, 1970). The ``mtime_t`` type is a signed 64-bit integer.

The current date can be retrieved with ``mdate()``. The execution of a thread can be suspended until a certain date via ``mwait ( mtime_t date )``. You can sleep for a fixed number of microseconds with ``msleep ( mtime_t delay )``.

Warning
~~~~~~~

Please remember to wake up slightly before the presentation date, if some particular treatment needs to be done (e.g. a chroma transformation). For instance in ``modules/codec/libmpeg2.c``, track of the average decoding times is kept to ensure pictures are not decoded too late.

Core Source code details
------------------------

All the `libVLCcore <libVLCcore>`__ source files are located in the directory and its subdirectories:

```audio_output/`` <{{#rel2abs:../Audio_Output}}>`__
   Initializes the audio mixer, ie. finds the right playing frequency, and then resamples audio frames received from the decoder(s).
``config/``
   Load the configuration from command line and configuration file, provides functions for the modules to read and write to configuration
``control/``
   Functions to control the behaviour of `libVLCcore <libVLCcore>`__, like Play/Pause, volume management, fullscreen, log verbosity, etc.
``extras/``
   Mostly platform-specific code
```input/`` <{{#rel2abs:../Input}}>`__
   Opens an input module, reads packets, parses them and passes reconstituted elementary streams to the decoder(s).
```interface/`` <{{#rel2abs:../Interfaces}}>`__
   Contains code for user interaction such as key presses and device ejection.
``misc/``
   Miscellaneous utilities used in other parts of libvlc, such as the thread system, the message queue, CPU detection, the object lookup system, or platform-specific code.
``modules/``
   Modules management
``network/``
   Network interface (socket management, network errors, etc.)
``osd/``
   On Screen Display manipulation
``playlist/``
   Manages playlist interaction such as stop, play, next, or random playback.
``stream_output/``
   Functions to stream audio and video to the network
``test/``
   libVLC needs to be tested, and not only by users :)
``text/``
   Charset stuff
```video_output/`` <{{#rel2abs:../Video_Output}}>`__
   Initializes the video display, gets all pictures and subpictures (ie. subtitles) from the decoder(s), optionally converts them to another format (such as YUV to RGB), and displays them.

.. raw:: mediawiki

   {{Hacker_Guide}}
