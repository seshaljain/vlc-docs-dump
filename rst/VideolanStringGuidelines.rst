'''Draft 0.1.1'''

The goal of this guide is to ensure that all configuration and interface
[[strings]] will be consistent, well-written and well-translated,
providing a better user experience.

= Developers =

== Write correct English ==

Many VLC developers are not native English speakers, which often leads
to <s>badly</s> poorly written strings.

Please always have your strings proofread, preferably by a native
English speaker (even if you are one yourself).

== Avoid technical jargon as much as possible ==

If some terms sound common to you, they may be impossible to understand
for others. If you cannot avoid using them, try explaining them (for
configuration options, use the extended descriptions, for interfaces,
use tool tips). Try not being too verbose either.

Of course, some advanced concepts are quite hard to explain. Don't try
too much explaining things, and don't hesitate to ask the user to read
the documentation.

== Make your string translatable if needed ==

Only strings that are visible in the GUI must be translated, such as: \*
interface description \* module descriptions / longnames / shortnames \*
configuration options \* "mms://", "http://", "UDP", "RTP" don't need to
be translated \* module shortcuts and shortnames must not be made
translatable \* Debug messages must not be made translatable.

-  \_("") makes a string translatable and also actually does translation
   (calls gettext)

\* \_NS("") is the macosx variant of \_(""). It's short for
<nowiki>[NSApp localizedString: ""]</nowiki>. There is also a
<nowiki>[NSApp delocalizeString:@""]</nowiki>. Note that OS X is
entirely UTF-8 native. \* `N <>`__\ () only makes a string translatable.
It is safe to use it in #defines and in arrays. Also use this when
translating strings during the creation of config variables. \* Try to
keep strings UTF-8 where possible, to make sure a string can be
displayed in Chinese just as easily as in English. \* wxU is used for c
UTF-8 strings to Unicode conversion. wxL2U transforms from current
locale to Unicode.

Since 0.9.0 use qfu(), qtr(), qtu(). See
[http://trac.videolan.org/vlc/browser/trunk/modules/gui/qt4/qt4.hpp
modules/gui/qt4/qt4.hpp] for more.

== Use correct syntax == \* Sentences must end with a period. \* All GUI
strings, such as the following, should start with a capital letter: \*\*
module names \*\* short and long descriptions \*\* menu items \* Debug
messages don't start with a capital and don't end with a point \* For
menu items, put a Capital At Each Word. \* Put a space after ',' ';' ':'
'.' '?' and '!'. There is no space before these characters. \* ...

== Configuration option descriptions ==

Configuration option descriptions consist of a short and a long
description.

=== The short description ===

The short description must be kept short (40 characters maximum). Keep
in mind that translations are often longer than the English version.

The short description should be easily understandable for an advanced
user. It must not be a full sentence, must not contain question marks or
words like "setting". Because as it is in the preferences it's a
setting.

=== The long description ===

The long description should not just repeat the short description (and
in most cases, not repeat it at all). This is pointless and probably
proves that your descriptions are not properly thought.

The extended description should ''generally'' use complete sentences.
Use of paragraphs is encouraged to improve readability and separate
ideas.

Don't be too verbose. This clutters the help output and the interfaces.

Avoid using structures like "Please choose", "select" or "specify".
Passive voice should be preferred over second person: Use "When this
option is enabled" rather "If you enable this option".

Bad: "Please specify an integer for foo" Good: "An integer for foo,
which is ..."

=== Specifics ===

\* ''String, integer, float'': The short description should be a prompt,
never a question. \*\* Bad : "IP Address ?" or "Which channel ?" \*\*
Good: "IP Address " or "Channel " *:The short description must include
range and unit, if available. Example: "Frequency (1000-20000 Hz)"*:The
long description should rather explain what the user should enter rather
than merely rephrasing the short description.

-  Multi-select choices: Use a prompt. Do not use "please choose" or
   "please select", the user can guess that...

\* Booleans: The short description should not be a direct question \*\*
Bad : "Video overlay ?" \*\* Good : "Video overlay" \*:For the long
description, please prefer "Enable foo to get bar" rather than "If you
enable foo, you will get bar" (which produces long heavy sentences)

== Miscellaneous ==

-  msg_Dbg can be quite cryptic. msg_Warn, msg_Info and msg_Err MUST be
   explicit and understandable.
-  All strings in all languages should be gender-neutral.
-  You should never use the first person (neither "I" nor "we").
   Computers don't speak and our strings don't speak for the VideoLAN
   team.
-  Try reusing strings. This avoids translation efforts and improves
   consistency.
-  Don't make assumptions on the way interfaces are organized. Don't
   forget your strings should apply to the command line and to the GUI
   likewise. So don't use "If you choose yes", "If you tick this
   checkbox" etc.

== Common translations ==

[TODO: Gather them here!]

= Translators =

All user-visible strings are translated. Debug messages are not.

== Don't desperately try to translate ==

Many video specific terms have no equivalent in other languages. Don't
desperately try to translate them. This often leads to quite ridiculous
expressions.

What you can do is quote the English word in the short description /
menu item and explain it in your own words in the long description /
tool tip, without trying to translate word for word.

== Test your translation ==

Compile your translation and enable it (this is explained on the
developers page). You should particularly look for overflows (too long
translated strings).

If you feel you can't reduce the size of your string, you should contact
the developer(s) so that the problem can be solved smoothly

== Consistency ==

It is recommended to choose translations for command terms and to use
them everywhere. You should probably use the wiki [TODO].

== External Links ==
\*[\ http://developer.apple.com/library/mac/documentation/UserExperience/Conceptual/APStyleGuide/APSG_2009.pdf
Apple Style Guide] - Quite useful guide on strings (not limited to Mac
OS X)

[[Category:Coding]]
