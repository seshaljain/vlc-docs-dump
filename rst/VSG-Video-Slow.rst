==Video displays first frames and black/grey only==

<p> This is the symptom of a slow decoding, and this is especially the
case with high bitrate H264 or HEVC. </p>

<p> If you're using VLC < 3.0, you need turn on hardware acceleration.
Preferences -> Input Codecs -> Hardware Acceleration. </p>

Is your Graphic card able to accelerate decoding ?

<br/> <b>For 4K H264</b> <ul> <li>Quick Sync 4 (Intel Broadwell ~)</li>
<li>PureVideo HD 5 cards (Nvidia GT 520 ~)</li> <li>UVD 5.0 cards (AMD
Radeon R9 ~)</li> </ul>

<br/> <b>For HEVC</b> <ul> <li>Quick Sync 5 (Intel Skylake ~)</li>
<li>PureVideo HD 7 cards (Nvidia GTX 950 ~, or GTX 750 SE)</li> <li>UVD
6.0 cards (AMD Radeon Rx300 ~)</li> </ul>

<br/> <b>For HEVC 10bit</b> <ul> <li>Quick Sync 6 (Intel Kaby Lake
~)</li> <li>PureVideo HD 7 cards (Nvidia GTX 950 ~, or GTX 750 SE)</li>
<li>UVD 6.0 Fiji/Carrizo cards (AMD Radeon Rx400 ~)</li> </ul>

<br/> <b>All information per chip</b> <br/>
https://en.wikipedia.org/wiki/Intel_Quick_Sync_Video\ <br/>
https://en.wikipedia.org/wiki/Unified_Video_Decoder\ <br/>
https://en.wikipedia.org/wiki/Nvidia_PureVideo\ <br/>

{{VSG}}
