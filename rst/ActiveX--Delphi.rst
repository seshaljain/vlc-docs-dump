.. raw:: mediawiki

   {{See also|Using libvlc with Delphi}}

.. raw:: mediawiki

   {{howto| use the [[ActiveX]] control with Delphi|nosort=yes}}

Getting started
---------------

What you need
~~~~~~~~~~~~~

-  Borland Delphi 3 or newer
-  a running System with Microsoft Windows
-  `The VideoLan Client <http://www.videolan.org/>`__ (VLC) including the `ActiveX <ActiveX>`__ Plugin installed

Import the ActiveX-Component
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Start your Borland Delphi
-  < Delphi2005: Select Components --> Import ActiveX --> VideoLan VLC ActiveX Plugin
-  >= Delphi 2006: Select Components --> Import component --> Import ActiveX Control --> VideoLan VLC ActiveX Plugin
-  Otherwise try creating a new package using the created *AXVLC_TLB.pas*

Confirm successfull installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  You should now be able to add the *TVLCPlugin* from the ActiveX-Tab of your Component toolbox.

Usage Development-Time
----------------------

The VLC-Player Object *TVLCPlugin* can be found in your ActiveX-Components Tabsheet. Place one of it in your Form1, place a TButton and use the following code:

.. code:: delphi

    unit Unit1;
    
    interface
    
    uses
      Windows, Variants, Forms, Classes, Controls, StdCtrls, OleCtrls,
      AXVLC_TLB;
    
    type
      TForm1 = class(TForm)
        VLCPlugin1: TVLCPlugin;
        Button1: TButton;
        procedure Button1Click(Sender: TObject);
      private
        { Private-Deklarationen }
      public
        { Public-Deklarationen }
      end;
    
    type
      VLCPlaylistMode = TOleEnum;
    
    const
      VLCPlayListInsert      = $00000001;
      VLCPlayListReplace     = $00000002;
      VLCPlayListAppend      = $00000004;
      VLCPlayListGo          = $00000008;
      VLCPlayListCheckInsert = $00000010;
    
    var
      Form1: TForm1;
    
    implementation
    
    {$R *.dfm}
    
    procedure TForm1.Button1Click(Sender: TObject);
    begin
      VLCPlugin1.addTarget('C:\video.mpg', null, VLCPlayListInsert, 0);
      // you can use any MRL with parameters instead of 'c:\video.mpg' here
      VLCPlugin1.play;
    end;
    
    end.

Usage Runtime
-------------

If you're planning to use the VLC-Player in your application but don't know when and where, use this code to create the component on-demand.

.. code:: delphi

    unit Unit1;
    
    interface
    
    uses
      Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms, OleCtrls,
      AXVLC_TLB, StdCtrls, Registry, Dialogs;
    
    type
      TForm1 = class(TForm)
        Button1: TButton;
        Button2: TButton;
        procedure Button2Click(Sender: TObject);
        procedure Button1Click(Sender: TObject);
      private
        { Private-Deklarationen }
      public
        { Public-Deklarationen }
      end;
    
    var
      Form1: TForm1;
      VLCPlugin1: TVLCPlugin;
      blVLCPluginFound: boolean;
    
    type
      VLCPlaylistMode = TOleEnum;
    
    const
      VLCPlayListInsert      = $00000001;
      VLCPlayListReplace     = $00000002;
      VLCPlayListAppend      = $00000004;
      VLCPlayListGo          = $00000008;
      VLCPlayListCheckInsert = $00000010;
    
    implementation
    
    {$R *.dfm}
    
    procedure TForm1.Button1Click(Sender: TObject);
    var
      Reg: TRegistry;
    begin
      blVLCPluginFound := false;
    
      // Is VLC ActiveX Plugin installed on this PC?
      Reg := TRegistry.Create;
      try
        Reg.RootKey := HKEY_LOCAL_MACHINE;
        if Reg.OpenKeyReadOnly('\Software\Classes\VideoLAN.VLCPlugin.1\') then begin
            blVLCPluginFound := true;
        end;
      finally
        FreeAndNil(Reg);
      end;
    
      if blVLCPluginFound then begin
        VLCPlugin1 := TVLCPlugin.Create(Self);
        VLCPlugin1.Parent := Self; // Means: Place the VLC-Player into Form1
        VLCPlugin1.Width  := 400;
        VLCPlugin1.Height := 300;
        VLCPlugin1.Top  := 50;
        VLCPlugin1.Left := 50;
        VLCPlugin1.Show;
        VLCPlugin1.addTarget('C:\video.mpg', null, VLCPlayListInsert, 0);
        // you can use any MRL with parameters instead of 'c:\video.mpg' here
        VLCPlugin1.play;
      end else begin
        ShowMessage('I am really sorry, but VLC (or its ActiveX Plugin) is currently not installed on this PC!');
      end;
    end;
    
    procedure TForm1.Button2Click(Sender: TObject);
    begin
      if blVLCPluginFound then begin
        VLCPlugin1.stop;
        FreeAndNil(VLCPlugin1);
      end;
    end;
    
    end.

Alternative way to bring VLC to your Delphi Application
-------------------------------------------------------

Much easier way to bring VLC to your Delphi Application is to paste a TWebbrowser Object in your Form, is generate Code for the HTML and m3u file and let the Webbrowser load the HTML-file. For detailed information have a look at `ActiveX/HTML <ActiveX/HTML>`__.

You can also use `LibVLC <LibVLC>`__ like in `VideoLAN for Delphi <http://tothpaul.free.fr/sources.php?dprgrp.vld>`__.

See also
--------

`ActiveX/HTML <ActiveX/HTML>`__
