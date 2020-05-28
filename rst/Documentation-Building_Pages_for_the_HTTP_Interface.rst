.. raw:: mediawiki

   {{Historical}}

.. raw:: mediawiki

   {{RightMenu|Documentation TOC}}

Introduction
------------

This appendix describes the language used for writing dynamic web pages for the `HTTP interface <HTTP_interface>`__.

Pages must be placed in the ``share/http`` folder in either VLC's folder (Windows, Mac) or ``/usr/share/vlc/share/http`` or ``/usr/local/share/vlc/share/http`` (or wherever vlc's shared files are installed).

Some files are handled a bit specially:

-  Files beginning with '.' are not exported.
-  A '.access' file will be opened and the http interface will expect to find at the first line a login/password (written as login:password). This login/password will be used to protect all files in this directory. Be careful that only files in this directory will be protected. (sub-directories won't be protected.)
-  A '.hosts' file will be opened and the http interface will expect to find a list of network/mask pairs separated by new line, for instance 192.168.0.0/255.255.255.0. If this file is present, then the default behaviour is to deny access from hosts which don't match any of the network/mask pairs to all the files of the directory. If the file is not present, then any host has access to the files of the directory. Be careful that only files in this directory will be protected. (sub-directories won't be protected.)
-  The file

   .. raw:: html

      <dir>

   /index.html will be exported as

   .. raw:: html

      <dir>

   and

   .. raw:: html

      <dir>

   / and not as index.html.

The MIME type is set by looking at the file extension and cannot be specified nor modified for a specific file. Unknown extensions will have "application/octet-stream" as MIME type.

You should avoid exporting big files. Each file is indeed first loaded into the memory before being sent to the client, so please be careful.

VLC macros
----------

Each time a .html/.htm page is requested, it is parsed by VLC before being sent. The parser searches for the VLC macros, and executes or substitutes them. Moreover, URL arguments received by the GET method can be interpreted.

A VLC macro looks like:

.. code:: xml

    <vlc id="macro-name" param1="macro-parameters1" param2="macro-parameters2" />

"id" is the only mandatory field, param1 and param2 may or may not be present and depend on the value of "id".

You should take care that you **have to** respect this syntax, VLC won't like invalid syntax. (It could easily leads to crashes).

Examples:

Correct:

.. code:: xml

    <vlc id="value" param1="version" />

Incorrect:

.. code:: xml

    <vlc id="value" param1="version" > <!--(missing tag ending)-->
    <vlc id=value param1="version" /> <!--(missing "" )-->

Valid macros are:

-  **control** (1 optional parameter)
-  **include** (1 parameter)
-  **get** (2 parameters)
-  **set** (2 parameters)
-  **rpn** (1 parameter)
-  **if** (1 optional parameter)
-  **else** (no parameter)
-  **end** (no parameter)
-  **value** (1 optional parameter)
-  **foreach** (2 parameters)

For powerful macros, you may use these tools:

-  RPN Evaluator (see part 2)
-  Stacks: The stack is a place where you can push numbers and strings, and then pop them backs. It's used with the little RPN evaluator.
-  Local variables: You can dynamically create new variables and changes their values. Some local variables are predefined:

   -  **url_value**: parameter of the URL
   -  **url_param**: 1 if url_value isn't empty else 0
   -  **version**: the VLC version
   -  **copyright**: the VLC copyright
   -  **vlc_compile_time, vlc_compile_by, vlc_compile_host, vlc_compile_domain, vlc_compiler, vlc_changeset**: information on the VLC build
   -  **stream_position, stream_time, stream_length, stream_state**: information on the currently playing stream
   -  **volume**: current volume setting

Remark: The stacks, and local variables context is reset before the page is executed.

The RPN evaluator
-----------------

RPN means Reverse Polish Notation.

RPN Introduction
~~~~~~~~~~~~~~~~

RPN may look strange but it's a fast and easy way to write expressions. It also avoids the use of ``(`` and ``)``.

Instead of writing ``( 1 + 2 ) * 5`` you just use ``1 2 + 5 *``.

