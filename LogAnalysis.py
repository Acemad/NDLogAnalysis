#!/usr/bin/env python3
import psycopg2


def main():
    print('Hello\n')


def queryDB(query):
    db = psycopg2.connect('dbname=news')
    cursor = db.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    db.close()
    return rows


if __name__ == '__main__':
    main()
