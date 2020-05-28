<!---->{{top box ??}}} n}}} \| y \| '''encode''' and }} '''decode'''
this [[container]]. {{{info}}}<!-- -->page}}}<!-- -->\| page =
'''{{docmod{{{id}}}}}}}}'''<!-- -->\| none = {{{mod #default =
[{{{module link}}} {{{mod}}}<!-- -->}}}<!-- -->The [[module]] name to
use at the [[command line]] is unknown.<!-- -->}}<!---->}}<includeonly>
[[Category:Container]] {{ #ifeq: {{{encoder y \|
[[Category:Container_Encoder]] }} [[Category:Container_Decoder]]
</includeonly><noinclude>

==Usage==
   <nowiki>{{muxencoder= module link= { page, none, <value> } altid2=
   \|mod= }}</nowiki>

id is supposed to be what you'd put in the command line, like
   --sout='#std{mux='''id''',url=....}'

If there is more than one shortcut, use altid for the others.

Parameter <code>'''id=movvalue}} - URL to the Git file

It will add it to [[:Category:Container]] (all containers) and
[[:Category:Container_Decoder]] (containers which can be decoded...
which is all containers <span title="wink">;-)</span> If you think
that's stupid, change it!

If encoder is "y" then it also adds it to
[[:Category:Container_Encoder]] and changes the text a bit.

Info is for extra text in the box.

==Examples== Example, [[avi]] <nowiki>{{muxencoder=y}}</nowiki> becomes
{{muxencoder=y}}

Example, [[asf]]
   <nowiki>{{muxencoder=y|info=This works with mp2v, blah
   blah}}</nowiki>

becomes {{muxencoder=y|info=This works with mp2v, blah blah}}

Example, [[mp4]]
   <nowiki>{{muxencoder=yaltid2=3gp}}</nowiki>

becomes {{muxencoder=yaltid2=3gp}}

==See also== \* {{tlCodec video}} \* {{tlProtocol}}

[[Category:Templates]] </noinclude>
