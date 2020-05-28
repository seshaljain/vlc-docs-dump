{{Lowercase}} {{Example code|for=libVLC}} {{Outdated}}

This sample code will render a video into a Qt QWidget.

This was tested with vlc-0.9.9 and Qt 4.5.1 on WinXP and Linux

This was tested with vlc-1.1.9 and Qt 4.7.2 and Ubuntu 11.04

== How to use? ==

You need [[LibVLC|''libvlc headers'']] and ''Qt headers''.Take those 3
files, put them in a folder. Run qmake -project

Edit the .pro file and add
   LIBS += -L*path to vlc lib\* #if you are at windows os LIBS += -lvlc

Run
   qmake

and then
   make or mingw32-make under a Windows OS

On win os you have to use the zip file. the lib and the header files are
located in the sdk-folder.

== Notes ==

Depending on your distribution and the way you install Qt and Vlc it may be a good idea to reset the vlc's module cache:
   sudo /usr/lib/vlc/vlc-cache-gen -f /usr/lib/vlc/plugins/

or:
   vlc --reset-plugins-cache

== VLC 1.1.5 and Ubuntu Lucid == [Rafael
Capucho<rafael.capucho@gmail.com> 20120713] Modified to include properly
QX11EmbedContainer header that was missing.- tested ok

[Ondrej Spilka 20101201] slightly modified for the modest versions... -
X11 embed container have to be used, therefore QX11EmbedContainer rather
than QFrame have to be used.- tested ok

== Files ==

main.cpp: <syntaxhighlight lang="cpp-qt"> /\* libVLC and Qt sample code
\* Copyright © 2009 Alexander Maringer <maringer@maringer-it.de> \*/

#include "vlc_on_qt.h" #include <QtGui/QApplication>

int main(int argc, char \*argv[]) { QApplication a(argc, argv); Player
p; p.resize(640,480); p.playFile("rtp://@:2626"); // Replace with what
you want to play p.show(); return a.exec(); } </syntaxhighlight>

vlc_on_qt.h: <syntaxhighlight lang="cpp-qt"> /\* libVLC and Qt sample
code \* Copyright © 2009 Alexander Maringer <maringer@maringer-it.de>
\*/ #ifndef VLC_ON_QT_H #define VLC_ON_QT_H

#include <vlc/vlc.h>

#include <QWidget> #include <QX11EmbedContainer>

class QVBoxLayout; class QPushButton; class QTimer; class QFrame; class
QSlider;

#define POSITION_RESOLUTION 10000

class Player : public QWidget { Q_OBJECT QSlider *\_positionSlider;
QSlider*\ \_volumeSlider; // [20101201 Ondra Spilka] // on Linux/Ubuntu
Lucid and VLC >= 1.0 (at least 1.1.5 was tested) XWindow handle have to
be passed // therefore QX11EmbedContainer have to be used instead of
QFrame #ifdef Q_WS_X11 QX11EmbedContainer *\_videoWidget; #else
QFrame*\ \_videoWidget; #endif QTimer *poller; bool \_isPlaying;
libvlc_exception_t \_vlcexcep; libvlc_instance_t*\ \_vlcinstance;
libvlc_media_player_t *\_mp; libvlc_media_t*\ \_m;

public:
   Player(); ~Player(); void raise(libvlc_exception_t \* ex);

public slots:
   void playFile(QString file); void updateInterface(); void
   changeVolume(int newVolume); void changePosition(int newPosition);

}; #endif </syntaxhighlight>

vlc_on_qt.cpp: <syntaxhighlight lang="cpp-qt"> /\* libVLC and Qt sample
code \* Copyright © 2009 Alexander Maringer <maringer@maringer-it.de>
\*/ #include "vlc_on_qt.h"

#include <QX11EmbedContainer> #include <QVBoxLayout> #include
<QPushButton> #include <QSlider> #include <QTimer> #include <QFrame>

