{{See alsoDocumentation:Modules/http intf}} {{Moduletype=Control
interface|description=Control VLC via a telnet connection}}

The telnet module [[Control VLC instancetelnet]] protocol. The original
module was provided until 1.1.0, when it was re-written in
[[wikipedia:Lua (programming language)|Lua]]. The old module was renamed
to oldtelnet and removed in 2.0.0.

Telnet should not be used for sensitive applications.

To find module information on the command-line for VLC 2.0.0 and above,
use <code>vlc -p lua --advanced --help-verbose</code> and look for the
''Lua Telnet'' section.

Options as of 3.0.6 are listed below: {{Option value=string
name=telnet-port default=4212 name=telnet-password description=A single
password restricts access to this interface }} {{Option value=string
\|description=? }}

{{Documentation footer}}
