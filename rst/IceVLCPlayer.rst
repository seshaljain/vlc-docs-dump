{{Historical}} {{Example codebinding]] to use [[VLC media player|VLC
(media) player]] (0.8.6i) in your application.

----IceVLCPlayer.pas:

<syntaxhighlight lang="delphi"> unit IceVLCPlayer;

{ TIceVLCPlayer - VLC Player for Delphi (0.8.6i) (c)2008 by Norbert
Mereg }

interface

uses
   SysUtils, Classes, Controls, ExtCtrls, libVLC, Graphics, Windows,
   Forms;

type
   TEVLCException = class(Exception); TEVLCNotFound = class(Exception);
   TEVLCLoadLibrary = class(Exception);

   TErrorEvent = procedure(Sender: TObject; ErrorCode: integer;
   ErrorMessage: string) of object;

   TIceVLCPlayer = class(TCustomPanel) private VLC : libvlc_instance;
   VLCVideo : integer; VLCInput : libvlc_input; VLCError :
   libvlc_exception; FLength: Int64; FIsPlaying: boolean; FTime: Int64;
   FPosition: Single;

      FTimer: TTimer; FVideoWidth: integer; FVideoHeight: integer;

      FOnPlay: TNotifyEvent; FOnStop: TNotifyEvent; FOnError:
      TErrorEvent;

      function CheckError: boolean; procedure FTimerTimer(Sender:
      TObject); procedure StartPlaying; procedure SetOnPlay(const Value:
      TNotifyEvent); procedure StopPlaying; procedure SetOnStop(const
      Value: TNotifyEvent); procedure SetOnError(const Value:
      TErrorEvent); procedure StopIfPlaying;

      { Private declarations }

   protected
      { Protected declarations }

   public
      { Public declarations } property Length: Int64 read FLength;
      property Time: Int64 read FTime; property Position: Single read
      FPosition; property IsPlaying: boolean read FIsPlaying; property
      VideoWidth: integer read FVideoWidth; property VideoHeight:
      integer read FVideoHeight;

      constructor Create(AOwner: TComponent); override; destructor
      Destroy; override;

      procedure Play(const FileName: string); procedure PlayTV(const
      CaptureDev: string; const Channel: integer; const Country: integer
      = 0);

      procedure Stop;

   published
      { Published declarations } property Align; property OnPlay:
      TNotifyEvent read FOnPlay write SetOnPlay; property OnStop:
      TNotifyEvent read FOnStop write SetOnStop; property OnError:
      TErrorEvent read FOnError write SetOnError;

   end;

procedure Register;

implementation

procedure Register; begin RegisterComponents('IcePackage',
[TIceVLCPlayer]); end;

{ TIceVLCPlayer }

constructor TIceVLCPlayer.Create(AOwner: TComponent); var Args: array
[0..1] of PChar;

