== Logo 'next to' VideoLAN links. ==

Hi,

While looking around the wiki, I noticed the little icon that has been
put in to be next to links. While this works for me in Firefox 3.5b4,
for some reason, in my main browser (Safari 4 Public Beta) and in Chrome
(2.0.172.27) the icons appear beneath the link, obscuring the text and
the icons are missing ''entirely'' in Internet Explorer 7 (haven't
checked IE8, I don't really use Windows much) and Konqueror 4...

If it's of any use, here is the code that MediaWiki 1.11 seems to use to
show icons next to external links:

<pre> #bodyContent a.external, #bodyContent a[href^="gopher://"] {
-moz-background-clip:border; -moz-background-inline-policy:continuous;
-moz-background-origin:padding; background:transparent
url(\ http://wiki.videolan.org/skins/monobook/external.png) no-repeat
scroll right center; padding-right:13px; } </pre>

so perhaps you could simply override that with
'http://www.videolan.org/favicon.ico'

One problem could be that the 'ico' format is not brilliant for inline
images and a png would be more suitable... Yours is currently: MS
Windows icon resource - 2 icons, 32x32, 256-colors

Altogether, I hope this helps sort out these little icons (or we could
just remove them :P)

--[[User:Tek|Tek]] 15:28, 16 May 2009 (CEST)

== Welcome templates ==

Hi 'The thing' - it might be better IMO to wait until the user has made
at least one contribution, since a lot of the new users are probably
spambots (username patterns are weird too).

BTW which developer, if any, are you on vlc-devel or IRC?

Thanks, [[User:EdwardwThe thing]] <sup>([[User talk:The
thingContribs]])</sup> 22:21, 22 February 2012 (CET)
