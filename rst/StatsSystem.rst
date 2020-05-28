{{Historical}} = Requirements =

== Goal ==

Central system for storing statistics and timings

== Stored data ==

What we might want to collect:

-  per-stream/global decoded, dropped frames
-  per-stream/global packets read/errors
-  per-stream/global packets/bytes sent/errors (if sout)
-  stats about httpd/vod, per request

Each thing could be stored as average, max, counter, ...

== Data access ==

-  Access stats from the GUI (simple)
-  Dump HTTP server access data
-  Dump some raw access data to output

= Design =

== Data storage ==

=== Stats object ===

Stored as a singleton in p_libvlc

=== Counters ===

<pre> counter_sample_t { value date }

counter_elem_t { name type pp_samples / i_samples } </pre>

-  Name contains the originating object id, like "267.frames_displayed"
   .How to separate by http request ? "httpd_object_id.request_id.XXX" ?
-  Type is one of MAX, LAST, COUNTER, DERIVATIVE, ...

=== Timing ===

<pre> timing_elem_t { name

   last_time,

   total_time, total_samples,

   running, start_time

} </pre>

== Reporting ==

\* In GUI: \*\* Integrated in streams and media information for relevant
items (make it available for VLM streams too) \*\* Where to put global
data ?

\* Data log: \*\* Make global options to enable and driver logger module
\*\* Add some logging facility to httpd \*\* RRD output (muwahahahaha)

[[Category:Dev Discussions]]
