import psycopg2
import pandas as pd
conn = psycopg2.connect("host=localhost password=5985 dbname=Testdb1 user=postgres")
cur = conn.cursor()
cur.execute('select * from student')
df = pd.DataFrame(cur)
df.to_csv("D:/studentinfo.csv")
print(df)
conn.close()
cur.close()