CREATE VIEW vw_authors
AS
SELECT
  a.id AS ArticleId,
  a.Title,
  a.Slug,
  a.Time,
  au.Id AS AuthorId,
  au.Name AS AuthorName,
  l.Path,
  l.Views
FROM articles a
LEFT JOIN (SELECT
  "path",
  REPLACE("path", '/article/', '') AS Slug,
  COUNT(*) AS Views
FROM "log"
WHERE "path" LIKE '/article/%'
AND "status" = '200 OK'
GROUP BY "path") l
  ON a.slug = l.slug
LEFT JOIN authors au
  ON a.author = au.id;
  
 
CREATE VIEW vw_authors
AS
SELECT
  au.id AS AuthorId,
  au.name AS AuthorName,
  (SELECT
    SUM(views) AS TotalViews
  FROM vw_articles
  WHERE authorid = au.id)
  AS TotalViews
FROM authors au;


CREATE VIEW vw_responses
AS
SELECT
  s.Day,
  Success,
  Failure,
  (Success + Failure) As Total,
  (cast(Failure as decimal) / cast((Success + Failure) as decimal) * 100) as FailureRate
FROM (SELECT
  date_trunc('day', time) AS Day,
  COUNT(*) AS Success
FROM log
WHERE status LIKE '2%'
OR status LIKE '3%'
GROUP BY day) s
LEFT JOIN (SELECT
  date_trunc('day', time) AS Day,
  COUNT(*) AS Failure
FROM log
WHERE status LIKE '4%'
OR status LIKE '5%'
GROUP BY day) f
  ON s.Day = f.Day;