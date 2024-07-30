-- CREATE DATABASE
-- CREATE TABLE
-- GRANT PERMISSION
CREATE DATABASE IF NOT EXISTS tyrell_corp;
USE tyrell_corp;
CREATE TABLE nexus6
  (id INT,
   name VARCHAR(255));
INSERT INTO nexus6 (id, name) VALUES
  (1, "Leon");
GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';
