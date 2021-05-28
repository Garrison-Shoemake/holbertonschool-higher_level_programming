-- a script that shows all shows contained in the dumped database
-- shows all that have at least one genre linked
-- ordered in ASC by tv title and genre id
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genre
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
