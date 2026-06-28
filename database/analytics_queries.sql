-- Count total ideas
SELECT COUNT(*) FROM ideas;

-- Average score
SELECT AVG(score) FROM ideas;

-- Highest score
SELECT MAX(score) FROM ideas;

-- Ideas per project
SELECT
    project_id,
    COUNT(*)
FROM ideas
GROUP BY project_id;

-- Rank projects by idea count
SELECT
    project_id,
    COUNT(*)
FROM ideas
GROUP BY project_id
ORDER BY COUNT(*) DESC;

-- Top project
SELECT
    project_id,
    COUNT(*)
FROM ideas
GROUP BY project_id
ORDER BY COUNT(*) DESC
LIMIT 1;
-- Show which user created which project

SELECT
    u.name,
    p.project_name
FROM users u
INNER JOIN projects p
ON u.user_id = p.user_id;
-- Number of projects created by each user

SELECT
    u.name,
    COUNT(p.project_id)
FROM users u
INNER JOIN projects p
ON u.user_id = p.user_id
GROUP BY u.name;
-- Show all users even if they have not created projects

SELECT
    u.name,
    p.project_name
FROM users u
LEFT JOIN projects p
ON u.user_id = p.user_id;
-- Users who have not created any project

SELECT
    u.name
FROM users u
LEFT JOIN projects p
ON u.user_id = p.user_id
WHERE p.project_id IS NULL;
/* ============================================================
   USER ACTIVITY DASHBOARD
   Feature: Most Active User
   Sprint: Day 7
   ============================================================ */

-- Show the most active user based on the number of projects created

SELECT
    u.name,
    COUNT(p.project_id) AS total_projects
FROM users u
LEFT JOIN projects p
ON u.user_id = p.user_id
GROUP BY
    u.user_id,
    u.name
ORDER BY
    COUNT(p.project_id) DESC
LIMIT 1;