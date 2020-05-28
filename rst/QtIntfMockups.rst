{{Back toPherthyl]] 23:44, 23 November 2006 (CET)

==Open Network==

The open network stream is a mess in the old interface. Most of the
protocols require basically the same info, and yet we have 4 radio
buttons to select from protocols, then 2 URL fields, 2 Port selectors, 1
address field (URL/Address, why the distinction).

I propose to change it to something simpler:
[http://www.mushroomstamp.ca/vlc/qtintfmockup1.png Open Network]

Basically, you select the protocol from the dropdown, then you type in
your address. If you just paste a url into the address field, the
dropdown automatically detects the correct protocol from the url (if it
can) and sets the correct value. If you have a url, and then change the
protocol from the dropdown, it will modify the url appropriately. If you
select a protocol where the port or the options are meaningless, they
will be disabled (either that or they won't be shown unless they are
relevant.

:Looks better indeed :) The port number thing is kind of problematic
though. If you get stuff like an mms url on the web it'll use something
like "mms://host.example.com:8080/myteststream". If the user specified
port is left null, like in your screen shot, i guess that we can
disregard it. But what happens if the user specifies the port number ?
(maybe that port input should only be available for udp/rtp (and their
multicast conterparts)) [[User:Dionoea|Dionoea]] 11:42, 24 November 2006
(CET)

::Good point. I think we have 2 options here: :: 1. When a user
types/pastes an address like "mms://host.example.com:8080/myteststream"
with a port number, we detect this and set the port correctly. If they
change the port number in the combobox, we update the textual URL to
match. While this probably wouldn't be a problem to implement, it's kind
of redundant to show the port in two places. :: 2. Only show/enable the
port selector for protocols that cannot specify the port in the address,
or where it is more common to get an address without a port (UDP/RDP).
This is more consistent with the previous way of doing things, probably
preferrable. --[[User:Pherthyl|Pherthyl]] 21:05, 24 November 2006 (CET)

::: I'd do number 2. [[User:Dionoea|Dionoea]] 15:34, 25 November 2006
(CET)

== Mock-up Submissions == *If it is not too late, I have created some
mock-ups and ideas that can be found on [[QtIntfMockups-DericksIdea|this
page]]. --[[User:Zephyrxero|Zephyrxero]] 06:02, 2 January 2007
(CET)*\ Found an orphaned page of an image set [[QtImageset|here]]
that's created on April 2008. --19:14, 23 November 2010 (UTC)

[[Category:Dev Discussions]] [[Category:Qt]]
