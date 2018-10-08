QUERY1 = '''
SELECT title, count(*) as NBViews
FROM log, articles
WHERE log.path like ('%' || articles.slug)
    AND status = '200 OK'
    AND path != '/'
GROUP BY title
ORDER BY NBViews DESC
LIMIT 3;
'''

QUERY2 = '''
SELECT name, count(*) as NBViews
FROM authors, articles, log
WHERE authors.id = articles.author
    AND log.path like ('%' || articles.slug)
GROUP BY name
ORDER BY NBViews DESC;
'''

QUERY3 = '''
SELECT date, trunc(cast(rate AS numeric),2)
FROM
 (
  SELECT req_day.date,
    (
      (cast(err_day.reqs AS real) * 100) / cast(req_day.reqs AS real)
    ) AS rate
  FROM req_day, err_day
  WHERE req_day.date = err_day.date
 ) AS subq
WHERE rate > 1.0;
'''
