.. raw:: mediawiki

   {{howto|Use the HTTP interface to control VLC from a web browser}}

|The new HTTP interface in VLC 2.0| |The new Mobile interface in VLC 2.0|

-  `Start VLC on the server with the Web Interface <Documentation:Modules/http_intf#VLC_2.0.0_and_later>`__.
-  Type the IP address (or URL) of the host in the location field (address bar). You may need to specify the port (VLC defalts to using port 8080)

      An example is http://127.0.0.1:8080 - 127.0.0.1 refers to the local machine.

-  If you want to control VLC from a computer that is not the one running VLC then you will need to enable access in the .hosts file (from 0.9.6 onwards)
-  Add the files to be streamed to the playlist like /home/file.mpg (unless you use the UI to select the file in the next step)
-  Add streaming destination to the server in the sout field udp://\ :1234, using these steps in the UI:

   -  Go to File -> Open File
   -  Click Browse to select the file you want to play
   -  Select Stream/Save and click Settings
   -  Optional: Select Play Locally to make sure everything is working correctly
   -  Select UDP and fill in the client IP address and port number (default: 1234)
   -  Click OK, OK, and press play

-  Open VLC on the client to receive the video stream, in one of two ways:

   -  At the terminal, with **vlc**\ udp://@:1234
   -  Start up VLC normally

      -  Go to File -> Open network stream...
      -  Leave the default options (Radio button UDP selected, port set to 1234)
      -  Press OK

Note: the VLC Web Interface does not have an option to adjust the server's input stream. Direct to the host is required for changing the input media.

`Category:Control VLC <Category:Control_VLC>`__

.. |The new HTTP interface in VLC 2.0| image:: VLC_http_intf.png
.. |The new Mobile interface in VLC 2.0| image:: Android_webintf.jpg

