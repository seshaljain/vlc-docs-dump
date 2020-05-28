.. raw:: mediawiki

   {{example code|l=LGPL|for=.Net Interface to VLC}}

.. code:: csharp

   /*****************************************************************************
    * NativeLibVlc.cs: NativeLibVlc class definition
    *****************************************************************************
    * Copyright (C) 2006 Chris Meadowcroft
    *
    * Authors: Chris Meadowcroft
    *
    * This program is free software; you can redistribute it and/or modify
    * it under the terms of the GNU Lesser General Public License as published by
    * the Free Software Foundation.
    *
    * This program is distributed in the hope that it will be useful,
    * but WITHOUT ANY WARRANTY; without even the implied warranty of
    * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    * GNU General Public License for more details.
    *
    * You should have received a copy of the GNU Lesser General Public License
    * along with this program; if not, write to the Free Software
    * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston MA 02110-1301, USA.
    *****************************************************************************/

   using System;
   using System.Collections.Generic;
   using System.Diagnostics;
   using System.Drawing;
   using System.IO;
   using System.Reflection;
   using System.Runtime.InteropServices;
   using System.Text;
   using System.Windows.Forms;
   using Microsoft.Win32;

   namespace VLanControl
   {
       internal enum ObjectType : int
       {
           VLC_OBJECT_ROOT = (-1),
           VLC_OBJECT_VLC = (-2),
           VLC_OBJECT_MODULE = (-3),
           VLC_OBJECT_INTF = (-4),
           VLC_OBJECT_PLAYLIST = (-5),
           VLC_OBJECT_ITEM = (-6),
           VLC_OBJECT_INPUT = (-7),
           VLC_OBJECT_DECODER = (-8),
           VLC_OBJECT_VOUT = (-9),
           VLC_OBJECT_AOUT = (-10),
           VLC_OBJECT_SOUT = (-11),
           VLC_OBJECT_HTTPD = (-12),
           VLC_OBJECT_PACKETIZER = (-13),
           VLC_OBJECT_ENCODER = (-14),
           VLC_OBJECT_DIALOGS = (-15),
           VLC_OBJECT_VLM = (-16),
           VLC_OBJECT_ANNOUNCE = (-17),
           VLC_OBJECT_DEMUX = (-18),
           VLC_OBJECT_ACCESS = (-19),
           VLC_OBJECT_STREAM = (-20),
           VLC_OBJECT_OPENGL = (-21),
           VLC_OBJECT_FILTER = (-22),
           VLC_OBJECT_VOD = (-23),
           VLC_OBJECT_SPU = (-24),
           VLC_OBJECT_TLS = (-25),
           VLC_OBJECT_SD = (-26),
           VLC_OBJECT_XML = (-27),
           VLC_OBJECT_OSDMENU = (-28),
           VLC_OBJECT_STATS = (-29),
           VLC_OBJECT_HTTPD_HOST = (-30),

           VLC_OBJECT_GENERIC = (-666),
       }

       internal enum VlcError : int
       {
           Success = -0,
           NoMem = -1,
           Thread = -2,
           Timeout = -3,

           NoMod = -10,

           NoObj = -20,
           BadObj = -21,

           NoVar = -30,
           BadVar = -31,

           Exit = -255,
           Generic = -666,

           Exception = -998,
           NoInit = -999,
       };

       internal enum InputState : int
       {
           INIT_S = 0,
           OPENING_S = 1,
           BUFFERING_S = 2,
           PLAYING_S = 3,
           PAUSE_S = 4,
           END_S = 5,
           ERROR_S = 6,
       }

       internal class NativeLibVlc : IDisposable
       {
           #region private vlc enums

           enum Mode : int
           {
               Insert      = 0x01,
               Replace     = 0x02,
               Append      = 0x04,
               Go          = 0x08,
               CheckInsert = 0x10
           };

           public const Int32 EndOfPlaylist = -666;

           [Flags]
           enum ObjectSearchMode : int
           {
               FIND_PARENT         = 0x0001,
               FIND_CHILD          = 0x0002,
               FIND_ANYWHERE       = 0x0003,
               FIND_STRICT         = 0x0010,
           }

           [Flags]
           enum VarFlags : int
           {
               /** \defgroup var_flags Additive flags
                * These flags are added to the type field of the variable. Most as a result of
                * a __var_Change() call, but some may be added at creation time
                * @{
                */
               VLC_VAR_HASCHOICE     = 0x0100,
               VLC_VAR_HASMIN        = 0x0200,
               VLC_VAR_HASMAX        = 0x0400,
               VLC_VAR_HASSTEP       = 0x0800,

               VLC_VAR_ISLIST        = 0x1000,
               VLC_VAR_ISCOMMAND     = 0x2000,
               VLC_VAR_ISCONFIG      = 0x2000,

               /** Creation flag */
               VLC_VAR_DOINHERIT     = 0x8000,

               /**
                * \defgroup var_action Variable actions
                * These are the different actions that can be used with __var_Change().
                * The parameters given are the meaning of the two last parameters of
                * __var_Change() when this action is being used.
                * @{
                */

               /**
                * Set the minimum value of this variable
                * \param p_val The new minimum value
                * \param p_val2 Unused
                */
               VLC_VAR_SETMIN              = 0x0010,
               /**
                * Set the maximum value of this variable
                * \param p_val The new maximum value
                * \param p_val2 Unused
                */
               VLC_VAR_SETMAX              = 0x0011,
               VLC_VAR_SETSTEP             = 0x0012,
               /**
                * Set the value of this variable without triggering any callbacks
                * \param p_val The new value
                * \param p_val2 Unused
                */
               VLC_VAR_SETVALUE            = 0x0013,

               VLC_VAR_SETTEXT             = 0x0014,
               VLC_VAR_GETTEXT             = 0x0015,

               VLC_VAR_ADDCHOICE           = 0x0020,
               VLC_VAR_DELCHOICE           = 0x0021,
               VLC_VAR_CLEARCHOICES        = 0x0022,
               VLC_VAR_SETDEFAULT          = 0x0023,
               VLC_VAR_GETCHOICES          = 0x0024,
               VLC_VAR_FREECHOICES         = 0x0025,
               VLC_VAR_GETLIST             = 0x0026,
               VLC_VAR_FREELIST            = 0x0027,
               VLC_VAR_CHOICESCOUNT        = 0x0028,

               VLC_VAR_INHERITVALUE        = 0x0030,
               VLC_VAR_TRIGGER_CALLBACKS   = 0x0035,
           }

           enum playlist_command : int
           {
               PLAYLIST_PLAY = 0,      /**< No arg.                            res=can fail*/
               PLAYLIST_AUTOPLAY = 1,  /**< No arg.                            res=cant fail*/
               PLAYLIST_VIEWPLAY = 2,  /**< arg1= int, arg2= playlist_item_t*,*/
                                   /**  arg3 = playlist_item_t*          , res=can fail */
               PLAYLIST_ITEMPLAY = 3,  /** <arg1 = playlist_item_t *         , res=can fail */
               PLAYLIST_PAUSE = 4,     /**< No arg                             res=can fail*/
               PLAYLIST_STOP = 5,      /**< No arg                             res=can fail*/
               PLAYLIST_SKIP = 6,      /**< arg1=int,                          res=can fail*/
               PLAYLIST_GOTO = 7,      /**< arg1=int                           res=can fail */
               PLAYLIST_VIEWGOTO = 8   /**< arg1=int                           res=can fail */
           }

           enum CONFIG_ITEM : int
           {
               CONFIG_ITEM_STRING = 0x0010,
               CONFIG_ITEM_FILE = 0x0020,
               CONFIG_ITEM_MODULE = 0x0030,
               CONFIG_ITEM_INTEGER = 0x0040,
               CONFIG_ITEM_BOOL = 0x0050,
               CONFIG_ITEM_FLOAT = 0x0060,
           }

           enum input_query_e : int
           {
               /* input variable "position" */
               INPUT_GET_POSITION = 0,         /* arg1= double *       res=    */
               INPUT_SET_POSITION,         /* arg1= double         res=can fail    */

               /* input variable "length" */
               INPUT_GET_LENGTH,           /* arg1= int64_t *      res=can fail    */

               /* input variable "time" */
               INPUT_GET_TIME,             /* arg1= int64_t *      res=    */
               INPUT_SET_TIME,             /* arg1= int64_t        res=can fail    */

               /* input variable "rate" (1 is DEFAULT_RATE) */
               INPUT_GET_RATE,             /* arg1= int *          res=    */
               INPUT_SET_RATE,             /* arg1= int            res=can fail    */

               /* input variable "state" */
               INPUT_GET_STATE,            /* arg1= int *          res=    */
               INPUT_SET_STATE,            /* arg1= int            res=can fail    */

               /* input variable "audio-delay" and "sub-delay" */
               INPUT_GET_AUDIO_DELAY,      /* arg1 = int* res=can fail */
               INPUT_SET_AUDIO_DELAY,      /* arg1 = int  res=can fail */
               INPUT_GET_SPU_DELAY,        /* arg1 = int* res=can fail */
               INPUT_SET_SPU_DELAY,        /* arg1 = int  res=can fail */

               /* Meta datas */
               INPUT_ADD_INFO,   /* arg1= char* arg2= char* arg3=...     res=can fail */
               INPUT_GET_INFO,   /* arg1= char* arg2= char* arg3= char** res=can fail */
               INPUT_DEL_INFO,   /* arg1= char* arg2= char*              res=can fail */
               INPUT_SET_NAME,   /* arg1= char* res=can fail    */

               /* Input config options */
               INPUT_ADD_OPTION,      /* arg1= char * arg2= char *  res=can fail*/

               /* Input properties */
               INPUT_GET_BYTE_POSITION,     /* arg1= int64_t *       res=    */
               INPUT_SET_BYTE_SIZE,         /* arg1= int64_t *       res=    */

               /* bookmarks */
               INPUT_GET_BOOKMARKS,   /* arg1= seekpoint_t *** arg2= int * res=can fail */
               INPUT_CLEAR_BOOKMARKS, /* res=can fail */
               INPUT_ADD_BOOKMARK,    /* arg1= seekpoint_t *  res=can fail   */
               INPUT_CHANGE_BOOKMARK, /* arg1= seekpoint_t * arg2= int * res=can fail   */
               INPUT_DEL_BOOKMARK,    /* arg1= seekpoint_t *  res=can fail   */
               INPUT_SET_BOOKMARK,    /* arg1= int  res=can fail    */

               /* On the fly input slave */
               INPUT_ADD_SLAVE        /* arg1= char * */
           }

           #endregion

           #region private vlc structs
           [StructLayout(LayoutKind.Sequential)]
           struct libvlc_exception_t
           {
               public Int32 b_raised;
               public IntPtr psz_message;

               public void Init()
               {
                   libvlc_exception_init(out this);
               }

               public bool WasExceptionRaised()
               {
                   if(0 != libvlc_exception_raised(ref this))
                   {
                       libvlc_exception_clear(ref this);
                       return true;
                   }
                   return false;
               }
           }

           [StructLayout(LayoutKind.Sequential)]
           struct libvlc_instance_t
           {
               public IntPtr p_vlc;
               public IntPtr p_playlist;
               public IntPtr p_vlm;
               public Int32 i_vlc_id;

               public libvlc_instance_t(IntPtr vlc, IntPtr playlist, int vlcHandle)
               {
                   this.p_vlc = vlc;
                   this.p_playlist = playlist;
                   this.p_vlm = IntPtr.Zero;
                   this.i_vlc_id = vlcHandle;
               }
           }

           [StructLayout(LayoutKind.Sequential)]
           struct vlc_list_t
           {
               public Int32 i_count;
               public IntPtr p_values;
               public IntPtr pi_types;
           }

           [StructLayout( LayoutKind.Explicit )]
           struct vlc_value_t
           {
               [FieldOffset( 0 )]  public Int32   i_int;
               [FieldOffset( 0 )]  public Int32   b_bool;
               [FieldOffset( 0 )][MarshalAs(UnmanagedType.R4)]  public float   f_float;
               [FieldOffset( 0 )]  public IntPtr  psz_string;
               [FieldOffset( 0 )]  public IntPtr  p_address;
               [FieldOffset( 0 )]  public IntPtr  p_object;
               [FieldOffset( 0 )]  public IntPtr  p_list;
               [FieldOffset( 0 )][MarshalAs(UnmanagedType.I8)]  public Int64   i_time;

               [FieldOffset( 0 )]  public IntPtr  psz_name;
               [FieldOffset( 4 )]  public Int32   i_object_id;
           }

           [StructLayout(LayoutKind.Sequential)]
           struct module_config_t
           {
               public CONFIG_ITEM i_type;
           }

           #endregion

           #region vlc api interop
           const int AOUT_VOLUME_MAX = 1024;
           const int VOLUME_MAX = 200;
           const int DEFAULT_CHAN = 1;
           const String Playlist_Current = "item-change";
           const String Now_Playing = "Now Playing";
           const String Meta_information = "Meta-information";
           const String Meta_title = "meta-title";
           const String Meta_author = "meta-author";
           const String Meta_artist = "meta-artist";
           const String Meta_genre = "meta-genre";
           const String Meta_description = "meta-description";
           const String Meta_url = "meta-url";
           
           [DllImport("libvlc")]
           static extern int VLC_Create();
           [DllImport("libvlc")]
           static extern VlcError VLC_Init(int iVLC, int Argc, [MarshalAs(UnmanagedType.LPArray, ArraySubType = UnmanagedType.LPStr)]string[] Argv);
           [DllImport("libvlc")]
           static extern string VLC_Version();
           [DllImport("libvlc")]
           static extern VlcError VLC_CleanUp(int iVLC);
           [DllImport("libvlc")]
           static extern VlcError VLC_Destroy(int iVLC);
           [DllImport("libvlc")]
           static extern string VLC_Error(int i_err);

           [DllImport("libvlc")]
           static extern IntPtr vlc_current_object(int i_object);
           [DllImport("libvlc")]
           static extern IntPtr __vlc_object_find(IntPtr p_vlc, ObjectType objectType, ObjectSearchMode mode);
           [DllImport("libvlc")]
           static extern void __vlc_object_release(IntPtr p_vlc);
           [DllImport("libvlc")]
           static extern VlcError __var_Set(IntPtr p_vlc, String name, vlc_value_t value);
           [DllImport("libvlc")]
           static extern VlcError __var_Get(IntPtr p_this, String name, ref vlc_value_t value);
           [DllImport("libvlc")]
           static extern VlcError __var_Change(IntPtr p_this, String name, VarFlags varFlags,
               ref vlc_value_t value, ref vlc_value_t value2);

           [DllImport("libvlc")]
           static extern VlcError __aout_VolumeGet(IntPtr p_vlc, ref Int16 volume);
           [DllImport("libvlc")]
           static extern VlcError __aout_VolumeSet(IntPtr p_vlc, Int16 volume);
           [DllImport("libvlc")]
           static extern VlcError __aout_VolumeMute(IntPtr p_vlc, IntPtr alwaysNull);

           [DllImport("libvlc")]
           static extern void libvlc_exception_init(out libvlc_exception_t p_exception);
           [DllImport("libvlc")]
           static extern Int32 libvlc_exception_raised(ref libvlc_exception_t p_exception);
           [DllImport("libvlc")]
           static extern void libvlc_exception_clear(ref libvlc_exception_t p_exception);

           [DllImport("libvlc")]
           static extern void libvlc_playlist_play(ref libvlc_instance_t libvlc, Int32 id, 
               Int32 optionsCount, IntPtr optionsAlwaysNull, ref libvlc_exception_t p_exception);
           [DllImport("libvlc")]
           static extern IntPtr libvlc_playlist_get_input(ref libvlc_instance_t libvlc, ref libvlc_exception_t p_exception);

           [DllImport("libvlc")]
           static extern int VLC_PlaylistIndex(int vlcObject);
           [DllImport("libvlc")]
           static extern int VLC_PlaylistNumberOfItems(int vlcObject);

           [DllImport("libvlc")]
           static extern void libvlc_input_free(IntPtr p_input);

           [DllImport("libvlc")]
           static extern int libvlc_video_get_width(IntPtr p_input, ref libvlc_exception_t p_exception);
           [DllImport("libvlc")]
           static extern int libvlc_video_get_height(IntPtr p_input, ref libvlc_exception_t p_exception);

           [DllImport("libvlc", CallingConvention=CallingConvention.Cdecl)]
           static extern VlcError playlist_LockControl(IntPtr p_playlist, playlist_command i_query);
           [DllImport("libvlc", CallingConvention = CallingConvention.Cdecl)]
           static extern VlcError playlist_LockControl(IntPtr p_playlist, playlist_command i_query, Int32 arg1);
           [DllImport("libvlc")]
           static extern VlcError playlist_Clear(IntPtr p_playlist);
           [DllImport("libvlc")]
           static extern VlcError playlist_AddExt(IntPtr p_playlist, String mrl, String mrlDuplicate, 
               Mode mode, Int32 pos, Int64 mtime_t, 
               [MarshalAs(UnmanagedType.LPArray, ArraySubType=UnmanagedType.LPStr)]string[] Options,
               int OptionsCount);

           [UnmanagedFunctionPointer(CallingConvention.Cdecl)]
           delegate int VarChangedCallback(IntPtr vlc, String variable, vlc_value_t old_val, 
               vlc_value_t new_val, IntPtr param);

           [DllImport("libvlc")]
           static extern int __var_AddCallback(IntPtr vlc, String variable, VarChangedCallback cb, 
               IntPtr param);
           [DllImport("libvlc")]
           static extern int __var_DelCallback(IntPtr vlc, String variable, VarChangedCallback cb, 
               IntPtr param);
           [DllImport("libvlc", CallingConvention = CallingConvention.Cdecl, CharSet=CharSet.Ansi)]
           static extern VlcError input_Control(IntPtr input_thread_t, input_query_e i_query, String category, String name,
               ref IntPtr result);

           [DllImport("libvlc", CallingConvention = CallingConvention.Cdecl)]
           static extern void __vout_OSDMessage(IntPtr p_input, int i_channel, String message);
           [DllImport("libvlc")]
           static extern IntPtr config_FindConfig(IntPtr vlc, String name);
           [DllImport("libvlc")]
           static extern void __config_PutInt(IntPtr vlc, String name, int value);
           [DllImport("libvlc")]
           static extern void __config_PutFloat(IntPtr vlc, String name, float value);
           [DllImport("libvlc")]
           static extern void __config_PutPsz(IntPtr vlc, String name, String value);

           [DllImport("libvlc")]
           static extern int __config_GetInt(IntPtr vlc, String name);
           [DllImport("libvlc")]
           static extern float __config_GetFloat(IntPtr vlc, String name);
           [DllImport("libvlc")]
           static extern String __config_GetPsz(IntPtr vlc, String name);

           #endregion

           static NativeLibVlc()
           {
               NativeLibVlc.vlcInstallDirectory = Path.GetDirectoryName(Assembly.GetExecutingAssembly().CodeBase).Substring(6);
               //NativeLibVlc.vlcInstallDirectory = Environment.CurrentDirectory;
               //NativeLibVlc.vlcInstallDirectory = QueryVlcInstallPath();
           }

           public NativeLibVlc()
           {
           }

           #region IDisposable
           public void Dispose()
           {
               if(vlcHandle != -1)
               {
                   try
                   {
                       if(this.gch.IsAllocated)
                       {
                           UnhookPlaylistChanges();
                       }
                       VideoOutput = null;
                       VLC_CleanUp(this.vlcHandle);
                       VLC_Destroy(this.vlcHandle);
                   }
                   catch { }
               }
               vlcHandle = -1;
           }
           #endregion

           #region internal Vlc interop helper classes
           internal class VlcObject : IDisposable
           {
               IntPtr vlc = IntPtr.Zero;
               IntPtr subObject = IntPtr.Zero;
               bool isDisposed;

               public VlcObject(int vlcHandle, ObjectType objectType)
               {
                   vlc = vlc_current_object(vlcHandle);
                   if(IntPtr.Zero != vlc)
                   {
                       if(objectType == ObjectType.VLC_OBJECT_VLC)
                       {
                           subObject = vlc;
                       }
                       else
                       {
                           subObject = __vlc_object_find(vlc, objectType, ObjectSearchMode.FIND_CHILD);
                       }
                   }
               }

               public IntPtr Vlc { get { return this.vlc; } }
               public IntPtr SubObject { get { return this.subObject; } }

               public void Dispose()
               {
                   Dispose(true);
                   GC.SuppressFinalize(this);
               }

               protected virtual void Dispose(bool disposing)
               {
                   if(!this.isDisposed)
                   {
                       this.isDisposed = true;
                       if((IntPtr.Zero != subObject) && (subObject != vlc))
                       {
                           __vlc_object_release(subObject);
                       }
                       if(IntPtr.Zero != vlc)
                       {
                           __vlc_object_release(vlc);
                       }
                   }
               }

               protected bool IsDisposed { get { return this.isDisposed; } }

               ~VlcObject()
               {
                   Dispose(false);
               }
           }

           private class VlcPlaylistObject : VlcObject
           {
               public libvlc_instance_t libvlc;
               public libvlc_exception_t exception;

               public VlcPlaylistObject(int vlcHandle)
                   : base(vlcHandle, ObjectType.VLC_OBJECT_PLAYLIST)
               {
                   if(this.SubObject != IntPtr.Zero)
                   {
                       this.libvlc = new libvlc_instance_t(this.Vlc, this.SubObject, vlcHandle);
                       this.exception.Init();
                   }
               }
           }
           #endregion

           #region public Vlc interop helper functions
           public VlcObject OpenVlcObject(ObjectType objectType)
           {
               return new VlcObject(this.vlcHandle, objectType);
           }

           public int GetVlcObjectInt(ObjectType objectType, String propertyName, int errorReturn)
           {
               try
               {
                   using(VlcObject vobj = new VlcObject(this.vlcHandle, objectType))
                   {
                       vlc_value_t intValue = new vlc_value_t();
                       if((vobj.SubObject != IntPtr.Zero) &&
                           (VlcError.Success == __var_Get(vobj.SubObject, propertyName, ref intValue)))
                       {
                           return intValue.i_int;
                       }
                   }
               }
               catch(Exception ex)
               {
                   this.lastErrorMessage = ex.Message;
               }
               return errorReturn;
           }

           public VlcError SetVlcObjectInt(ObjectType objectType, String propertyName, int value)
           {
               try
               {
                   using(VlcObject vobj = new VlcObject(this.vlcHandle, objectType))
                   {
                       if(vobj.SubObject != IntPtr.Zero)
                       {
                           vlc_value_t intValue = new vlc_value_t();
                           intValue.i_int = value;
                           return __var_Set(vobj.SubObject, propertyName, intValue);
                       }
                   }
               }
               catch(Exception ex)
               {
                   this.lastErrorMessage = ex.Message;
               }
               return VlcError.NoObj;
           }

           public long GetVlcObjectLong(ObjectType objectType, String propertyName, long errorReturn)
           {
               try
               {
                   using(VlcObject vobj = new VlcObject(this.vlcHandle, objectType))
                   {
                       vlc_value_t longValue = new vlc_value_t();
                       if((vobj.SubObject != IntPtr.Zero) &&
                           (VlcError.Success == __var_Get(vobj.SubObject, propertyName, ref longValue)))
                       {
                           return longValue.i_time;
                       }
                   }
               }
               catch(Exception ex)
               {
                   this.lastErrorMessage = ex.Message;
               }
               return errorReturn;
           }

           public VlcError SetVlcObjectLong(ObjectType objectType, String propertyName, long value)
           {
               try
               {
                   using(VlcObject vobj = new VlcObject(this.vlcHandle, objectType))
                   {
                       if(vobj.SubObject != IntPtr.Zero)
                       {
                           vlc_value_t longValue = new vlc_value_t();
                           longValue.i_time = value;
                           return __var_Set(vobj.SubObject, propertyName, longValue);
                       }
                   }
               }
               catch(Exception ex)
               {
                   this.lastErrorMessage = ex.Message;
               }
               return VlcError.NoObj;
           }

           public float GetVlcObjectFloat(ObjectType objectType, String propertyName, float errorReturn)
           {
               try
               {
                   using(VlcObject vobj = new VlcObject(this.vlcHandle, objectType))
                   {
                       vlc_value_t floatValue = new vlc_value_t();
                       if((vobj.SubObject != IntPtr.Zero) &&
                           (VlcError.Success == __var_Get(vobj.SubObject, propertyName, ref floatValue)))
                       {
                           return floatValue.f_float;
                       }
                   }
               }
               catch(Exception ex)
               {
                   this.lastErrorMessage = ex.Message;
               }
               return errorReturn;
           }

           public VlcError SetVlcObjectFloat(ObjectType objectType, String propertyName, float value)
           {
               try
               {
                   using(VlcObject vobj = new VlcObject(this.vlcHandle, objectType))
                   {
                       if(vobj.SubObject != IntPtr.Zero)
                       {
                           vlc_value_t floatValue = new vlc_value_t();
                           floatValue.f_float = value;
                           return __var_Set(vobj.SubObject, propertyName, floatValue);
                       }
                   }
               }
               catch(Exception ex)
               {
                   this.lastErrorMessage = ex.Message;
               }
               return VlcError.NoObj;
           }

           public String GetVlcObjectString(ObjectType objectType, String propertyName, String errorReturn)
           {
               try
               {
                   using(VlcObject vobj = new VlcObject(this.vlcHandle, objectType))
                   {
                       vlc_value_t stringValue = new vlc_value_t();
                       if((vobj.SubObject != IntPtr.Zero) &&
                           (VlcError.Success == __var_Get(vobj.SubObject, propertyName, ref stringValue)))
                       {
                           return Marshal.PtrToStringAnsi(stringValue.psz_string);
                       }
                   }
               }
               catch(Exception ex)
               {
                   this.lastErrorMessage = ex.Message;
               }
               return errorReturn;
           }

           public VlcError SetVlcObjectString(ObjectType objectType, String propertyName, String value)
           {
               try
               {
                   using(VlcObject vobj = new VlcObject(this.vlcHandle, objectType))
                   {
                       if(vobj.SubObject != IntPtr.Zero)
                       {
                           vlc_value_t stringValue = new vlc_value_t();
                           IntPtr valuePtr = Marshal.StringToCoTaskMemAnsi(value);
                           stringValue.psz_string = valuePtr;
                           VlcError ret = __var_Set(vobj.SubObject, propertyName, stringValue);
                           Marshal.ZeroFreeCoTaskMemAnsi(valuePtr);
                           return ret;
                       }
                   }
               }
               catch(Exception ex)
               {
                   this.lastErrorMessage = ex.Message;
               }
               return VlcError.NoObj;
           }

           public VlcError GetVlcVariableChoiceList(ObjectType objectType, String propertyName,
               out int[] choiceIds, out String[] choiceText)
           {
               try
               {
                   using(VlcObject vobj = new VlcObject(this.vlcHandle, objectType))
                   {
                       if(vobj.SubObject != IntPtr.Zero)
                       {
                           vlc_value_t idValues = new vlc_value_t();
                           vlc_value_t textValues = new vlc_value_t();
                           if(VlcError.Success == __var_Change(vobj.SubObject, propertyName,
                               VarFlags.VLC_VAR_GETLIST, ref idValues, ref textValues))
                           {
                               try
                               {
                                   vlc_list_t idList = (vlc_list_t)Marshal.PtrToStructure(
                                       idValues.p_list, typeof(vlc_list_t));
                                   vlc_list_t textList = (vlc_list_t)Marshal.PtrToStructure(
                                       textValues.p_list, typeof(vlc_list_t));

                                   int choiceCount = idList.i_count;
                                   choiceIds = new Int32[choiceCount];
                                   choiceText = new String[choiceCount];

                                   for(int index = 0; index < choiceCount; index++)
                                   {
                                       IntPtr idPtr = new IntPtr(idList.p_values.ToInt32() +
                                           index * Marshal.SizeOf(typeof(vlc_value_t)));
                                       vlc_value_t idValue = (vlc_value_t)Marshal.PtrToStructure(
                                           idPtr, typeof(vlc_value_t));
                                       choiceIds[index] = idValue.i_int;

                                       IntPtr textPtr = new IntPtr(textList.p_values.ToInt32() +
                                           index * Marshal.SizeOf(typeof(vlc_value_t)));
                                       vlc_value_t textValue = (vlc_value_t)Marshal.PtrToStructure(
                                           textPtr, typeof(vlc_value_t));
                                       choiceText[index] = Marshal.PtrToStringAnsi(textValue.psz_string);
                                   }
                                   return VlcError.Success;
                               }
                               finally
                               {
                                   __var_Change(vobj.SubObject, propertyName, VarFlags.VLC_VAR_FREELIST,
                                       ref idValues, ref textValues);
                               }
                           }
                       }
                   }
               }
               catch(Exception ex)
               {
                   this.lastErrorMessage = ex.Message;
               }

               choiceIds = new int[0];
               choiceText = new string[0];
               return VlcError.NoObj;
           }

           public VlcError GetVlcVariableChoiceList(ObjectType objectType, String propertyName,
               out String[] choices, out String[] choiceText)
           {
               try
               {
                   using(VlcObject vobj = new VlcObject(this.vlcHandle, objectType))
                   {
                       if(vobj.SubObject != IntPtr.Zero)
                       {
                           vlc_value_t idValues = new vlc_value_t();
                           vlc_value_t textValues = new vlc_value_t();
                           if(VlcError.Success == __var_Change(vobj.SubObject, propertyName,
                               VarFlags.VLC_VAR_GETLIST, ref idValues, ref textValues))
                           {
                               try
                               {
                                   vlc_list_t idList = (vlc_list_t)Marshal.PtrToStructure(
                                       idValues.p_list, typeof(vlc_list_t));
                                   vlc_list_t textList = (vlc_list_t)Marshal.PtrToStructure(
                                       textValues.p_list, typeof(vlc_list_t));

                                   int choiceCount = idList.i_count;
                                   List<String> choiceList = new List<string>(choiceCount);
                                   List<String> choiceTextList = new List<string>(choiceCount);
                                   Dictionary<String, int> choiceDict = new Dictionary<string, int>(choiceCount);
                                   for(int index = 0; index < choiceCount; index++)
                                   {
                                       IntPtr idPtr = new IntPtr(idList.p_values.ToInt32() +
                                           index * Marshal.SizeOf(typeof(vlc_value_t)));
                                       vlc_value_t idValue = (vlc_value_t)Marshal.PtrToStructure(
                                           idPtr, typeof(vlc_value_t));
                                       String choice = Marshal.PtrToStringAnsi(idValue.psz_name);
                                       choiceList.Add(choice);
                                       if(choiceDict.ContainsKey(choice))
                                       {
                                           choiceDict[choice] = choiceDict[choice] + 1;
                                       }
                                       else
                                       {
                                           choiceDict[choice] = 1;
                                       }

                                       IntPtr textPtr = new IntPtr(textList.p_values.ToInt32() +
                                           index * Marshal.SizeOf(typeof(vlc_value_t)));
                                       vlc_value_t textValue = (vlc_value_t)Marshal.PtrToStructure(
                                           textPtr, typeof(vlc_value_t));
                                       choiceTextList.Add(Marshal.PtrToStringAnsi(textValue.psz_string));
                                   }

                                   int listIndex = 0;
                                   for(int index = 0; index < choiceCount; index++)
                                   {
                                       String choice = choiceList[listIndex];
                                       if((choiceDict[choice] > 1) && (choiceTextList[listIndex] == null))
                                       {
                                           choiceList.RemoveAt(listIndex);
                                           choiceTextList.RemoveAt(listIndex);
                                           choiceDict[choice] = choiceDict[choice] - 1;
                                       }
                                       else
                                       {
                                           listIndex++;
                                       }
                                   }
                                   for(int index = 0; index < choiceList.Count; index++)
                                   {
                                       if(choiceTextList[index] == null)
                                       {
                                           choiceTextList[index] = choiceList[index];
                                       }
                                   }

                                   choices = choiceList.ToArray();
                                   choiceText = choiceTextList.ToArray();
                                   return VlcError.Success;
                               }
                               finally
                               {
                                   __var_Change(vobj.SubObject, propertyName, VarFlags.VLC_VAR_FREELIST,
                                       ref idValues, ref textValues);
                               }
                           }
                       }
                   }
               }
               catch(Exception ex)
               {
                   this.lastErrorMessage = ex.Message;
               }

               choices = new string[0];
               choiceText = new string[0];
               return VlcError.NoObj;
           }
           #endregion

           #region public Properties
           public static string VlcInstallDir
           {
               get{ return vlcInstallDirectory; }
               set{ vlcInstallDirectory = value; }
           }

           public bool IsInitialized
           {
               get{return (vlcHandle != -1);}
           }

           public Control VideoOutput
           {
               get { return outputWindow; }
               set
               {
                   if(value == null)
                   {
                       if(outputWindow != null)
                       {
                           outputWindow = null;
                           if(vlcHandle != -1)
                           {
                               SetVlcObjectInt(ObjectType.VLC_OBJECT_VLC, "drawable", 0);
                           }
                       }
                   }
                   else
                   {
                       outputWindow = value;
                       if(vlcHandle != -1)
                       {
                           SetVlcObjectInt(ObjectType.VLC_OBJECT_VLC, "drawable", outputWindow.Handle.ToInt32());
                       }
                   }
               }
           }

           public string LastError
           {
               get{return lastErrorMessage;}
           }

           public event MetaDataEventHandler NowPlaying;

           protected virtual void OnNowPlaying(MetaDataUpdateEventArgs args)
           {
               if(this.NowPlaying != null)
               {
                   this.NowPlaying(this, args);
               }
           }

           protected delegate void HandleNowPlaying(MetaDataUpdateEventArgs args);

           protected virtual void VlcNowPlayingChanged(String newText)
           {
               // switch out of the Vlc thread to our User Interface thread if possible
               if(this.VideoOutput != null)
               {
                   this.VideoOutput.BeginInvoke(new HandleNowPlaying(OnNowPlaying),
                       new MetaDataUpdateEventArgs(MetaData.NowPlaying, newText));
               }
               else
               {
                   OnNowPlaying(new MetaDataUpdateEventArgs(MetaData.NowPlaying, newText));
               }
           }

           public int Length
           {
               get
               {
                   if(this.artificialLength != 0)
                   {
                       return this.artificialLength;
                   }
                   else
                   {
                       return Convert.ToInt32(GetVlcObjectLong(ObjectType.VLC_OBJECT_INPUT, "length", 0) / 1000000L);
                   }
               }
           }

           public void SetArtificialLength(int newLength)
           {
               this.artificialLength = newLength;
           }

           public int Time
           {
               get
               {
                   int time = Convert.ToInt32(GetVlcObjectLong(ObjectType.VLC_OBJECT_INPUT, "time", 0) / 1000000L);
                   if((time == 0) && (this.artificialLength != 0))
                   {
                       time = Convert.ToInt32(Position * this.artificialLength + .5d);
                   }
                   if(this.timeScaling != 0.0d)
                   {
                       time = Convert.ToInt32(time / this.timeScaling);
                   }
                   return time;
               }
               set
               {
                   if(this.artificialLength != 0)
                   {
                       float position = Convert.ToSingle(value) / Convert.ToSingle(this.artificialLength);
                       if(this.timeScaling != 0.0d)
                       {
                           position = Convert.ToSingle(position * this.timeScaling);
                       }
                       Debug.WriteLine(String.Format("Set Position {0}", position));
                       SetVlcObjectFloat(ObjectType.VLC_OBJECT_INPUT, "position", position);
                   }
                   else
                   {
                       long time = Convert.ToInt64(value) * 1000000L;
                       if(this.timeScaling != 0.0d)
                       {
                           time = Convert.ToInt64(time * this.timeScaling);
                       }
                       Debug.WriteLine(String.Format("Set Time {0}", time));
                       SetVlcObjectLong(ObjectType.VLC_OBJECT_INPUT, "time", time);
                   }
               }
           }

           public double TimeScaling
           {
               get { return this.timeScaling; }
               set { this.timeScaling = value; }
           }

           public double Position
           {
               get
               {
                   double position = GetVlcObjectFloat(ObjectType.VLC_OBJECT_INPUT, "position", 0.0f);
                   if(this.timeScaling != 0.0d)
                   {
                       position = position / this.timeScaling;
                   }
                   return position;
               }
               set
               {
                   double position = value;
                   if(this.timeScaling != 0.0d)
                   {
                       position = position * this.timeScaling;
                   }
                   Debug.WriteLine(String.Format("Set Position {0}", position));
                   SetVlcObjectFloat(ObjectType.VLC_OBJECT_INPUT, "position", Convert.ToSingle(position));
               }
           }

           public int Volume
           {
               get
               {
                   IntPtr vlc = vlc_current_object(vlcHandle);
                   if(IntPtr.Zero != vlc)
                   {
                       try
                       {
                           Int16 aoutVol = 0;
                           if(__aout_VolumeGet(vlc, ref aoutVol) == VlcError.Success)
                           {
                               return (aoutVol * VOLUME_MAX + AOUT_VOLUME_MAX / 2) / AOUT_VOLUME_MAX;
                           }
                       }
                       catch(Exception)
                       {
                       }
                       finally
                       {
                           __vlc_object_release(vlc);
                       }
                   }
                   return 0;
               }
               set
               {
                   IntPtr vlc = vlc_current_object(vlcHandle);
                   if(IntPtr.Zero != vlc)
                   {
                       try
                       {
                           Int16 aoutVol = Convert.ToInt16((value * AOUT_VOLUME_MAX + VOLUME_MAX / 2) / VOLUME_MAX);
                           __aout_VolumeSet(vlc, aoutVol);
                       }
                       catch(Exception)
                       {
                       }
                       finally
                       {
                           __vlc_object_release(vlc);
                       }
                   }
               }
           }

           public bool Fullscreen
           {
               get
               {
                   int isFullScreen = GetVlcObjectInt(ObjectType.VLC_OBJECT_VLC, "fullscreen", -666);
                   if((isFullScreen != -666) && (isFullScreen != 0))
                   {
                       return true;
                   }
                   return false;
                  
               }
               set
               {
                   SetVlcObjectInt(ObjectType.VLC_OBJECT_VLC, "fullscreen", value ? 1 : 0);
               }
           }

           public int PlaylistIndex
           {
               get
               {
                   try
                   {
                       return VLC_PlaylistIndex(this.vlcHandle);
                   }
                   catch(Exception ex)
                   {
                       this.lastErrorMessage = ex.Message;
                       return -1;
                   }
               }
           }

           public int PlaylistCount
           {
               get
               {
                   try
                   {
                       return VLC_PlaylistNumberOfItems(this.vlcHandle);
                   }
                   catch(Exception ex)
                   {
                       this.lastErrorMessage = ex.Message;
                       return -1;
                   }
               }
           }

           #endregion

           #region public Methods
           public bool Initialize()
           {
               // check if already initializes
               if(vlcHandle != -1)
                   return true;

               string oldDir = Environment.CurrentDirectory;
               // try init
               try
               {
                   // create instance
                   Environment.CurrentDirectory = NativeLibVlc.vlcInstallDirectory;
                   this.vlcHandle = VLC_Create();

                   if(this.vlcHandle < 0)
                   {
                       lastErrorMessage = "Failed to create VLC instance";
                       return false;
                   }

                   string[] initOptions = {    NativeLibVlc.vlcInstallDirectory,
                                               ":no-one-instance",
                                               ":no-loop",
                                               ":no-drop-late-frames",
                                               ":disable-screensaver",
                                               ":vout=vout_directx",
                                               "--plugin-path=" + NativeLibVlc.vlcInstallDirectory + @"\plugins",
                       };

                   // init libvlc
                   VlcError errVlcLib = VLC_Init(vlcHandle, initOptions.Length, initOptions);
                   if(errVlcLib != VlcError.Success)
                   {
                       VLC_Destroy(vlcHandle);
                       lastErrorMessage = "Failed to initialise VLC";
                       this.vlcHandle = -1;
                       return false;
                   }
               }
               catch
               {
                   lastErrorMessage = "Could not find libvlc";
                   return false;
               }
               finally
               {
                   Environment.CurrentDirectory = oldDir;
               }

               // check output window
               if(outputWindow != null)
               {
                   SetVlcObjectInt(ObjectType.VLC_OBJECT_VLC, "drawable", outputWindow.Handle.ToInt32());
               }

               return true;
           }

           // there's an overhead to supporting Vlc events, a memory leak, so we need to have them off by default
           public bool ProducingEvents
           {
               get { return this.gch.IsAllocated; }
               set
               {
                   if(value)
                   {
                       if(!this.gch.IsAllocated)
                       {
                           HookPlaylistChanges();
                       }
                   }
                   else
                   {
                       if(this.gch.IsAllocated)
                       {
                           UnhookPlaylistChanges();
                       }
                   }
               }
           }

           private static String AdjustFilterString(String current, String filter, bool add)
           {
               String newFilter = null;
               int findFilter = current.IndexOf(filter);
               if(findFilter == -1)
               {
                   if(add)
                   {
                       if(current.Length == 0)
                       {
                           newFilter = filter;
                       }
                       else
                       {
                           newFilter = String.Format("{0}:{1}", current, filter);
                       }
                   }
               }
               else
               {
                   if(!add)
                   {
                       int colonAfterAdjust = current.IndexOf(':', findFilter + 1);
                       if(findFilter == 0)
                       {
                           if(colonAfterAdjust == -1)
                           {
                               newFilter = String.Empty;
                           }
                           else
                           {
                               newFilter = current.Substring(colonAfterAdjust + 1);
                           }
                       }
                       else
                       {
                           if(colonAfterAdjust == -1)
                           {
                               newFilter = current.Substring(0, findFilter - 1);
                           }
                           else
                           {
                               newFilter = current.Substring(0, findFilter - 1) +
                                   current.Substring(colonAfterAdjust);
                           }
                       }
                   }
               }
               return newFilter;
           }

           const String VideoFilterList = "vout-filter";
           const String AdjustFilter = "adjust";

           public bool AllowVideoAdjustments
           {
               get
               {
                   String voutFilter = GetVlcObjectString(ObjectType.VLC_OBJECT_VOUT, VideoFilterList, null);
                   if(voutFilter == null)
                   {
                       GetConfigVariable(VideoFilterList, out voutFilter);
                   }
                   if(voutFilter != null)
                   {
                       return voutFilter.IndexOf(AdjustFilter) != -1;
                   }
                   else
                   {
                       return false;
                   }
               }
               set
               {
                   bool useConfig = false;
                   String voutFilter = GetVlcObjectString(ObjectType.VLC_OBJECT_VOUT, VideoFilterList, null);
                   if(voutFilter == null)
                   {
                       using(VlcObject vlc = new VlcObject(this.vlcHandle, ObjectType.VLC_OBJECT_VLC))
                       {
                           GetConfigVariable(VideoFilterList, out voutFilter);
                           useConfig = true;
                       }
                   }
                   if(voutFilter != null)
                   {
                       String newVoutFilter = AdjustFilterString(voutFilter, AdjustFilter, value);
                       if(newVoutFilter != null)
                       {
                           if(useConfig)
                           {
                               SetConfigVariable(VideoFilterList, newVoutFilter);
                           }
                           else
                           {
                               SetVlcObjectString(ObjectType.VLC_OBJECT_VOUT, VideoFilterList, newVoutFilter);
                           }
                       }
                   }
               }
           }

           public VlcError AddTarget(string target, ref int itemId)
           {
               try
               {
                   using(VlcObject vobj = new VlcObject(this.vlcHandle, ObjectType.VLC_OBJECT_PLAYLIST))
                   {
                       if(vobj.SubObject != IntPtr.Zero)
                       {
                           VlcError enmErr = playlist_AddExt(vobj.SubObject, target, target, Mode.Append, 
                               EndOfPlaylist, -1L, null, 0);
                           if(enmErr >= VlcError.Success)
                           {
                               itemId = (int)enmErr;
                           }
                           return enmErr;
                       }
                       else
                       {
                           return VlcError.NoObj;
                       }
                   }
               }
               catch(Exception ex)
               {
                   this.lastErrorMessage = ex.Message;
                   return VlcError.Exception;
               }
           }

           public VlcError AddTarget(string target, string[] options, ref int itemId)
           {
               int optionsCount = 0;
               if(options != null)
               {
                   optionsCount = options.Length;
               }

               try
               {
                   using(VlcObject vobj = new VlcObject(this.vlcHandle, ObjectType.VLC_OBJECT_PLAYLIST))
                   {
                       if(vobj.SubObject != IntPtr.Zero)
                       {
                           VlcError enmErr = playlist_AddExt(vobj.SubObject, target, target, Mode.Append,
                               EndOfPlaylist, -1L, options, optionsCount);
                           if(enmErr >= VlcError.Success)
                           {
                               itemId = (int)enmErr;
                           }
                           return enmErr;
                       }
                       else
                       {
                           return VlcError.NoObj;
                       }
                   }
               }
               catch(Exception ex)
               {
                   this.lastErrorMessage = ex.Message;
                   return VlcError.Exception;
               }
           }

           public Size VideoSize
           {
               get
               {
                   try
                   {
                       using(VlcPlaylistObject vpobj = new VlcPlaylistObject(this.vlcHandle))
                       {
                           if(vpobj.SubObject != IntPtr.Zero)
                           {
                               IntPtr p_input = libvlc_playlist_get_input(ref vpobj.libvlc, ref vpobj.exception);
                               if(vpobj.exception.WasExceptionRaised())
                               {
                                   this.lastErrorMessage = Marshal.PtrToStringAnsi(vpobj.exception.psz_message);
                               }
                               else
                               {
                                   try
                                   {
                                       int width = libvlc_video_get_width(p_input, ref vpobj.exception);
                                       if(!vpobj.exception.WasExceptionRaised())
                                       {
                                           int height = libvlc_video_get_height(p_input, ref vpobj.exception);
                                           if(!vpobj.exception.WasExceptionRaised())
                                           {
                                               return new Size(width, height);
                                           }
                                       }
                                   }
                                   finally
                                   {
                                       libvlc_input_free(p_input);
                                   }
                               }
                           }
                       }
                   }
                   catch(Exception ex)
                   {
                       this.lastErrorMessage = ex.Message;
                   }
                   return new Size();
               }
           }

           public VlcError Play(int itemId)
           {
               try
               {
                   this.artificialLength = 0;
                   this.timeScaling = 0.0d;
                   using(VlcPlaylistObject vpobj = new VlcPlaylistObject(this.vlcHandle))
                   {
                       if(vpobj.SubObject != IntPtr.Zero)
                       {
                           libvlc_playlist_play(ref vpobj.libvlc, itemId, 0, IntPtr.Zero, 
                               ref vpobj.exception);
                           if(vpobj.exception.WasExceptionRaised())
                           {
                               return VlcError.Generic;
                           }
                           return VlcError.Success;
                       }
                   }
               }
               catch(Exception ex)
               {
                   this.lastErrorMessage = ex.Message;
                   return VlcError.Exception;
               }
               return VlcError.NoObj;
           }

           public VlcError Play()
           {
               try
               {
                   using(VlcObject vobj = new VlcObject(this.vlcHandle, ObjectType.VLC_OBJECT_PLAYLIST))
                   {
                       if(vobj.SubObject != IntPtr.Zero)
                       {
                           return playlist_LockControl(vobj.SubObject, playlist_command.PLAYLIST_PLAY);
                       }
                       else
                       {
                           return VlcError.NoObj;
                       }
                   }
               }
               catch(Exception ex)
               {
                   this.lastErrorMessage = ex.Message;
                   return VlcError.Exception;
               }
           }

           public VlcError Pause()
           {
               try
               {
                   using(VlcObject vobj = new VlcObject(this.vlcHandle, ObjectType.VLC_OBJECT_PLAYLIST))
                   {
                       if(vobj.SubObject != IntPtr.Zero)
                       {
                           return playlist_LockControl(vobj.SubObject, playlist_command.PLAYLIST_PAUSE);
                       }
                       else
                       {
                           return VlcError.NoObj;
                       }
                   }
               }
               catch(Exception ex)
               {
                   this.lastErrorMessage = ex.Message;
                   return VlcError.Exception;
               }
           }

           public VlcError Stop()
           {
               try
               {
                   using(VlcObject vobj = new VlcObject(this.vlcHandle, ObjectType.VLC_OBJECT_PLAYLIST))
                   {
                       if(vobj.SubObject != IntPtr.Zero)
                       {
                           return playlist_LockControl(vobj.SubObject, playlist_command.PLAYLIST_STOP);
                       }
                       else
                       {
                           return VlcError.NoObj;
                       }
                   }
               }
               catch(Exception ex)
               {
                   this.lastErrorMessage = ex.Message;
                   return VlcError.Exception;
               }
           }

           public VlcError PlaylistClear()
           {
               try
               {
                   using(VlcObject vobj = new VlcObject(this.vlcHandle, ObjectType.VLC_OBJECT_PLAYLIST))
                   {
                       if(vobj.SubObject != IntPtr.Zero)
                       {
                           return playlist_Clear(vobj.SubObject);
                       }
                       else
                       {
                           return VlcError.NoObj;
                       }
                   }
               }
               catch(Exception ex)
               {
                   this.lastErrorMessage = ex.Message;
                   return VlcError.Exception;
               }
           }

           public VlcError ToggleVolumeMute()
           {
               IntPtr vlc = vlc_current_object(vlcHandle);
               if(IntPtr.Zero != vlc)
               {
                   try
                   {
                       return __aout_VolumeMute(vlc, IntPtr.Zero);
                   }
                   catch(Exception)
                   {
                   }
                   finally
                   {
                       __vlc_object_release(vlc);
                   }
               }
               return VlcError.NoObj;
           }

           public VlcError PressKey(string strKey)
           {
               int key = GetVlcObjectInt(ObjectType.VLC_OBJECT_VLC, strKey, -666);
               if(key != -666)
               {
                   return SetVlcObjectInt(ObjectType.VLC_OBJECT_VLC, "key-pressed", key);
               }
               return VlcError.NoVar;
           }

           public VlcError ShowMessage(String message)
           {
               try
               {
                   using(VlcObject vobj = new VlcObject(this.vlcHandle, ObjectType.VLC_OBJECT_INPUT))
                   {
                       if(vobj.SubObject != IntPtr.Zero)
                       {
                           __vout_OSDMessage(vobj.SubObject, DEFAULT_CHAN, message);
                           return VlcError.Success;
                       }
                       else
                       {
                           return VlcError.NoObj;
                       }
                   }
               }
               catch(Exception ex)
               {
                   this.lastErrorMessage = ex.Message;
                   return VlcError.Exception;
               }
           }

           public VlcError GetConfigVariable(String name, out String value)
           {
               value = null;
               using(VlcObject vlc = new VlcObject(this.vlcHandle, ObjectType.VLC_OBJECT_VLC))
               {
                   if(IntPtr.Zero == vlc.SubObject)
                   {
                       return VlcError.NoObj;
                   }

                   IntPtr p_item = config_FindConfig(vlc.SubObject, name);
                   if(IntPtr.Zero == p_item)
                   {
                       return VlcError.NoVar;
                   }

                   try
                   {
                       module_config_t mod = (module_config_t)Marshal.PtrToStructure(p_item, typeof(module_config_t));
                       switch(mod.i_type)
                       {
                       case CONFIG_ITEM.CONFIG_ITEM_BOOL:
                           {
                               bool result = (__config_GetInt(vlc.SubObject, name) == 0);
                               value = result.ToString();
                           }
                           break;
                       case CONFIG_ITEM.CONFIG_ITEM_INTEGER:
                           {
                               int intResult = __config_GetInt(vlc.SubObject, name);
                               value = intResult.ToString();
                           }
                           break;
                       case CONFIG_ITEM.CONFIG_ITEM_FLOAT:
                           {
                               float floatResult = __config_GetFloat(vlc.SubObject, name);
                               value = floatResult.ToString();
                           }
                           break;
                       case CONFIG_ITEM.CONFIG_ITEM_STRING:
                           value = __config_GetPsz(vlc.SubObject, name);
                           break;
                       default:
                           return VlcError.BadVar;
                       }
                   }
                   catch(Exception e)
                   {
                       this.lastErrorMessage = e.Message;
                       return VlcError.Exception;
                   }
               }
               return VlcError.Success;
           }

           public VlcError SetConfigVariable(String name, String value)
           {
               using(VlcObject vlc = new VlcObject(this.vlcHandle, ObjectType.VLC_OBJECT_VLC))
               {
                   if(IntPtr.Zero == vlc.SubObject)
                   {
                       return VlcError.NoObj;
                   }

                   IntPtr p_item = config_FindConfig(vlc.SubObject, name);
                   if(IntPtr.Zero == p_item)
                   {
                       return VlcError.NoVar;
                   }
                   try
                   {
                       module_config_t mod = (module_config_t)Marshal.PtrToStructure(p_item, typeof(module_config_t));
                       switch(mod.i_type)
                       {
                       case CONFIG_ITEM.CONFIG_ITEM_BOOL:
                           {
                               bool boolResult;
                               if(Boolean.TryParse(value, out boolResult))
                               {
                                   __config_PutInt(vlc.SubObject, name, boolResult ? 1 : 0);
                               }
                               else
                               {
                                   return VlcError.BadVar;
                               }
                           }
                           break;
                       case CONFIG_ITEM.CONFIG_ITEM_INTEGER:
                           {
                               int intResult;
                               if(Int32.TryParse(value, out intResult))
                               {
                                   __config_PutInt(vlc.SubObject, name, intResult);
                               }
                               else
                               {
                                   return VlcError.BadVar;
                               }
                           }
                           break;
                       case CONFIG_ITEM.CONFIG_ITEM_FLOAT:
                           {
                               float floatResult;
                               if(Single.TryParse(value, out floatResult))
                               {
                                   __config_PutFloat(vlc.SubObject, name, floatResult);
                               }
                               else
                               {
                                   return VlcError.BadVar;
                               }
                           }
                           break;
                       case CONFIG_ITEM.CONFIG_ITEM_STRING:
                           __config_PutPsz(vlc.SubObject, name, value);
                           break;
                       default:
                           return VlcError.BadVar;
                       }
                   }
                   catch(Exception e)
                   {
                       this.lastErrorMessage = e.Message;
                       return VlcError.Exception;
                   }
               }
               return VlcError.Success;
           }

           #endregion

           #region private members, properties and methods

           private static string vlcInstallDirectory = "";
           private int vlcHandle = -1;
           private Control outputWindow = null;
           private string lastErrorMessage = "";
           private int artificialLength;
           private double timeScaling;
           private GCHandle gch;
           private VarChangedCallback currentTrackCallback;
           private string previousNowPlaying = String.Empty;

           /// -------------------------------------------------------------------
           /// <summary>
           /// Method name      :   QueryVlcInstallPath
           /// Author         :   Odysee
           ///   Date         :   10.11.2006
           /// </summary>
           /// -------------------------------------------------------------------
           private static string QueryVlcInstallPath()
           {
               // open registry
               RegistryKey regkeyVlcInstallPathKey = Registry.LocalMachine.OpenSubKey(@"SOFTWARE\VideoLAN\VLC");
               if(regkeyVlcInstallPathKey == null)
                   return "";
               return (string)regkeyVlcInstallPathKey.GetValue("InstallDir","");
           }

           private void HookPlaylistChanges()
           {
               using(VlcObject vlc = new VlcObject(this.vlcHandle, ObjectType.VLC_OBJECT_PLAYLIST))
               {
                   if(vlc.SubObject != IntPtr.Zero)
                   {
                       this.gch = GCHandle.Alloc(this);
                       this.currentTrackCallback = new VarChangedCallback(CurrentTrackChanged);

                       int isSet = __var_AddCallback(vlc.SubObject, Playlist_Current,
                           this.currentTrackCallback, (IntPtr)this.gch);
                       //Debug.WriteLine("__var_AddCallback playlistObject = " + isSet.ToString());
                   }
               }
           }

           private void UnhookPlaylistChanges()
           {
               using(VlcObject vlc = new VlcObject(this.vlcHandle, ObjectType.VLC_OBJECT_PLAYLIST))
               {
                   if(vlc.SubObject != IntPtr.Zero)
                   {
                       __var_DelCallback(vlc.SubObject, Playlist_Current,
                           this.currentTrackCallback, (IntPtr)this.gch);
                   }
               }
               this.gch.Free();
           }

           private static int CurrentTrackChanged(IntPtr vlc, String variable, vlc_value_t old_val,
               vlc_value_t new_val, IntPtr param)
           {
               //Debug.WriteLine("CurrentTrackChanged: " + new_val.i_int.ToString());
               GCHandle gch = (GCHandle)param;
               NativeLibVlc thisVlc = (NativeLibVlc)gch.Target;
               try
               {
                   using(VlcObject vobj = new VlcObject(thisVlc.vlcHandle, ObjectType.VLC_OBJECT_INPUT))
                   {
                       if(vobj.SubObject != IntPtr.Zero)
                       {
                           IntPtr resultString = IntPtr.Zero;
                           input_Control(vobj.SubObject, input_query_e.INPUT_GET_INFO,
                               Meta_information, Now_Playing, ref resultString);
                           String nowPlaying = Marshal.PtrToStringAnsi(resultString);
                           if(nowPlaying != thisVlc.previousNowPlaying)
                           {
                               thisVlc.previousNowPlaying = nowPlaying;
                               Debug.WriteLine(String.Format("nowPlaying: {0}", nowPlaying));
                               thisVlc.VlcNowPlayingChanged(nowPlaying);
                           }
                       }
                   }
               }
               catch(Exception ex)
               {
                   thisVlc.lastErrorMessage = ex.Message;
               }
               return (int)VlcError.Success;
           }

           #endregion
       }

       /* future features

       add_bool( "brightness-threshold", 0, NULL,
                 THRES_TEXT, THRES_LONGTEXT, VLC_FALSE );
        */
   }
