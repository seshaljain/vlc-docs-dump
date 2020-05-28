.. raw:: mediawiki

   {{See also|Category:Container}}

.. raw:: mediawiki

   {{Wikipedia|Demultiplexer (media file)}}

**Demuxing** is an abbreviation of **demultiplexing**. Demuxing is the process of reading a multi-part stream and saving each part – audio, video, and subtitles (if any) – as a separate stream. It is the logical reverse of the `muxing <muxing>`__ process.

For example, `AVI <AVI>`__ is a container that means *audio-video interleave*. The processing of demuxing an AVI requires separating the *audio* and *visual* components so (after being decoded by other modules) they can finally reach the speaker and monitor, respectively.

Most media file formats are multiplexed together in this way and VLC uses *demuxer* modules to separate them. Examples of demuxers that VLC uses are `asf <Documentation:Modules/asf>`__ (for `ASF <ASF>`__), `ogg <Documentation:Modules/ogg>`__ (for `Ogg <Ogg>`__) and `mkv <Documentation:Modules/mkv>`__ (for `Matroska <Matroska>`__).

See also
--------

-  `Hacker Guide/Demux <Hacker_Guide/Demux>`__

`Category:Glossary <Category:Glossary>`__
