===================
Module:
===================
Type
First VLC version
Last VLC version
Operating system(s)
Description
Shortcut(s)
===================

Template for Documentation:Modules/\* pages.

Usage
-----

::

    {{Module
     |type          = module type
     |first_version = Version of VLC in which plugin first appeared
     |last_version  = Version of VLC in which plugin last appeared before being removed
     |os            = Operating system of the plugin
     |description   = A short, brief description of the plugin
     |sc            = Shortcut
     |sc2           = Shortcut 2
     |sc3           = Shortcut 3
     |sc4           = Shortcut 4
     ...
     |sc11          = Shortcut 11
    }}

| Source code identifies shortcuts with ``add_shortcut( "foo", "bar" )`` in the module descriptor. Generally omit non-specific shortcuts. Pass the first shortcut to **``|sc=``**, a possible second to **``|sc2=``**, etc.
| If **``|sc=``** is set to *none* (none) will be shown. No data is indicated with -. 

`Category:Accesses <Category:Accesses>`__ `Category:Access demux <Category:Access_demux>`__ `Category:Access filters <Category:Access_filters>`__ `Category:Access output <Category:Access_output>`__ `Category:Audio decoders <Category:Audio_decoders>`__ `Category:Audio encoders <Category:Audio_encoders>`__ `Category:Audio output <Category:Audio_output>`__ `Category:Muxers <Category:Muxers>`__ `Category:Packetisers <Category:Packetisers>`__ `Category:Packetisers <Category:Packetisers>`__ `Category:Services discovery <Category:Services_discovery>`__ `Category:Stream output <Category:Stream_output>`__ `Category:Video filters <Category:Video_filters>`__ `Category:Video output <Category:Video_output>`__ `Category:Video output filters <Category:Video_output_filters>`__ `Category:Video output splitters <Category:Video_output_splitters>`__ `Category:Video sub-filters <Category:Video_sub-filters>`__ `Category:Visualisations <Category:Visualisations>`__ `Category:Modules <Category:Modules>`__ `\* <Category:Modules>`__ `Category:Templates <Category:Templates>`__
