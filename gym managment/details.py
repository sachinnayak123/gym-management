import pymysql
connection= pymysql.connect("localhost","root","123sachin","test")
cursor=connection.cursor()


            try:
                query = "INSERT INTO 'plans' (pname,duration,price) VALUES (?,?,?) "
                cursor.execute(query , [name,duration,price])
                connection.commit()
                messagebox.showinfo("success","contact added")
            except EXCEPTION as e:
                messagebox.showerror("Error",str(e))

            cursor=connection.cursor()
            query = "INSERT INTO 'plans' ('pname','duration','price') VALUES (%s,%s,%s) "
            cursor.execute(query,(name,duration,price))
            connection.commit()
            messagebox.showinfo("success","contact added");
            connection.close();



#..................................................................................................CUSTOMERS.............................................................................................................................................................................................................................................#
def addCustomer():
    cid = int(input('Enter id'))
	name = input('Enter name: ')
	email = input('Enter email: ')
	gender=input('enter gender')
	cphone=input('phone no')
	pid=input('enter package id')
	initial_amt=input('enter initial amount')
	start=input('starting date')
	end=input('ending date') 
	
	query = "INSERT INTO customers (cid,name,email,gender,cphone,pid,initial_amt,start,end) VALUES ("+str(cid)+",'"+name+"','"+email+"','"+gender+"',"+str(cphone)+","+str(pid)+","+str(phone)+","+str(initial_amt)+","+str(start)+","+str(end)+");"
	cursor.execute(query)
	connection.commit()
	connection.close()


def deleteCustomer():
    cid=int(input('Enter Customer id: '))
    query = "DELETE FROM customers WHERE cid="+str(cid)+";"
    cursor.execute(query)
    connection.commit()
    connection.close()


def updateDetails():
    cid = int(input('Enter id of customer'))
    name = input('Enter to be updated name: ')
    email = input('Enter to be updated email: ')
    query = "UPDATE customers SET name ="+name+",email="+email+" WHERE cid="+str(cid)+";"
    cursor.execute(query)
    connection.commit()
    connection.close()    

#..................................................................................................CUSTOMERS.............................................................................................................................................................................................................................................#



#..................................................................................................PLANS............................................................................................................................................................................................................................................#


def addPlans():
	pid = int(input('Enter plan id'))
	pname = input('Enter package name: ')
	duration = input('Enter duration: ')
	price=input('enter price')

	
	query = "INSERT INTO plans (pid,pname,duration,price) VALUES ("+str(pid)+",'"+pname+"'',"+str(duration)+","+str(price)+");"
	cursor.execute(query)
	connection.commit()
	connection.close()


def deletePlans():
    pid=int(input('Enter plan id: '))
    query = "DELETE FROM plans WHERE pid="+str(pid)+";"
    cursor.execute(query)
    connection.commit()
    connection.close()


def updatePlans():

    cursor.execute(query)
    connection.commit()
    connection.close()    


#..................................................................................................PLANS............................................................................................................................................................................................................................................#





    



#..................................................................................................EQUIPMENTS...........................................................................................................................................................................................................................................#

def addEquipments():
    eqid=int(input('enter equipment id'))
	ename = int(input('Enter equipment'))
	quantity = input('Enter quamtity: ')
	date = input('date: ')
	remark=input('enter gender'
	query = "INSERT INTO equipments (eqid,ename,quantity,date,remark) VALUES ("+str(eqid)+",'"+ename+"',"+str(quantity)+","+str(date)+","+remark+");"
	cursor.execute(query)
	connection.commit()
	connection.close()


def deleteEquipments():
    eqid=int(input('Enter equipment id: '))
    query = "DELETE FROM equipments WHERE cid="+str(eqid)+";"
    cursor.execute(query)
    connection.commit()
    connection.close()


def updateEquipments():
 
    cursor.execute(query)
    connection.commit()
    connection.close()    





#..................................................................................................EQUIPMENT............................................................................................................................................................................................................................................#





    




#..................................................................................................EMPLOYEE...........................................................................................................................................................................................................................................#



def addEmployees():
	empid = int(input('Enter employee id'))
	empname = input('Enter employee  name: ')
	designation=input('enter designation)
	salary=input('ending salary')
	emp_mail = input('Enter employee email: ')
	empphone=input('enter employee phone no')
	query = "INSERT INTO employees (empid,empname,designation,salary,emp_mail,empphone) VALUES ("+str(empid)+",'"+empname+"','"+designation+"',"+str(salary)+",'"+emp_mail+"',"+str(empphone)+");"
	cursor.execute(query)
	connection.commit()
	connection.close()


def deleteEmployees():();
    empid=int(input('Enter Employee id: '))
    query = "DELETE FROM employees WHERE cid="+str(emid)+";"
    cursor.execute(query)
    connection.commit()
    connection.close()


def updateEmployees():

    cursor.execute(query)
    connection.commit()
    connection.close()    




    
#..................................................................................................EMPLOYEE............................................................................................................................................................................................................................................#    



#..................................................................................................DIET_CHART...........................................................................................................................................................................................................................................#    



#..................................................................................................DIET_CHART...........................................................................................................................................................................................................................................#    
