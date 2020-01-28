import psycopg2
import pandas as pd
import csv

conn= psycopg2.connect("dbname=Testdb1 user=postgres password=5985 host=localhost")
cur=conn.cursor()
with open("C:/Users/venkatadri manubolu/Documents/studentdata.csv",'r')as f:
    reader=csv.reader(f)
    next(reader)
    count=0
    for row in reader:
        cur.execute("insert into student values(%s,%s,%s,%s)",row)
        count +=cur.rowcount
    print("total number of rows inserted:",count)
conn.commit()
print("commited sucessfully")
cur.close()
conn.close()