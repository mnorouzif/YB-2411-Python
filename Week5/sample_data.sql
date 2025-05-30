
CREATE DATABASE IF NOT EXISTS userdb;
USE userdb;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    age INT
);

INSERT INTO users (name, email, age) VALUES
('John Doe', 'john@example.com', 28),
('Jane Smith', 'jane@example.com', 34);
