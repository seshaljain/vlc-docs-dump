{{example codefor=.Net Interface to VLC}} <syntaxhighlight
lang="csharp">
/*************************************************************************\***\*
\* VlcUserControl.cs: VlcUserControl partial class
definition**\ \***********************************************************************\*\ **\*
\* Copyright (C) 2006 Chris Meadowcroft \* \* Authors: Chris Meadowcroft
\* \* This program is free software; you can redistribute it and/or
modify \* it under the terms of the GNU Lesser General Public License as
published by \* the Free Software Foundation. \* \* This program is
distributed in the hope that it will be useful, \* but WITHOUT ANY
WARRANTY; without even the implied warranty of \* MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the \* GNU General Public License
for more details. \* \* You should have received a copy of the GNU
Lesser General Public License \* along with this program; if not, write
to the Free Software \* Foundation, Inc., 51 Franklin Street, Fifth
Floor, Boston MA 02110-1301,
USA.**\ \***************************************************************************/

using System; using System.Collections.Generic; using
System.ComponentModel; using System.Drawing; using System.Data; using
System.Diagnostics; using System.Runtime.InteropServices; using
System.Text; using System.Windows.Forms;

namespace VLanControl { public delegate void
NowPlayingEventHandler(MetaData data, String text);

   [ComVisible(true)]
   [InterfaceTypeAttribute(ComInterfaceType.InterfaceIsIDispatch)]
   [Guid("98029A85-9804-47d6-9430-F90933AE8650")] public interface
   IVlcUserControlEvents { [DispIdAttribute(0x60020000)] void
   NowPlayingEvent(MetaData data, String text); }

