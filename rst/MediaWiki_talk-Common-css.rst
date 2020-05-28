== Testing if I broke something == { Test ! Test Test \|\| Test \|}

{ Test ! Test Test \|\| Test \|}

{\| \| Test ! Test Test \|\| Test \|}

Yay! --[[User:H2g2bob|h2g2bob]] 04:47, 17 December 2006 (CET)

== Link Styling ==

Hi everyone. I made it so that all links to videolan.org have a little
picture by them. Is that okay? [[User talk:The thingThe thing]]
<sup>([[User talk:The thingContribs]])</sup> 22:23, 13 July 2008 (CEST)

== Pre text wrapping ==

Hi all, I'm about to make a change for everyone here. Text in
<code><nowiki><pre>...</pre></nowiki></code> tags will now soft-wrap.<br
/> Here's a line from [[Documentation:Streaming HowTo/Advanced Streaming
Using the Command Line]] that shows you what I mean.<br /> Before (no
wrapping): <pre style="white-space:pre;word-break:normal;">% vlc
input_stream --sout
"#module1{option1=parameter1{parameter-option1},option2=parameter2}:module2{option1=...,option2=...}:..."</pre>
After (wrapping): <pre
style="white-space:pre-wrap;word-break:break-all;">% vlc input_stream
--sout
"#module1{option1=parameter1{parameter-option1},option2=parameter2}:module2{option1=...,option2=...}:..."</pre>
I prefer this because I can read without having to scroll. If you feel
differently [[User talk:DoesItReallyMatter|tell me]] and I'll revert the
change (or you can do it yourself).

{{User:DoesItReallyMatter/real_sig}} 08:11, 30 January 2019 (CET)
