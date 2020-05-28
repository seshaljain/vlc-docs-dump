.. raw:: mediawiki

   {{Back to|Hacker Guide}}

VLC Object Management
---------------------

Introduction
~~~~~~~~~~~~

This paper will discuss VLC objects and the general `object oriented <wikipedia:Object-oriented_programming>`__ practices involved in developing and extending `libvlc <libvlc>`__.

Object Creation
~~~~~~~~~~~~~~~

In VLC everything is an object. Each object can have a parent and multiple children. The following functions are used for creating an object and attaching to parents and children. Note that this list may not be complete. For reference see the file `include/vlc_objects.h <https://www.videolan.org/developers/vlc/doc/doxygen/html/vlc__objects_8h.html>`__.

``vlc_object_create()``
   Create an object and set its refcount to 0
``vlc_object_destroy()``
   De-allocate an object iff its refcount = 0
``vlc_object_attach()``
   Bidirectionally link an object with its parent
``vlc_object_detach()``
   Remove all links between an object and its parent

Inheritance
~~~~~~~~~~~

Objects can have multiple levels of inheritance. Each object is represented by the type ```vlc_object_t`` <https://www.videolan.org/developers/vlc/doc/doxygen/html/structvlc__object__t.html>`__. Every object inherits from this type and can be cast to it. Inheritance is achieved in the C language by embedding a macro of common structure elements (``VLC_COMMON_MEMBERS``) inside each inherited object structure. For example, a libvlc instance of type ``libvlc_int_t`` inherits from ``vlc_object_t`` by embedding the ``VLC_COMMON_MEMBERS`` inside the ``libvlc_int_t`` structure as seen in example 1 below.

Example 1: libvlc_int_t : vlc_object_t

.. code:: c

   struct libvlc_int_t 
   {
       VLC_COMMON_MEMBERS

       /* Everything Else */
   }

Reference Counts
~~~~~~~~~~~~~~~~

In order to simplify garbage collection, every object has a reference count. When an object is created (``malloc()``'d) its reference count is set to 0. Anytime the object is acquired for use by a caller that caller must increase its reference count by 1. When the caller is done using the object it must decrease the object's reference count by 1. Luckily, most of this is handled by internal object management acquisition and removal functions. In order to destroy (``free()``) the object the reference count of the object must be 0. The following functions are used to manipulate object reference counts. Note that this list may not be complete. For reference see the file `include/vlc_objects.h <https://www.videolan.org/developers/vlc/doc/doxygen/html/vlc__objects_8h.html>`__.

``vlc_object_hold()``
   Increase the refcount of an object by 1. This function should only be used in object management functions! Careless usage will lead to memory leaks!
``vlc_object_release()``
   Decrease the refcount of an object by 1. This function should only be used in object management functions! Careless usage can lead to early object destruction, while the object may still be in use!

.. raw:: mediawiki

   {{Hacker_Guide}}
