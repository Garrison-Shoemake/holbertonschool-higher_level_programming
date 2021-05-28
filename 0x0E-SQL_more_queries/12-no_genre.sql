-- lists shows contained in database by specific parameters:
-- displays tv_shows.title, and tv_show_genres.genre_id
-- sorted in ASC by tv_shows.title and tv_show_genres.genre_id
SELECT title, genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON id = show_id
WHERE genre_id IS NULL;
