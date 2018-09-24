-- Drop all tables from postgres magic

DROP SCHEMA public CASCADE;
CREATE SCHEMA public;
GRANT ALL ON SCHEMA public to postgres;
GRANT ALL ON SCHEMA public to public;

-- Table definitions

CREATE TABLE club (
  id   SERIAL PRIMARY KEY,
  name VARCHAR(64) NOT NULL
);

CREATE TABLE participant (
  id          SERIAL PRIMARY KEY,
  club_id     INTEGER REFERENCES club,
  first_name  VARCHAR(64) NOT NULL,
  middle_name VARCHAR(64) NOT NULL,
  last_name   VARCHAR(64) NOT NULL
);

CREATE TABLE breed (
  id   SERIAL PRIMARY KEY,
  name VARCHAR(128) NOT NULL
);

CREATE TABLE ring (
  id SERIAL PRIMARY KEY,
  breed_id INTEGER REFERENCES breed
);

CREATE TABLE dog (
  id            SERIAL PRIMARY KEY,
  fancy_name    VARCHAR(64) NOT NULL,
  age           INTEGER CHECK (age > 0),
  fathers_breed INTEGER REFERENCES breed,
  mothers_breed INTEGER REFERENCES breed
);

CREATE TABLE experts (
  participant_id INTEGER REFERENCES participant UNIQUE,
  ring_id        INTEGER REFERENCES ring
);

CREATE TABLE prizes (
  id SERIAL PRIMARY KEY,
  dog_id  INTEGER REFERENCES dog UNIQUE,
  place   SMALLINT CHECK (place >= 1 AND place <= 3),
  ring_id INTEGER REFERENCES ring
);