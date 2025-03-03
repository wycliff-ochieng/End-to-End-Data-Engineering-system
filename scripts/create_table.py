import os
import sys
import psycopg2
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.constants import DB_FIELDS

with open('passkey.txt','r') as f:
    pw = f.read()

dbname="postgres"
host="localhost"
port=5433
password=pw
user="postgres"

conn = psycopg2.connect(dbname=dbname,user=user,port=port,password=password,host=host)

cursor = conn.cursor()

def try_execute_sql(sql:str):
    try:
        cursor.execute(sql)
        conn.commit()
        print("Execution successfill")
    except Exception as e:
        print(f"Not executed.Error:{e}")
        conn.rollback()

def create_table():
    create_table_sql = f"""CREATE TABLE rappel_conso(
    {DB_FIELDS[0]} text PRIMARY KEY,"""

    for field in DB_FIELDS[1:-1]:
        column_sql = f"{field} text, \n"
        create_table_sql+=column_sql

    create_table_sql+=f"{DB_FIELDS[-1]} text \n"+");"
    try_execute_sql(create_table_sql)
    cursor.close()
    conn.close()

if __name__ == "__main__" :
    create_table()

    