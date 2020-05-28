== Thanks to the article's author ==

I would like to extend my deepest thanks to the author of this article
for simplifying the process of integrating VLC into the Delphi
mainstream.

I find the tips in this article most helpful, and love the VideoLAN
system immensley.

Simon

== To author: ==

Thank you for your time and effort. Would it be too much to ask you to
give us guidelines how to stream files using Delphi and ActiveX
component? : ''(unsigned by [[User:Derran|Derran]])''

You can start streaming any time by modifying the MRL.
   VLCPlugin1.addTarget('C:video.mpg', null, VLCPlayListInsert, 0); //
   you can use any MRL with parameters instead of 'c:video.mpg' here

See
http://www.videolan.org/doc/streaming-howto/en/streaming-howto-en.html
to create the MRL fitting to your desires.

You can also create a playliste-file (like .m3u) and embedd the
streaming parameters to this file. --[[User:Hogi|Hogi]] 00:01, 9
February 2007 (CET)

== VLC and Delphi ==

Delphi can also use the [[ExternalAPI]] like in
[http://tothpaul.free.fr/sources.php?dprgrp.vld VideoLAN for Delphi] :D

   { val:TValue } val.AsInteger := IntToStr(Panel1.Width);
   VLCLib.VLC_VariableSet('conf::width',val); val.AsInteger :=
   inttostr(Panel1.Height); VLCLib.VLC_VariableSet('conf::height',val);

== Controlling the size and client panel ==

The ActiveX runs like a champ, but it wants to create its own window to display. I need it to show on a panel (or anything else to set size and position) within an application. I was able to set the size by:
   val := inttostr(Panel1.Width);
   VLCPlugin1.setVariable('conf::width',val); val :=
   inttostr(Panel1.Height); VLCPlugin1.setVariable('conf::height',val);

But this results in no display:
   val := inttostr(Panel1.Handle);
   VLCPlugin1.setVariable('drawable',val);

You can hear the sound when you continue with:
   VLCPlugin1.addTarget(OpenDialog.FileName, null, $1, 0);
   VLCPlugin1.play;

The 'drawable' variable is evidently not right, but it doesn't kick a
compile error. What is the correct variable? Or is there a whole
different way I should be doing this? Thanks.
