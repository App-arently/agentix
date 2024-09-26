```sql
-- Creating a function to fetch all scores from database
CREATE OR REPLACE FUNCTION fetch_all_scores() 
RETURNS TABLE (
  id INT,
  user_id INT,
  score INT,
  game_id INT,
  date TIMESTAMP
) AS $$
BEGIN
  -- Select the scores from the scores table, ordering by date for latest first
  RETURN QUERY 
    SELECT id, user_id, score, game_id, date
    FROM scores
    ORDER BY date DESC;
END; $$ LANGUAGE plpgsql;

-- Creating a function to fetch a user's specific scores
CREATE OR REPLACE FUNCTION fetch_scores_by_user_id(p_user_id INT) 
RETURNS TABLE (
  id INT,
  score INT,
  game_id INT,
  date TIMESTAMP
) AS $$
BEGIN
  -- Select scores for the provided user, 
  -- ordering by date descending to get latest scores first
  RETURN QUERY 
    SELECT id, score, game_id, date
    FROM scores
    WHERE user_id = p_user_id
    ORDER BY date DESC;
END; $$ LANGUAGE plpgsql;

-- Creating a function to fetch scores for a specific game
CREATE OR REPLACE FUNCTION fetch_scores_by_game_id(p_game_id INT) 
RETURNS TABLE (
  id INT,
  user_id INT,
  score INT,
  date TIMESTAMP
) AS $$
BEGIN
  -- Select scores for the provided game, 
  -- ordering by score descending to get the highest scores first
  RETURN QUERY 
    SELECT id, user_id, score, date
    FROM scores
    WHERE game_id = p_game_id
    ORDER BY score DESC;
END; $$ LANGUAGE plpgsql;
```

Note that these functions are designed to be used in PostgreSQL, which supports user-defined functions through its PL/pgSQL language. Each function returns a table of scores, either all scores, scores by a specific user, or scores from a specific game. The functions are invoked with a SELECT statement, as shown in this example:

```sql
SELECT * FROM fetch_all_scores();
SELECT * FROM fetch_scores_by_user_id(123);
SELECT * FROM fetch_scores_by_game_id(456);
``` 

If you're using a different SQL server like MySQL, you may need to adjust the syntax to suit. Also, it's likely that in a real-world scenario, you'd want to handle errors (for example, invalid user or game ids), add additional parameters (like limiting the number of result records), and log usage stats or other metada.