Help!

When I installed the vlc-0.8.6d-1.el4.rf.i386.rpm in Redhat ES release 4,following warning appeared:

I know that these warning means I should install these rpm packages before install vlc,but it is

a very hard work,I know I can use yum to install vlc automatic,but my redhat server is in

internal network and can not connect internet directly.

Who can give me a advice.

warning: vlc-0.8.6d-1.el4.rf.i386.rpm: V3 DSA signature: NOKEY, key ID 6b8d79e6 error: Failed dependencies:

| ``       libSDL_image-1.2.so.0 is needed by vlc-0.8.6d-1.el4.rf.i386``
| ``       liba52.so.0 is needed by vlc-0.8.6d-1.el4.rf.i386``
| ``       libaa.so.1 is needed by vlc-0.8.6d-1.el4.rf.i386``
| ``       libcaca.so.0 is needed by vlc-0.8.6d-1.el4.rf.i386``
| ``       libcddb.so.2 is needed by vlc-0.8.6d-1.el4.rf.i386``
| ``       libcdio.so.7 is needed by vlc-0.8.6d-1.el4.rf.i386``
| ``       libcucul.so.0 is needed by vlc-0.8.6d-1.el4.rf.i386``
| ``       libdvbpsi.so.4 is needed by vlc-0.8.6d-1.el4.rf.i386``
| ``       libdvdnav.so.4 is needed by vlc-0.8.6d-1.el4.rf.i386``
| ``       libdvdread.so.3 is needed by vlc-0.8.6d-1.el4.rf.i386``
| ``       libebml.so.0 is needed by vlc-0.8.6d-1.el4.rf.i386``
| ``       libfaac.so.0 is needed by vlc-0.8.6d-1.el4.rf.i386``
| ``       libfaad.so.0 is needed by vlc-0.8.6d-1.el4.rf.i386``
| ``       libid3tag.so.0 is needed by vlc-0.8.6d-1.el4.rf.i386``
| ``       libiso9660.so.5 is needed by vlc-0.8.6d-1.el4.rf.i386``
| ``       liblirc_client.so.0 is needed by vlc-0.8.6d-1.el4.rf.i386``
| ``       libmad.so.0 is needed by vlc-0.8.6d-1.el4.rf.i386``
| ``       libmatroska.so.0 is needed by vlc-0.8.6d-1.el4.rf.i386``
| ``       libmodplug.so.0 is needed by vlc-0.8.6d-1.el4.rf.i386``
| ``       libmp3lame.so.0 is needed by vlc-0.8.6d-1.el4.rf.i386``
| ``       libmpcdec.so.3 is needed by vlc-0.8.6d-1.el4.rf.i386``
| ``       libmpeg2.so.0 is needed by vlc-0.8.6d-1.el4.rf.i386``
| ``       libopendaap.so.0 is needed by vlc-0.8.6d-1.el4.rf.i386``
| ``       libupnp.so.2 is needed by vlc-0.8.6d-1.el4.rf.i386``
| ``       libvcdinfo.so.0 is needed by vlc-0.8.6d-1.el4.rf.i386``
| ``       libwx_baseu-2.6.so.0 is needed by vlc-0.8.6d-1.el4.rf.i386``
| ``       libwx_baseu-2.6.so.0(WXU_2.6) is needed by vlc-0.8.6d-1.el4.rf.i386``
| ``       libwx_baseu_net-2.6.so.0 is needed by vlc-0.8.6d-1.el4.rf.i386``
| ``       libwx_baseu_xml-2.6.so.0 is needed by vlc-0.8.6d-1.el4.rf.i386``
| ``       libwx_gtk2u_adv-2.6.so.0 is needed by vlc-0.8.6d-1.el4.rf.i386``
| ``       libwx_gtk2u_adv-2.6.so.0(WXU_2.6) is needed by vlc-0.8.6d-1.el4.rf.i386``
| ``       libwx_gtk2u_core-2.6.so.0 is needed by vlc-0.8.6d-1.el4.rf.i386``
| ``       libwx_gtk2u_core-2.6.so.0(WXU_2.6) is needed by vlc-0.8.6d-1.el4.rf.i386``
| ``       libwx_gtk2u_core-2.6.so.0(WXU_2.6.2) is needed by vlc-0.8.6d-1.el4.rf.i386``
| ``       libwx_gtk2u_html-2.6.so.0 is needed by vlc-0.8.6d-1.el4.rf.i386``
| ``       libwx_gtk2u_qa-2.6.so.0 is needed by vlc-0.8.6d-1.el4.rf.i386``
| ``       libwx_gtk2u_xrc-2.6.so.0 is needed by vlc-0.8.6d-1.el4.rf.i386``
| ``       libx264.so.55 is needed by vlc-0.8.6d-1.el4.rf.i386``
| ``       libxosd.so.2 is needed by vlc-0.8.6d-1.el4.rf.i386``

== API for :sout=#duplicate command ==

Hi All,

Can someone help me in identifying the API's for executing following command in vlc.

   sout=#duplicate{dst=std{access=file,mux=raw,dst=D:\Work\abc.mpg}}
