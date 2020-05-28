| ``# External URLs matching this list will *not* be blocked even if they would``
| ``# have been blocked by blacklist entries.``
| ``# For documentation see ``\ ```http://www.mediawiki.org/wiki/Extension:SpamBlacklist`` <http://www.mediawiki.org/wiki/Extension:SpamBlacklist>`__
| ``#  ``

::

   #
   # Syntax is as follows:
   #   * Everything from a "#" character to the end of the line is a comment
   #   * Every non-blank line is a regex fragment which will only match hosts inside URLs

   videolan\.org
   example\.com

    #
