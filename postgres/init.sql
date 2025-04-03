-- Create database and user
CREATE DATABASE va2ptdb;
ALTER USER va2pt WITH PASSWORD 'va2ptpass';
GRANT ALL PRIVILEGES ON DATABASE va2ptdb TO va2pt;