   [ComVisible(true)] [ClassInterface(ClassInterfaceType.None),
   ComSourceInterfaces(typeof(IVlcUserControlEvents))]
   [Guid("FB99D376-ED98-4ac0-B2C9-F2E974E0849F")] public partial class
   VlcUserControl : UserControl, IPlayer2 { private bool isPaused;
   private NativeLibVlc nativeVlc = new NativeLibVlc(); private bool
   useMpegVbrOffset; private bool usingPausedPosition; private int
   pausedTime; private double pausedPosition; private int
   shuttleSeconds; private bool useVlcCrop = false; private int cropTop;
   private int cropBottom; private int cropLeft; private int cropRight;

      const long SavingPostionTimespan = 5000000L; // .5 seconds in
      ticks

      public VlcUserControl() { InitializeComponent(); }

      protected override void OnLoad(EventArgs e) { base.OnLoad(e);
      this.nativeVlc.Initialize(); this.innerVlc.Bounds =
      this.ClientRectangle; this.nativeVlc.VideoOutput = this.innerVlc;
      this.nativeVlc.NowPlaying += this.NowPlayingUpdate; }

      // there's an overhead to supporting Vlc events, a memory leak, so
      we need to have them off by default // you can hook to the events
      before doing this, but none will occur [Browsable(false)]
      [DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
      public bool ProducingEvents { get { return
      this.nativeVlc.ProducingEvents; } set {
      this.nativeVlc.ProducingEvents = value; } }

      public void DisplayMessage(String message) {
      this.nativeVlc.ShowMessage(message); }

      [Browsable(false)]
      [DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
      public Size VideoSize { get { return this.nativeVlc.VideoSize; } }

      public void PrecomputeCrop(Size videoSize, int cropLeft, int
      cropRight, int cropTop, int cropBottom) { this.cropTop = cropTop;
      this.cropBottom = cropBottom; this.cropLeft = cropLeft;
      this.cropRight = cropRight; ComputeCrop(videoSize); }

      public bool ComputeCrop() { if(!this.useVlcCrop &&
      this.IsHandleCreated && (this.nativeVlc.VideoOutput != null) &&
      (this.State != PlayerState.None)) { Size vidSize =
      this.nativeVlc.VideoSize; if(!vidSize.IsEmpty) {
      ComputeCrop(this.nativeVlc.VideoSize); return true; } } return
      false; }

      private void ComputeCrop(Size videoSize) { Size mySize =
      ClientSize; Debug.WriteLine("Video Sizes = " +
      videoSize.ToString() + ", " + mySize.ToString());
      Debug.WriteLine("Crop = " + cropLeft.ToString() + ", " +
      cropTop.ToString() + ", " + cropRight.ToString() + ", " +
      cropBottom.ToString()); this.topBlocker.Visible = false;
      this.bottomBlocker.Visible = false; this.leftBlocker.Visible =
      false; this.rightBlocker.Visible = false;

         double myAspect = Convert.ToDouble(mySize.Width) /
         Convert.ToDouble(mySize.Height); if((this.cropTop == 0) &&
         (this.cropBottom == 0) && (this.cropLeft == 0) &&
         (this.cropRight == 0)) { double vlcAspect =
         Convert.ToDouble(videoSize.Width) /
         Convert.ToDouble(videoSize.Height); if(vlcAspect > myAspect) {
         // gray borders on the top and bottom int perfectHeight =
         Convert.ToInt32(mySize.Width / vlcAspect); this.innerVlc.Bounds
         = new Rectangle(new Point(0, (mySize.Height - perfectHeight) /
         2), new Size(mySize.Width, perfectHeight));
         //Debug.WriteLine("vlcAspect > myAspect " +
         this.innerVlc.Bounds.ToString()); } else { // gray borders on
         the left and right int perfectWidth =
         Convert.ToInt32(mySize.Height \* vlcAspect);
         this.innerVlc.Bounds = new Rectangle(new Point((mySize.Width -
         perfectWidth) / 2, 0), new Size(perfectWidth, mySize.Height));
         //Debug.WriteLine("vlcAspect < myAspect " +
         this.innerVlc.Bounds.ToString()); } } else { double
         realVlcAspect = Convert.ToDouble(videoSize.Width -
         this.cropRight - this.cropLeft) /
         Convert.ToDouble(videoSize.Height - this.cropTop -
         this.cropBottom); if(realVlcAspect > myAspect) { // gray
         borders on the top and bottom, and possible blocking panels //
         first, position and size the innerVlc as if there was no top or
         bottom cropping int videoPixelWidth = videoSize.Width -
         this.cropRight - this.cropLeft; double fakeVlcAspect =
         Convert.ToDouble(videoPixelWidth) /
         Convert.ToDouble(videoSize.Height); int perfectHeight =
         Convert.ToInt32(mySize.Width / fakeVlcAspect);
         Debug.WriteLine("perfectHeight = " + perfectHeight.ToString());

            double scalingFactor = Convert.ToDouble(mySize.Width) /
            Convert.ToDouble(videoPixelWidth); int innerVlcLeft =
            -Convert.ToInt32(Convert.ToDouble(this.cropLeft) \*
            scalingFactor); int innerVlcWidth =
            Convert.ToInt32(Convert.ToDouble(videoSize.Width) \*
            scalingFactor);

            int offTheTop =
            Convert.ToInt32(Convert.ToDouble(this.cropTop) \*
            scalingFactor); int offTheBottom =
            Convert.ToInt32(Convert.ToDouble(this.cropBottom) \*
            scalingFactor); int innerVlcTop = (mySize.Height -
            (perfectHeight - offTheTop - offTheBottom)) / 2; innerVlcTop
            -= offTheTop;

            this.innerVlc.Bounds = new Rectangle(new Point(innerVlcLeft, innerVlcTop),
               new Size(innerVlcWidth, perfectHeight));

            Debug.WriteLine("toowide innerVlc.Bounds = " +
            this.innerVlc.Bounds.ToString());

            // then, add blocking panels if necessary for the top and
            bottom cropping if(this.cropTop != 0) { if(offTheTop +
            innerVlcTop > 0) { this.topBlocker.Bounds = new Rectangle(
            new Point(0, innerVlcTop), new Size(mySize.Width,
            offTheTop)); this.topBlocker.Visible = true;
            Debug.WriteLine("topBlocker.Bounds = " +
            this.topBlocker.Bounds.ToString()); } } if(this.cropBottom
            != 0) { if(innerVlcTop + perfectHeight - offTheBottom <
            mySize.Height) { this.bottomBlocker.Bounds = new Rectangle(
            new Point(0, innerVlcTop + perfectHeight - offTheBottom),
            new Size(mySize.Width, offTheBottom));
            this.bottomBlocker.Visible = true;
            Debug.WriteLine("bottomBlocker.Bounds = " +
            this.bottomBlocker.Bounds.ToString()); } }

         ..

            } else { // gray borders on the left and right, and possible
            blocking panels // first, position and size the innerVlc as
            if there was no left or right cropping int videoPixelHeight
            = videoSize.Height - this.cropBottom - this.cropTop; double
            fakeVlcAspect = Convert.ToDouble(videoSize.Width) /
            Convert.ToDouble(videoPixelHeight); int perfectWidth =
            Convert.ToInt32(mySize.Height \* fakeVlcAspect);
            Debug.WriteLine("perfectWidth = " +
            perfectWidth.ToString());

               double scalingFactor = Convert.ToDouble(mySize.Height) /
               Convert.ToDouble(videoPixelHeight); int innerVlcTop =
               -Convert.ToInt32(Convert.ToDouble(this.cropTop) \*
               scalingFactor); int innerVlcHeight =
               Convert.ToInt32(Convert.ToDouble(videoSize.Height) \*
               scalingFactor);

               int offTheLeft =
               Convert.ToInt32(Convert.ToDouble(this.cropLeft) \*
               scalingFactor); int offTheRight =
               Convert.ToInt32(Convert.ToDouble(this.cropRight) \*
               scalingFactor); int innerVlcLeft = (mySize.Width -
               (perfectWidth - offTheLeft - offTheRight)) / 2;
               innerVlcLeft -= offTheLeft;

               this.innerVlc.Bounds = new Rectangle(new Point(innerVlcLeft, innerVlcTop),
                  new Size(perfectWidth, innerVlcHeight));

               Debug.WriteLine("toohigh innerVlc.Bounds = " +
               this.innerVlc.Bounds.ToString());

               // then, add blocking panels if necessary for the left
               and right cropping if(this.cropLeft != 0) { if(offTheLeft
               + innerVlcLeft > 0) { this.leftBlocker.Bounds = new
               Rectangle( new Point(innerVlcLeft, 0), new
               Size(offTheLeft, mySize.Height));
               this.leftBlocker.Visible = true;
               Debug.WriteLine("leftBlocker.Bounds = " +
               this.leftBlocker.Bounds.ToString()); } }
               if(this.cropRight != 0) { if(innerVlcLeft + perfectWidth
               - offTheRight < mySize.Width) { this.rightBlocker.Bounds
               = new Rectangle( new Point(innerVlcLeft + perfectWidth -
               offTheRight, 0), new Size(offTheRight, mySize.Height));
               this.rightBlocker.Visible = true;
               Debug.WriteLine("rightBlocker.Bounds = " +
               this.rightBlocker.Bounds.ToString()); } }

            }

         }

      }

      public String GetConfigVariable(String name, String returnOnError)
      { String value; if(this.nativeVlc.GetConfigVariable(name, out
      value) == VlcError.Success) { return value; } else { return
      returnOnError; } }

      public bool SetConfigVariable(String name, String value) { return
      this.nativeVlc.SetConfigVariable(name, value) == VlcError.Success;
      }

      [Browsable(false)]
      [DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
      public int Time { get { try { return this.nativeVlc.Time; }
      catch(Exception) { return 0; } } }

      [Browsable(false)]
      [DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
      public double Position { get { return this.nativeVlc.Position; } }

      public void MoveToPosition(TrackPosition newTrackPosition) {
      if((newTrackPosition.position >= 0.0d) &&
      (newTrackPosition.position < 1.0d)) { this.nativeVlc.Position =
      newTrackPosition.position; if(this.IsPaused) {
      this.usingPausedPosition = true; this.pausedTime =
      newTrackPosition.time; this.pausedPosition =
      newTrackPosition.position; this.shuttleSeconds = 0; } } }

      private TrackPosition CalculateShuttle(int origTime, double
      origPosition, int offsetSeconds) { int newTime = origTime +
      offsetSeconds;

         double positionPerTime; if(origPosition > .5d) {
         positionPerTime = origPosition / Convert.ToDouble(origTime); }
         else { positionPerTime = (1.0d - origPosition) /
         Convert.ToDouble(this.nativeVlc.Length - origTime); } double
         newPosition = origPosition + Convert.ToDouble(offsetSeconds) \*
         positionPerTime;

         //Debug.WriteLine(String.Format("CalculateShuttle time={0}
         pos={1}", newTime, newPosition));

         return new TrackPosition(newTime, newPosition);

      }

      public TrackPosition Shuttle(int offsetSeconds) {
      if(!this.IsPaused) { TrackPosition newPosition =
      CalculateShuttle(this.nativeVlc.Time, this.nativeVlc.Position,
      offsetSeconds); if(this.useMpegVbrOffset) {
      this.nativeVlc.Position = newPosition.position; } else {
      this.nativeVlc.Time = newPosition.time; } return newPosition; }

         if(!this.usingPausedPosition) { this.usingPausedPosition =
         true; this.pausedTime = this.nativeVlc.Time;
         this.pausedPosition = this.nativeVlc.Position;
         this.shuttleSeconds = 0; }

         this.shuttleSeconds += offsetSeconds; return
         CalculateShuttle(this.pausedTime, this.pausedPosition,
         this.shuttleSeconds);

      }

      [Browsable(false)]
      [DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
      public int Volume { get { return this.nativeVlc.Volume; } set {
      this.nativeVlc.Volume = value; } }

      const int MinRate = -2; const int MaxRate = 2; const int
      NormalRate = 0;

      public void GetRates(out int minRate, out int maxRate, out int
      normalRate) { minRate = MinRate; maxRate = MaxRate; normalRate =
      NormalRate; }

      [Browsable(false)]
      [DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
      public int Rate { get { // 1000 is normal, 2000 is half speed, 500
      is double speed, etc. int bigRate =
      this.nativeVlc.GetVlcObjectInt(ObjectType.VLC_OBJECT_INPUT,
      "rate", 1000); if(bigRate > 3000) { return -2; } if(bigRate >
      1500) { return -1; } if(bigRate > 750) { return 0; } if(bigRate >
      400) { return 1; } return 2; } set { int newRate = NormalRate;
      switch(value) { case 2: newRate = 250; break; case 1: newRate =
      500; break; case 0: newRate = 1000; break; case -1: newRate =
      2000; break; case -2: newRate = 4000; break; default: throw new
      ArgumentOutOfRangeException(); }
      this.nativeVlc.SetVlcObjectInt(ObjectType.VLC_OBJECT_INPUT,
      "rate", newRate); } }

      [Browsable(false)]
      [DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
      public int Length { get { try { return this.nativeVlc.Length; }
      catch(Exception) { return -1; } } set {
      this.nativeVlc.SetArtificialLength(value); } }

      [Browsable(false)]
      [DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
      public double TimeScaling { get { return
      this.nativeVlc.TimeScaling; } set { this.nativeVlc.TimeScaling =
      value; } }

      [Browsable(false)]
      [DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
      public PlayerState State { get { int state =
      this.nativeVlc.GetVlcObjectInt(ObjectType.VLC_OBJECT_INPUT,
      "state", (int)InputState.INIT_S); switch((InputState)state) { case
      InputState.PAUSE_S: return PlayerState.Paused; case
      InputState.PLAYING_S: return PlayerState.Playing; default: return
      PlayerState.None; } } }

      [Browsable(false)]
      [DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
      public bool IsPlaying { get { return this.State ==
      PlayerState.Playing; } }

      [Browsable(false)]
      [DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
      public bool IsPaused { get { return this.State ==
      PlayerState.Paused; } }

      [Browsable(false)]
      [DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
      public bool IsMute { get { return (this.nativeVlc.Volume == 0); }
      }

      public void ToggleMute() { this.nativeVlc.ToggleVolumeMute(); }

      private String JoinArraysWithCR(Array data, String[] dataText) {
      StringBuilder sb = new StringBuilder(); for(int index = 0; index <
      data.Length; index++) { if(index != 0) { sb.Append("n"); }
      sb.Append(data.GetValue(index).ToString()); sb.Append("n");
      sb.Append(dataText[index]); } return sb.ToString(); }

      public String DeinterlaceModesAsString() { String[] choices;
      String[] choiceText;
      this.nativeVlc.GetVlcVariableChoiceList(ObjectType.VLC_OBJECT_VOUT,
      "deinterlace", out choices, out choiceText); return
      JoinArraysWithCR(choices, choiceText); }

      public void DeinterlaceModes(out String[] choices, out String[]
      choiceText) {
      this.nativeVlc.GetVlcVariableChoiceList(ObjectType.VLC_OBJECT_VOUT,
      "deinterlace", out choices, out choiceText); }

      [Browsable(false)]
      [DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
      public String DeinterlaceMode { get { return
      this.nativeVlc.GetVlcObjectString(ObjectType.VLC_OBJECT_VOUT,
      "deinterlace", String.Empty); } set {
      this.nativeVlc.SetVlcObjectString(ObjectType.VLC_OBJECT_VOUT,
      "deinterlace", value); } }

      public String AspectRatiosAsString() { String[] choices; String[]
      choiceText;
      this.nativeVlc.GetVlcVariableChoiceList(ObjectType.VLC_OBJECT_VOUT,
      "aspect-ratio", out choices, out choiceText); return
      JoinArraysWithCR(choices, choiceText); }

      public void AspectRatios(out String[] choices, out String[]
      choiceText) {
      this.nativeVlc.GetVlcVariableChoiceList(ObjectType.VLC_OBJECT_VOUT,
      "aspect-ratio", out choices, out choiceText); }

      [Browsable(false)]
      [DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
      public String AspectRatio { get { return
      this.nativeVlc.GetVlcObjectString(ObjectType.VLC_OBJECT_VOUT,
      "aspect-ratio", String.Empty); } set {
      this.nativeVlc.SetVlcObjectString(ObjectType.VLC_OBJECT_VOUT,
      "aspect-ratio", value); } }

      public String CropModesAsString() { String[] choices; String[]
      choiceText;
      this.nativeVlc.GetVlcVariableChoiceList(ObjectType.VLC_OBJECT_VOUT,
      "crop", out choices, out choiceText); return
      JoinArraysWithCR(choices, choiceText); }

      public void CropModes(out String[] choices, out String[]
      choiceText) {
      this.nativeVlc.GetVlcVariableChoiceList(ObjectType.VLC_OBJECT_VOUT,
      "crop", out choices, out choiceText); }

      [Browsable(false)]
      [DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
      public String CropMode { get { return
      this.nativeVlc.GetVlcObjectString(ObjectType.VLC_OBJECT_VOUT,
      "crop", String.Empty); } set {
      this.nativeVlc.SetVlcObjectString(ObjectType.VLC_OBJECT_VOUT,
      "crop", value); } }

      [Browsable(false)]
      [DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
      public int CroppingLeft { get { if(this.useVlcCrop) { return
      this.nativeVlc.GetVlcObjectInt(ObjectType.VLC_OBJECT_VOUT,
      "crop-left", 0); } else { return this.cropLeft; } } set {
      if(this.useVlcCrop) {
      this.nativeVlc.SetVlcObjectInt(ObjectType.VLC_OBJECT_VOUT,
      "crop-left", value); } else { this.cropLeft = value;
      ComputeCrop(); } } }

      [Browsable(false)]
      [DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
      public int CroppingRight { get { if(this.useVlcCrop) { return
      this.nativeVlc.GetVlcObjectInt(ObjectType.VLC_OBJECT_VOUT,
      "crop-right", 0); } else { return this.cropRight; } } set {
      if(this.useVlcCrop) {
      this.nativeVlc.SetVlcObjectInt(ObjectType.VLC_OBJECT_VOUT,
      "crop-right", value); } else { this.cropRight = value;
      ComputeCrop(); } } }

      [Browsable(false)]
      [DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
      public int CroppingTop { get { if(this.useVlcCrop) { return
      this.nativeVlc.GetVlcObjectInt(ObjectType.VLC_OBJECT_VOUT,
      "crop-top", 0); } else { return this.cropTop; } } set {
      if(this.useVlcCrop) {
      this.nativeVlc.SetVlcObjectInt(ObjectType.VLC_OBJECT_VOUT,
      "crop-top", value); } else { this.cropTop = value; ComputeCrop();
      } } }

      [Browsable(false)]
      [DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
      public int CroppingBottom { get { if(this.useVlcCrop) { return
      this.nativeVlc.GetVlcObjectInt(ObjectType.VLC_OBJECT_VOUT,
      "crop-bottom", 0); } else { return this.cropBottom; } } set {
      if(this.useVlcCrop) {
      this.nativeVlc.SetVlcObjectInt(ObjectType.VLC_OBJECT_VOUT,
      "crop-bottom", value); } else { this.cropBottom = value;
      ComputeCrop(); } } }

      public String AudioTracksAsString() { int[] choices; String[]
      choiceText;
      this.nativeVlc.GetVlcVariableChoiceList(ObjectType.VLC_OBJECT_INPUT,
      "audio-es", out choices, out choiceText); return
      JoinArraysWithCR(choices, choiceText); }

      public void AudioTracks(out int[] trackIds, out String[]
      trackNames) {
      this.nativeVlc.GetVlcVariableChoiceList(ObjectType.VLC_OBJECT_INPUT,
      "audio-es", out trackIds, out trackNames); }

      [Browsable(false)]
      [DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
      public int AudioTrack { get { return
      this.nativeVlc.GetVlcObjectInt(ObjectType.VLC_OBJECT_INPUT,
      "audio-es", -1); } set {
      this.nativeVlc.SetVlcObjectInt(ObjectType.VLC_OBJECT_INPUT,
      "audio-es", value); } }

      public String SubTitleTracksAsString() { int[] choices; String[]
      choiceText;
      this.nativeVlc.GetVlcVariableChoiceList(ObjectType.VLC_OBJECT_INPUT,
      "spu-es", out choices, out choiceText); return
      JoinArraysWithCR(choices, choiceText); }

      public void SubTitleTracks(out int[] trackIds, out String[]
      trackNames) {
      this.nativeVlc.GetVlcVariableChoiceList(ObjectType.VLC_OBJECT_INPUT,
      "spu-es", out trackIds, out trackNames); }

      [Browsable(false)]
      [DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
      public int SubTitleTrack { get { return
      this.nativeVlc.GetVlcObjectInt(ObjectType.VLC_OBJECT_INPUT,
      "spu-es", -1); } set {
      this.nativeVlc.SetVlcObjectInt(ObjectType.VLC_OBJECT_INPUT,
      "spu-es", value); } }

      public String ProgramsAsString() { int[] choices; String[]
      choiceText;
      this.nativeVlc.GetVlcVariableChoiceList(ObjectType.VLC_OBJECT_INPUT,
      "program", out choices, out choiceText); return
      JoinArraysWithCR(choices, choiceText); }

      public void Programs(out int[] trackIds, out String[] trackNames)
      {
      this.nativeVlc.GetVlcVariableChoiceList(ObjectType.VLC_OBJECT_INPUT,
      "program", out trackIds, out trackNames); }

      [Browsable(false)]
      [DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
      public int Program { get { return
      this.nativeVlc.GetVlcObjectInt(ObjectType.VLC_OBJECT_INPUT,
      "program", -1); } set {
      this.nativeVlc.SetVlcObjectInt(ObjectType.VLC_OBJECT_INPUT,
      "program", value); } }

      [Browsable(false)]
      [DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
      public bool AllowVideoAdjustments { get { return
      this.nativeVlc.AllowVideoAdjustments; } set {
      this.nativeVlc.AllowVideoAdjustments = value; } }

      [Browsable(false)]
      [DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
      public float Contrast { get { return
      this.nativeVlc.GetVlcObjectFloat(ObjectType.VLC_OBJECT_VOUT,
      "contrast", 1.0f); } set { VlcError err =
      this.nativeVlc.SetVlcObjectFloat(ObjectType.VLC_OBJECT_VOUT,
      "contrast", value); } }

      [Browsable(false)]
      [DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
      public float Brightness { get { return
      this.nativeVlc.GetVlcObjectFloat(ObjectType.VLC_OBJECT_VOUT,
      "brightness", 1.0f); } set { VlcError err =
      this.nativeVlc.SetVlcObjectFloat(ObjectType.VLC_OBJECT_VOUT,
      "brightness", value); } }

      [Browsable(false)]
      [DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
      public int Hue { get { return
      this.nativeVlc.GetVlcObjectInt(ObjectType.VLC_OBJECT_VOUT, "hue",
      0); } set { VlcError err =
      this.nativeVlc.SetVlcObjectInt(ObjectType.VLC_OBJECT_VOUT, "hue",
      value); } }

      [Browsable(false)]
      [DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
      public float Saturation { get { return
      this.nativeVlc.GetVlcObjectFloat(ObjectType.VLC_OBJECT_VOUT,
      "saturation", 1.0f); } set { VlcError err =
      this.nativeVlc.SetVlcObjectFloat(ObjectType.VLC_OBJECT_VOUT,
      "saturation", value); } }

      [Browsable(false)]
      [DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
      public float Gamma { get { return
      this.nativeVlc.GetVlcObjectFloat(ObjectType.VLC_OBJECT_VOUT,
      "gamma", 1.0f); } set { VlcError err =
      this.nativeVlc.SetVlcObjectFloat(ObjectType.VLC_OBJECT_VOUT,
      "gamma", value); } }

      public void RotateCropModes() {
      this.nativeVlc.PressKey("key-crop"); }

      [Browsable(false)]
      [DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
      public int AudioDelay { get { long delay =
      this.nativeVlc.GetVlcObjectLong(ObjectType.VLC_OBJECT_INPUT,
      "audio-delay", 0L); return Convert.ToInt32(delay / 1000L);

         } set { long delay = Convert.ToInt64(value) \* 1000L;
         this.nativeVlc.SetVlcObjectLong(ObjectType.VLC_OBJECT_INPUT,
         "audio-delay", delay); }

      }

      [Browsable(false)]
      [DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
      public int SubTitleDelay { get { long delay =
      this.nativeVlc.GetVlcObjectLong(ObjectType.VLC_OBJECT_INPUT,
      "spu-delay", 0L); return Convert.ToInt32(delay / 1000L);

         } set { long delay = Convert.ToInt64(value) \* 1000L;
         this.nativeVlc.SetVlcObjectLong(ObjectType.VLC_OBJECT_INPUT,
         "spu-delay", delay); }

      }

      [Browsable(false)]
      [DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
      public int ChapterCount { get { int[] chapterIds; String[]
      chapterText;
      this.nativeVlc.GetVlcVariableChoiceList(ObjectType.VLC_OBJECT_INPUT,
      "chapter", out chapterIds, out chapterText); return
      (chapterIds.Length > 0) ? chapterIds.Length - 1 : 0; } }

      [Browsable(false)]
      [DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
      public int Chapter { get { return
      this.nativeVlc.GetVlcObjectInt(ObjectType.VLC_OBJECT_INPUT,
      "chapter", -1); } set {
      this.nativeVlc.SetVlcObjectInt(ObjectType.VLC_OBJECT_INPUT,
      "chapter", value); } }

      private void RepositionAfterPause() { if(this.usingPausedPosition
      && (this.shuttleSeconds != 0)) { TrackPosition newPosition =
      CalculateShuttle(this.pausedTime, this.pausedPosition,
      this.shuttleSeconds); if(this.useMpegVbrOffset) {
      this.nativeVlc.Position = newPosition.position; } else {
      this.nativeVlc.Time = newPosition.time; } }
      this.usingPausedPosition = false; }

      public void Play() { this.isPaused = false; this.nativeVlc.Play();
      RepositionAfterPause(); }

      public void ClearPlayList() { this.usingPausedPosition = false;
      //Debug.WriteLine("ClearPlayList");
      this.nativeVlc.PlaylistClear(); }

      public void AddAndPlay(String fileName, String options) { String[]
      optionsArray = options.Split('n'); int id =
      AddToPlayList(fileName, "", optionsArray); PlayItem(id); }

      public int AddToPlayList(String fileName, String title, String[]
      options) { //MessageBox.Show(fileName); this.usingPausedPosition =
      false; int index = 0; this.nativeVlc.AddTarget(fileName, options,
      ref index); Debug.WriteLine("Added to Playlist " + fileName);
      Debug.WriteLine("index = " + index.ToString()); return index; }

      public void PlayItem(int itemId) { this.usingPausedPosition =
      false; this.isPaused = false;
      this.nativeVlc.SetArtificialLength(0); this.nativeVlc.TimeScaling
      = 0.0d;

         int currentIndex = this.nativeVlc.PlaylistIndex;
         Debug.WriteLine("PlayItem index = " + itemId.ToString(), "
         currentIndex = " + currentIndex.ToString()); if(currentIndex <
         0) { this.nativeVlc.Play(); } else {
         //this.nativeVlc.PlaylistPrevious();
         this.nativeVlc.Play(itemId); }

      }

      public void Stop() { this.usingPausedPosition = false;
      this.nativeVlc.Stop(); this.isPaused = false; }

      public void TogglePause() { bool wasPaused = this.IsPaused;
      this.nativeVlc.Pause(); if(wasPaused) { RepositionAfterPause(); }
      this.isPaused = !wasPaused; }

      public void RotateSubtitles() {
      this.nativeVlc.PressKey("key-subtitle-track"); }

      public void RotateAudioTrack() {
      this.nativeVlc.PressKey("key-audio-track"); }

      public void RotateDeinterlaceMode() {
      this.nativeVlc.PressKey("key-deinterlace"); }

      public void RotateAspectRatio() {
      this.nativeVlc.PressKey("key-aspect-ratio"); }

      public void CropTop() { //this.nativeVlc.PressKey("key-crop-top");
      this.CroppingTop = this.CroppingTop + 1; }

      public void UnCropTop() {
      //this.nativeVlc.PressKey("key-uncrop-top"); int crop =
      this.CroppingTop - 1; if(crop >= 0) { this.CroppingTop = crop; } }

      public void CropBottom() {
      //this.nativeVlc.PressKey("key-crop-bottom"); this.CroppingBottom
      = this.CroppingBottom + 1; }

      public void UnCropBottom() {
      //this.nativeVlc.PressKey("key-uncrop-bottom"); int crop =
      this.CroppingBottom - 1; if(crop >= 0) { this.CroppingBottom =
      crop; } }

      public void CropLeft() {
      //this.nativeVlc.PressKey("key-crop-left"); this.CroppingLeft =
      this.CroppingLeft + 1; }

      public void UnCropLeft() {
      //this.nativeVlc.PressKey("key-uncrop-left"); int crop =
      this.CroppingLeft - 1; if(crop >= 0) { this.CroppingLeft = crop; }
      }

      public void CropRight() {
      //this.nativeVlc.PressKey("key-crop-right"); this.CroppingRight =
      this.CroppingRight + 1; }

      public void UnCropRight() {
      //this.nativeVlc.PressKey("key-uncrop-right"); int crop =
      this.CroppingRight - 1; if(crop >= 0) { this.CroppingRight = crop;
      } }

      public bool UseMpegVbrOffset { get { return this.useMpegVbrOffset;
      } set { this.useMpegVbrOffset = value; } }

      public void NextDvdTrack() {
      this.nativeVlc.PressKey("key-title-next"); }

      public void PreviousDvdTrack() {
      this.nativeVlc.PressKey("key-title-prev"); }

      public void NextDvdChapter() {
      this.nativeVlc.PressKey("key-chapter-next"); }

      public void PreviousDvdChapter() {
      this.nativeVlc.PressKey("key-chapter-prev"); }

      public event MetaDataEventHandler NowPlaying; // this 2nd event is
      a non-standard prototype needed for Com Interop event sourcing
      public event NowPlayingEventHandler NowPlayingEvent;

      private void OnNowPlaying(MetaDataUpdateEventArgs args) {
      if(this.NowPlaying != null) { this.NowPlaying(this, args); }
      if(this.NowPlayingEvent != null) { this.NowPlayingEvent(args.Data,
      args.Text); } }

      private void NowPlayingUpdate(object sender,
      MetaDataUpdateEventArgs args) { OnNowPlaying(args); }

      protected override void OnResize(EventArgs e) { base.OnResize(e);
      if(!ComputeCrop()) { this.innerVlc.Bounds = this.ClientRectangle;
      } }

   }

} </syntaxhighlight>
