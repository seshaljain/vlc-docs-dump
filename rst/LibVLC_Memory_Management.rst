{{Lowercase}} == Reference Counting ==

[[libVLC]] uses a certain number of objects. Each one maintains a
references count, which is used to know when the object must be
released. The three related functions are:

-  `libvlc_object_name <>`__'''new'''() ''Create an object with a
   refcount equal to 1.''
-  `libvlc_object_name <>`__'''retain'''() ''Increment the object
   refcount by 1.''
-  `libvlc_object_name <>`__'''release'''() ''Decrement the refcount by
   1, and release the object if the new refcount is less than zero.''

=== Example === <syntaxhighlight lang="c"> libvlc_media_list_t \*p_ml =
libvlc_media_list_new(libvlc_inst)

   /\* Free the memory used by media_list release \*/
   libvlc_media_list_release(p_ml);

</syntaxhighlight>

=== Objects that don't follow this rule ===

-  libvlc_event_manager_t: Those are supposed to be accessed only during
   the life of their parent `libvlc <>`__\ \* object.

== Getters and Setters ==

Usually object properties are set through getters and setters.

\* Usually getters are in the form:
`libvlc <>`__''object_name''_''object''

\* Setters are: `libvlc <>`__''object_name''_''set_object''

\* Variations: \*\* Setter: libvlc_media_list_add_media_descriptor \*\*
Getter: libvlc_media_list_item_at_index

For setters and getters the memory management rules are: \* Getters
internally '''retain''' the object before returning it, so is means you
must '''release''' the object after use. \* Setters internally
'''retain''' the object, so basically you never need to keep the object
around. (This also applies to strings where retain is '''strdup''' and
release is '''free''')

Notable exceptions to those rules are: \*
`libvlc <>`__''object_name''_'''event_manager''': This getter never
retains the object prior returning it. That means you '''mustn't
release''' it.

[[Category:libVLC]]
