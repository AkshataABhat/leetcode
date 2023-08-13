SELECT user_id, COUNT(*) AS followers_count
FROM Followers
GROUP BY user_id
ORDER by user_id