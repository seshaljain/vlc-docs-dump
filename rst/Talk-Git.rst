Patch submission chain
----------------------

To answer jpd:

Generated patch mails should have a "reply to" which set the first email as the direct parent of all emails, not reply-to each other in chain for what I understand. First, it is more readable in inboxes (folding, indentations), and maybe (don't know) this can have an effect on the receiver git process when it applies patches from emails.

So the schema explain how patch-emails should be dependents.