Player::Player() : QWidget() { //preparation of the vlc command const
char \* const vlc_args[] = { "--verbose=2", //be much more verbose then
normal for debugging purpose "--plugin-path=C:\vlc-0.9.9-win32\plugins\"
};

#ifdef Q_WS_X11
   \_videoWidget=new QX11EmbedContainer(this);

#else
   \_videoWidget=new QFrame(this);

#endif

   \_volumeSlider=new QSlider(Qt::Horizontal,this);
   \_volumeSlider->setMaximum(100); //the volume is between 0 and 100
   \_volumeSlider->setToolTip("Audio slider");

   // Note: if you use streaming, there is no ability to use the
   position slider \_positionSlider=new QSlider(Qt::Horizontal,this);
   \_positionSlider->setMaximum(POSITION_RESOLUTION);

   QVBoxLayout \*layout = new QVBoxLayout;
   layout->addWidget(_videoWidget); layout->addWidget(_positionSlider);
   layout->addWidget(_volumeSlider); setLayout(layout);

   \_isPlaying=false; poller=new QTimer(this);

   //Initialize an instance of vlc //a structure for the exception is
   neede for this initalization libvlc_exception_init(&_vlcexcep);

   //create a new libvlc instance
   \_vlcinstance=libvlc_new(sizeof(vlc_args) / sizeof(vlc_args[0]),
   vlc_args,&_vlcexcep); //tricky calculation of the char space used
   raise (&_vlcexcep);

   // Create a media player playing environement \_mp =
   libvlc_media_player_new (_vlcinstance, &_vlcexcep); raise
   (&_vlcexcep);

   //connect the two sliders to the corresponding slots (uses Qt's
   signal / slots technology) connect(poller, SIGNAL(timeout()), this,
   SLOT(updateInterface())); connect(_positionSlider,
   SIGNAL(sliderMoved(int)), this, SLOT(changePosition(int)));
   connect(_volumeSlider, SIGNAL(sliderMoved(int)), this,
   SLOT(changeVolume(int)));

   poller->start(100); //start timer to trigger every 100 ms the
   updateInterface slot

}

//desctructor Player::~Player() { /\* Stop playing \*/
libvlc_media_player_stop (_mp, &_vlcexcep);

   /\* Free the media_player \*/ libvlc_media_player_release (_mp);

   libvlc_release (_vlcinstance); raise (&_vlcexcep);

}

void Player::playFile(QString file) { //the file has to be in one of the
following formats /perhaps a little bit outdated) /\*
[file://%5Dfilename Plain media file
`http://ip:port/file <http://ip:port/file>`__ HTTP URL
`ftp://ip:port/file <ftp://ip:port/file>`__ FTP URL
`mms://ip:port/file <mms://ip:port/file>`__ MMS URL screen:// Screen
capture [dvd://][device][@raw_device] DVD device [vcd://][device] VCD
device [cdda://][device] Audio CD device udp:[[<source address>]@[<bind
address>][:<bind port>]] \*/

   /\* Create a new LibVLC media descriptor \*/ \_m = libvlc_media_new
   (_vlcinstance, file.toAscii(), &_vlcexcep); raise(&_vlcexcep);

   libvlc_media_player_set_media (_mp, \_m, &_vlcexcep);
   raise(&_vlcexcep);

   // /!Please note /!// // passing the widget to the lib shows vlc at
   which position it should show up // vlc automatically resizes the
   video to the ´given size of the widget // and it even resizes it, if
   the size changes at the playing

   /\* Get our media instance to use our window \*/ #if
   defined(Q_OS_WIN) libvlc_media_player_set_drawable(_mp,
   reinterpret_cast<unsigned int>(_videoWidget->winId()), &_vlcexcep );
   //libvlc_media_player_set_hwnd(_mp, \_videoWidget->winId(),
   &_vlcexcep ); // for vlc 1.0 #elif defined(Q_OS_MAC)
   libvlc_media_player_set_drawable(_mp, \_videoWidget->winId(),
   &_vlcexcep ); //libvlc_media_player_set_agl (_mp,
   \_videoWidget->winId(), &_vlcexcep); // for vlc 1.0 #else //Linux
   //[20101201 Ondrej Spilka] obsolete call on libVLC >=1.1.5
   //libvlc_media_player_set_drawable(_mp, \_videoWidget->winId(),
   &_vlcexcep ); //libvlc_media_player_set_xwindow(_mp,
   \_videoWidget->winId(), &_vlcexcep ); // for vlc 1.0

      /\* again note X11 handle on Linux is needed
         winID() returns X11 handle when QX11EmbedContainer us used \*/

         int windid = \_videoWidget->winId();
         libvlc_media_player_set_xwindow (mp, windid );

   #endif raise(&_vlcexcep);

   /\* Play \*/ libvlc_media_player_play (_mp, &_vlcexcep );
   raise(&_vlcexcep);

   \_isPlaying=true;

}

