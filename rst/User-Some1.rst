Some1, on the mini tasks it said there was a request for Windows remote
compatibility. The easiest way to do this is to receive the
WM_APPACTIVATE in a Windows message loop and check the wParam and lParam
arguments to determine what kind of message was received. This will also
enable VLC to work with media keyboards. I will see what I can do
personally with the code. [[User:Stinkman|Stinkman]] 00:25, 4 November
2007 (CET)
