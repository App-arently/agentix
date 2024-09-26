```sql
-- Creating database named 'game_scores'
CREATE DATABASE IF NOT EXISTS game_scores;
USE game_scores;

-- Creating table 'high_scores' 
CREATE TABLE IF NOT EXISTS high_scores (
    -- unique id for each score entry
    id INT AUTO_INCREMENT PRIMARY KEY,
    -- player's user id
    user_id INT NOT NULL,
    -- game_id identifying the game
    game_id INT NOT NULL,
    -- player's score, assuming score as integer
    score INT NOT NULL,
    -- timestamp of the score submission
    score_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    -- Foreign key referencing to user table to ensure the player exists Also, ON DELETE CASCADE will automatically delete score when the user gets deleted
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    -- Foreign key referencing to game table to ensure the game exists Also, this keeps game's high scores even if a game is deleted (can change based on requirements)
    FOREIGN KEY (game_id) REFERENCES games(id) 
);

-- Creating index on score will speed up score-related queries
CREATE INDEX idx_score ON high_scores(score);
-- Creating index on game_id and user_id will speed up search by game and user.
CREATE INDEX idx_game_user ON high_scores(game_id, user_id);

-- Let's assume users and games tables exist in our database with at least 'id' column; a real scenario would have more columns in these tables.
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS games (
    id INT AUTO_INCREMENT PRIMARY KEY
);

-- Use INNODB for foreign key support; default in recent versions of MySQL, but this is to make sure
ALTER TABLE high_scores ENGINE=INNODB;
ALTER TABLE users ENGINE=INNODB;
ALTER TABLE games ENGINE=INNODB;
```