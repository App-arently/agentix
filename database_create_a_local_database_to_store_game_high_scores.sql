-- SQL Code to create a database with a table to store game high scores

-- Create a new database named 'GameDB'
CREATE DATABASE GameDB;

-- Use the new created database 'GameDB'
USE GameDB;

-- Create table named 'HighScores'
CREATE TABLE HighScores (
  -- Assign ID as Primary Key. Auto-increment feature will automatically insert unique IDs for every new column
  ID INT AUTO_INCREMENT PRIMARY KEY,

  -- Create column for user name, setting character length limit to 100
  UserName VARCHAR(100) NOT NULL,

  -- Create column for game name, setting character length limit to 100
  GameName VARCHAR(100) NOT NULL,

  -- Create column for high score, which is of type float to accommodate decimal points
  Score FLOAT NOT NULL,

  -- Create column for the date of the high score. Set it to automatically fill with the current date and time when a record is inserted
  ScoreDate DATETIME DEFAULT CURRENT_TIMESTAMP,

  -- Add index to columns that are frequently searched or ordered to improve performance
  INDEX (UserName, GameName)
);
  
-- Following best security practices, for retrieving high scores data, a SELECT statement can be provided. 
-- For instance, to fetch top 5 scores for a particular game, you can use:
-- SELECT * FROM HighScores WHERE GameName = 'Game name here' ORDER BY Score DESC LIMIT 5;
  
-- Make sure to avoid SQL Injection attacks by utilizing parameterized queries or prepared statements in your application.  