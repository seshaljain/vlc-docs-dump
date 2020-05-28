{{Example code}} Here is a small tutorial intended to make a quick tour
of the ''stream to memory'' module (smem) , included in VLC 1.1.0. This
module allows you to write a code which handles the video and audio data
read by VLC. This page shows a basic code written in C which uses this
module.

/!Starting from VLC 2.2, smem uses <code>size_t</code> instead of
<code>unsigned int</code> for buffer sizes.

== Including VLC library ==

<syntaxhighlight lang="c"> #include <stdio.h> #include <stdint.h>

#include <vlc/vlc.h> </syntaxhighlight>

== Defining callbacks ==

VLC sends you the data you need via two functions that you define
yourself. They will be run before and after the data is rendered. There
are two functions for the audio data, and two for the video one. In this
example I will just show how to deal with audio data, the process is the
same for video handling. <syntaxhighlight lang="c"> void
prepareRender(void\* p_audio_data, uint8_t*\* pp_pcm_buffer , size_t
size); // Audio prerender callback void handleStream(void\*
p_audio_data, uint8_t\* p_pcm_buffer, unsigned int channels, unsigned
int rate, unsigned int nb_samples, unsigned int bits_per_sample, size_t
size, int64_t pts); // Audio postrender callback // Video prerender and
postrender callbacks not implemented. </syntaxhighlight>

== Creating a VLC instance ==

As with every application you build with libvlc, you have to initialize
the library. But you also have to tell VLC the address of each callback
you wrote. This is made by writing the address in the parameters used to
launch VLC. <syntaxhighlight lang="c">int main(int argc, char \*\ *argv)
{ // VLC pointers libvlc_instance_t*\ vlcInstance; libvlc_media_player_t
*mp; libvlc_media_t*\ media;

   // VLC options char smem_options[256];

   sprintf(smem_options, "#transcode{acodec=s16l}:smem{audio-postrender-callback=%lld,audio-prerender-callback=%lld}",
      // We are using transcode because smem only support raw audio and
      video formats

         (long long int)(intptr_t)(void*)&handleStream, (long long
         int)(intptr_t)(void*)&prepareRender);

      // We print (as a decimal value) the addresses. Note that you can
      also define smem-audio-data : this pointer // will be passed to
      your callbacks (it may be useful to retrive some extra
      informations) but isn't required at all.

   const char \* const vlc_args[] = {
      "--verbose=2", // Be much more verbose then normal for debugging
      purpose "--sout", smem_options // Stream to memory };

   // We launch VLC vlcInstance = libvlc_new(sizeof(vlc_args) /
   sizeof(vlc_args[0]), vlc_args);

   mp = libvlc_media_player_new(vlcInstance);

   // To be continued.

   return 0;

} </syntaxhighlight>

== Implementing callbacks == {{mmwikiPCM}} The {{docmod|smem}} module
sends us the data in [[PCM]] format.

The first callback, called <code>prepareRender</code> in this example,
locks the mutex and sets the data pointer (i.e. where the data will be
written). All you have to do here is to ensure that
<code>*pp_pcm_buffer</code> points now to a valid array where
<var>size</var> bytes can be written.

The second callback, here <code>handleStream</code>, is the place where
you can do everything you want with the data you got !

The <code>p_audio_data</code> pointer is linked to the object you set in
the command line parameters. It can be useful in order to communicate
with the rest of the program.

<syntaxhighlight lang="c"> void prepareRender (void\* p_audio_data,
uint8_t*\* pp_pcm_buffer , size_t size) { // TODO: Lock the mutex

   \*pp_pcm_buffer = // TODO

}

void handleStream(void\* p_audio_data, uint8_t\* p_pcm_buffer, unsigned
int channels, unsigned int rate, unsigned int nb_samples, unsigned int
bits_per_sample, size_t size, int64_t pts ) { // TODO: explain how data
should be handled // TODO: Unlock the mutex } </syntaxhighlight>

== Handling the data == The PCM format is very raw, but you may still
have to do some small transformations in order to be able to get the
exact waveform of the audio stream.

First, the audio data is sent as an array of bytes, but each sample may
be coded on more bytes : if you use the unchanged array, the values
won't mean anything. The parameter <code>bits_per_sample</code> helps
you to know how to tackle this problem.

Then, the data is still in an unsigned format : the negative values have
an offset which makes the data look weird.

[[Category:Coding]] [[Category:libVLC]]