begin
   inherited Create(AOwner);

   VLC := nil; VLCInput := nil; FIsPlaying := False;

   ParentBackground := False; Color := clBlack; Width := 320; Height :=
   240; Caption := ''; BevelOuter := bvNone;

   case VLD_Startup of
      VLD_SUCCESS :
         begin

         end;

      VLD_NOLIB :
         begin
            raise TEVLCLoadLibrary.Create('VLC Player not installed!
            Please re-install.'); exit;

         end;

      VLD_NOTFOUND :
         begin
            raise TEVLCNotFound.Create('VLC Player not installed or
            wrong version! Please re-install.'); exit;

         end;

   end;

   //Clear error var. FillChar(VLCError,SizeOf(VLCError),0);

   //Create new VLC object Args[0] := PChar(VLD_LibPath); Args[1] :=
   nil; VLC := libvlc_new( 1, @Args[0], VLCError);

   FTimer := TTimer.Create(nil); FTimer.Enabled := False;
   FTimer.Interval := 500; FTimer.OnTimer := FTimerTimer;

end;

destructor TIceVLCPlayer.Destroy; begin FTimer.Free;

   // NTDLL.DLL error :( // if Assigned(VLC) then //
   libvlc_destroy(VLC);

   inherited;

end;

procedure TIceVLCPlayer.Stop; begin StopIfPlaying; end;

procedure TIceVLCPlayer.StopIfPlaying; begin if IsPlaying then begin if
Assigned(VLCInput) then begin libvlc_playlist_stop(VLC, VLCError);
CheckError; end; libvlc_playlist_clear(VLC, VLCError); CheckError;

   FTimer.Enabled := False; FIsPlaying := False;

   libvlc_input_free(VLCInput); VLCInput := nil;

..

   end;

end;

procedure TIceVLCPlayer.Play(const FileName: string); begin
StopIfPlaying;

   VLCVideo := libvlc_playlist_add(VLC, PChar(UTF8Encode(FileName)), '',
   VLCError); CheckError;

   StartPlaying;

end;

procedure TIceVLCPlayer.PlayTV(const CaptureDev: string; const Channel,
Country: integer); var Args: array[0..14] of PChar; DevStr: string;
begin StopIfPlaying;

   args[0] := ':dshow-adev=""'; args[1] := ':dshow-size=""'; args[2] :=
   ':dshow-caching=200'; args[3] := ':dshow-chroma=""'; args[4] :=
   ':dshow-fps=0.000000'; args[5] := ':no-dshow-config'; args[6] :=
   ':no-dshow-tuner'; args[7] := PChar(':dshow-tuner-channel=' +
   IntToStr(Channel)); args[8] := PChar(':dshow-tuner-country=' +
   IntToStr(Country)); args[9] := ':dshow-tuner-input=2'; //1-Cable,
   2-Antenna args[10] := ':dshow-video-input=-1'; args[11] :=
   ':dshow-audio-input=-1'; args[12] := ':dshow-video-output=-1';
   args[13] := ':dshow-audio-output=-1'; args[14] := nil;

   DevStr := 'dshow:// :dshow-vdev="' + CaptureDev + '"'; VLCVideo :=
   libvlc_playlist_add_extended(VLC, PChar(UTF8Encode(DevStr)), '', 14,
   @Args[0], VLCError); CheckError;

   StartPlaying;

end;

function TIceVLCPlayer.CheckError: boolean; var ErrorCode: Integer;
ErrorMsg: string; begin if VLCError.Code <> 0 then begin Result :=
False; ErrorCode := VLCError.Code; ErrorMsg := VLCError.Message;
libvlc_exception_clear(VLCError);

   if Assigned(OnError) then
      OnError(Self, ErrorCode, ErrorMsg);

// raise TEVLCException.CreateFmt('Error %d! %s', [ErrorCode, ErrorMsg]);
   end else Result := True;

end;

procedure TIceVLCPlayer.StartPlaying; begin //Set current parent (Self)
libvlc_video_set_parent(VLC, Self.Handle, VLCError); CheckError;

   //Start play libvlc_playlist_play(VLC, VLCVideo, 0, nil, VLCError);
   CheckError;

   FLength := -2; //returned Length = -1 - stream; 0 - TV , >0 - local
   file

   FTimer.Enabled := true;

end;

procedure TIceVLCPlayer.StopPlaying; begin FTimer.Enabled := False;
FIsPlaying := False;

   //Freeing current input libvlc_input_free(VLCInput); VLCInput := nil;

   if Assigned(OnStop) then
      OnStop(Self);

end;

procedure TIceVLCPlayer.FTimerTimer(Sender: TObject); var Ln: int64;
begin FTimer.Enabled := False;

   try
      //Get current input VLCInput := libvlc_playlist_get_input(VLC,
      VLCError); CheckError;

      //Get current movie length (msec) Ln :=
      libvlc_input_get_length(VLCInput, VLCError);

      if not CheckError then begin if IsPlaying then begin //If end of
      movie then cause error. FIsPlaying := False; StopPlaying; exit;
      end else begin FTimer.Enabled := True; exit; end; end; FLength :=
      Ln;

      //Get current movie current time (msec) FTime :=
      libvlc_input_get_time(VLCInput, VLCError); CheckError;

      //Get current movie current position (0 -> 1) FPosition :=
      libvlc_input_get_position(VLCInput, VLCError); CheckError;

      if CheckError and (not IsPlaying) then begin FIsPlaying := True;

         if Assigned(OnPlay) then
            OnPlay(Self);

      end;

// FVideoWidth := libvlc_video_get_width(VLCInput, VLCError); //
CheckError; // FVideoHeight := libvlc_video_get_height(VLCInput,
VLCError); // CheckError;

   FTimer.Enabled := True;

..

   Except
      if IsPlaying then
         StopPlaying;

   end;

end;

procedure TIceVLCPlayer.SetOnError(const Value: TErrorEvent); begin
FOnError := Value; end;

procedure TIceVLCPlayer.SetOnPlay(const Value: TNotifyEvent); begin
FOnPlay := Value; end;

procedure TIceVLCPlayer.SetOnStop(const Value: TNotifyEvent); begin
FOnStop := Value; end;

end. </pre>

---------------------------------------------------------------------------libVLC.pas
- Thanks to Paul TOTH