void Player::changeVolume(int newVolume) {
libvlc_exception_clear(&_vlcexcep); libvlc_audio_set_volume
(_vlcinstance,newVolume , &_vlcexcep); raise(&_vlcexcep); }

void Player::changePosition(int newPosition) {
libvlc_exception_clear(&_vlcexcep); // It's possible that the vlc
doesn't play anything // so check before libvlc_media_t \*curMedia =
libvlc_media_player_get_media (_mp, &_vlcexcep);
libvlc_exception_clear(&_vlcexcep); if (curMedia == NULL) return;

   float pos=(float)(newPosition)/(float)POSITION_RESOLUTION;
   libvlc_media_player_set_position (_mp, pos, &_vlcexcep);
   raise(&_vlcexcep);

}

void Player::updateInterface() { if(!_isPlaying) return;

   // It's possible that the vlc doesn't play anything // so check
   before libvlc_media_t \*curMedia = libvlc_media_player_get_media
   (_mp, &_vlcexcep); libvlc_exception_clear(&_vlcexcep); if (curMedia
   == NULL) return;

   float pos=libvlc_media_player_get_position (_mp, &_vlcexcep); int
   siderPos=(int)(pos*(float)(POSITION_RESOLUTION));
   \_positionSlider->setValue(siderPos); int
   volume=libvlc_audio_get_volume (_vlcinstance,&_vlcexcep);
   \_volumeSlider->setValue(volume);

} void Player::raise(libvlc_exception_t \* ex) { if
(libvlc_exception_raised (ex)) { fprintf (stderr, "error: %sn",
libvlc_exception_get_message(ex)); exit (-1); } } </syntaxhighlight>

== VLC 1.2 and OpenSuse 11.3 == [Rafael
Capucho<rafael.capucho@gmail.com> 20120713] Modified to include properly
QX11EmbedContainer header that was missing.- tested ok

[Jofre Guevara 20101215] Modifications of original template based on new
VLC version.

[Ondrej Spilka 20101201] slightly modified for the modest versions...

== Files ==

main.cpp: <syntaxhighlight lang="cpp-qt"> /\* libVLC and Qt sample code
\* Copyright © 2009 Alexander Maringer <maringer@maringer-it.de> \*/�

#include "vlc_on_qt.h" #include <QtGui/QApplication>

int main(int argc, char \*argv[]) { QApplication a(argc, argv); Player
p; p.resize(640,480); p.playFile("rtp://@:2626"); // Replace with what
you want to play p.show(); return a.exec(); } </syntaxhighlight>

vlc_on_qt.h: <syntaxhighlight lang="cpp-qt"> /\* libVLC and Qt sample
code \* Copyright © 2009 Alexander Maringer <maringer@maringer-it.de>
\*/ #ifndef VLC_ON_QT_H #define VLC_ON_QT_H

#include <vlc/vlc.h>

#include <QX11EmbedContainer> #include <QWidget>

