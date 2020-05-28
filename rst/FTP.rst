.. raw:: mediawiki

   {{Protocol|FTP}}

**File Transfer Protocol** or **FTP** is used to download or upload files.

TLS support (encryption) was added in 2.2.0. Implicit TLS is preferable over Explicit TLS.

The syntax for Implicit TLS (most secure):

| ``ftps://host/file``
| ``ftps://host:port/file``

The syntax for Explicit TLS:

| ``ftpes://host/file``
| ``ftpes://host:port/file``

Or for no encryption:

| ``ftp://host/file``
| ``ftp://host:port/file``
