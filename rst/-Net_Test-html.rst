{{example code|for=.Net Interface to VLC}} <syntaxhighlight
lang="html4strict"> <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0
Transitional//EN"> <META HTTP-EQUIV='Content-Type' CONTENT='text/html;
charset=iso-8859-1' />

<HTML>
   <HEAD>
      <TITLE>Sink managed event in Internet Explorer</TITLE>

   </HEAD>

   <BODY>

      <OBJECT id="myVLan"
      classid="clsid:FB99D376-ED98-4ac0-B2C9-F2E974E0849F" width="720"
      height="480"> </OBJECT> <br /> <SCRIPT LANGUAGE="JScript"> var
      selectionsEmpty = true;

         function myVLan::NowPlayingEvent(a, b) {
         document.getElementById('nowPlaying').innerText = b;
         //alert(b); }

         function FillSelectionList(choiceArray, selectedChoice,
         selectId) { var selectElement =
         document.getElementById(selectId);
         while(selectElement.hasChildNodes()) {
         selectElement.removeChild(selectElement.lastChild); }

            for(index = 0; index < choiceArray.length; index += 2) { var
            choice = choiceArray[index]; var choiceText =
            choiceArray[index + 1]; var newOption =
            document.createElement('option'); newOption.value = choice;
            newOption.appendChild(document.createTextNode(choiceText));
            if(choice == selectedChoice) { newOption.selected =
            'selected'; } selectElement.appendChild(newOption); }

         }

         function FillSelectionsWhenPlaying() { if(selectionsEmpty &&
         (myVLan.State != 0)) { selectionsEmpty = false; var audioTracks
         = myVLan.AudioTracksAsString();
         FillSelectionList(audioTracks.split('n'), myVLan.AudioTrack,
         'AudioTracks'); var subTracks =
         myVLan.SubTitleTracksAsString();
         FillSelectionList(subTracks.split('n'), myVLan.SubTitleTrack,
         'SubTitleTracks'); var deints =
         myVLan.DeinterlaceModesAsString();
         FillSelectionList(deints.split('n'), myVLan.DeinterlaceMode,
         'DeinterlaceModes'); } }

         function EnableVideoAdjustments() { var vidCheck =
         document.getElementById("VideoAdjustmentCheck");
         if(vidCheck.checked) { myVLan.AllowVideoAdjustments = true;
         document.getElementById("Gamma").disabled = false;
         document.getElementById("Gamma").value = '';
         document.getElementById("Saturation").disabled = false;
         document.getElementById("Saturation").value = ''; } else {
         myVLan.AllowVideoAdjustments = false;
         document.getElementById("Gamma").disabled = true;
         document.getElementById("Saturation").disabled = true; } }

         myVLan.ProducingEvents = true; var options = new
         Array(":ffmpeg-pp-q=6", ":no-loop");
         ////////////////////////////////////////////////////////////////
         // CHANGE THE NEXT LINE TO A MEDIA FILE ON YOUR OWN HARD-DISK
         ////////////////////////////////////////////////////////////////
         myVLan.AddAndPlay("X:\Kiki.mpg", options.join('n')); var
         timerId = setInterval(FillSelectionsWhenPlaying, 1000);
         //myVLan.AddAndPlay("http://66.225.205.8:80",
         options.join('n'));

      </SCRIPT> <div style='float:left;margin:5px'> Audio Track<br />
      <select id="AudioTracks"
      onclick="myVLan.AudioTrack=document.getElementById('AudioTracks').value"></select>
      </div> <div style='float:left;margin:5px'> Subtitle Track<br />
      <select id="SubTitleTracks"
      onclick="myVLan.SubTitleTrack=document.getElementById('SubTitleTracks').value"></select>
      </div> <div style='float:left;margin:5px'> Deinterlace Mode<br />
      <select id="DeinterlaceModes"
      onclick="myVLan.DeinterlaceMode=document.getElementById('DeinterlaceModes').value;"></select>
      </div> <div style='float:left;margin:5px'> <input type="checkbox"
      id="VideoAdjustmentCheck" onclick="EnableVideoAdjustments();" />
      <label for="VideoAdjustmentCheck">Enable Video
      Adjustments</label><br /> Gamma<br /> <select id="Gamma"
      disabled="true"
      onchange="myVLan.Gamma=document.getElementById('Gamma').value">
      <option value='0.01'>0.01</option> <option
      value='0.5'>0.5</option> <option value='1.0'
      selected='selected'>1.0</option> <option value='1.5'>1.5</option>
      <option value='2.0'>2.0</option> <option value='2.5'>2.5</option>
      <option value='3.0'>3.0</option> <option value='3.5'>3.5</option>
      <option value='4.0'>4.0</option> <option value='4.5'>4.5</option>
      <option value='5.0'>5.0</option> <option value='5.5'>5.5</option>
      <option value='6.0'>6.0</option> <option value='6.5'>6.5</option>
      <option value='7.0'>7.0</option> <option value='7.5'>7.5</option>
      <option value='8.0'>8.0</option> <option value='8.5'>8.5</option>
      <option value='9.0'>9.0</option> <option value='9.5'>9.5</option>
      <option value='10.0'>10.0</option> </select><br /> Saturation<br
      /> <select id="Saturation" disabled="true"
      onchange="myVLan.Saturation=document.getElementById('Saturation').value">
      <option value='0'>0</option> <option value='0.5'>0.5</option>
      <option value='1' selected='selected'>1</option> <option
      value='1.5'>1.5</option> <option value='2'>2</option> <option
      value='2.5'>2.5</option> <option value='3'>3</option> </select>
      </div> <div id="nowPlaying"></div>

   </BODY>

</HTML> </syntaxhighlight> [[Category:Example code]]
