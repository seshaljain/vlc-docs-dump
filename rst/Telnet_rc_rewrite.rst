==Abstract== Rewriting the remote control and telnet interfaces has been
a long standing issue. Once the new playlist is finished in 0.8.6, we
can begin merging those two interfaces ... well in fact rewriting most
of the stuff.

==Ideas/goals/...== \* use new playlist \* advanced shell/telnet
features (autocompletion, history, ...) \* allow multiple remote
connections on the interface \* authentification: should we have only
one level or several ? \* make it possible to "browse" the modules like
a file system. This would be usefull to change variables which
registered callbacks on the fly. (On a developer's point of view it
would also simplify visualisation of the different module's interaction)
\* keep backwards compatibilty with old telnet and rc modules. telnet is
definitively a must have, i don't really know about rc.

==TODO== \* define all the commands and different features which will be
needed. \* authentification method like this: Executing any script when
user connecting via VoD link rtsp://server/test. If return 0 then
starting streaming else not starting.

==References== \* [https://trac.videolan.org/vlc/ticket/203 Trac ticket
#203] \* [http://www.via.ecp.fr/via/ml/vlc-devel/2005-04/msg00069.html
old mailing list discussion]

[[Category:Dev Discussions]]
