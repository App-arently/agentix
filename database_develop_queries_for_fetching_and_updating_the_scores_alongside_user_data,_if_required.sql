```sql
-- QUERY TO FETCH USER DATA AND SCORES

-- The following query selects all necessary fields from the users and scores tables. 
-- We use the INNER JOIN operation to combine rows from two tables based on a related column (user_id).
-- The WHERE clause is used to filter records that have a score_id greater than 100.

SELECT users.user_id, users.first_name, users.last_name, scores.score_id, scores.score
FROM users
INNER JOIN scores ON users.user_id = scores.user_id
WHERE scores.score_id > 100;

-- QUERY TO UPDATE SCORE FOR A PARTICULAR USER

-- This query updates a user's score. 
-- The SET command is used to specify the new score value. 
-- The WHERE clause is used to specify which user's score we should update, based on the user_id and score_id. 
-- For instance, the user with the user_id of 3 now has the score of 85.

UPDATE scores
SET score = 85
WHERE user_id = 3 AND score_id = 1;


-- As a security measure, the user_id and score_id should be verified before running the above queries. 
-- This ensures that an authorized user cannot make changes to another user's data.

-- Additionally, frequently backing up your database and using secure network connections can further enhance 
-- the security of your data. Also, limit the privileges of database accounts to prevent unauthorized access.

-- For performance, consider indexing the user_id and score_id columns, as they are frequently searched and 
-- updated. Regularly analyze your database performance and optimize your schema and queries as necessary.


-- Note: Assuming that we have the following table structures:

-- USERS TABLE
-- user_id   INT(11)     PRIMARY KEY
-- first_name  VARCHAR(50)
-- last_name   VARCHAR(50)

-- SCORES TABLE
-- score_id   INT(11)     PRIMARY KEY
-- user_id    INT(11)    FOREIGN KEY REFERENCES users(user_id)
-- score      INT(11)
```