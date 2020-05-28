{{Historical}} VLS (aka VideoLAN Server) is an outdated streaming
solution. More information is available on
http://www.videolan.org/vlc/streaming.html.

Unless you really know what you are doing,
[https://forum.videolan.org/viewtopic.php?f=3&t=11405 we advise] that
you use [[VLC]] instead as it is far more powerful than VLS.

==Known problems==

VLS isn't compatible with GCC 4. You will thus need to use GCC 2.9, 3.3
or 3.4 to compile, or submit a patch to fix compilation problems on GCC
4.

== Solutions ==

=== Mandrake Patch ===

Mandrake Linux supplies a patch for vls 0.5.6 that fixes compilation on
gcc 3.4. The patch also works for gcc 4+ (Tested with 4.0.2 & 4.1.2).
The patch file (vls-0.5.6-gcc34.patch from vls-0.5.6-5mdk.src.rpm):

<syntaxhighlight lang="diff">

--- ./src/core/library.cpp.tv 2004-06-30 18:58:00.527941222 +0200 +++
./src/core/library.cpp 2004-06-30 18:58:45.777047645 +0200 @@ -25,7
+25,7 @@ \*
\*******************************************************************************/

-+#include <dlfcn.h>

   //------------------------------------------------------------------------------//
   Preamble

@@ -79,7 +79,7 @@
   # ifdef RTLD_NOW
      m_hHandle = dlopen(m_strName.GetString(), RTLD_NOW);

   # else

-  m_hHandle = dlopen(m_strName.GetString(), DL_LAZY);

+ m_hHandle = dlopen(m_strName.GetString(), RTLD_LAZY);
   # endif
      if(m_hHandle == NULL) {

--- ./src/core/hashtable.h.tv 2004-06-30 18:53:44.712993043 +0200 +++
./src/core/hashtable.h 2004-06-30 18:53:13.241614538 +0200 @@ -63,7
+63,7 @@ };

-class C_HashMethod<u32> +template <> class C_HashMethod<u32> { public:
inline C_HashMethod(u32 uiMaxHash); @@ -76,7 +76,7 @@ };

-class C_HashMethod<u16> +template <> class C_HashMethod<u16> { public:
inline C_HashMethod(u32 uiMaxHash); @@ -89,7 +89,7 @@ };

-class C_HashMethod<handle> +template <> class C_HashMethod<handle> {
public: inline C_HashMethod(u32 uiMaxHash); --- ./src/core/stream.cpp.tv
2004-06-30 18:59:00.374759370 +0200 +++ ./src/core/stream.cpp 2004-06-30
19:01:02.921339327 +0200 @@ -317,6 +317,8 @@ template <class IOStream>
C_Stream<IOStream>& C_Stream<IOStream>::operator >> (C_Serializable&
cObject) { + C_ClassDescription cObjectDescription = cObject.Reflect();
+ C_Serializer cSerializer(&cObject, cObjectDescription); try { u32
iByteCount = cSerializer.NextBytesCount(); @@ -324,11 +326,12 @@ { const
byte aBytes[iByteCount]; u32 iOffset = 0; + int iRc;

   // Read the data to deserialize on the stream do {

-  int iRc = m_pIOStream->Read(aBytes+iOffset, iByteCount-iOffset);

+ iRc = m_pIOStream->Read(aBytes+iOffset, iByteCount-iOffset);
   ASSERT(iRc >= 0 \|\| iRc == FILE_EOF); iOffset += iRc;

..

   }

</syntaxhighlight>

=== libdvbpsi ===

Use [https://download.videolan.org/pub/videolan/libdvbpsi/0.1.4
libdvbpsi3-0.1.4]. Later versions have incompatible API changes.

=== Dependency Errors ===

This error indicates that Makefile.dep and Makefile.module.dep need to
have some spare newlines removed. See
[https://forum.videolan.org/viewtopic.php?f=3&t=30869 this forum thread]
for details.

<syntaxhighlight lang="bash"> root@jan:/usr/src/vls/vls-0.5.6# make
dep/core/application.dpp:1: **\* missing separator. Stop. make:**\ \*
[dep/core/application.dpp] Error 2 </syntaxhighlight>

[[Category:VideoLAN projects|†]]
