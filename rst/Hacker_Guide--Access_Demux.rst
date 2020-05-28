.. raw:: mediawiki

   {{Back to|Hacker Guide}}

Description
-----------

The modules of **'access_demux**' capability are designed to handle the `access <{{#rel2abs:../Access}}>`__ and part of the `demux <{{#rel2abs:../Demux}}>`__ stage in the same module.

Therefore, you are **required** to read `access <{{#rel2abs:../Access}}>`__ and `demux <{{#rel2abs:../Demux}}>`__ pages before going on.

An access-demuxer could be seen as a demuxer that handles the access at the same time.

In an access-demuxer, the stream s is null.

Examples of access-demuxer are DVD, Bluray, v4l2 modules.

Write an access-demux module
----------------------------

To write an access_demuxer module, start by reading the `introduction to module writing <{{#rel2abs:../How_To_Write_a_Module}}>`__.

Then, you should specify your module of being of access_demux type:

| ``set_capability( "access_demux", 60 )``
| ``set_category( CAT_INPUT )``
| ``set_subcategory( SUBCAT_INPUT_ACCESS )``

Functions to implement
----------------------

After implementing Open() and Close() functions, you will need to implement a few majors features that will be implemented by your functions.

As you can see in `demux <{{#rel2abs:../Demux}}>`__, you should define:

-  Demux, as in pf_demux
-  Control, as in pf_control *' NB:*' please refer to `demux Control documentation <{{#rel2abs:../Demux#Control}}>`__

After implementing those functions, you should assign them to the corresponding pf\_ function.

See and

Demux
-----

Demux in access_demux is a bit different than in a demux module, because all the seeking and access of the stream is internal to the module.

*Prototype*:

`` int (*pf_demux)  ( demux_t * ); ``

*Return*:

It should return 0 for EOF, something positive when success and something negative when fail to demux.

.. raw:: mediawiki

   {{Hacker_Guide}}
