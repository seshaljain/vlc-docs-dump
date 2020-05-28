{\| class="bordered wikitable template-module" Module: {{{name}}} Type
\| {{#switch:{{{type}}} Video sub-filter = Video sub-filter Access =
[[Category:Accesses]] Access filter = [[Category:Access filters]] Audio
decoder = [[Category:Audio decoders]] Audio output = [[Category:Audio
output]] Packetizer = [[Category:Packetisers]] Services discovery =
[[Category:Services discovery]] Video filter = [[Category:Video
filters]] Video output filter = [[Category:Video output filters]] Video
subfilter Visualization #default = [[Category:Modules]] }} First VLC
version \| {{{first_version-! scope="row" \| Last VLC version \|
{{{last_version}}} noerror}} 0noreplace}} }} Operating system(s) \|
{{{os-! scope="row" \| Description \| {{{description}}} Shortcut(s) \|
{{#switch:{{{sc}}}{{{sc3}}}{{{sc5}}}{{{sc7}}}{{{sc9}}}{{{sc11none =
(none) {{{sc}}}{{{sc2}}} = <code>{{{sc}}}</code>, <code>{{{sc2}}}</code>
{{{sc}}}{{{sc2}}}{{{sc3}}}{{{sc4}}} = <code>{{{sc}}}</code>,
<code>{{{sc2}}}</code>, <code>{{{sc3}}}</code>, <code>{{{sc4}}}</code>
{{{sc}}}{{{sc2}}}{{{sc3}}}{{{sc4}}}{{{sc5}}}{{{sc6}}} =
<code>{{{sc}}}</code>, <code>{{{sc2}}}</code>, <code>{{{sc3}}}</code>,
<code>{{{sc4}}}</code>, <code>{{{sc5}}}</code>, <code>{{{sc6}}}</code>
{{{sc}}}{{{sc2}}}{{{sc3}}}{{{sc4}}}{{{sc5}}}{{{sc6}}}{{{sc7}}}{{{sc8}}}
= <code>{{{sc}}}</code>, <code>{{{sc2}}}</code>, <code>{{{sc3}}}</code>,
<code>{{{sc4}}}</code>, <code>{{{sc5}}}</code>, <code>{{{sc6}}}</code>,
<code>{{{sc7}}}</code>, <code>{{{sc8}}}</code>
{{{sc}}}{{{sc2}}}{{{sc3}}}{{{sc4}}}{{{sc5}}}{{{sc6}}}{{{sc7}}}{{{sc8}}}{{{sc9}}}{{{sc10}}}
= <code>{{{sc}}}</code>, <code>{{{sc2}}}</code>, <code>{{{sc3}}}</code>,
<code>{{{sc4}}}</code>, <code>{{{sc5}}}</code>, <code>{{{sc6}}}</code>,
<code>{{{sc7}}}</code>, <code>{{{sc8}}}</code>, <code>{{{sc9}}}</code>,
<code>{{{sc10}}}</code> #default = - }} \|}<noinclude> Template for
Documentation:Modules/\* pages. {{Clear}}

==Usage== <pre> {{Module first_version = Version of VLC in which plugin
first appeared os = Operating system of the plugin sc = Shortcut sc3 =
Shortcut 3 sc11 = Shortcut 11 }} </pre> Source code identifies shortcuts
with <code>add_shortcut( "foo", "bar" )</code> in the module descriptor.
Generally omit non-specific shortcuts. Pass the first shortcut to
<code>'''<nowiki>sc2=</nowiki>'''</code>, etc.<br /> If
<code>'''<nowiki>*]]<!-- To modify sortkey --> [[Category:Templates]]
</noinclude>
