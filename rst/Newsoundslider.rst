== new sound slider proposals ==

[[Image:Newslider 010210.png]]

*Pros*\ \*Combines two modes

*ConsUndefined behaviour between Normal sound state &amp; boosted sound
state*\ \*Boost mode should be dBA values

== new implementation ==

Current implementation is using library variables & functions within
widgets itself. Sound values changes if in hardmix mode and depends on
global defines & lib max values. No real split between values and
representation then.

New implementation requires and interface layer/adaptor between UI &
library. (wraps C or use existing C++ wrappers) Sound is 0-100%. UI
doesn't have to care about library values.

[[Category:Dev Discussions]]
