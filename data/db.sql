-- Active: 1729175559053@@127.0.0.1@3306@political_ai
CREATE DATABASE political_AI DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE political_AI;

CREATE TABLE news_links (
    id INT AUTO_INCREMENT PRIMARY KEY,
    published_at DATETIME,
    source VARCHAR(100),
    url VARCHAR(512) NOT NULL UNIQUE
);

SELECT * FROM news_links LIMIT 100