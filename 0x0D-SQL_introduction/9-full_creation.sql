-- script that creates a table with multiple rows
CREATE TABLE IF NOT EXISTS second_table(id INT, name VARCHAR(256), score INT);
INSERT INTO second_table (`id`, `name`, `score`) VALUES (1, "John", 10);
INSERT INTO second_table (`id`, `name`, `score`) VALUES (3, "Alex", 3);
INSERT INTO second_table (`id`, `name`, `score`) VALUES (14, "Bob", 14);
INSERT INTO second_table (`id`, `name`, `score`) VALUES (8, "George", 8);
