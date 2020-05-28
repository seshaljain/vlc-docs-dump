.. raw:: mediawiki

   {{Historical}}

.. raw:: mediawiki

   {{Lowercase}}

Intro
-----

Although vlc is moving `away <Qt_and_GTK>`__ from wxwidgets this is an attemp to move wxwidgets towards vlc (libvlc to be more precise).. The libvlc API is fairly new and VERY promissing.. It exports ALL the functionality of vlc into a nice c API . On the other hand wxWidgets is a very rich `1 <http://www.wxwidgets.org/docs/hierarchy_stable_image.htm>`__ ( and also community based ) growing X platform library. It covers the 3 basic platforms (MSW, LINUX, MAC) and more\ `2 <http://wiki.wxwidgets.org/Supported_Platforms>`__..

wxVLCBackend
------------

wxVLCBackend v2 is a wxMediaCtrl backend. The latter is a stub media player in wxWidgets and provides an interface for various kinds of backends (gssteamer, wmp,...). wxVLCBackend maybe integrated in the official wxwidgets code.. The backend code provides a guide to integrade libvlc in other c/c++ gui frameworks as well. In fact the only TRICKY part was to get a low-level hadle for the drawable surface.

**Right now** (29/10/08) The code is not mature enough for publication. There are some stability issues. To correct them i've created a mini (Poc) wxWidgets based app to isolate these issues, wxvlc_test.

wxvlc_test
----------

wxvlc_test is a simple wxWidgets based app. It has a textbox where you give a media filename and a play, stop button to control playback. In my tests wxvlc_test **crashes** when starting playing ( somewhere inside libavcodec library with no other dubuging symbols ) \*some\* avis.. On the other hand vlc plays these same files smoothly.

-  

   -  Tests were done on vlc-0.9.5

My intentions for this publication are : a) to test the glue code on other systems ( my tests are on **linux ONLY** so dont ask me, but windows could be tested too ) b) to check the glue code correctness by a vlc internalls well-knower (maybe i miss something, cause i cant explain that libavcodec crashes)

Information for wxvlc_test is provided in the README as well

wxvlc_test v0.1 source
~~~~~~~~~~~~~~~~~~~~~~

The program is provided under patch format here. Copy and paste the following to a new patch file ( say wxvlc.patch) and "apply" it with patch -Np0 < ../wxvlc.patch this will create a new dir with all the needed files inside

