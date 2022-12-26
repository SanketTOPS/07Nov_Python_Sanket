import sqlite3

try:
    dbcon=sqlite3.connect('newdb.db')
    print("Database connected!")
except Exception as e:
    print(e)

"""tbnm=input("Enter table name:")
create_tbl=f"create table {tbnm} (id integer primary key,name text,sub text)"
try:
    dbcon.execute(create_tbl)
    print("Table Created!")
except Exception as e:
    print(e)"""

# Inset Data
n=int(input("Enter number of records:"))
for i in range(n):
    stid=input("Enter ID:")
    stnm=input("Enter Name:")
    stsub=input("Enter Subject:")

    insert_data=f"insert into stud values({stid},'{stnm}','{stsub}')"
    try:
        dbcon.execute(insert_data)
        dbcon.commit()
        print("Record Inserted!")
    except Exception as e:
        print(e)