class QVBoxLayout; class QPushButton; class QTimer; class QFrame; class
QSlider;

#define POSITION_RESOLUTION 10000

class Player : public QWidget { Q_OBJECT QSlider *\_positionSlider;
QSlider*\ \_volumeSlider; // [20101215 JG] // Tested on Linux OpenSuse
and VLC 1.2.0. This version of VLC is not completely compatible with
previous versions of VLC. // [20101201 Ondra Spilka] // on Linux/Ubuntu
Lucid and VLC >= 1.0 (at least 1.1.5 was tested) XWindow handle have to
be passed // therefore QX11EmbedContainer have to be used instead of
QFrame #ifdef Q_WS_X11 QX11EmbedContainer *\_videoWidget; #else
QFrame*\ \_videoWidget; #endif // [20101215 JG] If KDE is used like
unique desktop environment, only use QFrame *\_videoWidget;
QTimer*\ poller; bool \_isPlaying; //libvlc_exception_t \_vlcexcep; //
[20101215 JG] Used for versions prior to VLC 1.2.0. libvlc_instance_t
*\_vlcinstance; libvlc_media_player_t*\ \_mp; libvlc_media_t \*_m;

public:
   Player(); ~Player(); //void raise(libvlc_exception_t \* ex); //
   [20101215 JG] Used for versions prior to VLC 1.2.0.

public slots:
   void playFile(QString file); void updateInterface(); void
   changeVolume(int newVolume); void changePosition(int newPosition);

}; #endif </syntaxhighlight>

vlc_on_qt.cpp: <syntaxhighlight lang="cpp-qt"> /\* libVLC and Qt sample
code \* Copyright © 2009 Alexander Maringer <maringer@maringer-it.de>
\*/ #include "vlc_on_qt.h"

#include <QX11EmbedContainer> #include <QVBoxLayout> #include
<QPushButton> #include <QSlider> #include <QTimer> #include <QFrame>

Player::Player() : QWidget() { //preparation of the vlc command const
char \* const vlc_args[] = { "--verbose=2", //be much more verbose then
normal for debugging purpose };

#ifdef Q_WS_X11
   \_videoWidget=new QX11EmbedContainer(this);

#else
   \_videoWidget=new QFrame(this);

#endif
   // [20101215 JG] If KDE is used like unique desktop environment, only
   use \_videoWidget=new QFrame(this);

   \_volumeSlider=new QSlider(Qt::Horizontal,this);
   \_volumeSlider->setMaximum(100); //the volume is between 0 and 100
   \_volumeSlider->setToolTip("Audio slider");

   // Note: if you use streaming, there is no ability to use the
   position slider \_positionSlider=new QSlider(Qt::Horizontal,this);
   \_positionSlider->setMaximum(POSITION_RESOLUTION);

   QVBoxLayout \*layout = new QVBoxLayout;
   layout->addWidget(_videoWidget); layout->addWidget(_positionSlider);
   layout->addWidget(_volumeSlider); setLayout(layout);

   \_isPlaying=false; poller=new QTimer(this);

   //Initialize an instance of vlc //a structure for the exception is
   neede for this initalization //libvlc_exception_init(&_vlcexcep); //
   [20101215 JG] Used for versions prior to VLC 1.2.0.

   //create a new libvlc instance
   \_vlcinstance=libvlc_new(sizeof(vlc_args) / sizeof(vlc_args[0]),
   vlc_args); //tricky calculation of the char space used
   //_vlcinstance=libvlc_new(sizeof(vlc_args) / sizeof(vlc_args[0]),
   vlc_args,&_vlcexcep); // [20101215 JG] Used for versions prior to VLC
   1.2.0. //raise (&_vlcexcep); // [20101215 JG] Used for versions prior
   to VLC 1.2.0.

   // Create a media player playing environement \_mp =
   libvlc_media_player_new (_vlcinstance); //_mp =
   libvlc_media_player_new (_vlcinstance, &_vlcexcep); // [20101215 JG]
   Used for versions prior to VLC 1.2.0. //raise (&_vlcexcep); //
   [20101215 JG] Used for versions prior to VLC 1.2.0.

   //connect the two sliders to the corresponding slots (uses Qt's
   signal / slots technology) connect(poller, SIGNAL(timeout()), this,
   SLOT(updateInterface())); connect(_positionSlider,
   SIGNAL(sliderMoved(int)), this, SLOT(changePosition(int)));
   connect(_volumeSlider, SIGNAL(sliderMoved(int)), this,
   SLOT(changeVolume(int)));

   poller->start(100); //start timer to trigger every 100 ms the
   updateInterface slot

}

