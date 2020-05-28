-  '''{{#if:<!--

| ``             -->|{{#if:``\ \ ``|''', ``\ ****\ `` or ``\ ****\ ``}} ''' or ``\ ****\ ``}} {{#if:``\ \ ``|<{{#switch:``\ 
| ``                       |boolean  = ``\ ```boolean`` <boolean>`__
| ``                       |float    = ``\ ```float`` <float>`__
| ``                       |integer  = ``\ ```integer`` <integer>`__
| ``                       |string   = ``\ ```string`` <string>`__
| ``                       |#default = ``\ 
| ``                     }}{{#if:``\ \ ``|> ``\ \ ``|{{#if:``\ \ ``|{{#if:``\ \ ``| [``\ \ `` .. ``\ \ ``] }} }}> }} |``\ \ ``}} ``\ *``':``\ ````\ \ ``{{#if:``\ \ ````\ ``|``*\ ``default value: ``\ \ ``'' }}``\ 

Usage:

-  name (required)

   -  alias (optional): an alias for the name
   -  alias2 (optional): a second alias for the name

-  value (optional)

   -  min (optional)
   -  max (optional)

-  select (optional): takes precedence over ``min`` and ``max``. ``{}`` will not be provided if not given (to avoid doubling). Use as e.g. ``{png,jpg,tiff}`` for documentation of options for ``--snapshot-format``
-  description (required)
-  default (optional)

min and max are only shown if both of them are specified, because no range should be given unbounded (if you think that is stupid, change it!)

`Category:Templates <Category:Templates>`__
