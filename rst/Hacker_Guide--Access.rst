.. raw:: mediawiki

   {{Back to|Hacker Guide}}

Description
-----------

The modules of **'access**' capability are designed to be the first and last elements of a modules chain.

They take an `MRL <MRL>`__ in, and output a bitstream, that can be fed to a `Demuxer <Demuxer>`__.

Access input and `output <{{#rel2abs:../Access_Output}}>`__ handles most of the basic **I/O** for VLC. They are usually **protocols** implementations (http, ftp,...) or **devices** access (Webcams, Capture cards).

We will discuss about **'input access**' in this page.

Write an access module
----------------------

To write an access module, read first the `introduction to module writing <{{#rel2abs:../How_To_Write_a_Module}}>`__.

Then, you should specify your module of being of access type:

.. code:: c

    set_capability( "access", 60 )  
    set_category( CAT_INPUT )                                                                                                                                                                                  
    set_subcategory( SUBCAT_INPUT_ACCESS )

Type
~~~~

Your module can be of either a **'Block**' or a **'Read**' type, depending on your medium:

-  if the underlying protocol **returns data blocks of unknown or unpredictable size**, **Block** is a better type,
-  if you **can control the size of the data requested** to the underlying protocol, **Read** is a better type.

Functions to implement
----------------------

After implementing ``Open()`` and ``Close()`` functions, you will need to implement a few major features that will be implemented by your functions.

As you can see in `include/vlc_access.h <https://www.videolan.org/developers/vlc/doc/doxygen/html/vlc__access_8h_source.html>`__, you should define:

-  Seek, as in ``pf_seek``,
-  Control, as in ``pf_control``,
-  Read or Block, depending on your module `type <#Type>`__.

After implementing those functions, you should assign them to the corresponding ``pf_`` function.

Seek
~~~~

*Prototype*:

.. code:: c

    int         (*pf_seek) ( access_t *, uint64_t );

The seeking function will be called whenever a seek is requested.

The arguments are a *pointer* to the module structure, and the requested **position**.

.. raw:: mediawiki

   {{Note-nb|Seeking function can be <code>NULL</code>, if it isn't possible to seek in the protocol or device.}}

You shall set ``p_access->info.b_eof`` to ``false`` if seek worked.

| *Return:*
| If the seek has succeeded, it should return ``VLC_SUCCESS``, else it should return ``VLC_EGENERIC``.

Control
~~~~~~~

*Prototype*:

.. code:: c

    int         (*pf_control)( access_t *, int i_query, va_list args);

Control function is quite easy, the input core will query the module using this function with:

-  A pointer to the module structure.
-  An **i_query** parameter that can be of several type. We will cover afterward the most important on.
-  A list of arguments, that depends on the **i_query** type.

*Return*:

If the query has succeeded, it should return ``VLC_SUCCESS``. Else it should return ``VLC_EGENERIC`` (*fail*).

Control Query types
^^^^^^^^^^^^^^^^^^^

The first ones are request to know what the module supports. They are all of `boolean <boolean>`__ type and should always succeed.

.. code:: c

    ACCESS_CAN_SEEK,        
    ACCESS_CAN_FASTSEEK,    
    ACCESS_CAN_PAUSE,       
    ACCESS_CAN_CONTROL_PACE,

| 
| The following one is a request for the **PTS delay**. It must always succeed.

.. code:: c

    ACCESS_GET_PTS_DELAY,

| 
| The following ones are for **requesting** various **info** about the input, like Metadata, Titles and Chapters or device signal strength. All of them can fail.

.. code:: c

    ACCESS_GET_TITLE_INFO,  
    ACCESS_GET_META,        
    ACCESS_GET_CONTENT_TYPE,
    ACCESS_GET_SIGNAL,      

| 
| Depending to the answer of the ``CAN_`` requests, the core can **set** a few things, like pausing or changing **title** or **chapter**

.. code:: c

    ACCESS_SET_PAUSE_STATE,
    ACCESS_SET_TITLE,
    ACCESS_SET_SEEKPOINT,

You can find the list of arguments corresponding to query types in the comments of ``access_query_e`` definition in vlc_access.h

Read
~~~~

*Prototype*:

.. code:: c

    ssize_t     (*pf_read) ( access_t *, uint8_t *, size_t );

*Return*:

Return ``-1`` if no data yet, ``0`` if no more data, else actual data read on the medium.

Block
~~~~~

*Prototype*:

.. code:: c

    block_t    *(*pf_block)( access_t * );

*Return:*

Returns a block of data in its 'natural' size. It will return ``NULL`` if there is not yet data or end-of-file (eof) has been reached.

To differentiate between *no data* and *eof*, you shall set ``p_access->info.b_eof`` to ``true`` in case of eof.

.. raw:: mediawiki

   {{Hacker_Guide}}
