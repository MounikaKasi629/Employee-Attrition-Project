import sqlite3
import pandas as pd

df = pd.read_csv("employee_attrition_cleaned.csv")

print("Cleaned Data Shape:", df.shape)

conn = sqlite3.connect("hr_analytics.db")

df.to_sql("employees", conn, if_exists="replace", index=False)

print("Data loaded into SQLite successfully")

query= """ SELECT COUNT(*) As total_employees FROM employees   """

result=pd.read_sql_query(query,conn)
print(result)




