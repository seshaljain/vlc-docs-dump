Ticket #156 (closed defect: fixed) Is restarting VLC the fix
------------------------------------------------------------

Is this fixed or is restarting VLC the fix? I am sending HD streams and after about 1 hour to 2 hours the CPU begins to spike at specific intervals corrupting the multicast stream that I am sending. I have to stop and restart VLC 0.8.5 to recover. "VLC on VTHR leaks memory (see videolan@vthr:prod/vlc.sh) while doing intensive TS/UDP multicast streaming input/output.

A restart is needed after some time. "

   Hmmm... I don't know, try both or something. `The thing <User:The_thing>`__ 02:06, 19 September 2006 (CEST)

Link to Developer's Site is broken
----------------------------------

Please replace the current link to the developer's site (located in the to right corner) with this one http://wiki.videolan.org/Developers_Corner.

Cheers, --`Materthron <User:Materthron>`__ 14:59, 19 December 2007 (CET)

   done.

-- Need to brush up the EN entries on the main page. How do I do that? PRedditt

".Net Interface to VLC" marshals strings falsely
------------------------------------------------

".Net Interface to VLC" marshals strings falsely. For ex,playlist_AddExt, can not add a file to playlist if the path/filename contains a non-english char such as ğ,ü,ş,i,ö,ç etc. More correct approach can be like below:

NativeLibVlc.cs

--------------

::

   static extern VlcError playlist_AddExt(
                IntPtr p_playlist, 
                [MarshalAs(UnmanagedType.CustomMarshaler,MarshalTypeRef=typeof(UTF8Marshaler))] String mrl, 
                [MarshalAs(UnmanagedType.CustomMarshaler,MarshalTypeRef=typeof(UTF8Marshaler))] String mrlDuplicate, 
                Mode mode,
                Int32 pos, 
                Int64 mtime_t, 
                [MarshalAs(UnmanagedType.CustomMarshaler, MarshalTypeRef = typeof(UTF8Marshaler))] string[] Options,
            int OptionsCount
   );

| ``   class UTF8Marshaler : ICustomMarshaler``
| ``   {``

``       static UTF8Marshaler _MyCustomMarshaler = null;``

| ``       public static ICustomMarshaler GetInstance(string Cookie)``
| ``       {``
| ``           if (_MyCustomMarshaler == null)``
| ``           {``
| ``               _MyCustomMarshaler = new UTF8Marshaler();``
| ``           }``
| ``           return _MyCustomMarshaler;``
| ``       }``

| ``       public void CleanUpManagedData(object ManagedObj)``
| ``       {``
| ``       }``

| ``       public void CleanUpNativeData(IntPtr pNativeData)``
| ``       {``
| ``       }``

| ``       public int GetNativeDataSize()``
| ``       {``
| ``           return -1;``
| ``       }``

| ``       public IntPtr MarshalManagedToNative(object ManagedObj)``
| ``       {``
| ``           if (ManagedObj is string)``
| ``           {``
| ``               unsafe``
| ``               {``
| ``                   byte[] buf = System.Text.Encoding.GetEncoding("UTF-8").GetBytes((string)ManagedObj);``
| ``                   fixed (void* ptr = &buf[0])``
| ``                   {``
| ``                       return new IntPtr(ptr);``
| ``                   }``
| ``               }``
| ``           }``
| ``           if (ManagedObj is string[]){``
| ``               unsafe``
| ``               {``
| ``                   string[] array = (string[])ManagedObj;``
| ``                   IntPtr[] buf = new IntPtr[array.Length];``
| ``                   for (int i = 0; i < buf.Length; i++)``
| ``                   {``
| ``                       byte[] b = System.Text.Encoding.GetEncoding("UTF-8").GetBytes(array[i]);``
| ``                       fixed(void *p=&b[0]){``
| ``                           buf[i] = (IntPtr)p;``
| ``                       }``
| ``                   }``
| ``                   fixed (void* ptr = &buf[0])``
| ``                   {``
| ``                       return new IntPtr(ptr);``
| ``                   }``
| ``               }``
| ``           }``
| ``           throw new Exception("UTF8Marshaler can only be used for \"string\" or \"string[]\". ");``
| ``       }``

| ``       public object MarshalNativeToManaged(IntPtr pNativeData)``
| ``       {``
| ``           return null;``
| ``       }``

``   }``

Wrong vlcInstallDirectory
-------------------------

If a .Net program using VLanControl is started from a network share like "\\server\share\program.exe", "vlcInstallDirectory" is calculated falsely.

