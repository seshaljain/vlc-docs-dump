.. raw:: mediawiki

   {{protocol|file}}

The **file** protocol plays files on your PC through the normal file system. This includes your hard drive and any data `CDs <CD>`__ or data `DVDs <DVD>`__ you have (in `Linux <Linux>`__, these must be `mounted <wikipedia:Mount_(computing)>`__ before use).

For example:

``{{%}} vlc "``\ ```file://C:\My`` <file://C:\My>`__\ `` Music\Abracadabra.mp3"``

If no other protocols are used, file:// is assumed:

``% vlc "C:\My Music\Abracadabra.mp3"``

Module options
--------------

   *See*\ `Documentation:Modules/file <Documentation:Modules/file>`__

Source code
-----------

.. raw:: mediawiki

   {{file|modules/access/file.c|access module}}
