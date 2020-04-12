
import sqlite3
from employee1 import Employee

conn= sqlite3.connect("employees.db")

c=conn.cursor()


c.execute("""create table employee(
	           first text,
	           last text,
	          pay int)""")

emp_1=Employee("karthi","palani",5000)
emp_2=Employee("sarvesh","palani",6500)

c.execute("insert into employee values(?,?,?)",(emp_1.first,emp_1.last,emp_1.pay))
conn.commit()

c.execute("insert into employee values(:first,:last,:pay)",{'first':emp_2.first,'last':emp_2.last,'pay':emp_2.pay})

c.execute("select * from employee where last=?",('palani',))
print (c.fetchall())

c.execute("select * from employee where first=:first",{'first':'indhu'})
print (c.fetchall())

conn.commit()

conn.close()




