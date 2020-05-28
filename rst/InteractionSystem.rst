{{Historical}} == Goal ==

Reference : https://trac.videolan.org/vlc/ticket/27

The goal is to implement a system to:

-  Alert the user of critical errors (cannot play file). Should be
   blocking.

\* Ask the user a question \*\* Are you sure? \*\* Try to Fix index of
avi? \*\* Overwrite File ? \* Inform the user, without disturbing him.
(Buffering stream). This might require a displaytime or something.
Because how do we know how long this information should be displayed?
Also think of buffering 0-100% \* present a user/passwd dialog when we
get an authentication failure on a stream.

== Roadmap ==

Scheduled for implementation in 0.8.5

Some work will have to be done in all interfaces

== Objects architecture ==

\* Interaction object \*\* void \* pointer for interface specific stuff

\* Widget object \*\* for input, associated with a vlc_value_t

\* Interaction manager \*\* Maintains a list of currently active
interaction displays \*\* When a new interaction is requested, forward
the request to the interface (ASYNCHRONOUS !) \*\* Asks the interface to
show/modify/remove a display \*\* Active polling ?

\* Signalling the interface : \*\* function pointer **\* easier to know
if interface does not support** variable **\* cleaner ?** "control"
function

\* Requester \*\* Builds the interaction object \*\* Add it to the
interaction manager request queue. **\* Queue or single with lock
?**\ \* Analyze deadlock possibility

[[Category:Dev Discussions]]
