NOTA BENE
---------

The following conventions are the 'classical' VLC code conventions. Those are **not enforced anymore**.

The important is to keep consistency of codestyle when you modify a file.

If you write a new file, select your style. Common used styles are **VLC Style** and **K&R**.

Code conventions
----------------

Here you find conventions about how the developers write their code.

Function naming
~~~~~~~~~~~~~~~

All functions are named accordingly: *module name* (in lower case) + \_ + *function name* (in mixed case, without underscores). For instance: ``intf_FooFunction``. Static functions don't need the module name.

Variable naming
~~~~~~~~~~~~~~~

We use Hungarian notation. That is, we have the following prefixes:

-  ``i_`` for integers (sometimes ``l_`` for long integers)
-  ``b_`` for booleans
-  ``d_`` for doubles
-  ``f_`` for floats
-  Generally, we add a ``p`` when the variable is a pointer to a type

   -  ``pf_`` for function pointers
   -  ``psz_`` for a pointer to a string terminated by a zero (C-string)

If a variable has no basic type (for instance a complex structure), don't put any prefix (except ``p_`` if it's a pointer). After one prefix, put an explicit variable name in lower case. If several words are required, join them with an underscore (no mixed case).

Examples:

-  ``data_packet_t * p_buffer``
-  ``char psz_msg_date[42]``
-  ``int pi_es_refcount[MAX_ES];``
-  ``void (* pf_next_data_packet)( int * )``

A few words about white space
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Indentation
^^^^^^^^^^^

**Never** use tabs in the source (nevertheless you're entitled to use them in the Makefile :-).

Use ``set expandtab`` under vim or the equivalent under emacs.

Indents are 4 spaces long.

Spaces
^^^^^^

Put spaces before and after operators, and inside brackets. For instance:

``for( i = 0; i < 12; i++, j += 42 ); ``

Braces
^^^^^^

Leave braces alone on their lines (GNU style\ `1 <http://www.gnu.org/prep/standards/standards.html>`__). For instance:

| ``if( i_es == 42 )``
| ``{``
| ``   p_buffer[0] = 0x12;``
| ``}``

Comments
~~~~~~~~

ANSI C-style comments /\* ... \*/ are more commonly used for historical reasons, though C++/C99 comments are tolerated, but please don't mix both in the same file.

Qt interface added conventions
------------------------------

   **See\ **\ `HACKING <http://git.videolan.org/?p=vlc.git;a=blob;f=modules/gui/qt/HACKING>`__

Objective-C conventions
-----------------------

For new Objective-C code, do **not** use Hungarian notation, unless you are editing a file that still uses it. Use cameCase for properties and methods, as usual.

When adding new classes, make sure to state in the leading comment block what the use-case for that class is.

Try to document your methods with doxygen comments, where it makes sense, see `VLCRendererDiscovery.h <http://git.videolan.org/?p=vlc.git;a=blob;f=modules/gui/macosx/VLCRendererDiscovery.h;h=57d7fed0c1f91aa2450f99b5f06a884dad37ee50;hb=HEAD>`__ for an example.

Group your class, if it makes sense using pragma marks:

.. code:: objc

   #pragma mark -
   #pragma mark Helper methods

Partial availability
~~~~~~~~~~~~~~~~~~~~

If you call a method that is only available since a specific macOS version, make sure that you implement a proper fallback (if necessary). Add a preprocessor ``#ifdef`` to preven compilation with SDKs that do not define the method. Add a runtime check to make sure the method is not called in macOS versions that do not have it. Check out the example below:

.. code:: objc

   #ifdef MAC_OS_X_VERSION_10_10
   #pragma clang diagnostic push
   #pragma clang diagnostic ignored "-Wpartial-availability"
    
   if (OSX_YOSEMITE_OR_HIGHER) {
       /* Calling a method that is only available on macOS 10.10 or later */
   } else {
       /* Call the replacement for specific method, if necessary */
   }

   #pragma clang diagnostic pop
   #else

   /* Built with SDK that does not declare the necessary headers, always calling the replacement */

   #endif

(Avoid this, only do it if it is really necessary)

`Category:Coding <Category:Coding>`__
