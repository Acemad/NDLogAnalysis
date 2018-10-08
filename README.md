# ND Log Analysis Project
### For Full Stack Web Developer Nanodegree Program @ [Udacity](http://www.udacity.com)

This is my submission for the Log Analysis project. It is composed of two Python (v3) source files :

* `analysis.py` : Main program.
* `queries.py` : Contains the SQL queries needed to perform the requested analysis.

## Design

The program is structured in a very simple way, queries are stored in `queries.py` and imported by `analysis.py` which provides an interactive text-based interface allowing the user to choose which query to execute. 

Sorting / filtering data is done on the database side, our program is only concerned by querying the database and correctly displaying the output of the queries. Therefore, we've implemented a generic database query function `queryDB()` and functions to display the results of that function `printResults()` and `printResultsQ3()`.

## Prerequisites

This program interacts with the `news` database obtained from the project's page at Udacity.com.

In order to correctly run this program, one needs to create the following database views (especially needed for the 3rd query) :

```sql
-- This will create req_day view which displays the amount
-- of requests received each day.
CREATE VIEW req_day AS 
    SELECT date(time), count(*) AS reqs 
    FROM log GROUP BY date(time);
```
```sql
-- Similarly, this will create err_day view, which displays
-- the amount of erroneous responses each day.
CREATE VIEW err_day AS 
    SELECT date(time), count(*) AS reqs 
    FROM log 
    WHERE status != '200 OK' 
    GROUP BY date(time);
```

## Execution

The program is written and tested in Python 3.5, so you should run it using at least that version. ( depending on your system, you may run this program either using `python` or `python3` command, either way, you should make sure to have a Python version >= 3.5 )

```bash
$ python3 analysis.py
```
You'll be presented with a menu, and prompted to enter one of the options to launch a specific database query. Query results will be displayed after processing.
