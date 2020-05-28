{{howtonocat=y}} {{Historical|Use the interface at
http://www.videolan.org/vlc/skins.php}}

<div class="widebox" style="border-color: red;"> This page is designed
for those with access to videolan@ganesh.videolan.org. </div>

Skins are on ganesh. Log on ganesh as videolan.

== Add a skin == Download the skin and its image in
~videolan/www/vlc/skins2/

Connect to the postgresql database:
   % psql -d www-videolan

Add the skin to the skins table:
   INSERT INTO skins (name,min_version,author,image,url) VALUES
   ('<name>','<VLC version number>','<author>','<image name>','<vlt
   name>');

And rate the skin:
   INSERT INTO "skins-rating" (skin_id,rating) VALUES ((SELECT
   LAST_VALUE FROM skins_id_seq), '5');

(ratings can be 1, 2, 3, 4 or 5, 5 being the best rating) We need to
rate the skin at least once or it won't appear on the webpage (unless
someone fixes the SQL query).

Add a thumbnail for the skin, add it to the skin pack and update the skins size in the database:
   % skins-update

== Update a skin == Download the new skin and its new image in
~videolan/www/vlc/skins2/. Be sure the image and the skin have the same
name.

Connect to the postgresql database:
   % psql -d www-videolan

When connected, find the id of the skins like that
   % SELECT Id FROM skins WHERE name LIKE '<name>%';

Check that you only got ONE id. :D

And update the time
   % UPDATE skins SET date_modified = date(now()) WHERE id = <id>;

If needed, update the minimum VLC version requirement too
   % UPDATE skins SET min_version = '<the version>' WHERE id = <id>;

Update the thumbnail and size for the skin, update the skin pack:
   % skins-update

[[Category:Roots]] [[Category:Proposed deletion]]
