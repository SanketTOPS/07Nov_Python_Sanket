import pymysql

try:
    dbcon=pymysql.connect(host='localhost',user='root',password='',database='newdb')
    print("Database connected!")
except Exception as e:
    print(e)

cur=dbcon.cursor()

# Create Table
tbl_create="create table studinfo (id integer primary key auto_increment,name text,sub text)"
try:
    cur.execute(tbl_create)
    print("Table created!")
except Exception as e:
    print(e)

# Insert Data
"""insert_data="insert into studinfo (name,sub) values ('sanket','python'),('nirav','java'),('pratik','php'),('ashok','angular'),('hitesh','android')"
try:
    cur.execute(insert_data)
    dbcon.commit()
    print("Record inserted successfully!")
except Exception as e:
    print(e)"""

# Update Data
"""update_data="update studinfo set sub='react' where id=4"
try:
    cur.execute(update_data)
    dbcon.commit()
    print("Record updated successfully!")
except Exception as e:
    print(e)"""

# Delete Data
"""delete_data="delete from studinfo where id=5"
try:
    cur.execute(delete_data)
    dbcon.commit()
    print("Record deleted successfully!")
except Exception as e:
    print(e)"""

# Show Data
show_data="select * from studinfo"
try:
    cur.execute(show_data)
    data=cur.fetchall()
    #data=cur.fetchmany(3)
    #data=cur.fetchone()
    #print(data)
    n=1
    for i in data:
        #print(i)
        print(f"Record:{n} = {i[2]}")
        n+=1
except Exception as e:
    print(e)