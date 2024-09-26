```SQL
-- Create a database for the high scores
CREATE DATABASE HighScoresDB;
GO

-- Use the created database
USE HighScoresDB;
GO

-- Creating table named HighScores to hold game_id, player_id, highscore, and date of the highscore
CREATE TABLE HighScores (
    id INT PRIMARY KEY IDENTITY, -- adds an primary key id that auto increments
    game_id INT NOT NULL, -- id of the game the highscore was achieved
    player_id INT NOT NULL, -- id of the player who achieved the highscore
    score INT NOT NULL, -- score the player achieved
    date_achieved DATETIME DEFAULT GETDATE() -- when the highscore was achieved, defaults to current date and time
);
GO

-- Adding indexes on game_id and player_id for performance. Indexes speed up the querying process.
CREATE INDEX idx_highscores_gameid ON HighScores(game_id);
GO

CREATE INDEX idx_highscores_playerid ON HighScores(player_id);
GO

-- Enabling data compression to minimize storage consumption.
ALTER TABLE HighScores REBUILD PARTITION = ALL WITH (DATA_COMPRESSION = PAGE);
GO

-- Putting unique index on game_id and player_id to ensure that each player can have only one highscore per game. Enforces data integrity.
CREATE UNIQUE INDEX idx_highscores_game_player
ON HighScores(game_id, player_id);
GO

-- Following the principal of least privilege to secure the data,
-- we will next setup roles and grant specific permissions. For example:

-- CREATE ROLE db_datareader;
-- GRANT SELECT ON HighScores TO db_datareader;

-- CREATE ROLE db_datawriter;
-- GRANT INSERT, UPDATE, DELETE ON HighScores TO db_datawriter;

-- Note: The GRANT statements have been commented out, as these CREATE ROLE and GRANT 
-- actions generally requires sysadmin permissions and should be executed cautiously.
```