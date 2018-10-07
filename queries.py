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

QUERY2 = '''
SELECT name, count(*) as num
FROM authors, articles, log
WHERE authors.id = articles.author
    AND log.path like ('%' || articles.slug)
GROUP BY name
ORDER BY num desc;
'''