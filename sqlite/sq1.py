
import sqlite3


conn= sqlite3.connect("employees.db")

c=conn.cursor()


c.execute("""create table employee(
	           first text,
	           last text,
	          pay int)""")

c.execute("insert into employee values('indhu','mathy',50000)")
c.execute("insert into employee values('karthi','sarvesh',70000)")

c.execute("select * from employee ")

print (c.fetchall())


conn.commit()

conn.close()




