.. raw:: mediawiki

   {{Image requested|reason=Add a screenshot.}}

.. raw:: mediawiki

   {{Module|name=puzzle|type=Video output filter|first_version=0.9.0|description=Turns the video in a jigsaw puzzle game}}

Options
-------

Note that the puzzle module has been improved in later versions; the option ``--puzzle-black-slot`` has been **removed** in favour of ``--puzzle-mode`` (use 1 for ``--puzzle-mode`` for the same effect).

.. raw:: mediawiki

   {{Option
   |name=puzzle-cols
   |value=integer
   |default=4
   |description=Specifies the number of columns in the puzzle
   }}

.. raw:: mediawiki

   {{Option
   |name=puzzle-rows
   |value=integer
   |default=4
   |description=Specifies the number of rows in the puzzle
   }}

.. raw:: mediawiki

   {{Option
   |name=puzzle-border
   |value=integer
   |default=
   |description=Border
   }}

.. raw:: mediawiki

   {{Option
   |name=puzzle-preview
   |value=boolean
   |default=disabled
   |description=Small preview
   }}

.. raw:: mediawiki

   {{Option
   |name=puzzle-preview-size
   |value=integer
   |default=
   |description=Small preview size
   }}

.. raw:: mediawiki

   {{Option
   |name=puzzle-shape-size
   |value=integer
   |default=
   |description=Piece edge shape size
   }}

.. raw:: mediawiki

   {{Option
   |name=puzzle-auto-shuffle
   |value=integer
   |default=
   |description=Puzzle auto shuffle
   }}

.. raw:: mediawiki

   {{Option
   |name=puzzle-auto-solve
   |value=integer
   |default=
   |description=Auto solve
   }}

.. raw:: mediawiki

   {{Option
   |name=puzzle-rotation
   |value=integer
   |default=
   |description=0 is (0), 1 is (0/180), 2 is (0/90/180/270), 3 is (0,90,180,270,mirror)
   }}

.. raw:: mediawiki

   {{Option
   |name=puzzle-mode
   |value=integer
   |default=
   |description=0 is jigsaw puzzle, 1 is sliding puzzle, 2 is swap puzzle, 3 is exchange puzzle
   }}

.. raw:: mediawiki

   {{Option
   |name=puzzle-black-slot
   |default=disabled
   |description=Change puzzle type to a sliding tile puzzle
   }}

.. raw:: mediawiki

   {{Documentation footer}}
