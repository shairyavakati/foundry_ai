-- User and project mapping

SELECT
    u.name,
    p.project_name
FROM users u
INNER JOIN projects p
ON u.user_id = p.user_id;

-- Projects per user

SELECT
    u.name,
    COUNT(*)
FROM users u
INNER JOIN projects p
ON u.user_id = p.user_id
GROUP BY u.name;