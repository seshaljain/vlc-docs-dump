.. raw:: mediawiki

   {{Wikipedia|Time to live}}

**TTL** or **Time to live** is a number used to prevent data from circulating indefinitely.

For each hop in a network the data passes through, the TTL value is decreased by one; when it reaches zero, the packet of data is discarded. In this way, endless loops are broken (such as *host A* sending data to *host B* sending data to *host C* sending data back to *host A*).

The default TTL value between `operating systems <operating_system>`__ differs, but it may not be greater than 255.

`Category:Glossary <Category:Glossary>`__