The idea behind it is: if we have a number or a string (using ''), push it on the stack. If it is an operator (like ``+``), pop the arguments from the stack, execute the operators and then push the result onto the stack. The result of the RPN sequence is the value on the top of the stack. A step by step explanation of the sequence **1 2 + 5 \*** is shown below, to illustrate this process:

============== ==== ===========================================================================================
Stack Contents Word Action taken on the stack
============== ==== ===========================================================================================
empty          1    1 is pushed on the stack
1              2    2 is pushed onto the stack, 'above' 1
1 \| 2         +    The plus operator results in removal of 1 and 2 from the stack, then write 3 onto the stack
3              5    5 is pushed on the stack
3 \| 5         \*   The multiplication operator removes 3 and 5 and writes 15 onto the stack.
15                  Final result.
============== ==== ===========================================================================================

Operators
~~~~~~~~~

Notation: ST(1) means the first stack element, ST(2) the second one … and op is the operator.

You have access to :

-  Standard arithmetics operators: **+, -, \*, /, %** these ones push the result of ST(1) op ST(2) onto the stack
-  Binary operators: **!** (push !ST(1)); **^, &, \|**: push the result ST(1) op ST(2)
-  test: **=, <, <=, >, >=**: execute ST(1) op ST(2) and push -1 if true else 0
-  string functions:

   -  **strcat**: pushes the result of 'ST(1)ST(2)
   -  **strcmp**: compares ST(1) and ST(2) (0 if equal)
   -  **strncmp**: compares the first ST(1) characters of ST(2) and ST(3) (0 if equal)
   -  **strsub**: extracts characters ST(2) to ST(1) of string ST(3)
   -  **strlen**: pushes the length of ST(1)
   -  **str_replace**: replaces string ST(2) with ST(1) in ST(3)
   -  **url_encode**: encodes non-alphanumeric characters of ST(1) as %XX so that they can be safely passed as GET or POST variables
   -  **url_extract**: performs the reverse operation of url_encode
   -  **addslashes**: protects single quotes (') and double quotes (") of ST(1) with backslashes (\) so that they can be safely passed to a VLC playlist function
   -  **stripslashes**: performs the reverse operation of addslashes
   -  **htmlspecialchars**: encodes &, ', ", <, and > of ST(1) as their &stuff; HTML counterpart, so that they don't interact with HTML tags
   -  **realpath**: parses ST(1) as a filename path, and pushes an absolute path to that file, removing ~ and ../

-  stack manipulation:

   -  **dup**: pops ST(1) and pushes the same string twice
   -  **drop**: pops ST(1) and drops it
   -  **swap**: exchanges ST(1) and ST(2)
   -  **flush**: empties the stack

-  variables manipulation:

   -  **store**: stores ST(2) in a local variable named ST(1)
   -  **value**: pushes the value of the local variable named ST(1)

-  player control:

   -  **vlc_play**: plays the playlist item whose ID is ST(1), and pushes the return value of the play function (0 in case of success); see playlist functions below
   -  **vlc_stop**: stops the playlist
   -  **vlc_pause**: pauses the playlist
   -  **vlc_next**: plays the next playlist item
   -  **vlc_previous**: plays the previous playlist item
   -  **vlc_seek**: seeks the current input to a location defined in ST(1), for instance+3m (minutes), -20s, 45%, 1:12, 1h12m25s
   -  **vlc_var_type**: pushes the type of the variable ST(2) of object ST(1); the type is one of these strings **VLC_VAR_BOOL, VLC_VAR_INTEGER, VLC_VAR_HOTKEY, VLC_VAR_STRING, VLC_VAR_MODULE, VLC_VAR_FILE, VLC_VAR_DIRECTORY, VLC_VAR_VARIABLE, VLC_VAR_FLOAT, UNDEFINED** (no such variable) or **INVALID** (no input stream); the object is one of **VLC_OBJECT_ROOT, VLC_OBJECT_VLC, VLC_OBJECT_INTF, VLC_OBJECT_PLAYLIST, VLC_OBJECT_INPUT, VLC_OBJECT_VOUT, VLC_OBJECT_AOUT** or **VLC_OBJECT_SOUT**
   -  **vlc_var_set**: sets variable ST(2) of object ST(1) to ST(3)
   -  **vlc_var_get**: pushes the value of the variable ST(2) of object ST(1)
   -  **vlc_object_exists**: checks if object ST(1) exists
   -  **vlc_config_type**: pushes the type of the configuration variable ST(1); see **vlc_var_type** for a list of types
   -  **vlc_config_set**: sets configuration variable ST(1) to ST(2)
   -  **vlc_config_get**: pushes the value of the configuration variable ST(1)
   -  **vlc_config_save**: saves the modification made to the configuration variables of module ST(1) to the configuration file (ST(1) may be empty, in which case the whole configuration is saved) and pushes the return status (0 in case of success)
   -  **vlc_config_reset**: resets the configuration file to the default value (use with caution)
   -  **vlc_volume_set**: sets the volume value to ST(1) which can be a raw value between 0 and 1024, or a relative one between 0% and 400%, where 1% is equal to the maximum volume value divided by 400 (thus, the maximum volume value is equal to 400%, that is 1024). If ST(1) begins with a '+' (or '-') operator, the volume is increased (or decreased) by the raw value which follows this operator
   -  **vlc_get_meta**: pushes the value of the meta information named by ST(1) from the stream being played. Available meta names are: "Title" (or "TITLE"), "Author", "Artist" (or "ARTIST"), "Genre" (or "GENRE"), "Copyright", "Album/movie/show title" (or "ALBUM"), "Track number/position in set", "Description", "Rating", "Date", "Setting", "URL", "Language", "Now Playing", "Publisher"
   -  **vlm_command** or **vlm_cmd**: sends the command that is on the stack to the VLM (VideoLan Manager). Since the command can contain more than one component on the stack, it must be ended by an ';' or an empty string pushed on the stack (e.g.: param1="';' 'command' 'my' 'this is' vlm_command"). Once the VLM has executed the command, the return value is assigned to the local variable **vlm_value** and the error string (if available) is assigned to **vlm_error**
   -  **snapshot**: takes a snapshot

-  playlist functions:

   -  **playlist_add**: adds MRL ST(1) to the playlist, with name ST(2) and returns the playlist ID associated to this item; special characters must be escaped with addslashes first; it is very convenient to call 'toto.mpg' playlist_add vlc_play
   -  **playlist_empty**: clears the playlist of all items
   -  **playlist_move**: moves playlist item at position ST(2) to position ST(1)
   -  **playlist_delete**: deletes playlist item ID ST(1)
   -  **playlist_sort**: sorts the playlist using the mode ST(2) and order ST(1). Available order values are 0 (normal order) and 1 (reverse order). Available mode values are 0 (sort by ID), 1 (sort by title), 2 (sort by title, nodes first), 3 (sort by author), 4 (sort by genre), 5 (sort randomly), 6 (sort by duration), 7 (numerically sort by title) and 8 (sort by album)
   -  **services_discovery_add**: adds the service discovery ST(1) to the playlist
   -  **services_discovery_remove**: removes the service discovery ST(1) from the playlist
   -  **services_discovery_is_loaded**: checks if the service discovery ST(1) is loaded in the playlist, and pushes the answer on the stack

The macros
----------

The *control* macro
~~~~~~~~~~~~~~~~~~~

**The use of the control macro is now deprecated in favour of the RPN functions above. The documentation is provided here for the maintenance of HTML pages still using this old API. The main problem with this API is that there is no way to retrieve the playlist ID of the last added item.**

When asking for a page, you can give arguments to it through the url. (e.g. using a ). Ex: *http://host:port/page.html?var=value&var2=value2*\ … The "control" macro tells a page to parse these arguments and to execute the ones that are allowed. param1 of this macro says which commands are allowed. If empty, all commands will be permitted.

Some commands require an argument that must be passed in the URL too.

-  URL commands

   -  Name, Argument, Description
   -  **play**, item (integer), Play the specified playlist item
   -  **stop**, ,Stop
   -  **pause**, Pause
   -  **next**, , Go to next playlist item
   -  **previous**, , Go to previous playlist item
   -  **add**, mrl (string), Add a `MRL <MRL>`__ to the playlist
   -  **delete**, item (integer), Delete the specified playlist item or list of playlist items
   -  **empty**, , Empty the playlist
   -  **close**, id (hexa), Close a specific connection
   -  **shutdown**, , Quit VLC

For example, you can restrict execution of the **shutdown** command to protected page (through a *.access* file), using the control macro in all unprotected pages.

The *include* macro
~~~~~~~~~~~~~~~~~~~

This macro is replaced by the contents of the file param1. If the file contains vlc macros, they are correctly parsed and replaced.

The *get* macro
~~~~~~~~~~~~~~~

This macro will be replaced by the value of the configuration variable which name is stored in param1 and which type is given by param2.

param1 must be the name of an existing configuration variable. param2 must be the right type of the variable. It can be one of *int*, *float*, or *string*.

Example:

.. code:: xml

    <vlc id="get" param1="sout" param2="string" /> will be replaced in the output page by the value of sout.

The *set* macro
~~~~~~~~~~~~~~~

This macro allows to set the value of a configuration variable. The name is given by param1 and the type by param2 (like for get). The value is retrieved from the url using the name given in param1.

For example, if player.html contains

.. code:: xml

    <vlc id="set" param1="sout" param2="string" />

and if you browse at *http://host:ip/player.html?sout=sout_value*, the sout variable will be set to "sout_value". If the URL doesn't contain sout, nothing will be done.

The *rpn* macro
~~~~~~~~~~~~~~~

This macro allows you to interpret RPN commands. (See II).

The *if,else,end* macro
~~~~~~~~~~~~~~~~~~~~~~~

This macro allows you to control the parsing of the HTML page.

If param1 isn't empty, it is first executed with the RPN evaluator. If the first element from the stack is not 0, the test value is true, else false..

.. code:: xml

    <vlc id="if" param1="1 2 =" />
        <!-- Never reached -->
    <vlc id="else" />
       <p> Test succeed: 1 isn't equal to 2 </p>
    <vlc id="end" />

You can also just use "if" and "end".

The *value* macro
~~~~~~~~~~~~~~~~~

If param1 isn't empty, it is first executed with the RPN evaluator. The macro is replaced with the value of the first element of the stack.

Note: If the element is the name of a local variable, its value will be displayed instead of its name.

The *foreach,end* macro
~~~~~~~~~~~~~~~~~~~~~~~

param1 is the name of the variable that will be used for the loop. param2 is the name of the set to be built:

-  integer: take the first element from the stack to construct a set of integer. The stack element should be a string like: ``first:last[:step][,first2:last2[:step2][,…]`` (Ex:1:5:2,6:8:1 will be expanded into 1,3,5,6,7,8)
-  directory: take the first element of the stack as the base directory and construct a set of filename and directly in it. Each element has the following fields:

   -  basename: file/directory name
   -  name: complete file/directory name (including path)
   -  ext: file extension in lowercase
   -  type: "directory" or "file" or "unknown"
   -  size: size of the file
   -  date

-  playlist: set based on the playlist with fields: current is 1 if item is currently selected, 0 else. index is the index value, that can be used by the play or delete control command. name is the

name of the item.

-  "information": Create information for the current playing stream. name is the name of the category, value is its value, info is a new set that can be parsed with a new foreach (subfields of info are name and value).
-  input variables such as "program", "title", "chapter", "audio-es", "video-es" and "spu-es": Create lists for the current playing stream. Every list has the following fields:

   -  name: item name (language for elementary streams, tracks, etc.) to display in places where a human-readable format is preferred
   -  id: item ID to pass to the RPN function vlc_var_set, and returned by vlc_var_get
   -  selected: 1 if the item is selected, 0 otherwise

-  the name of a foreach variable if it's a set of set of value.

.. code:: xml

    <vlc id="foreach" param1="cat" param2="informations" />
        <vlc id="value" param1="cat.name" />
        <ul>
            <vlc id="foreach" param1="info" param2="cat.info" />
               <li>
               <vlc id="value" param1="info.name" /> :
                       <vlc id="value" param1="info.value" />
               </li>
           <vlc id="end" />
       </ul>
    <vlc id="end" />

For more details, have a look at the directory of the VLC source tree…

.. raw:: mediawiki

   {{Documentation}}
