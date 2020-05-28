General presentation
--------------------

| Hello!
| My name is **Rémi BARBE** (aka Remiii).
| You can contact me : free-software ((>a >)) remibarbe ((>d o t>)) fr. Or look at my `CV <http://www.remibarbe.fr/cv-fr.html>`__ on my `Website <http://www.remibarbe.fr>`__.

VLC project
-----------

| I work in the « Quality Team » and for two personal DVB module
| Use my talk page to talk to me or give me some TODOs.
| ===Quality Team=== For more informations read this wiki `http://wiki.videolan.org/Quality Wiki Quality <http://wiki.videolan.org/Quality_Wiki_Quality>`__
| ===DVB access module project=== VLC can read a DVB Transport Stream which come from a DVB Tuner Card (like Hauppauge, TechniSat...), to do that you have to give options (like frequency, symbol rate, program...). It is not possible just to read the Transport Stream from the DVR device situated in the /dev/dvb/adapterX/dvrX tree without passing options.
| My module can directly read the DVB Transport Stream from the DVR device. For example, use szap for synchronize the service and run VLC with the command line ./vlc dvb:// --dvb-dvr.
| This project is a personal project, it is not included in the trac of VLC which is the official bugs tracker of VLC.
| If you want more information about this module contact me.
| ===DVB EIT Table module project=== This module is not completely defined.

Compilation on OSX
------------------

| Compilation guide on OSX.
| ===Environnement de développement=== Installer le kit de développement Mac OSX developer kit, celui-ci est disponible sur le CD d'installation de OSX.
| ===Récupérer les sources=== Deux méthodes sont possibles (téléchargement de la version stable ou téléchargement de la version en développement).
| ====Version stable==== Télécharger les sources à cette adresse http://www.videolan.org/vlc/download-sources.html
| Puis décompresser le fichier.

::

   $tar -xvzf vlc-0.8.6f.tar.gz

| 

Version en développement (déprécié)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(VLC se base maintenant sur `Git <Git>`__, et le dossier créé se nomme "vlc")

| Installer subversion http://metissian.com/projects/macosx/subversion/
| Puis télécharger les sources
| $svn co svn://svn.videolan.org/vlc/trunk vlc-trunk Cette commande va créer un dossier vlc-trunk là où vous vous situez actuellement dans le terminal et va copier à l'intérieur la toute dernière version des fichiers source de vlc, celle de développement.
| Si vous voulez une autre version que celle-ci, regardez cette page http://developers.videolan.org/svn.html
| NB : Il est recommandé de ne pas déplacer les fichiers sources une fois qu'on a travaillé avec ceux-ci. Donc, télécharger les fichiers immédiatement au bon endroit, c'est plus sûr.

Problème avec Fink
~~~~~~~~~~~~~~~~~~

| Il faut désactiver fink pour éviter les conflits. Pour cela retirer le répertoire */sw* de votre PATH.
| ===Build les libraires externes=== Aller dans le fichier extras/contrib

::

   $cd /extras/contrib

| Faire un bootstrap, cette étape sert à détecter les éléments fondamentaux de la configuration de votre machine (dans quel dossier VLC se trouve-t-il, quels sont les arguments à utiliser en conséquence lors de la compilation, ...).

::

   $./bootsstrap

| Puis un *make src*, qui va télécharger toutes les librairies externes, les mettre dans */extras/contrib/src*, puis les compiler. Cela peut prendre 2 ou 3 heures. Les arguments à la compilation et les dossiers où doivent aller les différents éléments sont calculés par la fonction *./bootstrap* plus haut. Cette étape de la compilation manuelle de VLC installe puis compile des milliers de fichiers, mais uniquement à l'intérieur du dossier VLC.

::

   $make src

| 
| ===Préparation de VLC build=== Retourner à la racine de VLC

::

   $cd ../..

| Faire un *bootstrap*

::

   $./bootsstrap

| 
| ===Configuration de VLC build=== Faire un configure, qui spécifie les éléments que l'on veut.
| Pour plus d'information:

::

   $./configure --help

| Exemple:

::

   $./configure --enable-debug --disable-x11 --disable-xvideo --disable-glx --enable-sdl --enable-mad --enable- 
   libdvbpsi --enable-a52 --disable-dvdplay --enable-dvdnav --enable-dvdread --enable-ffmpeg --enable-faad -- 
   enable-flac --enable-vorbis --enable-speex --enable-theora --enable-ogg --enable-shout --enable-cddb -- 
   disable-cddax --enable-vcdx --disable-skins --disable-skins2 --disable-wxwidgets --enable-freetype --enable- 
   fribidi --enable-caca --enable-live555 --enable-dts --enable-goom --enable-modplug --enable-gnutls --enable- 
   daap --enable-ncurses --enable-libtwolame --enable-x264 --enable-png --enable-realrtsp –disable-libtool

| 
| Remarque: Une option intéressante est *--enable-debug* qui en plus de faire un exécutable débuggable en fait un lié en dur aux extras. Si vous changez pour *--enable-release*, le VLC compilé sera alors capable d'être redistribué ailleurs que sur votre machine (et dans un autre dossier de votre machine).
| ===Build VLC=== Faire un make

::

   $make

| Remarque: Par contre, toute compilation *release* doit se refaire en entier (10 minutes environ), alors que si vous ne changez qu'un fichier et que vous êtes en debug, seul celui-ci est recompilé et la modification prend alors beaucoup moins de temps.
| ===Problème possible=== Lors du make dans *extras/contrib* il est possible que certain serveur soit momentanément indisponible. Il faut alors charger à la main les sources manquantes (pour les placer dans le dossier */extras/contrib/src*).
| ====Exemple====
| =====Probleme sur libtiff=====

::

   curl -O ftp://ftp.remotesensing.org/pub/libtiff/tiff-3.8.2.tar.gz
     % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                    Dload  Upload   Total   Spent    Left  Speed
     0     0    0     0    0     0      0      0 --:--:--  0:00:01 --:--:--     0
   curl: (9) FTP: access denied
   make[1]: *** [tiff-3.8.2.tar.gz] Error 9
   make: *** [src] Error 2

| Télécharger une image sur un autre miroir:
| http://www.libtiff.org
| http://dl.maptools.org/dl/libtiff/
| Prendre la tiff-3.8.2.tar.gz
| Puis la drop dans extras/contrib/src/

::

   $make src

| 
| =====Problème sur libIDL=====

::

   curl -O http://andrewtv.org/libIDL/libIDL-0.6.8.tar.gz
   curl: (7) couldn't connect to host
   make[1]: *** [libIDL-0.6.8.tar.gz] Error 7
   make: *** [src] Error 2
   $

| www.andrewtv.org ne marche pas.
| Donc
| ftp://ftp.mozilla.org/\ [..]lla/libraries/source/libIDL-0.6.8.tar.gz

Contributions
-------------

`My contributions to this wiki <Special:Contributions/Remiii>`__
