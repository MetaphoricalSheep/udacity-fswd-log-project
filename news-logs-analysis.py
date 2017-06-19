#!/usr/bin/env python

import psycopg2


def connect():
    """
    Connect to the PostgreSQL database.
    Returns a database connection and cursor or None on Failure.
    """
    try:
        conn = psycopg2.connect("dbname=news")
        cur = conn.cursor()
        return conn, cur
    except Exception, e:
        print('Could not connect: {0}'.format(e.message))
        return None, None


def read_query(qry):
    """
    Handles select queries.
    :param qry string:
    :return void:
    """
    conn, cur = connect()
    if conn is not None and cur is not None:
        try:
            cur.execute(qry)
            return cur.fetchall()
        except Exception, e:
            print('Could not execute query: {0}\n{1}'.format(qry, e.message))
        finally:
            conn.close()


def showPopularArticles(max=10):
    qry = 'SELECT Title, Views FROM vw_Articles ORDER BY views DESC LIMIT {0}'
    qry = qry.format(max)
    rows = read_query(qry)
    print('Popular Articles:')
    for row in rows:
        print('{0} - {1} views'.format(row[0], row[1]))
    print('')


def showPopularAuthors():
    qry = 'SELECT AuthorName, TotalViews FROM vw_authors '
    qry += 'ORDER BY TotalViews DESC'
    rows = read_query(qry)
    print('Popular Authors:')
    for row in rows:
        print('{0} - {1} views'.format(row[0], row[1]))
    print('')


def showExcessiveFailures(threshold=1.0):
    qry = 'SELECT Day, FailureRate FROM vw_responses WHERE '
    qry += 'FailureRate >= {0} ORDER BY Day'
    qry = qry.format(threshold)
    rows = read_query(qry)
    print('Excessive Failures:')
    for row in rows:
        print('{0} - {1}% errors'.format(row[0], round(row[1], 1)))
    print('')


def main():
    showPopularArticles(3)
    showPopularAuthors()
    showExcessiveFailures(1.0)


main()
