/\* Styling links to www.VideoLan.org \*/ /*#bodyContent a.external, #bodyContent a[href^="http://www.videolan.org/"] {

| ``   -moz-background-clip:border;``
| ``   -moz-background-inline-policy:continuous;``
| ``   -moz-background-origin:padding;``
| ``   background:transparent url(//www.videolan.org/favicon.ico) no-repeat scroll right center;``
| ``   padding-right:13px;``

}*/ /\* Shows |Folder_icon.gif| 2 pixels to the right of element for `Template:VLCSourceFolder <Template:VLCSourceFolder>`__.

``  To replace existing link icons use this with class plainlinks. */``

.folder-icon {

| `` background: transparent no-repeat url('``\ ```https://wiki.videolan.org/images/Folder_icon.gif`` <https://wiki.videolan.org/images/Folder_icon.gif>`__\ ``') center right;``
| `` padding-right: 18px;``

}

/\* Don't use these classes. See https://en.wikipedia.org/wiki/Wikipedia:HiddenStructure \*/ .hiddenStructure, .if {display: none}

/\* wikitable/prettytable class for skinning normal tables \*/ /\* wikitable is already defined in load.php -- this adds 1em right margin \*/ table.wikitable, table.prettytable {

| `` margin: 1em 1em 1em 0;``
| `` background: #f9f9f9;``
| `` border: 1px solid #aaa;``
| `` border-collapse: collapse;``

}

/\* table.wikitable already defined in load.php, skipping \*/ table.prettytable th, table.prettytable td {

| `` border: 1px solid #aaa;``
| `` padding: 0.2em;``

}

/\* table.wikitable already defined in load.php, skipping \*/ table.prettytable th {

| `` background: #f2f2f2;``
| `` text-align: center;``

}

/\* pad table elements -- cellpadding is obsolete \*/ table.cellpadding-1px th, table.cellpadding-1px td, table.wikitable.cellpadding-1px th, table.wikitable.cellpadding-1px td, table.prettytable.cellpadding-1px th, table.prettytable.cellpadding-1px td { padding: 1px; } table.cellpadding-2px th, table.cellpadding-2px td, table.wikitable.cellpadding-2px th, table.wikitable.cellpadding-2px td table.prettytable.cellpadding-2px th, table.prettytable.cellpadding-2px td { padding: 2px; } table.cellpadding-3px th, table.cellpadding-3px td, table.wikitable.cellpadding-3px th, table.wikitable.cellpadding-3px td, table.prettytable.cellpadding-3px th, table.prettytable.cellpadding-3px td { padding: 3px; } table.cellpadding-1em th, table.cellpadding-1em td, table.wikitable.cellpadding-1em th, table.wikitable.cellpadding-1em td, table.prettytable.cellpadding-1em th, table.prettytable.cellpadding-1em td { padding: 1em; }

/\* `Template:Module <Template:Module>`__ style \*/ table.wikitable.template-module {

| ``  width: 325px;``
| ``  float: right;``
| ``  clear: right;``
| ``  margin: 0.5em;``
| ``  padding: 0.2em;``
| ``  font-size: 95%;``

} table.wikitable.template-module > \* > tr > td {

| ``  color: black;``
| ``  background: #eee;``

}

/\* Infobox template style \*/

.infobox {

| ``  border: 1px solid #aaa;``
| ``  color: black;``
| ``  background-color: #f9f9f9;``
| ``  margin-bottom: 0.5em;``
| ``  margin-left: 1em;``
| ``  padding: 0.2em;``
| ``  float: right;``
| ``  clear: right;``

} .infobox td, .infobox th {

``  vertical-align: top;``

} .infobox caption {

``  font-size: larger;``

}

/\* For `Template:Side box <Template:Side_box>`__. Renamed from .infobox.sisterproject \*/ .infobox.sidebox {

| ``  width: 250px;``
| ``  font-size: 90%;``
| ``  padding: 4px;``

}

