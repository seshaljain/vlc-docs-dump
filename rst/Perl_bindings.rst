'''TODO: this wiki page is work in progress'''

== Installation ==

You need to have [[libvlc]] with headers already installed.

TODO: install from CPAN

== Usage == <syntaxhighlight lang="perl"> #!/usr/bin/env perl

use strict; use warnings; use 5.010;

use VideoLAN::LibVLC;

unless (@ARGV) {
   die "1 argument needed - path to a file.";

}

my $inst = VideoLAN::LibVLC::Instance->new; my $media =
VideoLAN::LibVLC::Media->new($inst, $ARGV[0], "path"); my $player =
VideoLAN::LibVLC::MediaPlayer->new($media);

$player->play;

sleep 5; say $player->fullscreen; $player->fullscreen(1); say
$player->fullscreen; sleep 5; $player->toggle_fullscreen; say
$player->fullscreen; sleep 5; </syntaxhighlight>

== Known issues ==

-  Libvlc event handling is not supported currently.
-  It's unknown whether it works under windows or not, I never tested it
   there.

[[Category:Bindings]]
