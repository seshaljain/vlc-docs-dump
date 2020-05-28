.. raw:: mediawiki

   {{SoCProject|year=2011|student=[[User:Akashm1990|Akash Mehrotra]]|mentor=confusedvorlon}}

| 

Abstract
--------

The primary aim of this project is to improve upon the luahttp interface and to add functions which are currently missing in the luahttp interface as compared to the qt interface. An additional aim is to redesign the http frontend and to create a lightweight http frontend for mobile devices.

Tentative list of improvements
------------------------------

-  [STRIKEOUT:enable playlist re-ordering]
-  add 'unminimise' command to the fullscreen command
-  allow user to get drives list on windows

in progress
~~~~~~~~~~~

-  enable access to the graphical equaliser
-  enable access to vout,aout through the lua interface
-  add ability to control picture controls (brightness, contrast, etc)
-  enable selection of a subtitle file (by path)
-  expose aspect ratio
-  use bonjour to advertise when http interface is live

done
~~~~

-  speed control
-  subtitle delay control
-  audio delay control
-  get the album art working(working already in luahttp)
-  implement pl_delete on luahttp

Suggestions for possible incorporation
--------------------------------------

-I'm adding this section as a place to store ideas that we might incorporate into the project, but which are still at the discussion stage.

-  create status.json and playlist.json - update: in progress by CV
-  update web interface pages to request and use json requests - update: probably not relevant with new interface by elminster
-  expose dvd info (chapter title)
