.. raw:: mediawiki

   {{example code|l=LGPL|for=.Net Interface to VLC}}

.. code:: csharp

   /*****************************************************************************
    * InnerVlcWindow.Designer.cs: InnerVlcWindow class definition
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
   namespace VLanControl
   {
       partial class InnerVlcWindow
       {
           /// <summary> 
           /// Required designer variable.
           /// </summary>
           private System.ComponentModel.IContainer components = null;

           /// <summary> 
           /// Clean up any resources being used.
           /// </summary>
           /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
           protected override void Dispose(bool disposing)
           {
               if(disposing && (components != null))
               {
                   components.Dispose();
               }
               base.Dispose(disposing);
           }

           #region Component Designer generated code

           /// <summary> 
           /// Required method for Designer support - do not modify 
           /// the contents of this method with the code editor.
           /// </summary>
           private void InitializeComponent()
           {
               components = new System.ComponentModel.Container();
               this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
           }

           #endregion
       }
   }


