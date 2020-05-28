{{Back to|Hacker Guide}} == VLC Object Management ==

=== Introduction ===

This paper will discuss VLC objects and the general
[[wikipedia:Object-oriented programming|object oriented]] practices
involved in developing and extending [[libvlc]].

=== Object Creation ===

In VLC everything is an object. Each object can have a parent and
multiple children. The following functions are used for creating an
object and attaching to parents and children. Note that this list may
not be complete. For reference see the file
[https://www.videolan.org/developers/vlc/doc/doxygen/html/vlc__objects_8h.html
include/vlc_objects.h].

; <code>vlc_object_create()</code> : Create an object and set its
refcount to 0 ; <code>vlc_object_destroy()</code> : De-allocate an
object iff its refcount = 0 ; <code>vlc_object_attach()</code> :
Bidirectionally link an object with its parent ;
<code>vlc_object_detach()</code> : Remove all links between an object
and its parent

=== Inheritance ===

Objects can have multiple levels of inheritance. Each object is
represented by the type
<code>[https://www.videolan.org/developers/vlc/doc/doxygen/html/structvlc__object__t.html
vlc_object_t]</code>. Every object inherits from this type and can be
cast to it. Inheritance is achieved in the C language by embedding a
macro of common structure elements (<code>VLC_COMMON_MEMBERS</code>)
inside each inherited object structure. For example, a libvlc instance
of type <code>libvlc_int_t</code> inherits from
<code>vlc_object_t</code> by embedding the
<code>VLC_COMMON_MEMBERS</code> inside the <code>libvlc_int_t</code>
structure as seen in example 1 below.

<u>Example 1:</u> libvlc_int_t : vlc_object_t <syntaxhighlight lang="c">
struct libvlc_int_t { VLC_COMMON_MEMBERS

   /\* Everything Else \*/

} </syntaxhighlight>

=== Reference Counts ===

In order to simplify garbage collection, every object has a reference
count. When an object is created (<code>malloc()</code>'d) its reference
count is set to 0. Anytime the object is acquired for use by a caller
that caller must increase its reference count by 1. When the caller is
done using the object it must decrease the object's reference count by
1. Luckily, most of this is handled by internal object management
acquisition and removal functions. In order to destroy
(<code>free()</code>) the object the reference count of the object must
be 0. The following functions are used to manipulate object reference
counts. Note that this list may not be complete. For reference see the
file
[https://www.videolan.org/developers/vlc/doc/doxygen/html/vlc__objects_8h.html
include/vlc_objects.h].

; <code>vlc_object_hold()</code> : Increase the refcount of an object by
1. This function should only be used in object management functions!
Careless usage will lead to memory leaks! ;
<code>vlc_object_release()</code> : Decrease the refcount of an object
by 1. This function should only be used in object management functions!
Careless usage can lead to early object destruction, while the object
may still be in use!

{{Hacker_Guide}}
