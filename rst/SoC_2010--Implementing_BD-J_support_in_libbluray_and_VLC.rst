.. raw:: mediawiki

   {{SoCProject|year=2010|student=[[User:Will07c5|William Hahne]]|mentor=[[User:Jpsaman|Jean-Paul Saman]] }}

Abstract
--------

This project will focus primarily on getting BD-J (Blu-ray Disc Java) support into libbluray. BD-J support is important because many of the advanced features and extra content in Blu-ray movies uses BD-J. Currently people with Blu-ray drives are tied to Windows if they want to access this content, they are forced to use proprietary Blu-ray software which does not run on Linux or various other operating systems. This project will also integrate the BD-J support into VLC.

Todo
----

=========== ============================================ ========
Status      Description                                  Comments
=========== ============================================ ========
In Progress Learning relevant parts of VLC plugin system
Done        List of BD-J classes needed                 
In Progress Make general structure of LibBDJ            
Not Started Implement loading and executing jar files   
Not Started Implement org.bluray.\* classes             
Not Started Implement org.havi.\* classes               
Not Started Implement org.davic.\* classes              
Not Started Implement org.dvb.\* classes                
Not Started Implement javax.tv.\* classes               
=========== ============================================ ========

Here is a more detailed list of classes that need to be implemented. `1 <http://spreadsheets.google.com/pub?key=0AtoY0FArm6whdGF3cjh6TlhObGtIMHdKdENVSDd4NkE&output=html>`__

Timeline
--------

==================== ================= =========================================================================================================================
Date                 Period            Description
==================== ================= =========================================================================================================================
April 26 - May 24    Community bonding Get a more exact list of the which classes are most important and commonly used. Lay out the structure of the LibBDJ API.
May 24 - May 30      Week 1            Get basic LibBDJ API written.
May 31 - June 6      Week 2            Start working on the org.bluray.\* classes.
June 7 - June 13     Week 3            Continue working on the org.bluray.\* classes.
June 14 - June 20    Week 4            Finish up the org.bluray.\* classes.
June 21 - June 27    Week 5            Start adding in classes already implemented in XleTView.
June 28 - July 4     Week 6            Finish adding in classes already implemented in XleTView.
July 5 - July 11     Week 7            Start working on the remaining classes.
July 12 - July 18    Week 8            Continue working on the remaining classes.
July 19 - July 25    Week 9            Finish working on the remaining classes.
July 26 - August 1   Week 10           Start finishing up (fix remaining known bugs, testing).
August 2 - August 8  Week 11           Continue finishing up.
August 9 - August 15 Week 12           Finish up and do any final testing.
==================== ================= =========================================================================================================================

Repository
----------

None yet.
