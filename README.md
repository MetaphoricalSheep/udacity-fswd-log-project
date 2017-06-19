# Udacity Full Stack Web Developer Nanodegree

## Project 5: News Log Project

## The Spec

Your task is to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

The game tournament will use the Swiss system for pairing up players in each round: players are not eliminated, and each 
player should be paired with another player with the same number of wins, or as close as possible.

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?


## Getting Started

You will need python 2.7 and PostgreSQL installed on your system to run this project.

Clone the repo and ```cd``` into it
```bash
git clone https://github.com/MetaphoricalSheep/udacity-fswd-log-project.git .
cd udacity-fswd-log-project
```

Set up the database
```bash
cd /path/to/udacity-fswd-log-project
psql
-> \i views.sql
-> \q
```


## Running

```bash
cd /path/to/udacity-fswd-log-project
python news-logs-analysis.py
```


## Dependencies
* [python 2.7](https://www.python.org/downloads/)
* [PostgreSQL](https://www.postgresql.org/download/)
