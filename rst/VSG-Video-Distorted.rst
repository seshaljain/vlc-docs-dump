The video runs but the picture is distorted.
--------------------------------------------

| 
| There is probably a problem with the output layer. There are several ways of troubleshooting it. First, try with another output plugin, for instance:

| 
| % vlc -V sdl
| % vlc -V x11

| 
| Second, change your screen depth and/or definition. It quite often helps.

| Lastly, if running Unix, have a look at your X.Org video driver.
| 