A solution can be like below:

::

   static NativeLibVlc()
   {
       
       /* - */ //NativeLibVlc.vlcInstallDirectory = Path.GetDirectoryName(Assembly.GetExecutingAssembly().CodeBase).Substring(6);
       /* + */ NativeLibVlc.vlcInstallDirectory = Application.StartupPath;
   }

Correct English?
----------------

Perhaps someone would like to have a look over this and correct the English where needed? An immediate example being that, unlike with subversion, 'check out' is *two* words, not one. Just may be slightly clearer if the English is tidied up and would perhaps persuade more people to edit the wiki? Just a suggestion :D `Tek <User:Tek>`__ 12:29, 18 May 2009 (UTC)

when in doubt, hyphenate LOL.... but seriously, both are correct at times, but likely you are correct since the 8-letter word context unlikely to happen on this wiki (checkout is where you pay for items being bought.) My Point being: the error wouldn't be caught "spell-checking" the text... so give the editors a break. Homophones are a pet peeve of mine but since the editors are volunteers, i give them a little lee-way --`the Great and Almighty qazwiz <User:Qazwiz>`__ (`talk <User_talk:Qazwiz>`__) 04:29, 16 June 2017 (CEST)

Panel disappeared in Full Screen
--------------------------------

Initially when i installed VLC, the panel was being displayed at the bottom in Full Screen mode. Once, i clicked the running time in the panel to see the remaining time of the movie. Immediately after that the panel disappeared. Later, i can't get the panel in Full Screen mode.

Request: FAQ
------------

``... espically listing all feature in VLC that are NOT available that are in other tools``

such a matrix would be useful to present at the download page, allow people to quickly decide they get what tyhey wanted and if not to NOT download something that will frustrure them

example:

right now I am overburdened with episodes that are 550MB that ought be either 340MB or even smaller.... there are few types of vido content worthy of that much disk space...

Request: future features (if not present)
-----------------------------------------

what would be a really cool feature...?

after I watch something VLC asks if I want to archive it, and if so at what resulation and where to save it...

if I want it gone, then it skips the refuse basket, gets off the drive completely without having me do that typical two-step ...and at which point you could accumulate interest/worthiness statistics reflecting enjoyment (negative, positivs, my demographic, et al, all of which the script writers really want no matter what source...

otherwise if I deem it worth disk space, then I can watch soething else whilst the harddisk is spun through the file(s) to compress them as I wished

given how it could then be easily be adjusted into a batch process, i should be able to point to a folder (or folder of folders) with gudielines of which thing ought be stripped dowe for sake of clearing up space.... given new viewing platforms, 550MB for most episodes is overkill and too long to copy over to an IPAD to mention just one

example of low res show already downgraded by the production methods... SCI FI SANCUARTY... not worth more than 177MB per episode.... somehow it is posted as 1.03 GB... where and how and who? sxtunned I am

thanks

howeard_nyc@yahoo.com

please advise with suggestion and/or links if this sort of things already exists in VLS or other tool...

   please request new features at http://forum.videolan.org/viewforum.php?f=7 or using trac at https://trac.videolan.org/vlc/ --`Jan <User:J4n>`__ 22:47, 19 February 2012 (CET)

addons.videolan.org
-------------------

addons.videolan.org should be linked on the main page of this wiki --`Jan <User:J4n>`__ 22:11, 6 February 2012 (UTC)

wiki spam
---------

using better captcha will reduce wiki spam

http://www.mediawiki.org/wiki/Anti-spam_features

--`Jan <User:J4n>`__ 15:41, 8 February 2012 (UTC)

Links problem
-------------

The videolan icon to the the right of links to the videolan website go underneath the text, which looks horrible. I use chrome on a mac. I would fix it myself but, I don't exactly know how. `The thing <User:The_thing>`__ :sup:`(`\ `Talk <User_talk:The_thing>`__\ :sup:`•`\ `Contribs <Special:Contributions/The_thing>`__\ :sup:`)` 19:30, 18 February 2012 (CET)

   I concur. --`Jan <User:J4n>`__ 22:38, 19 February 2012 (CET)

Deinterlace information
-----------------------

I have captured a video from a Hi8 tape to a MPEG2 file. The playback is fuzzy (somewhat pixelated) Would some form of deinterlacing help? If so, which mode? Also, Can someone explain the functions of the deinterlace modes or direct me to a link that would?

Thanks. Jim B.

Vfilter erase-mask
------------------

The vfilter erase =-mask option, can this be used more than once ie. have a logo file placed in 2 positions on the screen?