<pre> unit libVLC;

{ VideoLAN libvcl.dll (0.8.6b) Interface for Delphi (c)2007 by Paul TOTH
   -  Modified by Norbert Mereg libvcl.dll (0.8.6i) }

// http://wiki.videolan.org/ExternalAPI#VLC_Control

interface

const
   LibName = 'libvlc.dll';

// Structures type libvlc_exception = record Code : integer; Message :
pchar; end;

   libvlc_instance = pointer; libvlc_input = pointer;

{$IFDEF STATIC}

// Core function libvlc_new(argc:integer; args:ppchar; var
exception:libvlc_exception):libvlc_instance; cdecl external lib;
procedure libvlc_destroy(vlc:libvlc_instance); cdecl external lib;
procedure libvlc_exception_clear(var exception:libvlc_exception); cdecl
external lib;

// Playlist function libvlc_playlist_add(vlc:libvlc_instance;
fileName,name:pchar; var exception:libvlc_exception):integer; cdecl
external lib; function libvlc_playlist_add_extended(vlc:libvlc_instance;
fileName,name:pchar; optCount:integer; opts:ppchar; var
exception:libvlc_exception):integer; cdecl external lib; procedure
libvlc_playlist_clear(vlc:libvlc_instance; var
exception:libvlc_exception); cdecl external lib; function
libvlc_playlist_items_count(vlc:libvlc_instance; var
exception:libvlc_exception):integer; cdecl external lib; function
libvlc_playlist_isplaying(vlc:libvlc_instance; var
exception:libvlc_exception):longbool; cdecl external lib; procedure
libvlc_playlist_play(vlc:libvlc_instance; index,optCount:integer;
opts:ppchar; var exception:libvlc_exception); cdecl external lib;
procedure libvlc_playlist_pause(vlc:libvlc_instance; var
exception:libvlc_exception); cdecl external lib; procedure
libvlc_playlist_stop(vlc:libvlc_instance; var
exception:libvlc_exception); cdecl external lib; procedure
libvlc_playlist_next(vlc:libvlc_instance; var
exception:libvlc_exception); cdecl external lib; procedure
libvlc_playlist_prev(vlc:libvlc_instance; var
exception:libvlc_exception); cdecl external lib; function
libvlc_playlist_get_input(vlc:libvlc_instance; var
exception:libvlc_exception):libvlc_input; cdecl external lib;

// Input procedure libvlc_input_free(input:libvlc_input); cdecl external
lib; function libvlc_input_get_length(input:libvlc_input; var
exception:libvlc_exception):int64; cdecl external lib; function
libvlc_input_get_time(input:libvlc_input; var
exception:libvlc_exception):int64; cdecl external lib; function
libvlc_input_get_position(input:libvlc_input; var
exception:libvlc_exception):single; cdecl external lib; procedure
libvlc_toggle_fullscreen(input:libvlc_input; var
exception:libvlc_exception); cdecl external lib; procedure
libvlc_set_fullscreen(input:libvlc_input; var
exception:libvlc_exception); cdecl external lib; function
libvlc_get_fullscreen(input:libvlc_input; var
exception:libvlc_exception):longbool; cdecl external lib;

// Video function libvlc_video_get_width(input:libvlc_input; var
exception:libvlc_exception):integer; cdecl external lib; function
libvlc_video_get_height(input:libvlc_input; var
exception:libvlc_exception):integer; cdecl external lib;

// Audio function libvlc_audio_get_mute(vlc:libvlc_instance; var
exception:libvlc_exception):longbool; cdecl external lib; procedure
libvlc_audio_set_mute(vlc:libvlc_instance; mute:longbool; var
exception:libvlc_exception); cdecl external lib; function
libvlc_audio_get_volume(vlc:libvlc_instance; var
exception:libvlc_exception):integer; cdecl external lib; procedure
libvlc_audio_set_volume(vlc:libvlc_instance; volume:integer; var
exception:libvlc_exception); cdecl external lib;

//Other procedure libvlc_video_set_parent(vlc:libvlc_instance;
libvlc_drawable_t:integer; var exception:libvlc_exception); cdecl
external lib; //function libvlc_video_get_parent(vlc:libvlc_instance;
var exception:libvlc_exception):integer; cdecl external lib; {$ELSE}

var

// Core
   libvlc_new:function(argc:integer; args:ppchar; var
   exception:libvlc_exception):libvlc_instance; cdecl;
   libvlc_destroy:procedure(vlc:libvlc_instance); cdecl;
   libvlc_exception_clear:procedure(var exception:libvlc_exception);
   cdecl;

