import psycopg2
import pandas as pd
import csv

conn = psycopg2.connect("dbname = Testdb1 user = postgres password = 5985 host = localhost")
cur = conn.cursor()
with open("D:\TTTExcel.csv", 'r') as f:
        reader = csv.reader(f)
        next(reader) # Skip the header row.
        count =0
        for row in reader:
            cur.execute("INSERT INTO TTTExcel VALUES(%s, %s, %s, %s,%s,%s,%s, %s, %s, %s,%s,%s,%s, %s, %s,%s,%s,%s,%s, %s, %s, %s,%s,%s,%s, %s, %s, %s,%s,%s,%s, %s, %s, %s,%s,%s)",row)
            count += cur.rowcount
        print("Total number of rows inserted :",count)
conn.commit()
print("commited successfully")
cur.close()
conn.close()