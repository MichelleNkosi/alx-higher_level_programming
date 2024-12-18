-- This script lists all genres from the hbtn_0d_tvshows database and displays
-- the number of shows linked to each genre.
-- The results are sorted in descending order by the number of shows linked to each genre.
-- Only genres with at least one show linked will be displayed.

SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
HAVING COUNT(tv_show_genres.show_id) > 0
ORDER BY number_of_shows DESC;