// Playlist
   libvlc_playlist_add:function(vlc:libvlc_instance;
   fileName,name:pchar; var exception:libvlc_exception):integer; cdecl;
   libvlc_playlist_add_extended:function(vlc:libvlc_instance;
   fileName,name:pchar; optCount:integer; opts:ppchar; var
   exception:libvlc_exception):integer; cdecl;
   libvlc_playlist_clear:procedure(vlc:libvlc_instance; var
   exception:libvlc_exception); cdecl;
   libvlc_playlist_items_count:function(vlc:libvlc_instance; var
   exception:libvlc_exception):integer; cdecl;
   libvlc_playlist_isplaying:function(vlc:libvlc_instance; var
   exception:libvlc_exception):longbool; cdecl;
   libvlc_playlist_play:procedure(vlc:libvlc_instance;
   index,optCount:integer; opts:ppchar; var exception:libvlc_exception);
   cdecl; libvlc_playlist_pause:procedure(vlc:libvlc_instance; var
   exception:libvlc_exception); cdecl;
   libvlc_playlist_stop:procedure(vlc:libvlc_instance; var
   exception:libvlc_exception); cdecl;
   libvlc_playlist_next:procedure(vlc:libvlc_instance; var
   exception:libvlc_exception); cdecl;
   libvlc_playlist_prev:procedure(vlc:libvlc_instance; var
   exception:libvlc_exception); cdecl;
   libvlc_playlist_get_input:function(vlc:libvlc_instance; var
   exception:libvlc_exception):libvlc_input; cdecl; // Input (Vout)
   libvlc_input_free:procedure(input:libvlc_input); cdecl;
   libvlc_input_get_length:function(input:libvlc_input; var
   exception:libvlc_exception):int64; cdecl;
   libvlc_input_get_time:function(input:libvlc_input; var
   exception:libvlc_exception):int64; cdecl;
   libvlc_input_get_position:function(input:libvlc_input; var
   exception:libvlc_exception):single; cdecl;
   libvlc_toggle_fullscreen:procedure(input:libvlc_input; var
   exception:libvlc_exception); cdecl;
   libvlc_set_fullscreen:procedure(input:libvlc_input; var
   exception:libvlc_exception); cdecl;
   libvlc_get_fullscreen:function(input:libvlc_input; var
   exception:libvlc_exception):longbool; cdecl; // audio
   libvlc_video_get_width:function(input:libvlc_input; var
   exception:libvlc_exception):integer; cdecl;
   libvlc_video_get_height:function(input:libvlc_input; var
   exception:libvlc_exception):integer; cdecl; // Audio
   libvlc_audio_get_mute:function(vlc:libvlc_instance; var
   exception:libvlc_exception):longbool; cdecl;
   libvlc_audio_set_mute:procedure(vlc:libvlc_instance; mute:longbool;
   var exception:libvlc_exception); cdecl;
   libvlc_audio_get_volume:function(vlc:libvlc_instance; var
   exception:libvlc_exception):integer; cdecl;
   libvlc_audio_set_volume:procedure(vlc:libvlc_instance;
   volume:integer; var exception:libvlc_exception); cdecl;

   //Other libvlc_video_set_parent:procedure(vlc:libvlc_instance;
   libvlc_drawable_t:integer; var exception:libvlc_exception); cdecl;
   libvlc_video_get_parent:function(vlc:libvlc_instance; var
   exception:libvlc_exception):integer; cdecl;

const
   VLD_SUCCESS = 0; VLD_NOLIB = -1; VLD_NOTFOUND = -2;

// load libvlc.dll (get Install path from registry) function
VLD_LoadLibrary:integer; // return Install path found in registry by
VLD_LoadLibrary function VLD_LibPath:string; // return libvlc.dll proc
adress function VLD_GetProcAddress(Name:pchar; var
addr:pointer):integer; // return (and clear) last VLD error function
VLD_LastError:integer; // load everything (dll & procs) and return last
VLD error function VLD_Startup:integer;

{$ENDIF}

implementation

{$IFNDEF STATIC}

uses
   Windows;

var
   LibVLCHandle: THandle = 0; LibPath: string; LastError: integer =
   VLD_SUCCESS; VLCLibLoaded: boolean = false;

