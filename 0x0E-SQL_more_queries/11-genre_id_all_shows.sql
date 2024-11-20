-- This script lists all TV shows and their associated genre IDs from the hbtn_0d_tvshows database.
-- Shows without genres will have a genre_id of NULL.
-- The results are sorted by show title and genre ID in ascending order.

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;

