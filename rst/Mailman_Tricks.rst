**Removing mails from the archives**

- stop mailman

- create a backup of archives/private/$name.mbox/

- mutt -f archives/private/$name.mbox/$name.mbox, remove mails, quit

- /usr/lib/mailman/bin/arch --wipe $name, which will remove generated .gz/.html.gz and re-do the archives

- start mailman again

`Category:Roots <Category:Roots>`__ `Category:Security <Category:Security>`__
