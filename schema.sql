CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
);

CREATE TABLE items (
    id INTEGER PRIMARY KEY,
    bird_species TEXT,
    municipality TEXT,
    location TEXT,
    additional_info TEXT,
    user_id INTEGER REFERENCES users,
    time_added TEXT
);