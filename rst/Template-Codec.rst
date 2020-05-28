{{top box }}}??[[Category:Codecs missing ids]]}} audio = an
[[Codec#Audiovideo = a [[Codec#Video#default = a [[codec]]<!---->}}. The
name to use at the [[command line]] is
{{#if:{{{id'''{{{id}}}'''}}}}}}n}}}<!-- -->n = <!-- -->{{{encoder}}}]]
module.<!-- -->}}<!--Line 3: -->{{#if:{{{for <br />This codec can be
used inside the {{{for}}} containers.}}<!--Line 4: -->{{#if:{{{mod <br
/>This codec is from the
[[Documentation:Modules/{{{mod}}}bgcol={{#switch:{{{type}}}<!-- -->\|
audio = #f0fcfc<!-- -->\| video = #fcf0fc<!-- -->\| #default = White<!--
-->}} audio = #a0c0c0<!-- -->\| video = #c0a0c0<!-- -->\| #default =
#aaa<!-- -->}} }} <includeonly>{{#switch:{{{type}}}<!-- -->\| audio =
[[Category:Audio codecs]] [[Category:Codecs]]<!-- -->\| video =
[[Category:Video codecs]] [[Category:Codecs]]<!-- -->\| #default =
[[Category:Codecs]]<!-- -->}}</includeonly><noinclude>
<!-------------------- Documentation goes below this line
---------------------> A meta-template for codecs.

Usage:
   <nowiki>{{codec id= \| altid= \| altid2= \| encoder= \| for= \| mod=
   }}</nowiki>

You should supply type and id, the rest are optional. \* type: the type
of codec, currently audio or video \* id: the module name for the codec.
If other shortcuts to the same module exist, also list them with altid,
or altid and altid2 \* for: a list of containers this codec is
compatible with. Put the names in <nowiki>[[ ]]</nowiki> so they link
properly \* mod: module name from [[Documentation:Modules]] \* encoder:
\*\* If equal to <kbd>y</kbd>, display a message, currently "<samp>VLC
can '''encode''' using this codec.</samp>" \*\* If equal to <kbd>n</kbd>
(default), do nothing \*\* All other values attempt to link to a module
of that name (even if it doesn't exist!). Useful for e.g. H.264 and
H.265, which decode and encode through separate modules

== See also == \* {{tlCodec audio}} \* {{tlMux}}

[[Category:Templates]]
<!----------------------------------------------------------------------------->
</noinclude>
