== TODO ==

-  weird to begin with a 3rd level title (very often a second level)
   (<nowiki>===</nowiki> instead of <nowiki>==</nowiki>?)
-  Does the wiki preference link and VLC preference files should be
   merged in the same page?
-  --[[User:Thannoy|Thannoy]] 15:31, 29 September 2008 (CEST)

== <span id="Playback_States"></span> Playback States == === Saving
State ===

We have different settings and options per media and per Application in
the clients. The settings should behave the same across all of
Platforms. This document tries to formulate a guideline on how to
persist these states

====What states need to be considered for persistance?====

{\| border="1" cellpadding="2" class="wikitable" style="border: 1px
solid dark green; text-align: center; align: left; margin: 1em auto 1em
auto" ! scope="col" width="150px" \| State/Setting ! scope="col"
width="100px" \| Media ! scope="col" width="100px" \| Application !
scope="col" width="100px" \| has Default Repeat \|\| {{No}} \|\| {{Yes}}
\|\| {{No}} \|\| Playback speed \|\| {{Yes}} \|\| {{No}} \|\| {{Yes}}
\|\| Shuffle \|\| {{No}} \|\| {{Yes}} \|\| {{No}} \|\| Audio/Video track
\|\| {{Yes}} \|\| {{No}} \|\| {{No}} \|\| Aspect Ratio \|\| {{Yes}} \|\|
{{No}} \|\| {{No}} \|\| Audio/Video sync \|\| {{Yes}} \|\| {{No}} \|\|
{{Yes}} \|\| Equalizer \|\| {{No}} \|\| {{Yes}} \|\| {{No}} \|\|
Subtitle sync \|\| {{Yes}} \|\| {{No}} \|\| {{Yes}} \|\| last played
media \|\| {{No}} \|\| {{Yes}} \|\| {{No}} \|\| play as audio \|\|
{{No}} \|\| {{Yes}} \|\| {{No}} \|\| Current renderer \|\| {{No}} \|\|
{{Yes}} \|\| {{No}} \|\| Current position in playlist \|\| {{No}} \|\|
{{Yes}} \|\| {{No}} \|\| \|}

has Default: means that there is a general value and can be changed in
the settings or somewhere in the application

Application: means that it is application wide one state

Media: just a state per media

====Reasoning====

=====Playback Speed=====

If you watch conference videos you might want to double the speed.
Persisting this across the Application when you change it on one Media
item and applying it to the next might be confusing and unwanted.
Instead there should be a default playback speed that can be set. Up for
discussion is still if it should be a checkmark next to the playback
speed control like [x] always apply or if it should be somewhere hidden
in the settings. On Android Devices we also detect the medium, like
Podcast or Audiobook to set a different playback speed automatically.

===== Audio Video sync, subtitle sync ===== For bluetooth headsets some
users want a default delay to make up for the delay experienced due to
bluetooth connectivity
