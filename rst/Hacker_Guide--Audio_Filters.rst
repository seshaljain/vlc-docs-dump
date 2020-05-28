{{Back to|Hacker Guide}}

==Writing an audio filter==

===Module descriptor=== <syntaxhighlight lang="c"> static int Open (
[vlc_object_t] *p_this ); static void Close ( [vlc_object_t]*\ p_this );
static block_t *DoWork (filter_t*\ filter, block_t \*block)

   vlc_module_begin()
      set_description( `N <>`__\ ("audio filter x") ) set_shortname(
      `N <>`__\ ("audio filter x") ) set_category( CAT_AUDIO )
      set_subcategory( SUBCAT_AUDIO_AFILTER ) add_shortcut( "afx" )
      set_capability( "audio filter", 0 ) set_callbacks( Open, Close )

   vlc_module_end()

</syntaxhighlight>

===I/O Buffers=== Data comes in and out the plugin in an
[https://www.videolan.org/developers/vlc/doc/doxygen/html/structaout__buffer__t.html
aout_buffer_t], one sample at a time, and in each sample, one block by
channel.

{\| class="wikitable center" data stream \| ch 1 \| ch 2 \| ch 1 \| ch 2
\| ch 1 \| ch 2 \| &hellip; samples \| colspan="2" \| Sample 1 \|
colspan="2" \| Sample 2 \| colspan="2" \| Sample 3 \| &hellip; \|}

An audio filter module is constituted of a constructor, a destructor,
and a <code>p_filter->pf_do_work</code> function. The constructor is
passed a p_filter structure, and it returns 0 if it is able to do the
whole transformation between <code>p_filter->input</code> and
<code>p_filter->output</code>. If you can do only part of the
transformation, say you can't do it (if the aout core doesn't find a
fitting filter, it will split the transformation and ask you again).

===Note===

Audio filters can be of three types :

-  Converters : change <code>i_format</code> (for instance from float32
   to s16).
-  Resamplers : change <code>i_rate</code> (for instance from 48 kHz to
   44.1 kHz).
-  Channel mixers : change
   <code>i_physical_channels</code>/<code>i_original_channels</code>
   (for instance from 5.1 to stereo).

Audio filters can also combine any of these types. For instance you can
have an audio filter which transforms [[A/52]] 5.1 to float32 stereo.

The constructor must also set <code>p_filter->b_in_place</code>. If it's
<code>0</code>, the aout core will allocate a new buffer for the output.
If it's <code>1</code>, when you write a byte in the output buffer, it
destroys the same byte in the input buffer (they share the same memory
area). Some filters can work in place because they just do a linear
transformation (like <code>float32->s16</code>), but most filters will
want <code>b_in_place = 0</code>. The filter can allocate private data
in <code>p_filter->p_sys</code>. Do not forget to deallocate it in the
destructor.

The <code>p_filter->pf_do_work</code> gets an input and an output buffer
as arguments, and process them. At the end of the processing, do not
forget to set <code>p_out_buf->i_nb_samples</code> and
<code>p_out_buf->i_nb_bytes</code>, since they aren't inited by the aout
core (their values can change between input and output and it's not
quite predictable).

==Writing an audio mixer==

Writing an audio mixer is very similar to writing an audio filter. The
only difference is that you have to deal with the input buffers
yourself, and request for new buffers when you need to. Between two
calls to <code>pf_do_work</code>, the position in the buffer is
remembered in <code>p_input->p_first_byte_to_mix</code> (it isn't always
the start of the buffer, since input and output buffers can be of
different length). It is your job to set this pointer at the end of
<code>pf_do_work</code>.

For more details, please have a look at the float32 mixer. It's much
more understandable than lines of documentation.

{{Hacker Guide}}
