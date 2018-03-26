import psycopg2

try:
    conn = psycopg2.("dbname='template1' user='dbuser' host='localhost' password='dbpass'")