::

   diff -Nur wxvlc_test-0.1/Makefile wxvlc_test/Makefile
   --- wxvlc_test-0.1/Makefile 1970-01-01 02:00:00.000000000 +0200
   +++ wxvlc_test/Makefile 2008-10-28 12:09:10.000000000 +0200
   @@ -0,0 +1,44 @@
   +
   +CC = g++
   +CFLAGS += -O2 -g -Wall
   +# vlc incs should be on the system (at least for GTK )
   +INCS = `wx-config --cflags`
   +# <------------ MOD HERE
   +# xtra incs for the gtk build.... Don't know know how to contitionaly compile.. Comment out on non gtk platforms
   +INCS +=    -I/usr/include/gtk-2.0 \
   +       -I/usr/include/pango-1.0 \
   +       -I/usr/include/cairo \
   +       -I/usr/include/glib-2.0 \
   +       -I/usr/lib/glib-2.0/include \
   +       -I/usr/lib/gtk-2.0/include \
   +       -I/usr/include/atk-1.0
   +
   +LIBS = `wx-config --libs` -lvlc
   +OBJS = test2App.o test2Main.o vlc_bind.o
   +DEFS = 
   +
   +###########################################################################
   +
   +# it is first and executed by default
   +default: wxvlc_test
   +
   +all: wxvlc_test
   +
   +##### libraries
   +
   +wxvlc_test: $(OBJS) 
   +   $(CC) $(CFLAGS) $(DEFS) $(INCS) $(OBJS) $(LIBS) -o wxvlc_test
   +
   +# Make the o's out of c's
   +# $< she who initiated the implicit actions
   +# $* prefix shared by taget and deps
   +# c.o  c <= depends on <= o
   +.cpp.o: $*.h
   +   $(CC) $(CFLAGS) $(DEFS) $(INCS) -c $< -o $@
   +
   +
   +# Clean target
   +clean:
   +   rm -f *.[o] 
   +
   +
   diff -Nur wxvlc_test-0.1/README wxvlc_test/README
   --- wxvlc_test-0.1/README   1970-01-01 02:00:00.000000000 +0200
   +++ wxvlc_test/README   2008-10-28 12:38:54.000000000 +0200
   @@ -0,0 +1,29 @@
   +-- INTRO
   +wxvlc_test v0.1
   +
   +This is a mini library for libvlc integration into wxWidgets apps . Its a poC
   + and is intented to test it for stability. It is part of the wxVLCMediaBackend v2
   + for integration into wxMediaCtrl as a Bakend...[It is not published yet (10.08)] 
   +
   +
   +--USAGE
   +-Make sure you have wxWIdgets 2.8 installed (don't know for later versions, 
   +but i think 2.6 should work). 
   +-Make sure you have vlc installed.. Ok we test on linux, so it means libvlc is
   + in path as well as the plugins. 
   + You need to comment some lines at Makefile ( Noted) for windows and make 
   + sure the linker can "see"  libvlc.dll. It is not tested so don't ask me .
   +
   +$make
   +$./wxvlc_test
   +
   +
   +--ISSUES
   +It crashes with some AVI files. Dont know what it is ...
   +
   +
   +-- LIC
   +-this code is left to the "public" as is without ANY waranty, the authors CANNOT be
   +   held responsible if it blows your house or something...  
   +
   +   basos    2008    < noxelia 4t gmail c0m >
   diff -Nur wxvlc_test-0.1/test2App.cpp wxvlc_test/test2App.cpp
   --- wxvlc_test-0.1/test2App.cpp 1970-01-01 02:00:00.000000000 +0200
   +++ wxvlc_test/test2App.cpp 2008-11-08 20:06:37.000000000 +0200
   @@ -0,0 +1,64 @@
   +/***************************************************************

   + * Name:      test2App.cpp

   + * Purpose:   Code for Application Class

   + * Author:    basOS

   + * Created:   2008-07-05

   + * Copyright: basOS ()

   + * License:

   + **************************************************************/

   +

   +#ifdef WX_PRECOMP

   +#include "wx_pch.h"

   +#endif

   +

   +#ifdef __BORLANDC__

   +#pragma hdrstop

   +#endif //__BORLANDC__

   +

   +#include "test2App.h"

   +#include "test2Main.h"

   +#include "wx/cmdline.h"     //for wxCmdLineParser (optional)

   +

   +IMPLEMENT_APP(appVlctest)

   +

   +

   +bool appVlctest::OnInit()

   +{
   +   wxString filename ;

   +#if wxUSE_CMDLINE_PARSER
   +    //
   +    //  What this does is get all the command line arguments
   +    //  and treat each one as a file to put to the initial playlist
   +    //
   +    wxCmdLineEntryDesc cmdLineDesc[2];
   +    cmdLineDesc[0].kind = wxCMD_LINE_PARAM;
   +    cmdLineDesc[0].shortName = NULL;
   +    cmdLineDesc[0].longName = NULL;
   +    cmdLineDesc[0].description = wxT("input files");
   +    cmdLineDesc[0].type = wxCMD_LINE_VAL_STRING;
   +    cmdLineDesc[0].flags = wxCMD_LINE_PARAM_OPTIONAL | wxCMD_LINE_PARAM_MULTIPLE;
   +
   +    cmdLineDesc[1].kind = wxCMD_LINE_NONE;
   +
   +    //gets the passed media files from cmd line
   +    wxCmdLineParser parser (cmdLineDesc, argc, argv);
   +
   +    // get filenames from the commandline
   +    if (parser.Parse() == 0)
   +    {
   +        for (size_t paramNr=0; paramNr < parser.GetParamCount(); ++paramNr)
   +        {
   +            filename = parser.GetParam (paramNr) ;
   +           break ;
   +        }
   +    }
   +#endif 
   +

   +    f_main *frame  = new f_main( _T("Vlc test app"), wxPoint(50,150),wxSize(450,390));
   +   frame->filename = filename ;
   +    frame->Show(TRUE);

   +    SetTopWindow(frame);

   +

   +    return TRUE;

   +}

   +
   diff -Nur wxvlc_test-0.1/test2App.h wxvlc_test/test2App.h
   --- wxvlc_test-0.1/test2App.h   1970-01-01 02:00:00.000000000 +0200
   +++ wxvlc_test/test2App.h   2008-11-08 20:06:36.000000000 +0200
   @@ -0,0 +1,26 @@
   +/***************************************************************

   + * Name:      test2App.h

   + * Purpose:   Defines Application Class

   + * Author:    basOS 

   + * Created:   2008-07-05

   + * Copyright: basOS ()

   + * License:

   + **************************************************************/

   +

   +#ifndef TEST2APP_H

   +#define TEST2APP_H

   +

   +#include <wx/app.h>

   +

   +

   +

   +class appVlctest : public wxApp

   +{

   +    wxIcon* ic_app;

   +    virtual bool OnInit();

   +

   +    protected:


   +};

   +

   +

   +#endif // TEST2APP_H
   diff -Nur wxvlc_test-0.1/test2Main.cpp wxvlc_test/test2Main.cpp
   --- wxvlc_test-0.1/test2Main.cpp    1970-01-01 02:00:00.000000000 +0200
   +++ wxvlc_test/test2Main.cpp    2008-11-08 20:06:35.000000000 +0200
   @@ -0,0 +1,225 @@
   +/***************************************************************

   + * Name:      test2Main.cpp

   + * Purpose:   Code for Application Frame

   + * Author:    basOS

   + * Created:   2008-07-05

   + * Copyright: basOS ()

   + * License:

   + **************************************************************/

   +

   +#ifdef WX_PRECOMP

   +#include "wx_pch.h"

   +#endif

   +

   +#ifdef __BORLANDC__

   +#pragma hdrstop

   +#endif //__BORLANDC__

   +

   +#include "test2Main.h"

   +

   +#include <wx/dir.h>

   +#include <wx/filename.h>
   +#include <wx/debug.h>
   +
   +//#include <wx/filename.h>

   +

   +//helper functions

   +enum wxbuildinfoformat {

   +    short_f, long_f

   +};

   +

   +wxString wxbuildinfo(wxbuildinfoformat format)

   +{

   +    wxString wxbuild(wxVERSION_STRING);

   +

   +    if (format == long_f )

   +    {

   +#if defined(__WXMSW__)

   +        wxbuild << _T("-Windows");

   +#elif defined(__WXMAC__)

   +        wxbuild << _T("-Mac");

   +#elif defined(__UNIX__)

   +        wxbuild << _T("-Linux");

   +#endif

   +

   +#if wxUSE_UNICODE

   +        wxbuild << _T("-Unicode build");

   +#else

   +        wxbuild << _T("-ANSI build");

   +#endif // wxUSE_UNICODE

   +    }

   +

   +    return wxbuild;

   +}

   +

   +

   +   f_main::f_main(const wxString& title, const wxPoint& pos, const wxSize& size)

   +    : wxFrame(0L, -1, title)

   +    {

   +

   +        /*  add menu  */

   +        wxMenu *mnu = new wxMenu;

   +

   +        mnu->Append(ID_ABOUT, _("&About me"),_("Useless information"));

   +        mnu->Append(ID_QUIT, _("Qui&t da app"));

   +

   +        wxMenuBar *mnuB = new wxMenuBar;

   +        mnuB->Append (mnu, _("&Gen") ) ;

   +

   +        // Connect (wxEVT_PAINT,wxPaintEventHandler(f_main::OnPaint));

   +

   +        SetMenuBar (mnuB);

   +

   +        /* add status bar */

   +#if wxUSE_STATUSBAR

   +        CreateStatusBar(2);

   +        SetStatusText(wxbuildinfo(long_f), 1);

   +        SetStatusText ( _("Welcome to a wxwidgeted and vlc proof of concept"),0);

   +#endif

   +

   +        //initialize

   +        bt_capture_label[ON] = _("Stop");

   +        bt_capture_label[OFF] = _("Play");

   +

   +        //design form

   +
   +       wxBoxSizer* bxv1 = new wxBoxSizer( wxVERTICAL );

   +

   +        //create widgets

   +        pn_image = new wxPanel(this,-1,wxPoint(-1,-1),wxSize(250,250));
   +        pn_image->SetBackgroundColour( *wxBLACK ) ;
   +       bxv1->Add( pn_image, 1 ,wxALIGN_CENTER | wxSHAPED | wxALL, 5 );
   +
   +       wxBoxSizer* bxh12 = new wxBoxSizer( wxHORIZONTAL ) ;

   +        bt_cap = new wxButton(this,ID_PLAY,bt_capture_label[OFF]);

   +       bxh12->Add( bt_cap, 0, wxRIGHT, 5 ) ;
   +       wxButton* bt_stop = new wxButton(this, ID_STOP, _T("Stop") ) ;
   +       bxh12->Add( bt_stop, 0 , wxRIGHT, 5 );
   +       
   +       tx_fname = new wxTextCtrl( this, wxID_ANY, filename ) ;
   +       bxh12->Add( tx_fname,1, wxRIGHT, 5 ) ;
   +   
   +       bxv1->Add( bxh12, 0, wxEXPAND | wxALIGN_CENTER | wxALL, 5 );

   +

   +        this->SetSizer(bxv1);

   +        bxv1->SetSizeHints(this);
   +        bxv1->Fit(this) ;
   +
   +       // Backend
   +       //This takes the std out from vlc 
   +       //wxLogDebug(_T("starting up vlc engine...")) ;
   +       if ( vlc_bind( pn_image ) )
   +           wxLogDebug( _T("vlc library initialized ok"));
   +
   +
   +        //event handlers

   +        Connect (ID_ABOUT, wxEVT_COMMAND_MENU_SELECTED,wxCommandEventHandler(f_main::OnAbout));

   +        Connect (ID_QUIT, wxEVT_COMMAND_MENU_SELECTED,wxCommandEventHandler(f_main::OnQuit));

   +        Connect (wxEVT_CLOSE_WINDOW ,wxCloseEventHandler(f_main::OnClose));

   +        Connect (ID_PLAY,wxEVT_COMMAND_BUTTON_CLICKED , wxCommandEventHandler(f_main::OnPlay));
   +        Connect (ID_STOP,wxEVT_COMMAND_BUTTON_CLICKED , wxCommandEventHandler(f_main::OnStop));

   +

   +    }

   +

   +    //Event Handlers

   +

   +    void f_main::OnQuit(wxCommandEvent& WXUNUSED(event))

   +    {

   +       // Close(TRUE);

   +        wxMessageBox (_T("Bye...."),_T("exit"), wxOK | wxICON_HAND, this);
   +       Close() ;

   +    }

   +

   +    void f_main::OnAbout(wxCommandEvent& WXUNUSED(event))

   +    {
   +   #if 0

   +        wxDialog* mss = new wxDialog ((wxWindow*)this,(wxWindowID)-1,_("About Hello W"),wxPoint(-1,-1));

   +

   +

   +        // Create a box sizer

   +        wxBoxSizer* bxv = new wxBoxSizer(wxVERTICAL);

   +        wxBoxSizer* bxh1 = new wxBoxSizer(wxHORIZONTAL);

   +        wxSizer* bxh2 = mss->CreateButtonSizer(wxOK);

   +

   +        // add an icon to theleft and leave 10pxs border to the righ

   +        //wxIcon* icc = new wxIcon(this->GetIcon());

   +        //mss->SetIcon(*icc);

   +        //wxPanel* pic = new wxPanel(mss,-1,wxPoint(-1,-1),wxSize(icc->GetWidth(),icc->GetHeight()));

   +        //pic->Show();

   +        //wxClientDC* dc = new wxClientDC(pic);

   +        //dc->DrawBitmap(*icc,0,0,false);

   +        //bxh1->Add(pic, 0, wxEXPAND |wxALIGN_LEFT| wxRIGHT,10);

   +

   +        //Add a text label and leave 10 pxs from right

   +        wxStaticText* txx = new wxStaticText(mss,-1,_("This is a useless but proof of concept first program on wxWidgets programming\n style."

   +        " More on the edge of coding"));

   +        bxh1->Add(txx,1, wxRIGHT,10);

   +

   +        //add two horizontal sizers to the main vertical one

   +        bxv->Add(bxh1,1,wxBOTTOM | wxEXPAND,10); // add 10px border bottom

   +        bxv->Add(bxh2,1);

   +

   +        //Set the sizer to the dialog box

   +        mss->SetSizer(bxv);

   +

   +        //show da dialogi

   +        mss->ShowModal();

   +   #endif

   +        wxMessageDialog msg(this,_T("This is a useless but proof of concept first program on wxWidgets programming\n style."

   +        " More on the edge of coding"),_T("About Hello W"), wxOK);

   +        //wxIcon c_app_icon(wxICON(damage_smile));

   +        //msg.SetIcon(c_app_icon);

   +

   +        msg.ShowModal();

   +        

   +        //delete ics;

   +    }

   +

   +     void f_main::OnPlay(wxCommandEvent& WXUNUSED(event))

   +    {
   +
   +       wxString filename;
   +       filename = tx_fname->GetValue() ;
   +       if ( filename == _T("")) {
   +           wxLogError( _T("Empty text file") );
   +           return ;
   +       }
   +       if (!wxFileName::FileExists( filename) ) {
   +           wxLogError( _T("File %s does not exist"), filename.c_str() );
   +           return ;
   +       }
   +

   +        vlc_load( filename);
   +       wxMilliSleep( 1000* 1.5 );
   +       vlc_play() ;

   +    }
   +
   +     void f_main::OnStop(wxCommandEvent& WXUNUSED(event))

   +    {
   +       vlc_stop() ;
   +   }

   +

   + 

   +    void f_main::OnClose(wxCloseEvent& event)

   +    {

   +        if (event.CanVeto()) {

   +            //could ask user here

   +            //could avoid destr and call event.Veto();

   +            // and return

   +        }

   +

   +    /*    list_object_t::iterator iter;

   +        wxObject * tobj;

   +        for (iter = garbage_col.begin(); iter != garbage_col.end(); ++iter) {

   +            //make clean TM

   +            //List of type wxObjects. It stores pointer to objects so iter is a pointer to object

   +            tobj = *iter;

   +            delete(tobj);

   +        }
   +    */
   +       vlc_shut() ;

   +        this->Destroy();

   +

   +    }

   +

   +

   diff -Nur wxvlc_test-0.1/test2Main.h wxvlc_test/test2Main.h
   --- wxvlc_test-0.1/test2Main.h  1970-01-01 02:00:00.000000000 +0200
   +++ wxvlc_test/test2Main.h  2008-11-08 20:06:35.000000000 +0200
   @@ -0,0 +1,63 @@
   +/***************************************************************

   + * Name:      test2Main.h

   + * Purpose:   Defines Application Frame

   + * Author:    basOS 

   + * Created:   2008-07-05

   + * Copyright: basOS ()

   + * License:

   + **************************************************************/

   +

   +#ifndef TEST2MAIN_H

   +#define TEST2MAIN_H

   +

   +#ifndef WX_PRECOMP

   +    #include <wx/wx.h>

   +#endif

   +

   +#include "test2App.h"
   +#include "vlc_bind.h"
   +

   +

   +class f_main : public wxFrame

   +{

   +    public:

   +   wxString filename ;
   +

   +    f_main(const wxString& title, const wxPoint& pos, const wxSize& size);

   +

   +    private:

   +    enum {

   +        ID_QUIT ,

   +        ID_ABOUT,

   +        ID_PLAY,
   +       ID_STOP,

   +    };

   +

   +    //Event Handlers

   +

   +    void OnQuit(wxCommandEvent& WXUNUSED(event));

   +

   +    void OnAbout(wxCommandEvent& WXUNUSED(event));

   +

   +    void OnPlay(wxCommandEvent& event);
   +
   +    void OnStop(wxCommandEvent& event);

   +

   +    void OnClose(wxCloseEvent& event);

   +    //other

   +    wxString bt_capture_label[2];

   +    enum cap_state {

   +        ON = 0,

   +        OFF

   +    };
   +

   +    wxPanel* pn_image ;

   +    wxButton* bt_cap;
   +   wxTextCtrl* tx_fname ;

   +

   +    // garbage collector list

   +    //list_object_t garbage_col;

   +};

   +

   +

   +#endif // TEST2MAIN_H
   diff -Nur wxvlc_test-0.1/vlc_bind.cpp wxvlc_test/vlc_bind.cpp
   --- wxvlc_test-0.1/vlc_bind.cpp 1970-01-01 02:00:00.000000000 +0200
   +++ wxvlc_test/vlc_bind.cpp 2008-10-28 12:01:52.000000000 +0200
   @@ -0,0 +1,271 @@
   +#if 1
   +/* mini library for libvlc integration into wxWidgets apps 
   +   part of the wxVLCMediaBackend v2...  
   +    this code is left to the "public"   
   +   basos    2008    < noxelia 4t gmail c0m >
   +*/
   +
   +//#include <wx/dynlib.h>

   +//#include "test2Main.h"
   +#include <wx/string.h>
   +#include <wx/window.h>
   +#include <wx/log.h>
   +#include <wx/app.h>

   +#include <stdio.h>

   +#include <stdlib.h>

   +

   +#include <vlc/vlc.h>

   +
   +/* ** HACKS FOR WINDOW HANDLE **/
   +#ifdef __WXGTK__ 
   + #    include <gdk/gdkx.h> // GDK_WINDOW_XWINDOW is found here in wxWidgets 2.8.0
   + #    include "gdk/gdkprivate.h"
   + #if wxCHECK_VERSION(2, 8, 0)
   +  #ifdef __WXGTK20__
   +   #include <wx/gtk/win_gtk.h>
   +  #else
   +   #include <wx/gtk1/win_gtk.h>
   +  #endif
   + #else
   +  #include <wx/gtk/win_gtk.h>
   + #endif
   + #define GetXWindow(wxwin) (wxwin)->m_wxwindow ? \
   +                          GDK_WINDOW_XWINDOW(GTK_PIZZA((wxwin)->m_wxwindow)->bin_window) : \
   +                          GDK_WINDOW_XWINDOW((wxwin)->m_widget->window)
   +#endif
   +
   +
   +// GLOBALS
   +static libvlc_instance_t * inst = NULL;

   +static libvlc_media_player_t *mp = NULL;
   +

   +static void raisee (libvlc_exception_t * ex, wxString desc = _T(""))

   +{

   +    //if ((*pfnlibvlc_exception_raised) (ex))

   +    if (libvlc_exception_raised (ex))

   +    {

   +        wxString ss;

   +        const char * resp;

   +        wxCSConv mag(_T("ISO-8859-1"));

   +        resp = libvlc_exception_get_message(ex);

   +        //resp = (*pfnlibvlc_exception_get_message)(ex);

   +        wxString sex(resp, mag);

   +        ss.Printf(_T("Exeption error: %s : %s\n"),sex.c_str(), desc.c_str());

   +        //ss.Printf(_T("Exeption error: %s\n"),resp);

   +        wxLogError (ss);

   +

   +        wxExit ();

   +    }

   +}

   +
   +//Given the Low Level id (yes XID cuases the mess ) hook et up
   +void HookVideoWindow( libvlc_media_player_t* libvlc_mp, libvlc_drawable_t hwin)
   +{
   +    
   +    libvlc_exception_t ex ;
   +    libvlc_exception_init (&ex);
   +
   +   libvlc_media_player_set_drawable ( libvlc_mp, hwin, &ex );
   +   
   +}
   +
   +#ifdef __WXGTK__ //be it versions 1 or 2 ...
   +void GtkWindowRealized(GtkWidget* wid, libvlc_media_player_t* mp)
   +{
   +    libvlc_drawable_t xid = GDK_WINDOW_XWINDOW( GTK_PIZZA(wid)->bin_window );
   +    wxLogDebug(_T("wxVLCBackend::GtkRealization Callback wid=%x, **pizza=%x, XDrawable=%x"),
   +            wid,
   +            GTK_PIZZA( wid)->bin_window,
   +            xid );
   +    wxASSERT( xid );
   +    HookVideoWindow(mp, xid );
   +}
   +#endif
   +
   +
   +
   +bool vlc_load( wxString media )
   +{
   +   wxASSERT( mp );
   +    libvlc_exception_t ex ;
   +    libvlc_exception_init (&ex);
   +   
   +   const char * filename;
   +   wxCSConv convertor = wxConvLocal ;
   +    int i_tsiz = (media.Length() + 1) ;
   +    char* psz_tbuf = malloc( i_tsiz * sizeof(char) );
   +    wxCHECK( psz_tbuf, false ) ; //on error return false
   +    strncpy( psz_tbuf, media.mb_str( convertor ), i_tsiz );
   +   filename = psz_tbuf ;
   +   
   +    libvlc_media_t *m;
   +    /* Create a new item */

   +    //m = (*pfnlibvlc_media_new) (inst, filename, &ex);

   +    m = libvlc_media_new (inst, filename, &ex);

   +    raisee (&ex, _T("media new"));
   +
   +   //internally retain
   +   libvlc_media_player_set_media( mp, m, &ex );
   +   raisee( &ex, _T("media player set media")) ;
   +
   +    /* No need to keep the media now */

   +    //(*pfnlibvlc_media_release) (m);

   +    libvlc_media_release (m);
   +
   +    /* play the media_player */

   +   //(*pfnlibvlc_media_player_play) ( mp, &ex);

   +   return true ;
   +}
   +
   +void vlc_shut()
   +{
   +   if (mp)
   +       libvlc_media_player_release( mp );
   +   mp = NULL ;
   +   if ( inst )
   +       libvlc_release( inst ); 
   +   inst = NULL ;
   +}
   +
   +bool vlc_stop()
   +{
   +   wxASSERT( mp );
   +    libvlc_exception_t ex ;
   +
   +    libvlc_exception_init (&ex);
   +    libvlc_media_player_stop ( mp, &ex);

   +    raisee ( &ex, _T("media player stop"));
   +
   +   return true ;
   +}
   +
   +   
   +bool vlc_play()
   +{
   +   wxASSERT( mp );
   +    libvlc_exception_t ex ;
   +    libvlc_exception_init (&ex);
   +   libvlc_media_player_play ( mp, &ex);

   +   raisee ( &ex, _T("media player play"));
   +
   +   return true ;
   +}
   +

   +bool vlc_bind( wxWindow* output )

   +{

   +

   +   /* if (!libvlc.IsLoaded()) {

   +        wxLogError( _T("error: link lib"));

   +        return false;

   +    }*/

   +

   +     const char * const vlc_args[] = {

   +              "-I", "dummy", // Don't use any interface

   +              //"--no-dummy-quiet", // do not use a dos box

   +              //"--module-path=/set/your/path/to/libvlc/module/if/you/are/on/windows/or/macosx"

   +              };

   +    libvlc_exception_t ex ;
   +    //libvlc_instance_t * inst;

   +
   +    //libvlc_media_player_t *mp;

   +

   +

   +    libvlc_exception_init (&ex);

   +    //(*pfnlibvlc_exception_init) (&ex);

   +    /* init vlc modules, should be done only once */

   +    //inst = (*pfnlibvlc_new) (sizeof(vlc_args) / sizeof(vlc_args[0]), vlc_args, &ex);

   +    inst = libvlc_new (sizeof(vlc_args) / sizeof(vlc_args[0]), vlc_args, &ex);

   +    raisee (&ex);

   +

   +

   +

   +    /* Create a media player playing environement */

   +    //mp = (*pfnlibvlc_media_player_new_from_media) (m, &ex);

   +    mp = libvlc_media_player_new (inst, &ex);

   +    raisee (&ex,_T("media player new"));

   +

   +    /** TRICKY ** DIRTY ** NASTY ** HACK
   +      * Get a window's drawable surface. Low level handle::
   +      * MSW::HWND / GTK::XID / MAC::
   +      * Taken from wxVTK AND **GSTREAMER** Implemtation for wxWidgets
   +      */

   +   #if defined(__WXGTK__)
   +       if(!GTK_WIDGET_REALIZED(output->m_wxwindow)) {
   +           /** MOST TRICKY**
   +             * If the GtkWidget is not drawn on the screen yet it is not assigned an XID
   +             */
   +           //Not realized yet - set to connect at realization time
   +           g_signal_connect (output->m_wxwindow,
   +                                 "realize",
   +                                 G_CALLBACK (GtkWindowRealized),
   +                                 mp);
   +           wxLogDebug(_T("VLCBackend::Init GTK window Pizza for Gtkwidget %x not yet alive. Hooking a callback"), output->m_wxwindow );
   +           /*
   +           wxLogError ( _T(" ERROR: GTK windows Pizza for Gtkwidget not yet alive... Not hooking a Callback. Make sure the window is shown on the screen... Exiting..."));
   +           return false ;
   +           */
   +       }
   +       else
   +   #endif
   +   #if defined (__WXGTK__) || defined (__WXX11__)
   +           HookVideoWindow( mp, GetXWindow(output) ) ;
   +   #else
   +       HookVideoWindow( mp, output->GetHandle() ) ;
   +   #endif
   +
   +

   +

   +

   +

   +    //Sleep (10); /* Let it play a bit */

   +    //wxMilliSleep ( 20*1000);

   +

   +    /* Stop playing */

   +    //(*pfnlibvlc_media_player_stop) (mp, &ex);

   +

   +    /* Free the media_player */

   +    //(*pfnlibvlc_media_player_release) (mp);

   +

   +    //(*pfnlibvlc_destroy) (inst);

   +    //raisee (&ex);

   +

   +    return true;

   +}
   +
   +/*

   +wxDynamicLibrary libvlc(_T("libvlc"));

   +wxDynamicLibrary libvlccore(_T("libvlccore"));

   +

   +    typedef int (*ex_raised_t)(libvlc_exception_t *);

   +    wxDYNLIB_FUNCTION ( ex_raised_t, libvlc_exception_raised, libvlc );

   +    typedef char* (*ex_message_t)(libvlc_exception_t *);

   +    wxDYNLIB_FUNCTION ( ex_message_t , libvlc_exception_get_message , libvlc);

   +

   +    typedef void (*ex_init_t)(libvlc_exception_t*);

   +    wxDYNLIB_FUNCTION ( ex_init_t, libvlc_exception_init, libvlc );

   +    typedef  libvlc_instance_t * (*lib_new_t)(int,char* const *,libvlc_exception_t*);

   +    wxDYNLIB_FUNCTION ( lib_new_t, libvlc_new, libvlc );

   +    //typedef int (*play_add_t)( libvlc_instance_t *, const char *, const char *, libvlc_exception_t * );

   +    //wxDYNLIB_FUNCTION ( play_add_t, libvlc_playlist_add ,libvlc);

   +    //typedef void (*play_play_t)( libvlc_instance_t*, int, int, char **,libvlc_exception_t * );

   +    //wxDYNLIB_FUNCTION ( play_play_t, libvlc_playlist_play, libvlc);

   +    //typedef void (*vid_set_t)( libvlc_instance_t *, libvlc_drawable_t, libvlc_exception_t * );

   +    //wxDYNLIB_FUNCTION ( vid_set_t, libvlc_video_set_parent, libvlc);

   +    typedef int (*drawable_t)  ( libvlc_media_player_t *, libvlc_drawable_t, libvlc_exception_t * );

   +    wxDYNLIB_FUNCTION (drawable_t, libvlc_media_player_set_drawable, libvlc);

   +    typedef int (*lib_dest_t)(libvlc_instance_t*);

   +    wxDYNLIB_FUNCTION ( lib_dest_t, libvlc_destroy ,libvlc);

   +

   +    typedef libvlc_media_t* (*media_new_t)(libvlc_instance_t*, const char* , libvlc_exception_t*);

   +    wxDYNLIB_FUNCTION ( media_new_t, libvlc_media_new, libvlc);

   +    typedef void (*media_release_t)(libvlc_media_t*);

   +    wxDYNLIB_FUNCTION (media_release_t, libvlc_media_release, libvlc);

   +    typedef void (*mplay_play_t)(libvlc_media_player_t*, libvlc_exception_t*);

   +    wxDYNLIB_FUNCTION (mplay_play_t, libvlc_media_player_play, libvlc);

   +    typedef libvlc_media_player_t* (*mplayer_med_t)(libvlc_media_t*, libvlc_exception_t*);

   +    wxDYNLIB_FUNCTION (mplayer_med_t, libvlc_media_player_new_from_media, libvlc);

   +    typedef void (*mplayer_stop_t)(libvlc_media_player_t*, libvlc_exception_t*);

   +    wxDYNLIB_FUNCTION (mplayer_stop_t, libvlc_media_player_stop, libvlc);

   +*/
   +
   +#endif

   diff -Nur wxvlc_test-0.1/vlc_bind.h wxvlc_test/vlc_bind.h
   --- wxvlc_test-0.1/vlc_bind.h   1970-01-01 02:00:00.000000000 +0200
   +++ wxvlc_test/vlc_bind.h   2008-10-28 11:53:02.000000000 +0200
   @@ -0,0 +1,18 @@
   +/* mini library for libvlc integration into wxWidgets apps 
   +   part of the wxVLCMediaBackend v2...  
   +    this code is left to the "public"   
   +   basos    2008    < noxelia 4t gmail c0m >
   +*/
   +
   +#include <wx/string.h>
   +#include <wx/window.h>
   +
   +//prototype for vlc test func 

   +bool vlc_load(wxString media );
   +bool vlc_play() ;
   +bool vlc_bind(wxWindow*) ;
   +void vlc_shut() ;
   +bool vlc_stop() ;
   +
   +
   +

`Category:Bindings <Category:Bindings>`__
