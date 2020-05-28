{{Back to|Hacker Guide}}

{{Under construction}}

== Introduction ==

{{VLC}} has a powerful "object variable" infrastructure, that can be
used to pass information between modules.

It can be compared to an [[wikipedia:Observer pattern|observer
pattern]].

== Variable Functions ==

=== var_Get ===

'''va_Get*''' functions will get the value if the variable exists (and
will error otherwise).

   var_Get ( vlc_object_t *, const char*, vlc_value_t \* ); var_GetBool(
   p_obj, psz_name ); var_GetInteger( p_obj, psz_name ); var_GetTime(
   p_obj, psz_name ); var_GetFloat( p_obj, psz_name ); var_GetString(
   p_obj, psz_name ); var_GetNonEmptyString( p_obj, psz_name );
   var_GetAddress( p_obj, psz_name );

=== var_Inherit === '''var_Inherit*''' functions will get the default
value (from configuration, for example) or the one set by the parent
object.

This is the function you will want to use most of the time if you are
unsure.

General prototype:
   <type> var_Inherit<type>( vlc_object_t *obj, const char*\ name );

You are responsible for freeing any strings used.

   var_Inherit var_InheritBool var_InheritInteger var_InheritFloat
   var_InheritString var_InheritTime var_InheritAddress
   var_InheritURational

====Example==== Reading the "volume-step" configuration option:

   float volumeStep = var_InheritFloat( p_this, "volume-step" );

=== var_CreateGet ===

'''var_CreateGet*''' functions will create the variable and the get the
default value if the variable wasn't already created.

If the variable does exist before the call it will get the current value
(and increment its [[wikipedia:en:Refcount|refcount]]).

   var_Create(a,b,c) var_CreateGetInteger(a,b) var_CreateGetBool(a,b)
   var_CreateGetTime(a,b) var_CreateGetFloat(a,b)
   var_CreateGetString(a,b) var_CreateGetNonEmptyString(a,b)
   var_CreateGetAddress(a,b) var_CreateGetIntegerCommand(a,b)
   var_CreateGetBoolCommand(a,b) var_CreateGetTimeCommand(a,b)
   var_CreateGetFloatCommand(a,b) var_CreateGetStringCommand(a,b)
   var_CreateGetNonEmptyStringCommand(a,b)

A variable must be created if you want to add a callback or change the
value&nbsp;(with <code>var_Set</code>) of a variable <br>

{{Hacker_Guide}}
