== Websites' Status ==

Let me be clear: '''WE NEED HELP'''.

I mean, jokes aside, the website are not very maintained, but I did my
best to regroup them a bit.

=== Wiki === This wiki is out of date (I can update, just tell me what
to update to)

It lacks extensions (tell me which ones to install)

It lacks correct group management (ideas are welcome)

It is still full of crap and need someone with good Wikimedia knowledge
to bump it up.

=== Forum === The forum should be quite up-to-date (I don't trust phpBB
security) and works quite correctly.

=== Trac === Trac is in a mess I can't describe... But well, we need a
forge to do the same, and I haven't find one yet.

=== Main WWW === It needs some cleanup, some nice JS, some CSS
improvements and some contents correction (VLC description sucks)

You can get the code on our svn, you know?

=== Authentication === We need some simple to manage identification that
would work on phpBB, trac and wiki. Any good idea?

== Some suggestions and follow-up ==

Well, to start, thanks for the response and I'll suggest the little I
can...

=== Wiki ===

Rather than my own description, a more detailed explanation can be found
here:

[http://www.mediawiki.org/wiki/Manual:Upgrading Manual:Upgrading] (sorry
for the external link, Interwiki links seem not to work here)

Upgrading makes sense, mainly for bug-fixes and security but also for
the wealth of new features often introduced...

:: '''Upgrade done today to latest mediawiki''' [[User:J-b|jb]] 11:20,
18 May 2009 (UTC)

When it comes to extensions, I will have to think about which ones are
relevant to this wiki and I will see if I can come back to you on that.
In the meanwhile, perhaps some of the sysops around here could help? ::
We are a bit alone... I added the OpenID extension [[User:J-b|jb]]

::: Ah this is good to see. As you posted this message, I was in the
process of writing a response to your above message about upgrading
MediaWiki. I just successfully installed OpenID on my own private wiki
as well to test its stability and was about to post the result when you
mentioned that this is done. I will try and log in with my OpenID as
soon as I finish this message and hopefully all is well! I just wanted
to point out that the [[MediaWiki:SidebarTek]] 11:53, 18 May 2009 (UTC)

:::: Oh dear... It seems that every time I finish a message here,
another is posted beneath and I start again. I am just going to post
this before it gets overwritten again :D [[User:Tek|Tek]] 11:53, 18 May
2009 (UTC)

::::: Icons and CSS are back. OpenID still broken. DB tables weren't
created [[User:J-b|jb]] 11:58, 18 May 2009 (UTC)

:::::: '''Hi, having had a look at the problem you mention, it is clear
that the database hasn't been updated. The solution would be to run
'sudo php maintenance/update.php' in the mediawiki installation
directory to update the database. This may take a few minutes...'''

::::::: '''Hurray! OpenID works!!!'''

:::::::: I manually created the tables, using the sql file, but yes,
that works now. Issue closed. [[User:J-b|jb]] 12:32, 18 May 2009 (UTC)

In terms of group management, it makes sense for most of the pages on
this wiki to be editable by anyone, as they are documentation and as
such should be fine for anyone to edit. However, it may make sense to
use FlaggedRevs as does Wikinews and mark certain pages for approval or
to simply do as with Wikipedia and just ask for volunteers to watch the
documentation as it changes ([[Special:Recentchanges]]) and correct any
notable errors. This would probably not be inconceivable due to the low
rate at which articles are currently updated here (a few a day).

As for good Wikimedia knowledge, while I certainly couldn't consider
myself even vaguely qualified to help, I pick up on most things pretty
quickly and have been managing my own private wiki for a few years and
so may be able to help a little with the technical side of sorting out
the wiki (e.g. templating, tidying up) if not necessarily the community
side (though I have worked on/helped out with several small community
run sites) as I know how Mediawiki works in a fair amount of detail.
Once again however, perhaps some of the sysops I have seen around may
know a fair bit about this? :: So maybe add a power-user group?
[[User:J-b|jb]]

