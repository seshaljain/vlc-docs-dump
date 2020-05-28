{{SoCProjectstudent=[[User:Gurunathmentor=Kieran Khunya}}

<br>

== Abstract ==

The goal of this project is to add Multi-view coding (to be specific stereo 3D) support to x264 encoder. This will enable x264 to author 3D videos in H.264 Stereo High Profile MVC format. This will involve adding the encoding tools specific to secondary (right) view. 3D Bluray made H.264 MVC as the encoding format and the secondary goal of the poject is to implement 3D Bluray specific changes.

== Milestones ==

''This section will be updated after every milestone''<br>

{\| width="714" cellspacing="1" cellpadding="1" border="1" style="" Status ! scope="col" \| Deadline ! scope="col" \| Description valign="bottom" align="center" \| Done <br> \| valign="bottom" align="center" \| May 20<br> \| valign="bottom" align="center" \| All Intra scenario with constant QP&nbsp;option<br> valign="bottom" align="center" \| Done<br> \| valign="bottom" align="center" \| June 17<br> \| valign="bottom" align="center" \| Working IPPP stream with constant QP option<br> \|}

<br>

== Timeline ==

''The schedule is preliminary''

{\| cellspacing="1" cellpadding="1" border="1" style="width: 711px; height: 82px;" align="center" valign="bottom" \| '''Status''' \| align="center" width="150" valign="bottom" \| '''Date''' \| align="center" width="60" valign="bottom" \| '''Period''' \| align="center" valign="bottom" \| '''Description''' align="center" valign="bottom" \| &nbsp; Done<br> \| align="center" valign="bottom" \| &nbsp; May 09 - May 13<br> \| align="center" valign="bottom" \| &nbsp; week 1<br> \| align="center" valign="bottom" \| Subset SPS, AVC&nbsp;SPS changes<br> align="center" valign="bottom" \| &nbsp; Done<br> \| align="center" valign="bottom" \| &nbsp; May 16 - May 20<br> \| align="center" valign="bottom" \| &nbsp; week 2<br> \| align="center" valign="bottom" \| All Intra case with constant qp scenario<br> align="center" valign="bottom" \| &nbsp; Done<br> \| align="center" valign="bottom" \| &nbsp; May 23 - May 27<br> \| align="center" valign="bottom" \| &nbsp; week 3<br> \| align="center" valign="bottom" \| IP scenario without inter-view prediction (constant QP)<br> align="center" valign="bottom" \| &nbsp; Done<br> \| align="center" valign="bottom" \| May 30 - June 3 \| align="center" valign="bottom" \| week 4<br> \| align="center" valign="bottom" \| IP&nbsp;scenario without inter-view prediction (constant QP)<br> align="center" valign="bottom" \| &nbsp; Done<br> \| align="center" valign="bottom" \| June 6 - June 10 \| align="center" valign="bottom" \| week 5<br> \| align="center" valign="bottom" \| IP scenario with inter-view prediction (constant QP)<br> align="center" valign="bottom" \| Done<br> \| align="center" valign="bottom" \| June 13 - June 17 \| align="center" valign="bottom" \| week 6<br> \| align="center" valign="bottom" \| Testing &amp; Bug fixing<br> align="center" valign="bottom" \| Not started<br> \| align="center" valign="bottom" \| June 20 - June 24 \| align="center" valign="bottom" \| week 7<br> \| align="center" valign="bottom" \| IB..P scenario without inter-view prediction (constant QP)<br> align="center" valign="bottom" \| Not started<br> \| align="center" valign="bottom" \| June 27 - July 01 \| align="center" valign="bottom" \| week 8<br> \| align="center" valign="bottom" \| IB..P scenario with inter-view prediction (constant QP)<br> align="center" valign="bottom" \| Not started<br> \| align="center" valign="bottom" \| July 4 - July 8 \| align="center" valign="bottom" \| week 9<br> \| align="center" valign="bottom" \| IB..P scenario with inter-view prediction (constant QP)<br> align="center" valign="bottom" \| Not started<br> \| align="center" valign="bottom" \| July 11 - July 15 \| align="center" valign="bottom" \| week 10<br> \| align="center" valign="bottom" \| Testing &amp; Bug fixing<br> align="center" valign="bottom" \| Not started<br> \| align="center" valign="bottom" \| July 18 - July 22 \| align="center" valign="bottom" \| week 11<br> \| align="center" valign="bottom" \| Rate control related changes<br> align="center" valign="bottom" \| Not started<br> \| align="center" valign="bottom" \| July 25 - July 29 \| align="center" valign="bottom" \| week 12<br> \| align="center" valign="bottom" \| Rate control related changes<br> align="center" valign="bottom" \| Not started<br> \| align="center" valign="bottom" \| Aug 01 - Aug 05 \| align="center" valign="bottom" \| week 13<br> \| align="center" valign="bottom" \| Rate control related changes &amp; bug-fixing<br> align="center" valign="bottom" \| Not started<br> \| align="center" valign="bottom" \| Aug 08 - Aug 12 \| align="center" valign="bottom" \| week 14<br> \| align="center" valign="bottom" \| 3D Blu-ray related modifications<br> align="center" valign="bottom" \| Not started<br> \| align="center" valign="bottom" \| Aug 15 - Aug 19 \| align="center" valign="bottom" \| week 15<br> \| align="center" valign="bottom" \| 3D Blu-ray related modifications<br> align="center" valign="bottom" \| Not started<br> \| align="center" valign="bottom" \| Aug 22 - Aug 26 \| align="center" valign="bottom" \| week 16<br> \| align="center" valign="bottom" \| 3D Blu-ray related modifications<br> align="center" valign="bottom" \| Not started<br> \| align="center" valign="bottom" \| Aug 29 - Sep 02 \| align="center" valign="bottom" \| week 17<br> \| align="center" valign="bottom" \| Testing &amp; Bug fixing<br> \|}

<br>

== Repository ==

https://github.com/gurunathan/SHP-MVC-x264

To test the code<br> <pre> $ git clone git@github.com:gurunathan/SHP-MVC-x264.git $ cd shp-mvc-x264 $ git checkout shp-mvc-x264 $ ./configure $ make $ x264 &lt;args&gt; --stereo-mvc </pre> <br>

<br>

<br>
