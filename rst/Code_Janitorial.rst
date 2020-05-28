{{See also|Janitorial projects}} Here is some samples janitorial task
you can pick up:

=== General appearance ===

Keeping the source uniformly less than 78 characters wide so it and
patches both fit nicely on a 80 column screen is good general practice
but it doesn't always happen. Thus an opportunity to reformat clearly
overlong lines.

=== Function header === The function header commentary isn't uniformed
across files. We suggest you to try to tidy this.

   /**********************************************************************\***\*
   \| \* Get the Media descriptor associated with the instance \* \| <-
   function header
   commentary**\ \**********************************************************************\*\ */
   \| libvlc_media_descriptor_t*
   libvlc_media_instance_get_media_descriptor( libvlc_media_instance_t
   *p_mi, libvlc_exception_t*\ p_e ) { ... }

=== Janitorial commits ===

Please, please do not mix cosmetic (reformatting and so on) changes with
changes that alter code behaviour in the same commit. Put them in a
separate commit marked with <code>Cosmetic: (description here)</code>.
Make sure the changes compile before you commit anyway.

=== Doxygen ===

You can document some parts of VLC's code that aren't correctly
documented using Doxygen. Ask on IRC for help.

=== Warning fixes ===

Some warnings are easy to fix, don't hesitate to provide a fix.

[[Category:Coding]]
