-- This script lists all TV shows without any genre linked from the hbtn_0d_tvshows database.
-- The results are sorted by the show title and genre_id in ascending order.
-- Shows without genres will have a genre_id of NULL.

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id;

