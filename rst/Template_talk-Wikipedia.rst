Linking to a specific wikipedia page
------------------------------------

It would be nice if you could use {{wikipedia|Page_Name}} to link to a page with a different title than the current page. If no {{{1}}} is specified, then it would have to default to the current page's name. I don't know how you can do this {{{1}}} definition check. -- `Dionoea <User:Dionoea>`__ 00:27, 17 January 2006 (CET)

   I tried to use {{{1|default}}} which is avaliable in wikipedia, but i don't think it works here - {{{1}}} does work though. What I mean is that supporting both {{wikipedia}} and {{wikipedia|AAC}} would be impossible. I'll switch it back to the {{wikipedia|wikipedia_page}} format though. --`H2g2bob <User:H2g2bob>`__ 00:34, 17 January 2006 (CET)

      Great ! thanks -- `Dionoea <User:Dionoea>`__ 00:38, 17 January 2006 (CET)

      I'm guessing the configuration has changed a bit since then, but I just updated it to accept {{wikipedia}} (for a link to the page name), {{wikipedia|Foobar}} for the "Foobar" article, and {{wikipedia|Foobar|Bazquux}} for the "Foobar" article but labelled "Bazquux". `MichaelBillington <User:MichaelBillington>`__ 04:30, 14 September 2010 (UTC)

      I updated it to accept up to 4 articles—{{wikipedia|foo|bar|baz|qux}} now works, as does {{wikipedia}} and {{wikipedia|foobar}}. Instead of passing the desired display name as the second parameter, it accepts label1, label2, etc. as the name to show. Wikipedia does it this way with `Template:See also <https://en.wikipedia.org/wiki/Template:See_also/doc#Usage>`__.
      {{wikipedia|Foobar|label1=Foobar alt name}} will display the link as "Foobar alt name". Hope this makes sense! 11:51, 6 November 2016 (CET)
