#!/usr/bin/env python3
import psycopg2
from queries import QUERY1, QUERY2, QUERY3


def main():
    printResults(queryDB(QUERY2))


def printResults(rows):
    for row in rows:
        print('{} - {} Views'.format(row[0], row[1]))


def queryDB(query):
    db = psycopg2.connect('dbname=news')
    cursor = db.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    db.close()
    return rows


if __name__ == '__main__':
    main()
