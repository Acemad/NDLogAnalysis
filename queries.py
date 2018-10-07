QUERY1 = '''
SELECT title, count(*) as NBViews
FROM log, articles
WHERE log.path like ('%' || articles.slug)
    AND status = '200 OK'
    AND path != '/'
GROUP BY title
ORDER BY NBViews desc
LIMIT 3;
'''