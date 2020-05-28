.. raw:: mediawiki

   {{SoCProject|year=2009|student=[[User:Geal|Geoffroy Couprie]]|mentor=Jérôme Decoodt}}

DXVA Integration
================

Abstract
--------

The Windows DXVA API gives access to video decoding and processing in the graphic card. Decoding with the GPU will reduce the load on the CPU and (hopefully) speed up the decoding. This project aims at creating a MPEG2 and H.264 decoder for VLC using this API.

Calendar
--------

**May 23 :** Beginning of SoC

**July 13 :** Mid-term evaluations deadline

**August 24 :** Final evaluation deadline

TODO list
---------

======================= ========================================================================================================================================================================================================================================================================== =========== ===========
What                    WHAT!?                                                                                                                                                                                                                                                                     When        Status
======================= ========================================================================================================================================================================================================================================================================== =========== ===========
Writing headers         The DXVA headers are not provided by the w32api project, so I have to write down the headers files for all the interfaces I will use. This is the very boring part of the project...                                                                                       May-August  in progress
Create test programs    I have to test the API and the headers, so I need test cases. I can use the samples from the Platform SDK, but there are not many examples, and the ones provided won't compile at the beginning of the project, because they use part of the API I have still not written May-June    in progress
Create the codec plugin Using my test code, I'll be able to build a small codec plugin. Then, I'll use it to do all the further tests, and write the final part of the project                                                                                                                     June-August not started
======================= ========================================================================================================================================================================================================================================================================== =========== ===========
