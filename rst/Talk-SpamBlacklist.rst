Does this really work?
----------------------

i'm not really sure that this spam blacklist works ... could someone without admin right try entering links to one of the urls in the blacklist ? -- `Dionoea <User:Dionoea>`__ 01:01, 27 January 2006 (CET)

   The spam blacklist automatically hides changes which include a links to one of the sites mentioned on the blacklist (I think that's what happens - I'm not too sure myself). The page is set as protected so the spammers don't clear the list (or post spam on it ;).
   Meta has some stuff on how the list works: http://meta.wikimedia.org/wiki/Talk:Spam_blacklist
   --`H2g2bob <User:H2g2bob>`__ 13:39, 27 January 2006 (CET)

   -  ps- it uses regex, so if you know regex you can do some wacky matching stuff. Otherwise just use \\. instred of dots.
   -  pps - Full desctiption `here (media-wiki) <http://www.mediawiki.org/wiki/Extension:SpamBlacklist>`__

      ...I tested this under `an alt account without admin privileges <Special:Contribs/DoesItReallyMatter_sock>`__. I was able to add a dozen links listed on the SpamBlacklist [//wiki.videolan.org/index.php?oldid=27668][//wiki.videolan.org/index.php?oldid=27662] as well as "blacklisted words within URLs" [//wiki.videolan.org/index.php?oldid=27669] to the `SpamBlacklist/Test page <SpamBlacklist/Test_page>`__ page without anything more than a CAPTCHA. It doesn't feel like this will actually ward off spam. 21:00, 27 December 2014 (CET)

Can't edit the spam blacklist
-----------------------------

| I can't edit the SpamBlacklist because the word "x‍a‍n‍a‍x‍" triggers some filter; adding that word to *any* page prevents the edit from saving, even though I have admin privileges.
| Here I only sidestepped this by inserting invisible HTML entities within the word.

Does anybody have a clue what this is about or how to fix this? 21:07, 27 December 2014 (CET)

   Hmm. "s‍e‍o" is also on the filter list. I removed all links containing those words [//wiki.videolan.org/index.php?title=Sandbox&diff=prev&oldid=28263 here], fixed a regular-expression syntax error [//wiki.videolan.org/index.php?title=Sandbox&diff=prev&oldid=28265 here] (mistakenly a newline rather than a backslash-escape), then rolled my edits back because I wasn't sure what to do at that point. Maybe I'll have a better idea later.
   How ironic that I can't put certain words on a blacklist... 14:50, 6 February 2015 (CET)

      Finally I think I understand what's going on! Likely a user with access to the internal VideoLAN server edited [//www.mediawiki.org/wiki/Manual:$wgSpamRegex $wgSpamRegex] in an effort to oust spam, following repeated spammings containing either of those words. This variable affects edits differently than entries on `SpamBlacklist <SpamBlacklist>`__ do, which is why I couldn't [//www.mediawiki.org/wiki/Extension:SpamBlacklist#Whitelist circumvent this with a whitelist] on the page `MediaWiki:Spam-whitelist <MediaWiki:Spam-whitelist>`__—the VideoLAN server will reject edits from ANYONE that include either of those words, administrator or not.
      Going forward, I believe a sensible action would be to remove those words from the SpamBlacklist page (which will be safe, as users cannot spam with those words) and then anyone with administrator privileges should be able to edit `SpamBlacklist <SpamBlacklist>`__ at their leisure. 06:24, 18 February 2015 (CET)

         .. raw:: mediawiki

            {{Checkmark}}

         Seems to be okay now 09:47, 18 February 2015 (CET)
