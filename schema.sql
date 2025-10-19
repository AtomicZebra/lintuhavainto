CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
);

CREATE TABLE sighting (
    id INTEGER PRIMARY KEY,
    bird_species TEXT,
    municipality TEXT,
    location TEXT,
    additional_info TEXT,
    user_id INTEGER REFERENCES users,
    time_added TEXT
);

CREATE TABLE thread(
    id INTEGER PRIMARY KEY,
    sight_id INTEGER REFERENCES sighting,
    user_id INTEGER REFERENCES users,
    message TEXT,
    time_sent TEXT
);

CREATE TABLE classes (
    id INTEGER PRIMARY KEY,
    title TEXT,
    value TEXT
);

CREATE TABLE sighting_classes (
    id INTEGER PRIMARY KEY,
    sight_id INTEGER REFERENCES sighting,
    title TEXT,
    value TEXT
);