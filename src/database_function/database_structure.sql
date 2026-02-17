DROP DATABASE IF EXISTS favorites_futurama;
CREATE DATABASE IF NOT EXISTS favorites_futurama;
USE favorites_futurama;

CREATE TABLE characters_fav (
    id INT UNSIGNED PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    gender VARCHAR(20),
    image_url VARCHAR(120)
);

CREATE TABLE users (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    email VARCHAR(120) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    rol VARCHAR(100)
);

-- Tabla intermedia muchos a muchos (usuario - personaje favorito)
CREATE TABLE characters_saved (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    user_id INT UNSIGNED NOT NULL,
    character_id INT UNSIGNED NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (character_id) REFERENCES characters_fav(id)
);
