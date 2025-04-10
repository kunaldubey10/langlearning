-- Create the database
DROP DATABASE IF EXISTS language_portal;
CREATE DATABASE language_portal;
USE language_portal;

-- Users table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Lessons table
CREATE TABLE IF NOT EXISTS lessons (
    id INT AUTO_INCREMENT PRIMARY KEY,
    course_id INT,
    lesson_title VARCHAR(255),
    youtube_url TEXT
);

-- Questions table
CREATE TABLE IF NOT EXISTS questions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    language VARCHAR(50),
    question_text TEXT
);

-- Options table (for MCQs)
CREATE TABLE IF NOT EXISTS options (
    id INT AUTO_INCREMENT PRIMARY KEY,
    question_id INT,
    option_text TEXT,
    is_correct BOOLEAN,
    FOREIGN KEY (question_id) REFERENCES questions(id) ON DELETE CASCADE
);

-- Vocabulary table
CREATE TABLE IF NOT EXISTS vocabulary (
    id INT AUTO_INCREMENT PRIMARY KEY,
    language VARCHAR(50),
    word VARCHAR(100),
    meaning TEXT,
    audio_url TEXT,
    date_added DATE
);

-- ================================
-- 🔽 INSERT SAMPLE DATA
-- ================================

-- Lessons (YouTube videos)
INSERT INTO lessons (course_id, lesson_title, youtube_url) VALUES
(1, 'Spanish Basics - Greetings', 'https://www.youtube.com/watch?v=8dEbr2vP8jA'),
(2, 'French Basics - Introductions', 'https://www.youtube.com/watch?v=fypjBpN6qKk'),
(3, 'Japanese Basics - Hiragana', 'https://www.youtube.com/watch?v=6p9Il_j0zjc');

-- Vocabulary Words
INSERT INTO vocabulary (language, word, meaning, audio_url, date_added) VALUES
('Spanish', 'Hola', 'Hello', NULL, CURDATE()),
('French', 'Bonjour', 'Good Morning', NULL, CURDATE()),
('Japanese', 'ありがとう (Arigatou)', 'Thank You', NULL, CURDATE());

-- Quiz Questions
INSERT INTO questions (language, question_text) VALUES
('Spanish', 'What is the Spanish word for "Hello"?'),
('French', 'What does "Bonjour" mean in French?'),
('Japanese', 'What does "ありがとう (Arigatou)" mean in Japanese?');

-- Options for Spanish
INSERT INTO options (question_id, option_text, is_correct) VALUES
(1, 'Hola', TRUE),
(1, 'Merci', FALSE),
(1, 'Bonjour', FALSE);

-- Options for French
INSERT INTO options (question_id, option_text, is_correct) VALUES
(2, 'Thank You', FALSE),
(2, 'Good Morning', TRUE),
(2, 'Goodbye', FALSE);

-- Options for Japanese
INSERT INTO options (question_id, option_text, is_correct) VALUES
(3, 'Thank You', TRUE),
(3, 'Good Night', FALSE),
(3, 'See You', FALSE);
