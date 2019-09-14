
CREATE TABLE users(
   user_id serial PRIMARY KEY,
   full_name VARCHAR (100) NOT NULL,
   email VARCHAR (50) NOT NULL,
   created_on TIMESTAMP NOT NULL
);

INSERT INTO users (full_name, email, created_on) VALUES ('First CAES fake user', 'fake@fake.com', current_timestamp);
