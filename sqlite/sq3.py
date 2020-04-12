
import sqlite3
from employee1 import Employee

conn= sqlite3.connect("employees.db")

c=conn.cursor()


c.execute("""create table employee3(
	           first text,
	           last text,
	          pay int)""")

def insertemp(emp):
	with conn:
		c.execute("insert into employee3 values(?,?,?)",(emp.first,emp.last,emp.pay))


def get_emp_by_name(lastname):
	c.execute("select * from employee3 where last=:last",{'last':lastname})
	return c.fetchall()
		
emp_1=Employee("karthi","palani",5000)
emp_2=Employee("sarvesh","palani",6500)


insertemp(emp_1)
insertemp(emp_2)
emps=get_emp_by_name("palani")
print (emps)


conn.close()




