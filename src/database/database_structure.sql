CREATE DATABASE if not exists favorites_futurama;
use favorites_futurama;

CREATE TABLE favorites(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    gender VARCHAR(20)
);

CREATE TABLE users (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    email VARCHAR(120) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    rol VARCHAR(100),
    favorites_id INT UNSIGNED,
    FOREIGN KEY (favorites_id) REFERENCES favorites(id)
)

