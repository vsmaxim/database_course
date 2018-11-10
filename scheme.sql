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

CREATE TABLE dog (
  id            SERIAL PRIMARY KEY,
  fancy_name    VARCHAR(64) NOT NULL,
  age           INTEGER CHECK (age > 0)
);

CREATE TABLE participant (
  id          SERIAL PRIMARY KEY,
  first_name  VARCHAR(64) NOT NULL,
  middle_name VARCHAR(64) NOT NULL,
  last_name   VARCHAR(64) NOT NULL
);

CREATE TABLE breed (
  id   SERIAL PRIMARY KEY,
  name VARCHAR(128) NOT NULL
);

CREATE TABLE ring (
  id SERIAL PRIMARY KEY
);

CREATE TABLE experts (
  id SERIAL PRIMARY KEY
);

CREATE TABLE prizes (
  id SERIAL PRIMARY KEY,
  place   SMALLINT CHECK (place >= 1 AND place <= 3)
);

ALTER TABLE dog
    ADD COLUMN fathers_breed_id INTEGER REFERENCES breed,
    ADD COLUMN mothers_breed_id INTEGER REFERENCES breed,
    ADD COLUMN breed_id INTEGER REFERENCES breed;

ALTER TABLE participant
    ADD COLUMN dog_id INTEGER REFERENCES dog UNIQUE,
    ADD COLUMN club_id INTEGER REFERENCES club;

ALTER TABLE experts
    ADD COLUMN participant_id INTEGER REFERENCES participant UNIQUE,
    ADD COLUMN ring_id INTEGER REFERENCES ring UNIQUE;

ALTER TABLE ring
  ADD COLUMN breed_id INTEGER REFERENCES breed UNIQUE;

ALTER TABLE prizes
    ADD COLUMN dog_id INTEGER REFERENCES dog UNIQUE,
    ADD COLUMN ring_id INTEGER REFERENCES ring,
    ADD UNIQUE (place, ring_id);

