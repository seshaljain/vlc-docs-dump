{{example codefor=.Net Interface to VLC}} <syntaxhighlight
lang="csharp">
/*************************************************************************\***\*
\* VlcUserControl.cs: VlcUserControl partial class
definition**\ \***********************************************************************\*\ **\*
\* Copyright (C) 2006 Chris Meadowcroft \* \* Authors: Chris Meadowcroft
\* \* This program is free software; you can redistribute it and/or
modify \* it under the terms of the GNU Lesser General Public License as
published by \* the Free Software Foundation. \* \* This program is
distributed in the hope that it will be useful, \* but WITHOUT ANY
WARRANTY; without even the implied warranty of \* MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the \* GNU General Public License
for more details. \* \* You should have received a copy of the GNU
Lesser General Public License \* along with this program; if not, write
to the Free Software \* Foundation, Inc., 51 Franklin Street, Fifth
Floor, Boston MA 02110-1301,
USA.**\ \***************************************************************************/

namespace VLanControl { partial class VlcUserControl { /// <summary> ///
Required designer variable. /// </summary> private
System.ComponentModel.IContainer components = null;

   /// <summary> /// Clean up any resources being used. /// </summary>
   /// <param name="disposing">true if managed resources should be
   disposed; otherwise, false.</param> protected override void
   Dispose(bool disposing) { if(disposing) { this.nativeVlc.Dispose();
   if(components != null) { components.Dispose(); } }
   base.Dispose(disposing); }

   #region Component Designer generated code

   /// <summary> /// Required method for Designer support - do not
   modify /// the contents of this method with the code editor. ///
   </summary> private void InitializeComponent() { this.innerVlc = new
   VLanControl.InnerVlcWindow(); this.topBlocker = new
   System.Windows.Forms.Panel(); this.leftBlocker = new
   System.Windows.Forms.Panel(); this.rightBlocker = new
   System.Windows.Forms.Panel(); this.bottomBlocker = new
   System.Windows.Forms.Panel(); this.SuspendLayout(); // // innerVlc //
   this.innerVlc.Location = new System.Drawing.Point(31, 36);
   this.innerVlc.Name = "innerVlc"; this.innerVlc.Size = new
   System.Drawing.Size(82, 64); this.innerVlc.TabIndex = 0; // //
   topBlocker // this.topBlocker.Location = new System.Drawing.Point(26,
   10); this.topBlocker.Name = "topBlocker"; this.topBlocker.Size = new
   System.Drawing.Size(100, 17); this.topBlocker.TabIndex = 1;
   this.topBlocker.Visible = false; // // leftBlocker //
   this.leftBlocker.Location = new System.Drawing.Point(8, 33);
   this.leftBlocker.Name = "leftBlocker"; this.leftBlocker.Size = new
   System.Drawing.Size(18, 83); this.leftBlocker.TabIndex = 2;
   this.leftBlocker.Visible = false; // // rightBlocker //
   this.rightBlocker.Location = new System.Drawing.Point(126, 29);
   this.rightBlocker.Name = "rightBlocker"; this.rightBlocker.Size = new
   System.Drawing.Size(18, 78); this.rightBlocker.TabIndex = 2;
   this.rightBlocker.Visible = false; // // bottomBlocker //
   this.bottomBlocker.Location = new System.Drawing.Point(30, 118);
   this.bottomBlocker.Name = "bottomBlocker"; this.bottomBlocker.Size =
   new System.Drawing.Size(100, 17); this.bottomBlocker.TabIndex = 2;
   this.bottomBlocker.Visible = false; // // VlcUserControl //
   this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
   this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
   this.Controls.Add(this.rightBlocker);
   this.Controls.Add(this.leftBlocker);
   this.Controls.Add(this.bottomBlocker);
   this.Controls.Add(this.topBlocker); this.Controls.Add(this.innerVlc);
   this.Name = "VlcUserControl"; this.Resize += new
   System.EventHandler(this.VlcUserControl_Resize);
   this.ResumeLayout(false);

   }

   #endregion

   private InnerVlcWindow innerVlc; private System.Windows.Forms.Panel
   topBlocker; private System.Windows.Forms.Panel leftBlocker; private
   System.Windows.Forms.Panel rightBlocker; private
   System.Windows.Forms.Panel bottomBlocker;

..

   }

} </syntaxhighlight>
