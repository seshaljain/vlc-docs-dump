Requirements
------------

-  A JDK version 5.0 or higher
-  VLMa binary package

How to
------

First extract VLMa distribution archive to the folder of your choice, you should see the following folders:

-  bin/ Command line wrappers to manage VLMa
-  conf/ Configuration
-  data/ Data
-  lib/ Dependencies
-  logs/ Log directory
-  webapps/ Webapps to deploy
-  work/ Folder needed by the servlet container

UNIX specific
~~~~~~~~~~~~~

Ensure that the JAVA_HOME environment variable has been set. Run the following command:

``echo $JAVA_HOME``

If it does not print anything to the standard input but whitespaces, this means that JAVA_HOME has not been set. You can set JAVA_HOME using the following command:

``export JAVA_HOME=/path/to/your/JDK/installation``

Then open a terminal and go to the folder where you extracted VLMa. You can run VLMa daemon by running the following command:

``bin/vlmad start``

To run the web UI, open a new terminal and run:

``bin/vlmaw start``

Windows specific
~~~~~~~~~~~~~~~~

Ensure that the JAVA_HOME environment variable has been set and that it points to a valid JDK installation. To do this, have a look at:

-  http://support.microsoft.com/kb/310519 for Windows XP,
-  http://support.microsoft.com/kb/931715 for Windows Vista.

Then open a prompt and change directory to where you extracted VLMa. You can run VLMa daemon by running the following command:

``bin\vlmad start``

To run the web UI, open a new prompt and run:

``bin\vlmaw start``

The end
-------

To finish with, go to http://localhost:8080, you should see VLMa dashboard which tells you which medias are currently streamed and the list of servers VLMa didn't manage to contact through their telnet interface.

See also
--------

-  `VLMa documentation index <VLMa/Documentation>`__

`Category:VLMa <Category:VLMa>`__
