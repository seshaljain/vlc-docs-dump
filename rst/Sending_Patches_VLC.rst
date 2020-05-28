How to produce a patch for VLC
------------------------------

-  Get a modern `Git <Git>`__ version, 1.7 or higher.
-  Make your changes and commit them.
-  Check your commit.
-  Produce a `patch <patch>`__ according to `the Git page <Git#Submitting_patches>`__, but **don't send it yet**. Read the following before sending.

Writing an appropriate description
----------------------------------

-  The patch email's subject **should** be prefixed by "**[PATCH]**".
-  You **should** include a description that will be the commit log message of your patch.
-  A more **exhaustive explanation** is also welcomed along with your patch. This could be the **second paragraph** of your commit log.

Check List
----------

When you send a patch make sure that:

-  The code mostly **complies** with the `Code Conventions <Code_Conventions>`__.
-  The patch applies to the latest **master branch**.

   -  Do not submit patches against a bugfix branch, except to backport fixes already found on the master branch.
   -  Do not submit patches against releases. That would be completely useless.
   -  As a special exception, language translations go to the last bugfix branch directly.

-  Proper copyright license exists, and is stated where appropraite.
-  The changes do not break the build.

   -  Testing all combinations is impossible. But you should at least test one.

-  The tests suite still **passes** (i.e. **\`make check\`** runs without errors).
-  The compiler does not mention new compilation **warnings**.

   -  In some rare cases, warnings are unavoidable or counter-productive to fix. If so, explain it in the patch description.

-  If the patch adds, removes or moves one or more files, make sure the distribution still works, i.e. **\`make distcheck**\ \` runs succesfully to the end.
-  No **trailing spaces** are introduced (*git show --color* show them in red).
-  Indentation is correct, no **tabs** are introduced.
-  No unrelated changes are included in the patch.

   -  Especially changes to ``.po`` or ``.pot`` files do not belong within source code patches.
   -  As a necessary exception, tabs are allowed within Makefiles.

-  **Your name is correctly set**. That is, that you are using your fullname, which is correctly capitalized and so on.

   -  For example, if you are **John Smith** with an e-mail of **johnsmith@acme.example**, you should set your "Git name" to **John Smith <johnsmith@acme.example>** - real full name - not "jsmith", "John S", "J. Smith", "johnnykool1234", "J.S." or any other permutation.

-  The patch description makes sense.
-  Read your patch one more time using **git show**, and check that it looks OK.

Sending it to the vlc-devel list
--------------------------------

**Now** you can send it to the `vlc-devel <http://mailman.videolan.org/listinfo/vlc-devel>`__ mailing list.

*Please* subscribe to it before sending your patch; otherwise, it may not get through the list's spam filters. You will be able to unsubscribe later easily if needed.

*Try* to avoid sending patches bigger than 100kB on the mailing list, if you can.

Following your patch
--------------------

You can check if your patch was received by the list at the `list archive <http://mailman.videolan.org/pipermail/vlc-devel/>`__.

If the patch gets approved, then there will normally be a post to the vlc-devel list to say "patch applied". There will also be a post to the `vlc-commits <http://mailman.videolan.org/pipermail/vlc-commits/>`__ list (`subscribe here <http://mailman.videolan.org/listinfo/vlc-commits>`__).

Getting your patch merged
-------------------------

-  *Don't hesitate* to **re-ask** for review if after a week there are no replies or comments.
-  If there are comments, **please answer** to those and eventually correct your patch if possible.
-  Check regularly on the `patches website <http://patches.videolan.org/project/vlc-devel/list/>`__.

That should ensure that your patch gets merged.

`Category:Coding <Category:Coding>`__ `Category:Security <Category:Security>`__
