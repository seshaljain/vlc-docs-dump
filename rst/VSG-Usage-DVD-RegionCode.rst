== Play a DVD of a different region code.<br> ==

If you want to play a DVD which has a region code other than you, try to
test your DVD drive to can crack the other region code which you don't
have.

The most newer drives are RPC2 drives and you probably have this one.
These drives don't allow raw access until the drive's firmware has done
a region check, but in this particular case you don't have the right
code, so the region check will fail.

VLC uses libdvdcss who needs raw access to the DVD drive to crack the
encryption keys. But RPC2 doesn't allow you to use these raw access so
you can't get the region code and therefore you can't play your DVD. So
it's impossible to circumvent the region code if you have this kind of
drives. If you have a RPC2 which allows raw access, you can crack the
region code.

It´ll just take a long time to crack. If you have the first mentioned
RPC2, you can try to flash your firmware. The problem is, that there
sometimes isn't any alternative firmware for your drive.<br>