//desctructor Player::~Player() { /\* Stop playing \*/
libvlc_media_player_stop (_mp); //libvlc_media_player_stop (_mp,
&_vlcexcep); // [20101215 JG] Used for versions prior to VLC 1.2.0.

   /\* Free the media_player \*/ libvlc_media_player_release (_mp);

   libvlc_release (_vlcinstance); //raise (&_vlcexcep); // [20101215 JG]
   Used for versions prior to VLC 1.2.0.

}

void Player::playFile(QString file) { //the file has to be in one of the
following formats /perhaps a little bit outdated) /\*
[file://%5Dfilename Plain media file
`http://ip:port/file <http://ip:port/file>`__ HTTP URL
`ftp://ip:port/file <ftp://ip:port/file>`__ FTP URL
`mms://ip:port/file <mms://ip:port/file>`__ MMS URL screen:// Screen
capture [dvd://][device][@raw_device] DVD device [vcd://][device] VCD
device [cdda://][device] Audio CD device udp:[[<source address>]@[<bind
address>][:<bind port>]] \*/

   /\* Create a new LibVLC media descriptor \*/ \_m =
   libvlc_media_new_path(_vlcinstance, file.toAscii()); //_m =
   libvlc_media_new (_vlcinstance, file.toAscii(), &_vlcexcep); //
   [20101215 JG] Used for versions prior to VLC 1.2.0.
   //raise(&_vlcexcep); // [20101215 JG] Used for versions prior to VLC
   1.2.0.

   libvlc_media_player_set_media (_mp, \_m);
   //libvlc_media_player_set_media (_mp, \_m, &_vlcexcep); // [20101215
   JG] Used for versions prior to VLC 1.2.0. //raise(&_vlcexcep); //
   [20101215 JG] Used for versions prior to VLC 1.2.0.

   // /!Please note /!// // passing the widget to the lib shows vlc at
   which position it should show up // vlc automatically resizes the
   video to the ´given size of the widget // and it even resizes it, if
   the size changes at the playing

   /\* Get our media instance to use our window \*/ #if
   defined(Q_OS_WIN) libvlc_media_player_set_drawable(_mp,
   reinterpret_cast<unsigned int>(_videoWidget->winId()));
   //libvlc_media_player_set_drawable(_mp, reinterpret_cast<unsigned
   int>(_videoWidget->winId()), &_vlcexcep ); // [20101215 JG] Used for
   versions prior to VLC 1.2.0. //libvlc_media_player_set_hwnd(_mp,
   \_videoWidget->winId(), &_vlcexcep ); // for vlc 1.0 #elif
   defined(Q_OS_MAC) libvlc_media_player_set_drawable(_mp,
   \_videoWidget->winId()); //libvlc_media_player_set_drawable(_mp,
   \_videoWidget->winId(), &_vlcexcep ); // [20101215 JG] Used for
   versions prior to VLC 1.2.0. //libvlc_media_player_set_agl (_mp,
   \_videoWidget->winId(), &_vlcexcep); // for vlc 1.0 #else //Linux
   //[20101201 Ondrej Spilka] obsolete call on libVLC >=1.1.5
   //libvlc_media_player_set_drawable(_mp, \_videoWidget->winId(),
   &_vlcexcep ); //libvlc_media_player_set_xwindow(_mp,
   \_videoWidget->winId(), &_vlcexcep ); // for vlc 1.0

      /\* again note X11 handle on Linux is needed
         winID() returns X11 handle when QX11EmbedContainer us used \*/

         int windid = \_videoWidget->winId();
         libvlc_media_player_set_xwindow (_mp, windid );

   #endif //raise(&_vlcexcep); // [20101215 JG] Used for versions prior
   to VLC 1.2.0.

   /\* Play \*/ libvlc_media_player_play (_mp);
   //libvlc_media_player_play (_mp, &_vlcexcep ); // [20101215 JG] Used
   for versions prior to VLC 1.2.0. //raise(&_vlcexcep); // [20101215
   JG] Used for versions prior to VLC 1.2.0.

   \_isPlaying=true;

}