::: Well, the in-house power-user group is usually sysops but it is
quite possible, using wgGroupPermissions to add a power-user group with
some, but not all sysop abilities. I could definitely help set that up
if needed as I use wgGroupPermissions a lot myself... Perhaps a list
could be made of which permissions they should have?
[http://www.mediawiki.org/wiki/Manual:User_rights This page] should list
all rights...

=== Forum ===

The forum appears to work beautifully and happily appears to be on the
latest version of phpBB. Hurray!

=== Trac ===

While Trac does appear to be in a mess, it is certainly a brilliant and
trusted bug tracking system, used by many projects and hence surely
can't be impossible to get working again.

Unfortunately, of the mentioned systems, Trac is the one in which I have
the least experience and hence without looking at it further myself, I
couldn't really suggest much to be done.

When it comes to alternatives, [http://www.bugzilla.org/ Bugzilla] is
one, used by organisations such as the Linux kernel project, NASA and
Facebook. However, if you wish to stick with Python, there is the
excellent [http://roundup.sourceforge.net Roundup] too.

However, it probably does make sense, rather than switching, to try and
repair Trac and I will see if I can either have a look at it myself or
find a friend with more experience with this bug tracker. Once again, I
am sure there are some clear reasons for the errors involved. :: Well I
guess I'll have to hack on it manually. [[User:J-b|jb]] 11:51, 18 May
2009 (UTC)

=== Main WWW ===

Hmm... I will definitely have a look but the sites already have a
personality to them, which spreads beautifully across the multiple sites
(www, wiki, forum, though NOT Trac (note that Roundup and Bugzilla can
be made to look very good)).

However, if I can see any improvements that can be made to the various
sites I will try and suggest them. :: WWW could get some JS and CSS
improvements and could be simplified.

=== Authentication ===

As noted in your [[Admin TODO]] page, the idea of OpenID being
implemented is a good one and easily possible across all three systems:

-  Trac: http://trac.sandbox.lt/auth/wiki/AuthOpenIdPlugin - note that
   this does NOT interfere with the built in authentication (''You don't
   need to disable default authentication mechanism (trac.web.auth.*) if
   you are using it. OpenID plugin does not conflict with default
   authentication mechanism.'')
-  phpBB: http://phpbbopenid.com/viewtopic.php?f=2&t=2 and
   http://sourceforge.net/projects/phpbb-openid/ both seem to work but
   the second seems more integrated...
-  MediaWiki: Perhaps the easiest and most official of them all:
   http://www.mediawiki.org/wiki/Extension:OpenID which also,
   incidentally, if you so wish, allows users to use their MediaWiki
   User page to log into other OpenID sites...

and finally...

:: trac and mediawiki extensions installed: none work....

::: Hi, having had a look at the problem you mention, it is clear that
the database hasn't been updated. The solution would be to run 'sudo php
maintenance/update.php' in the mediawiki installation directory to
update the database. This may take a few minutes... [[User:Tek|Tek]]
12:03, 18 May 2009 (UTC)

:::: Works now. Only issue is trac and openID

::::: Hmm.. yes... I appear to be able to log into Trac fine with OpenID
but it does appear to keep logging me out every time I browse to a new
page. The odd part is, it appears to be storing a cookie called
'trac_session' and so should stay logged in. The only other thing I
notice is that it keeps telling me that I have limited permissions until
I validate my e-mail address, then telling me that my address is already
validated. Perhaps this problem is something to do with the manual
validation you mention that you have enabled to stop spammers?
[[User:Tek|Tek]] 12:43, 18 May 2009 (UTC)

:::::: Ah, I just noticed what may be the problem, which is that Trac is
not setting the cookie called 'trac_auth' which it sets when you log in
as a normal user. Perhaps this is the problem? [[User:Tek|Tek]] 12:47,
18 May 2009 (UTC)

::::::: Oh and I just thought I'd point out that oddly enough, my user
page: [[User:Tek]] is giving an nginx 404 error for some reason. Perhaps
the short URL configuration has gone haywire?

=== IRCWeb ===

For one reason or another, your link to your 'IRCWeb' client appears not
to work.

From: http://www.videolan.org/developers/ The link is to:
http://krishna.videolan.org/cgi-bin/irc/irc.cgi

From: http://www.videolan.org/support/ The link is to:
http://www.videolan.org/webirc/

However neither of these actually works. (with the /webirc/ folder
missing from the /videolan/www.videolan.org/ folder of your Subversion
respository)

Perhaps this just needs to be copied into place?

For the meanwhile, the following link should work (using Mibbit):
https://www.mibbit.com/chat/?url=irc%3A%2F%2Firc.videolan.org%2F%23videolan

Altogether, I hope this helps and that these issues can be resolved as
soon as possible. Finally, do tell me if I can be of any help and you
can of course e-mail me using: [[Special:Emailuser/Tek]]

:: Done for WebIRC [[User:J-b|jb]] 11:55, 18 May 2009 (UTC)

Hope this helps, [[User:Tek|Tek]] 14:49, 17 May 2009 (CEST)

== Finally ==

Sorry it took so long, but I finally got around to fixing the icons next
to the links.

--------------

Hurray! This is nice to hear and it's nice to see how well the VLC sites
are doing now, relatively.

I'm sorry I can't be around to help with things at the moment due to
lots of personal hassles but I hope to be able to help out some more
relatively soon...

[[User:Tek|Tek]] 14:19, 21 December 2009 (UTC)
