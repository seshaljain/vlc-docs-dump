================================
.. raw:: html                       
                                    
   <div class="banner-title">       
                                    
}}}}}{{#if:\|,}}                    
                                    
.. raw:: html                       
                                    
   </div>                           
                                    
{{#if:\|                            
                                    
.. raw:: html                       
                                    
   <div class="banner-subtitle">    
                                    
.. raw:: html                       
                                    
   </div>                           
                                    
}}                                  
================================

Usage
-----

``{{``\ \ ``|welcome to= |description= |links= |links2= |links3= }}``

Parameters
~~~~~~~~~~

-  **``|banner``\ ````\ ``title=``** (Custom) Specify custom text for the page name e.g. to translate it

   -  **``|welcome``\ ````\ ``to=``** (Optional, default page name) Specify custom text for the page name after Welcome to

-  **``|description=``** (Recommended, default blank) Describe the purpose of the page or its contents (e.g. The reference documentation on VideoLAN's projects.)
-  **``|links=``** (Optional) A bulleted list of links, defaults to generic links
-  **``|links2=``** (Optional) A bulleted list of links, defaults to generic links
-  **``|links3=``** (Optional) A bulleted list of links, defaults to generic links

Examples
~~~~~~~~

Main Page
^^^^^^^^^

| ``{{``\ 
| ``|welcome to=VideoLAN's Wiki``
| ``|description=The reference documentation and tips on VideoLAN's projects.``
| ``}}`` {{ \|welcome to=VideoLAN's Wiki \|description=The reference documentation and tips on VideoLAN's projects. }}

Main Page/de
''''''''''''

| ``{{``\ 
| ``|banner title=Willkommen bei [[{{PAGENAME}}|VideoLAN]]``
| ``}}``

``{{``\ \ ``|``

\|banner title=Willkommen bei `VideoLAN <Main_Page/de>`__ }}

VLC Developers Corner
^^^^^^^^^^^^^^^^^^^^^

| ``{{``\ 
| ``|description=This is a directory of everything to do with the development of VideoLAN's projects.<br />`` ``Check [[VLC media player|VLC's page]] to get info on VLC.``
| ``|links=``
| ``* [[VideoLAN]]``
| ``* [[VLC media player]]``
| ``** [https://addons.videolan.org Add-ons]``
| ``* [[Documentation:Documentation|Documentation]]``
| ``* [[VideoLAN_Sites#Developers|Developers' Sites]]``
| ``|links2=``
| ``* [https://www.videolan.org/developers Developer Zone]``
| ``* [https://nightlies.videolan.org Nightly builds]``
| ``* [https://jenkins.videolan.org Automatic builds]``
| ``|links3=``
| ``* [https://trac.videolan.org Trac, bugs, features, roadmap]``
| ``* [https://www.videolan.org/videolan/mirrors.html Mirrors check]``
| ``* [ftp://ftp.videolan.org/pub/videolan/ Main FTP]``
| ``}}``

``{{``\ 

| \|welcome to=VLC Developers Corner \|description=This is a directory of everything to do with the development of VideoLAN's projects.
| Check `VLC's page <VLC_media_player>`__ to get info on VLC. \|links=

-  `VideoLAN <VideoLAN>`__
-  `VLC media player <VLC_media_player>`__

   -  `Add-ons <https://addons.videolan.org>`__

-  `Documentation <Documentation:Documentation>`__
-  `Developers' Sites <VideoLAN_Sites#Developers>`__

\|links2=

-  `Developer Zone <https://www.videolan.org/developers>`__
-  `Nightly builds <https://nightlies.videolan.org>`__
-  `Automatic builds <https://jenkins.videolan.org>`__

\|links3=

-  `Trac, bugs, features, roadmap <https://trac.videolan.org>`__
-  `Mirrors check <https://www.videolan.org/videolan/mirrors.html>`__
-  `Main FTP <ftp://ftp.videolan.org/pub/videolan/>`__

}}

`Category:Templates <Category:Templates>`__
