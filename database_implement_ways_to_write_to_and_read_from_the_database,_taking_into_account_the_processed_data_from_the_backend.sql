-- Assuming that we are working with a 'users' table as a sample with fields id, name, email, and password

-- Writing data to a database (Inserting data)

INSERT INTO users (name, email, password)
VALUES ('John Doe', 'johndoe@example.com', 'SecurePass123') -- always store password securely e.g. as hashed
ON DUPLICATE KEY UPDATE 
email = VALUES(email),   
password = VALUES(password); -- This prevents duplicate entry of users based on the Unique ID 

-- Reading data from a database (Selecting data)

SELECT name, email
FROM users
WHERE id = 1;

-- To enhance performance, we can use indexes which can find data more directly and quickly. 
-- Since 'id' is frequently used as a reference, it's a good idea to add an index

CREATE INDEX idx_users_id 
ON users (id); 

-- For further smaller databases, you can add Full-Text indexes to search into texts 

-- ---------------------- 

-- For Security: Always validate and sanitize the input data before directly embedding them in the SQL. Use Parameterized Queries or Prepared Statements to prevent against SQL injection attacks
-- Avoid using SELECT * as it can be exploited in Blind-SQL Injection attacks. 

-- The PASSWORD field should be stored securely with salt and hash.

-- When coding out the database calls in the backend code (e.g. in Node.js, Ruby, Python, etc.), always use ORMs (Object Relational Mapping) or built-in ways that protect against most common SQL attacks.
-- With ORMs, the SQL coding part is mostly abstracted and wrapped securely for coder's ease and security.
