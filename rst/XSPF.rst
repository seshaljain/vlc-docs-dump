{{websitehttp://www.xspf.org/}} {{xiph|XSPF}} '''XSPF''', pronounced
"spiff", is a [[playlist]] in [[XML]] format, which is supported by
[[Xiph]]. It is a free and open format so can be easily, freely used for
sharing playlists.

== Sample == A very simple document looks like this: <syntaxhighlight
lang="xml"> <?xml version="1.0" encoding="UTF-8"?> <playlist version="1"
xmlns="http://xspf.org/ns/0/"> <trackList>
<track><location>file:///mp3s/song_1.mp3\ </location></track>
<track><location>file:///mp3s/song_2.mp3\ </location></track>
<track><location>file:///mp3s/song_3.mp3\ </location></track>
</trackList> </playlist> </syntaxhighlight>

== Compatibility == {{compat}}

== VLC Extensions == XSPF supports extensions to allow applications to
add special data. These extensions can appear in the following entries:
\* playlist \* track

The extension format is defined in the namespace
<code><nowiki>xmlns:vlc="http://www.videolan.org/vlc/playlist/ns/0/"</nowiki></code>:
<syntaxhighlight lang="xml"> <playlist version="1"
xmlns="http://xspf.org/ns/0/"
xmlns:vlc="http://www.videolan.org/vlc/playlist/ns/0/"> ... <extension
application="http://www.videolan.org/vlc/playlist/0"> ... </extension>
</playlist> </syntaxhighlight>

Currently, extensions support the following elements: \* vlc:node \*
vlc:item \* vlc:id \* vlc:option

The extensions vlc:node and vlc:item are used to specify how to display
the playlist tree, which is not supported by standard XSPF.

=== vlc:node === This element will be displayed as a node in the
playlist. It appears as an extension of the '''playlist''' block (under
playlist/extension). Only its name can be specified: <syntaxhighlight
lang="xml"> <vlc:node title="Node title"> [list of vlc:item or vlc:node]
</vlc:node> </syntaxhighlight>

=== vlc:item === This element represents a playlist item (not a node).
It appears as an extension of the '''playlist''' block (under
playlist/extension). It contains only a track id (see below, vlc:id):
<syntaxhighlight lang="xml"> <vlc:item tid="42" /> </syntaxhighlight>

=== vlc:id === This element specifies a track's id. It appears as an
extension of the '''track''' block (under
playlist/trackList/track/extension). <syntaxhighlight lang="xml">
<vlc:id>42</vlc:id> </syntaxhighlight> The value of the id corresponds
to the value of the attribute tid of vlc:item. Note that each vlc:id has
to be different, per entry, or it will not show them all.

=== vlc:option === This element allows you to add options to the input
item. It appears as an extension of the '''track''' block (under
playlist/trackList/track/extension). <syntaxhighlight lang="xml">
<vlc:option>option-name</vlc:option> </syntaxhighlight> Or, if the
option has a value: <syntaxhighlight lang="xml">
<vlc:option>option-name=option-value</vlc:option> </syntaxhighlight>

=== Example of XSPF with VLC extensions ===

Let's summarize these as an example. This one shows passing VLC options
per specified entry in the playlist. <syntaxhighlight lang="xml"> <?xml
version="1.0" encoding="UTF-8"?> <playlist version="1"
xmlns="http://xspf.org/ns/0/"
xmlns:vlc="http://www.videolan.org/vlc/playlist/ns/0/">
<title>Playlist</title> <location>D:/media/example.xspf</location>
<trackList> <track> <title>DVD seconds 42 to 45 muted</title>
<location>dvd://d:@1</location> <extension
application="http://www.videolan.org/vlc/playlist/0"> <vlc:id>3</vlc:id>
<vlc:option>start-time=42</vlc:option>
<vlc:option>stop-time=45</vlc:option> <vlc:option>no-audio</vlc:option>
<vlc:option>some-option=100</vlc:option> </extension> </track> <track>
<title>DVD seconds 49-55 unmuted (normal)</title>
<location>dvd://d:@1</location> <extension
application="http://www.videolan.org/vlc/playlist/0"> <vlc:id>4</vlc:id>
<vlc:option>start-time=49</vlc:option>
<vlc:option>stop-time=55</vlc:option> </extension> </track> </trackList>
</playlist> </syntaxhighlight> Here is an example that shows how you can
have it show nested entries within the playlist window: <syntaxhighlight
lang="xml"> <?xml version="1.0" encoding="UTF-8"?> <playlist version="1"
xmlns="http://xspf.org/ns/0/"
xmlns:vlc="http://www.videolan.org/vlc/playlist/ns/0/">
<title>Playlist</title> <location>D:/media/example.xspf</location>
<trackList> <track> <title>Track 1</title> ... <extension
application="http://www.videolan.org/vlc/playlist/0"> <vlc:id>0</vlc:id>
</extension>

   </track> <track> <title>Track 2</title> ... <extension
   application="http://www.videolan.org/vlc/playlist/0">
   <vlc:id>1</vlc:id> </extension> </track> <track> <title>Track
   3</title> ... <extension
   application="http://www.videolan.org/vlc/playlist/0">
   <vlc:id>2</vlc:id> </extension> </track> <track> <title>Track
   4</title> <location>dvd://e:@1</location> <extension
   application="http://www.videolan.org/vlc/playlist/0">
   <vlc:id>3</vlc:id> <vlc:option>my-option=100</vlc:option>
   <vlc:option>start-time=42</vlc:option>
   <vlc:option>stop-time=45</vlc:option>
   <vlc:option>no-audio</vlc:option> </extension> </track>

..

   </trackList> <extension
   application="http://www.videolan.org/vlc/playlist/0"> <vlc:node
   title="Node 1"> <vlc:item tid="0" /> <vlc:item tid="1" /> <vlc:node
   title="Node 2"> <vlc:item tid="2" /> <vlc:item tid="3" /> </vlc:node>
   </vlc:node> </extension>

   </playlist>

</syntaxhighlight>

This playlist example will be displayed as:
   Playlist - Node 1 \|- Track 1 \|- Track 2- Node 2 \|- Track 3 \`-
   Track 4

The input for ''Track 4'' will be created with the option ''my-option''
set to 42.

== See also == \* [[Media Library]] a function built into VLC media
player There are many advantages to using XML as the format. More
information is available at \* [http://www.xiph.org/ Xiph.org] \*
[http://www.xspf.org/quickstart/ XSPF project website].

== Unsafe operations == Some operations, like setting volume, setting
sout destination, etc. are deemed "unsafe" to be in the playlist, so
you'll have to add those settings to the command line instead. You'll
get the error message: '''unsafe option "sout-audio" has been ignored
for security reasons)''' or the like.

http://forum.videolan.org/viewtopic.php?f=14&t=78945

[[Category:Playlist]]
