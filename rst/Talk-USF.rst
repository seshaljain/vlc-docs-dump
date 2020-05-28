Changing the USF standard
-------------------------

I'm not a VLC developer, however I regularly use VLC as a testbed for interpretting standards which are not quite wide spread. So, I'm asking to open some discussion here as to the USF standard which in my opinion is incredbily incomplete.

I have implemented many of the professional subtitling formats in the application which I produce and have come to the realization that with the exception of only two or three formats, USF would be suitable as an intermediate format between the others and graphical representation. Since the software I develop is in use by many post processing facilities preparing subtitles for digital broadcast on DVB networks, I'd like to use my "pull" to try and make USF the defacto standard since the alternatives are closed formats from FAB and Screen Subtitling and they lack the richness of USF and are typically binary coded using unusual character encodings. An example of this format is PAC which is, in my personal experience the most used subtitling format in the scandinavian professional world. Sadly, formats such as .860 and .890 which are ancient also occur far too often.

Ok, biography over :)

While reading through the USF spec, I've learned that most any numbers that are size oriented are poorly represented. For example, when describing a font style, values that appear similar to an HTML font size are used. I'm under the impression that they should be interpretted as points, not pixels. Either way, the number is useless.

There is no DPI standard for TV screens and there is for that fact, no standard of any use for TV resolution. PAL and NTSC are now obsolete as system metrics.

Because of this, it is important to try and define the size attribute more clearly.

One option is to use the USF implementation of VLC as standard. I have not figured out yet what the specification from VideoLAN is.

The alternative is to define a metric that should be accepted among most of us as a standard and then take steps to alter the USF standard to reflect it.

Historically, the text-safe area of film has been user adjustable. This is represented by the positioning information of the standard which defines a horizontal and vertical margin.

Within the text-safe area, the pro standards have generally defined that a single line is either 1/10th or 1/12th of the vertical text-safe area.

I have found that most of my customers prefer that 12 lines of text is the nicest to look at and this has become the standard.

Since the USF standard appears to use the value 24 as their description of a normal text line, I believe that we should respect that.

From this information, it would be correct to assume that a font of size "24" would suggest a font height of 1/12th the vertical text-safe area of the screen.

An alternative suggestion would be to suggest that a single line of text would consume 14 lines of text from absolute top to absolute bottom of the screen. The justification of this suggestion even though it isn't mathematically correct in relation to the previous suggestion is, if vertical margins are defined in styles other than the "default" style, text rendered in one region will be disproportionate to text rendered in other regions of different styles. If the subtitler would have prefered different font sizes, there's more than a few ways they could have dealt with that and the vertical margins would be less refined of an approach.

So, my preferred solution to the problem is to demand that vertical and horizontal margins only be legal in the "default" style and that the definition of size "24" be interpretted as 1/12th the height of the vertical text safe range for the document.

Also, I recommend that as the standard suggests that the default style interprets the "internal default" value of the vertical margin as 10% and horizontal margin as 20% (which for the most part has little use except when word wrapping).

I will follow this posting later with steps towards how we may form a more formal group for standardizing the USF format which is apparently no longer maintained. I would even suggest an SMPTE working group for this purpose.

`Dstarr <User:Dstarr>`__ (`talk <User_talk:Dstarr>`__) 25 August 2007 (originally unsigned)

   j-b replied on your usertalk 06:38, 28 January 2019 (CET)
