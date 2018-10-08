#!/usr/bin/env python3
import psycopg2
from queries import QUERY1, QUERY2, QUERY3


def main():
    printMenu()
    choice = ''
    while (choice != 'q'):
        choice = input('Please choose an option [1,2,3,q] : ')
        if (choice == '1'):
            print('\nThe Most Popular 3 Articles of All Time are : ')
            printResults(queryDB(QUERY1))
        elif (choice == '2'):
            print('\nThe Most Popular Article Authors of All Time are : ')
            printResults(queryDB(QUERY2))
        elif (choice == '3'):
            print('\nMore than 1% of Requests Lead to Errors on : ')
            printResultsQ3(queryDB(QUERY3))


def printMenu():
    print('''
    Greetings ! What kind of information are you interested in ?

    [1] The most popular 3 articles of all time.
    [2] The most popular article authors of all time.
    [3] When did more than 1% of requests lead to errors.
    [q] Quit
    ''')


def printResults(rows):
    print()
    for row in rows:
        print('"{}" - {} Views'.format(row[0], row[1]))
    print()


def printResultsQ3(rows):
    print()
    for row in rows:
        print('{} - {}% Errors'.format(row[0].strftime('%B %d, %Y'), row[1]))
    print()


def queryDB(query):
    db = psycopg2.connect('dbname=news')
    cursor = db.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    db.close()
    return rows


if __name__ == '__main__':
    main()