void Player::changeVolume(int newVolume) {
//libvlc_exception_clear(&_vlcexcep); // [20101215 JG] Used for versions
prior to VLC 1.2.0. libvlc_audio_set_volume (_mp,newVolume);
//libvlc_audio_set_volume (_vlcinstance,newVolume , &_vlcexcep); //
[20101215 JG] Used for versions prior to VLC 1.2.0. //raise(&_vlcexcep);
// [20101215 JG] Used for versions prior to VLC 1.2.0. }

void Player::changePosition(int newPosition) {
//libvlc_exception_clear(&_vlcexcep); // [20101215 JG] Used for versions
prior to VLC 1.2.0. // It's possible that the vlc doesn't play anything
// so check before libvlc_media_t *curMedia =
libvlc_media_player_get_media (_mp); //libvlc_media_t*\ curMedia =
libvlc_media_player_get_media (_mp, &_vlcexcep); // [20101215 JG] Used
for versions prior to VLC 1.2.0. //libvlc_exception_clear(&_vlcexcep);
// [20101215 JG] Used for versions prior to VLC 1.2.0. if (curMedia ==
NULL) return;

   float pos=(float)(newPosition)/(float)POSITION_RESOLUTION;
   libvlc_media_player_set_position (_mp, pos);
   //libvlc_media_player_set_position (_mp, pos, &_vlcexcep); //
   [20101215 JG] Used for versions prior to VLC 1.2.0.
   //raise(&_vlcexcep); // [20101215 JG] Used for versions prior to VLC
   1.2.0.

}

void Player::updateInterface() { if(!_isPlaying) return;

   // It's possible that the vlc doesn't play anything // so check
   before libvlc_media_t *curMedia = libvlc_media_player_get_media
   (_mp); //libvlc_media_t*\ curMedia = libvlc_media_player_get_media
   (_mp, &_vlcexcep); // [20101215 JG] Used for versions prior to VLC
   1.2.0. //libvlc_exception_clear(&_vlcexcep); // [20101215 JG] Used
   for versions prior to VLC 1.2.0. if (curMedia == NULL) return;

   float pos=libvlc_media_player_get_position (_mp); //float
   pos=libvlc_media_player_get_position (_mp, &_vlcexcep); // [20101215
   JG] Used for versions prior to VLC 1.2.0. int
   siderPos=(int)(pos*(float)(POSITION_RESOLUTION));
   \_positionSlider->setValue(siderPos); int
   volume=libvlc_audio_get_volume (_mp); //int
   volume=libvlc_audio_get_volume (_vlcinstance,&_vlcexcep); //
   [20101215 JG] Used for versions prior to VLC 1.2.0.
   \_volumeSlider->setValue(volume);

} /*void Player::raise(libvlc_exception_t* ex) { if
(libvlc_exception_raised (ex)) { fprintf (stderr, "error: %sn",
libvlc_exception_get_message(ex)); exit (-1); } }*/ // [20101215 JG]
Used for versions prior to VLC 1.2.0. </syntaxhighlight>

[[Category:libVLC]] [[Category:Qt]]
