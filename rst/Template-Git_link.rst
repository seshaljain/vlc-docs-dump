<!---->{{#if:{{{p{{#if:{{{a{{#if:{{{f{{#if:{{{h{{#if:{{{hb[https://git.videolan.org/?p=\ {{{p}}};a={{{a}}};f={{{f}}};h={{{h}}};hb={{{hb}}}
{{{l[https://git.videolan.org/?p=\ {{{p}}};a={{{a}}};f={{{f}}};h={{{h}}}
{{{l{{#if:{{{hb[https://git.videolan.org/?p=\ {{{p}}};a={{{a}}};f={{{f}}};hb={{{hb}}}
{{{l[https://git.videolan.org/?p=\ {{{p}}};a={{{a}}};f={{{f}}}
{{{l{{#if:{{{h{{#if:{{{hb[https://git.videolan.org/?p=\ {{{p}}};a={{{a}}};h={{{h}}};hb={{{hb}}}
{{{l[https://git.videolan.org/?p=\ {{{p}}};a={{{a}}};h={{{h}}}
{{{l{{#if:{{{hb[https://git.videolan.org/?p=\ {{{p}}}
{{{l[https://git.videolan.org/?p=\ {{{p}}}
{{{l{{#if:{{{f{{#if:{{{h{{#if:{{{hb[https://git.videolan.org/?p=\ {{{p}}};f={{{f}}};h={{{h}}};hb={{{hb}}}
{{{l[https://git.videolan.org/?p=\ {{{p}}};f={{{f}}};h={{{h}}}
{{{l{{#if:{{{hb[https://git.videolan.org/?p=\ {{{p}}};f={{{f}}};hb={{{hb}}}
{{{l[https://git.videolan.org/?p=\ {{{p}}};f={{{f}}};
{{{l{{#if:{{{h{{#if:{{{hb[https://git.videolan.org/?p=\ {{{p}}};h={{{h}}};hb={{{hb}}}
{{{l[https://git.videolan.org/?p=\ {{{p}}};h={{{h}}}
{{{l{{#if:{{{hb[https://git.videolan.org/?p=\ {{{p}}}
{{{l[https://git.videolan.org/?p=\ {{{p}}} {{{l<!-- p not given branch:
show Git -->[https://git.videolan.org/ {{{lp= h= }}</nowiki></code> or
<code>{{ {{PAGENAME}} <nowiki>a= l= }}</nowiki></code> or <code>{{
{{PAGENAME}} <nowiki>a= p= f= \|h= }}</nowiki></code>

This is a meta-template, a wrapper around URL requests to
git.videolan.org. This template ''does not'' perform [[wikipedia:sanity
checkXSS]] requests from passed parameters.

Parameters: \* '''<code>a=</code>''' is the '''format''' e.g.
<kbd>blob</kbd>. This may be given free-form but only the following are
valid: <kbd>summary</kbd>, <kbd>shortlog</kbd>, <kbd>log</kbd>,
<kbd>commit</kbd>, <kbd>commitdiff</kbd>, <kbd>tree</kbd> and
<kbd>patch</kbd> \* '''<code>f=</kbd> as well if <kbd>h=</code>''' is
the '''hash''' e.g. <kbd>72f3067a6fddcd30e0ee33928a0ec6622ed2e74b</kbd>
\* '''<code>l=</code>''' is the '''label''' (optional) e.g.
<kbd>arbitrary</kbd>

Example 1:
   <code>{{{{PAGENAME}}<nowiki>a=commit|h=72f3067a6fddcd30e0ee33928a0ec6622ed2e74b}}</nowiki></code>

{{{{PAGENAME}}a=commit|h=72f3067a6fddcd30e0ee33928a0ec6622ed2e74b}}

Example 2:
   <code>{{{{PAGENAME}}<nowiki>a=commitl=First revision of
   VLC}}</nowiki></code>

{{{{PAGENAME}}a=commitl=First revision of VLC}}

Example 3:
   <code>{{{{PAGENAME}}<nowiki>a=tree|f=doc}}</nowiki></code>

{{{{PAGENAME}}a=tree|f=doc}}

Example 4:
   <code>{{{{PAGENAME}}<nowiki>a=commitdiff|h=72f3067a6fddcd30e0ee33928a0ec6622ed2e74b}}</nowiki></code>

{{{{PAGENAME}}a=commitdiff|h=72f3067a6fddcd30e0ee33928a0ec6622ed2e74b}}

Example 5:
   <code>{{{{PAGENAME}}<nowiki>a=history}}</nowiki></code>

{{{{PAGENAME}}a=history}}

Example 6:
   <code>{{{{PAGENAME}}<nowiki>a=blobh=b5e946097a7e7acbe0c90446d0752ff0f7f706ecl=This
   module no longer exists. Here's a link to it anyway}}</nowiki></code>

{{{{PAGENAME}}a=blobh=b5e946097a7e7acbe0c90446d0752ff0f7f706ecl=This
module no longer exists. Here's a link to it anyway}}

This template will branch to the most specific condition upon parameter
omission: \* <code>{{{{PAGENAME}}<nowiki>}}</nowiki></code> gives
{{{{PAGENAME}}<!---->}} rather than
https://git.videolan.org/?p=\ {{{p}}};a={{{a}}};f={{{f}}};h={{{h}}};hb={{{hb}}}
\*
<code>{{{{PAGENAME}}h=72f3067a6fddcd30e0ee33928a0ec6622ed2e74b<nowiki>}}</nowiki></code>
gives {{{{PAGENAME}}h=72f3067a6fddcd30e0ee33928a0ec6622ed2e74b}} because
no branch was specified \*
<code>{{{{PAGENAME}}a=summaryp=vlc.githb=HEAD}}

[[Category:Templates]] </noinclude>
