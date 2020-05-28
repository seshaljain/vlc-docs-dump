Orders assignment algorithm
===========================

Acknolegements
--------------

-  Every adapter has a score. This score is 0 when VLMa starts and then gets incremented by 5 when the order handled by this adapter is broadcasted and decremented by 1 otherwise.

-  The user can assign priorities to programs, so that a program with a higer priority is more likely to be broadcasted.

Steps of the assignment
-----------------------

Grouping
~~~~~~~~

Programs that can be handled by the same adapter (two DTT channels having the same frequency for example) are put together into what we call "Program groups".

Partitionment
~~~~~~~~~~~~~

Not every adapter can read a given program group. So the first step si to put together adapters and program groups by affinity, DVB-T adapters with DTT program groups, stream channels with stream program groups, or DBV-S adapters bound to satellite XXX with Satellite program groups whose media is bound to XXX.

Assignment
~~~~~~~~~~

For each partition, adapters are then sorted by score and program groups by priority (the priority of a group being the sum of the priorities of its programs).

Then the first program group is assigned to the first adapter, the 2nd program group with the 2nd adapter, etc.

See also
--------

-  `VLMa documentation index <VLMa/Documentation>`__

`Category:VLMa <Category:VLMa>`__