function GetLibPath: boolean; var Handle: HKEY; RegType: integer;
DataSize: integer; begin Result := False; if
(RegOpenKeyEx(HKEY_LOCAL_MACHINE, 'SoftwareVideoLANVLC', 0,
KEY_ALL_ACCESS, Handle) = ERROR_SUCCESS) then begin if
RegQueryValueEx(Handle, 'InstallDir', nil, @RegType, nil, @DataSize) =
ERROR_SUCCESS then begin SetLength(LibPath, Datasize);
RegQueryValueEx(Handle, 'InstallDir', nil, @RegType, PByte(@LibPath[1]),
@DataSize); LibPath[DataSize] := ''; Result := True; end;
RegCloseKey(Handle); end; end;

function VLD_LibPath: string; begin if LibPath = '' then getLibPath;
Result := LibPath; end;

function VLD_LoadLibrary:integer; begin if LibVLCHandle = 0 then begin
LibVLCHandle := LoadLibrary(LibName); if (LibVLCHandle = 0) and
(getLibPath) then LibVLCHandle := LoadLibrary(PChar(LibPath + LibName));
end;

   if LibVLCHandle <> 0 then
      Result := VLD_SUCCESS

   else begin LastError := VLD_NOLIB; Result := LastError; end;

end;

function VLD_GetProcAddress(Name: PChar; var Addr: Pointer): Integer;
begin if LibVLCHandle = 0 then begin Result := VLD_LoadLibrary; if
Result <> VLD_SUCCESS then exit; end;

   Addr := GetProcAddress(LibVLCHandle, Name); if Addr <> nil then
   Result := VLD_SUCCESS else begin LastError := VLD_NOTFOUND; Result :=
   LastError; end;

end;

function VLD_LastError: Integer; begin Result := LastError; LastError :=
VLD_SUCCESS; end;

function VLD_Startup: Integer; begin LastError := VLD_SUCCESS; if
VLD_LoadLibrary = VLD_SUCCESS then begin
VLD_GetProcAddress('libvlc_new', @libvlc_new);
VLD_GetProcAddress('libvlc_destroy', @libvlc_destroy);
VLD_GetProcAddress('libvlc_exception_clear', @libvlc_exception_clear);
VLD_GetProcAddress('libvlc_playlist_add', @libvlc_playlist_add);
VLD_GetProcAddress('libvlc_playlist_add_extended',
@libvlc_playlist_add_extended);
VLD_GetProcAddress('libvlc_playlist_clear', @libvlc_playlist_clear);
VLD_GetProcAddress('libvlc_playlist_items_count',
@libvlc_playlist_items_count);
VLD_GetProcAddress('libvlc_playlist_isplaying',
@libvlc_playlist_isplaying); VLD_GetProcAddress('libvlc_playlist_play',
@libvlc_playlist_play); VLD_GetProcAddress('libvlc_playlist_pause',
@libvlc_playlist_pause); VLD_GetProcAddress('libvlc_playlist_stop',
@libvlc_playlist_stop); VLD_GetProcAddress('libvlc_playlist_next',
@libvlc_playlist_next); VLD_GetProcAddress('libvlc_playlist_prev',
@libvlc_playlist_prev); VLD_GetProcAddress('libvlc_playlist_get_input',
@libvlc_playlist_get_input); VLD_GetProcAddress('libvlc_input_free',
@libvlc_input_free); VLD_GetProcAddress('libvlc_input_get_length',
@libvlc_input_get_length); VLD_GetProcAddress('libvlc_input_get_time',
@libvlc_input_get_time); VLD_GetProcAddress('libvlc_input_get_position',
@libvlc_input_get_position);
VLD_GetProcAddress('libvlc_toggle_fullscreen',
@libvlc_toggle_fullscreen); VLD_GetProcAddress('libvlc_set_fullscreen',
@libvlc_set_fullscreen); VLD_GetProcAddress('libvlc_get_fullscreen',
@libvlc_get_fullscreen); VLD_GetProcAddress('libvlc_video_get_width',
@libvlc_video_get_width); VLD_GetProcAddress('libvlc_video_get_height',
@libvlc_video_get_height); VLD_GetProcAddress('libvlc_audio_get_mute',
@libvlc_audio_get_mute); VLD_GetProcAddress('libvlc_audio_set_mute',
@libvlc_audio_set_mute); VLD_GetProcAddress('libvlc_audio_get_volume',
@libvlc_audio_get_volume); VLD_GetProcAddress('libvlc_audio_set_volume',
@libvlc_audio_set_volume);

   VLD_GetProcAddress('libvlc_video_set_parent',
   @libvlc_video_set_parent);

// VLD_GetProcAddress('libvlc_video_get_parent', @libvlc_video_get_parent);
   VLCLibLoaded := true;

end;
   Result := LastError;

end; {$ENDIF}

end. </syntaxhighlight>

[[Category:Bindings]] [[Category:libVLC]]
