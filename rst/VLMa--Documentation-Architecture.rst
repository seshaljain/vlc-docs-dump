=Architecture=

==The model==

The 2 key objects of the model are the media and the programmation.
Basically, a media stands for something that can be streamed whereas the
programmation tells you how it should be streamed.

==The threads==

The daemon is made of two main threads: \* a thread which monitors the
state of the servers (up/down), \* a thread which monitors the state or
programmation (whether programs are really streamed or not) and asks for
orders to be given again whether there is something wrong.

Most events are triggered by these two threads, the other events being
triggered from user interaction.

==Orders==

When VLMa notices that some programs are not really streamed, orders are
computed and then sent to the servers. Computing orders means: \*
identify available adapters, \* identify medias that should be streamed,
\* put together medias into groups of medias that should be streamed by
the same server (for example, because of their frequency in case of a
[[DVB]] input), \* map every media group to an available adapter, \*
send orders to the servers.

==A programmation state==

A media can have 3 states: \* not programmed, \* programmed but not
streamed, \* programmed and streamed.

To check whether programs are ''really'' streamed or not, there are
stream watchers. Currently, there are two main implementations : the
<code>DirectMulticastStreamWatcher</code> which joins the multicast
group of the program (in case of an UDP multicast streaming strategy)
and tries to receive data. If not enough data is received, the stream is
known as not streamed. The other watcher, <code>HttpStreamWatcher</code>
connects on the VLC http interface and verifies that no 404 error is
encountered.

==See also==

-  [[VLMa/Documentation \| VLMa documentation index]]

[[Category:VLMa]]
