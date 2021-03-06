VLMa build HOWTO
================

Requirements
------------

You need the following softwares to build VLMa:

-  A Java SDK version 5.0 or higher

You can check whether your Java installation is suitable by checking that the *javac* executable is available and that the version is higher than 5.0 (*javac -version*).

-  `Maven 2 <http://maven.apache.org>`__

VLMa uses Maven as a build system. If you are not familiar with this tool, check the `5 minutes guide <http://maven.apache.org/guides/getting-started/maven-in-five-minutes.html>`__.

-  VLMa source tree

You can either download the latest tarballs at http://www.videolan.org/vlma/download.html and extract them or check out the development tree using `Git <Git>`__

``$ git clone ``\ ```git://git.videolan.org/vlma.git`` <git://git.videolan.org/vlma.git>`__

Build
-----

Once you have downloaded VLMa source code, change directory to the root of the project and type:

``$ mvn install``

Maven will download VLMa dependencies and build the project according to the configuration located in the pom.xml files.

This method is currently not working(17/08/2014). Maven returns dependency errors during VLMa Core building. vthr.videolan.org is unknown host. At the moment theres no way known to build.

See also
--------

-  `VLMa documentation index <VLMa/Documentation>`__

`Category:Building <Category:Building>`__ `Category:VLMa <Category:VLMa>`__
