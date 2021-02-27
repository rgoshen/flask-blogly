
-- in terminal:
-- psql < users.sql
-- psql blogly

DROP DATABASE IF EXISTS  blogly;

CREATE DATABASE blogly;

\c blogly

CREATE TABLE users
(
  id SERIAL PRIMARY KEY,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  img_url TEXT NOT NULL );

INSERT INTO users
(first_name, last_name, img_url)
VALUES
('Alan', 'Alda', 'https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png'),
('Joel', 'Burton', 'https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png'),
('Jane', 'Smith', 'https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png');
