{{#if: \|{{#if: \|{{#if: \|{{#if: \|{{#if: \|[\ https://git.videolan.org/?p=\ ;a=;f=;h=;hb= }}}] \|[\ https://git.videolan.org/?p=\ ;a=;f=;h= }}}] }} \|{{#if: \|[\ https://git.videolan.org/?p=\ ;a=;f=;hb= }}}] \|[\ https://git.videolan.org/?p=\ ;a=;f= }}}] }} }} \|{{#if: \|{{#if: \|[\ https://git.videolan.org/?p=\ ;a=;h=;hb= ]}}}] \|[\ https://git.videolan.org/?p=\ ;a=;h= ]}}}] }} \|{{#if: \|[\ https://git.videolan.org/?p=\  }}}] \|[\ https://git.videolan.org/?p=\  }}}] }} }} }} \|{{#if: \|{{#if: \|{{#if: \|[\ https://git.videolan.org/?p=\ ;f=;h=;hb= }}}] \|[\ https://git.videolan.org/?p=\ ;f=;h= }}}] }} \|{{#if: \|[\ https://git.videolan.org/?p=\ ;f=;hb= }}}] \|[\ https://git.videolan.org/?p=\ ;f=; }}}] }} }} \|{{#if: \|{{#if: \|[\ https://git.videolan.org/?p=\ ;h=;hb= ]}}}] \|[\ https://git.videolan.org/?p=\ ;h= ]}}}] }} \|{{#if: \|[\ https://git.videolan.org/?p=\  }}}] \|[\ https://git.videolan.org/?p=\  }}}] }} }} }} }} \| ` <https://git.videolan.org/>`__ }}

Usage
-----

``{{``\ \ ``|p= |a= |h= }}``

or

``{{``\ \ ``|p= |a= |h= |l= }}``

or

``{{``\ \ ``|p= |a= |f= }}``

or

``{{``\ \ ``|p= |a= |f= |h= }}``

This is a meta-template, a wrapper around URL requests to git.videolan.org. This template *does not* perform `sanity checks <wikipedia:sanity_check>`__. It saves keystrokes and avoids `XSS <wikipedia:XSS>`__ requests from passed parameters.

Parameters:

-  **``|p=``** is the **branch** e.g. vlc.git, vlc/vlc-2.2.git or vlma.git (see https://git.videolan.org for a list of branch names)
-  **``|a=``** is the **format** e.g. blob. This may be given free-form but only the following are valid: summary, shortlog, log, commit, commitdiff, tree and patch
-  **``|f=``** is the **file** e.g. modules/demux/image.c. You can pass directory names to \|f= as well if \|a=tree
-  **``|h=``** is the **hash** e.g. 72f3067a6fddcd30e0ee33928a0ec6622ed2e74b
-  **``|hb=``** ???
-  **``|l=``** is the **label** (optional) e.g. arbitrary

Example 1:

\ ``;a=``\ \ ``;f=``\ \ ``;h=``\ \ ``;hb=``\ 

-  ``{{``\ \ ``|a=blob|h=72f3067a6fddcd30e0ee33928a0ec6622ed2e74b}}`` gives {{\|a=blob|h=72f3067a6fddcd30e0ee33928a0ec6622ed2e74b}} because no branch was specified
-  ``{{``\ \ ``|p=vlc.git|a=summary|hb=HEAD}}`` gives {{\|p=vlc.git|a=summary|hb=HEAD}}

`Category:Templates <Category:Templates>`__