/\* For `Template:Side box <Template:Side_box>`__. Counter MediaWiki CSS shifting bulleted items right by 1.5em \*/ .infobox-singleitem {

| ``  text-align: start;``
| ``  margin-left: 4.0em;``

} .infobox-multipleitem {

| ``  text-align: start;``
| ``  margin-left: 2.5em;``

} /\* For `Template:Documentation streaming howto toc <Template:Documentation_streaming_howto_toc>`__, `Template:Documentation toc <Template:Documentation_toc>`__ and `Template:Documentation TOC <Template:Documentation_TOC>`__ \*/ .tocsidebar {

| ``  font-size: 80%;``
| ``  border: 1px solid #aaa;``
| ``  padding: 5px;``

}

.widebox {

| ``   width: 80%;``
| ``   border: 1px solid #999;``
| ``   background: #f8f8f8;``
| ``   clear: both;``
| ``   padding: 2px;``
| ``   margin-left: auto;``
| ``   margin-right: auto;``

} .nowrap {

``   white-space: nowrap;``

} .hatnote {

| ``   font-style: italic;``
| ``   margin-left: 1.5em;``

} /\* pre tags do not clip content \*/

#. bodyContent pre {

| ``   white-space: pre-wrap;``
| ``   word-break: break-all;``

} /\* For `VLC Features Formats <VLC_Features_Formats>`__ and others \*/ .codec-table {

| ``   font-size: small;``
| ``   text-align: center;``
| ``   width: 100%;``
| ``   margin: 1em auto;``
| ``   border-width: 1px;``

} /\* For `Template:Banner <Template:Banner>`__:

``  Styling for the block element or table cell that holds banner-title and banner-subtitle */``

.banner-text {

| ``   width: 56%;``
| ``   background: none;``

} /\* For `Template:Banner <Template:Banner>`__ \*/ .banner-title {

| ``   font-size: 162%;``
| ``   margin: 0;``
| ``   padding: .1em;``

} /\* For `Template:Banner <Template:Banner>`__ \*/ .banner-subtitle {

| ``   top: +0.2em;``
| ``   font-size: 95%;``

} /\* For `Template:Banner <Template:Banner>`__ \*/ .banner {

| ``   width: 100%;``
| ``   margin: 0 auto 10px;``
| ``   color: black;``
| ``   background-color: #fcfcfc;``
| ``   border: 1px solid #ccc;``

} /\* For `Template:Banner <Template:Banner>`__ \*/ .banner-links-col1 {

| ``   width: 11%;``
| ``   font-size: 95%;``

} /\* For `Template:Banner <Template:Banner>`__ \*/ .banner-links-col2 {

| ``   width: 14%;``
| ``   font-size: 95%;``

} /\* For `Template:Banner <Template:Banner>`__ \*/ .banner-links-col3 {

| ``   width: 18%;``
| ``   font-size: 95%;``

} [class|=banner-links] {

``   vertical-align: top;``

} /\* General use \*/ div.plainlist ul > li {

``   list-style: none none;``

} /\* Creates two columns \*/ div.col2 {

| ``   -webkit-column-count: 2;``
| ``      -moz-column-count: 2;``
| ``        -o-column-count: 2;``
| ``           column-count: 2;``

} /\* Creates three columns \*/ div.col3 {

| ``   -webkit-column-count: 3;``
| ``      -moz-column-count: 3;``
| ``        -o-column-count: 3;``
| ``           column-count: 3;``

} /\* Creates four columns \*/ div.col4 {

| ``   -webkit-column-count: 4;``
| ``      -moz-column-count: 4;``
| ``        -o-column-count: 4;``
| ``           column-count: 4;``

} /\* Creates five columns \*/ div.col5 {

| ``   -webkit-column-count: 5;``
| ``      -moz-column-count: 5;``
| ``        -o-column-count: 5;``
| ``           column-count: 5;``

} /\* Creates six columns \*/ div.col6 {

| ``   -webkit-column-count: 6;``
| ``      -moz-column-count: 6;``
| ``        -o-column-count: 6;``
| ``           column-count: 6;``

} /\* Creates seven columns \*/ div.col7 {

| ``   -webkit-column-count: 7;``
| ``      -moz-column-count: 7;``
| ``        -o-column-count: 7;``
| ``           column-count: 7;``

}

.. |Folder_icon.gif| image:: Folder_icon.gif

