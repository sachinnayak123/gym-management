from tkinter import *
from tkinter import messagebox
import pymysql
connection= pymysql.connect("localhost","root","123sachin","gym")
cursor=connection.cursor()
#-----------------------------------------------------------------------plans ------------------------------------------------------------#
# events after clicking  plans button
    
#_updating the details
class updateplan(Toplevel):
    def __init__(self,pid):
        Toplevel.__init__(self)

        self.geometry("650x650+600+200")
        self.title("UPDATE PLAN")
        self.resizable(False,False)
        self.top =Frame(self , height =150 ,bg='#B9E9DD')
        self.top.pack(fill=X)
        self.botom =Frame(self , height =500 ,bg='#FCE393')
        self.botom.pack(fill=X)

    #    fetching the data from database 
        query="select * from plans where pid ='{}'".format(pid)
        result=cursor.execute(query)
        result=cursor.fetchone()
        self.pid=pid
        name=result[1]
        duration=result[2]
        price=result[3]

        print("name=",name)
        print("duration=",duration)
        print("price=",price) 


    #top frame design
         #icon
        self.top_image=PhotoImage(file= 'images\customer.png')
        self.top_image_label= Label(self.top, image=self.top_image,bg='#B9E9DD')
        self.top_image_label.place(x=200 ,y=40)
         #title
        self.heading=Label(self.top, text='UPDATE PLAN', font='opensans 20 bold',bg='#B9E9DD',fg='#595959' )
        self.heading.place(x=300,y=60)

#button
        self.label_name =Label(self.botom, text="name",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_name.place(x=49,y=40)
        self.entry_name=Entry(self.botom,width=30 ,bd=4)
        self.entry_name.insert(0,name)
        self.entry_name.place(x=150,y=40)

        self.label_duration =Label(self.botom, text="duration",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_duration.place(x=49,y=80)
        self.entry_duration=Entry(self.botom,width=30 ,bd=4)
        self.entry_duration.insert(0,duration)
        self.entry_duration.place(x=150,y=80)
   
        self.label_price =Label(self.botom, text="price",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_price.place(x=49,y=120)
        self.entry_price=Entry(self.botom,width=30 ,bd=4)
        self.entry_price.insert(0,price)
        self.entry_price.place(x=150,y=120)

        self.Button= Button(self.botom,text=' UPDATE  ',font='arial 15 bold',fg='#262626',bg='#B9E9DD',command=self.update_plan)
        self.Button.place(x=200,y=445)

    def update_plan(self):

        p_id=self.pid
        name = self.entry_name.get()
        duration = self.entry_duration.get()
        price = self.entry_price.get()

        query="update plans set pname=%s, duration=%s , price=%s where pid=%s"
        data=(name,duration,price,p_id)

        try:
            cursor.execute(query,data)
            connection.commit()
            messagebox.showinfo("success","updated succcesfully")
            self.destroy()
            


        except EXCEPTION as e:
            print(e)    
        
  
    

 








   
#_addition of the details


class addplan(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("650x650+600+200")
        self.title("ADD PLAN")
        self.resizable(False,False)
        self.top =Frame(self , height =150 ,bg='#B9E9DD')
        self.top.pack(fill=X)
        self.botom =Frame(self , height =500 ,bg='#FCE393')
        self.botom.pack(fill=X)

    #top frame design
         #icon
        self.top_image=PhotoImage(file= 'images\customer.png')
        self.top_image_label= Label(self.top, image=self.top_image,bg='#B9E9DD')
        self.top_image_label.place(x=200 ,y=40)
         #title
        self.heading=Label(self.top, text='ADD PLAN', font='opensans 20 bold',bg='#B9E9DD',fg='#595959' )
        self.heading.place(x=300,y=60)

#button
        self.label_name =Label(self.botom, text="name",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_name.place(x=49,y=40)
        self.entry_name=Entry(self.botom,width=30 ,bd=4)
        self.entry_name.insert(0,"")
        self.entry_name.place(x=150,y=40)

        self.label_duration =Label(self.botom, text="duration",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_duration.place(x=49,y=80)
        self.entry_duration=Entry(self.botom,width=30 ,bd=4)
        self.entry_duration.insert(0,"")
        self.entry_duration.place(x=150,y=80)
   
        self.label_price =Label(self.botom, text="price",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_price.place(x=49,y=120)
        self.entry_price=Entry(self.botom,width=30 ,bd=4)
        self.entry_price.insert(0," ")
        self.entry_price.place(x=150,y=120)

        self.Button= Button(self.botom,text=' ADD  ',font='arial 15 bold',fg='#262626',bg='#B9E9DD', command=self.add_plan)
        self.Button.place(x=200,y=445)
    
    def add_plan(self):
        name = self.entry_name.get()
        duration = self.entry_duration.get()
        price = self.entry_price.get()
        
        if name and duration and price !="":
            try:
                with connection.cursor() as cursor:
                    query = "INSERT INTO plans (pname,duration,price) VALUES (%s,%s,%s)"
                    cursor.execute(query,(name,duration,price))
                    connection.commit()
                    messagebox.showinfo("success","PLAN added")
                    self.destroy()
            except EXCEPTION as e:
                messagebox.showinfo("Error",str(e))

        else:
            messagebox.showerror("Error","fill all the fields",icon='warning')

                    
                    
                     
      

                     

                

           




           


        






#_viewing the details
class viewplan(Toplevel):
    def __init__(self,pid):
        Toplevel.__init__(self)

        self.geometry("650x650+600+200")
        self.title("VIEW PLAN")
        self.resizable(False,False)



        self.top =Frame(self , height =150 ,bg='#B9E9DD')
        self.top.pack(fill=X)
        self.botom =Frame(self , height =500 ,bg='#FCE393')
        self.botom.pack(fill=X)

    #    fetching the data from database 
        query="select * from plans where pid ='{}'".format(pid)
        result=cursor.execute(query)
        result=cursor.fetchone()
        self.pid=pid
        name=result[1]
        duration=result[2]
        price=result[3]

        print("name=",name)
        print("duration=",duration)
        print("price=",price) 


    #top frame design
         #icon
        self.top_image=PhotoImage(file= 'images\customer.png')
        self.top_image_label= Label(self.top, image=self.top_image,bg='#B9E9DD')
        self.top_image_label.place(x=200 ,y=40)
         #title
        self.heading=Label(self.top, text='VIEW PLAN', font='opensans 20 bold',bg='#B9E9DD',fg='#595959' )
        self.heading.place(x=300,y=60)




    #top frame design
         #icon
        self.top_image=PhotoImage(file= 'images\customer.png')
        self.top_image_label= Label(self.top, image=self.top_image,bg='#B9E9DD')
        self.top_image_label.place(x=200 ,y=40)
         #title
        self.heading=Label(self.top, text='VIEW PLAN', font='opensans 20 bold',bg='#B9E9DD',fg='#595959' )
        self.heading.place(x=300,y=60)

#button
        self.label_name =Label(self.botom, text="name",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_name.place(x=49,y=40)
        self.entry_name=Entry(self.botom,width=30 ,bd=4)
        self.entry_name.insert(0,name)
        self.entry_name.config(state='disabled')
        self.entry_name.place(x=150,y=40)

        self.label_duration =Label(self.botom, text="duration",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_duration.place(x=49,y=80)
        self.entry_duration=Entry(self.botom,width=30 ,bd=4)
        self.entry_duration.insert(0,duration)
        self.entry_duration.config(state='disabled')
        self.entry_duration.place(x=150,y=80)
   
        self.label_price =Label(self.botom, text="price",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_price.place(x=49,y=120)
        self.entry_price=Entry(self.botom,width=30 ,bd=4)
        self.entry_price.insert(0,price)
        self.entry_price.config(state='disabled')
        self.entry_price.place(x=150,y=120)


   

#-----------------------------------------------------------------------plans------------------------------------------------------------#
#
#
#
#
#
#
#
#
#
#
#--------------------------------------------------------------------customer-------------------------------------------------------------#


# events after clicking  customer button


#_updating the details
class updatecustomer(Toplevel):
    def __init__(self,cid):
        Toplevel.__init__(self)

        self.geometry("650x650+600+200")
        self.title("UPDATE CUSTOMERS")
        self.resizable(False,False)
        self.top =Frame(self , height =150 ,bg='#B9E9DD')
        self.top.pack(fill=X)
        self.botom =Frame(self , height =500 ,bg='#FCE393')
        self.botom.pack(fill=X)

    #    fetching the data from database 
        query="select * from customers where cid ='{}'".format(cid)
        result=cursor.execute(query)
        result=cursor.fetchone()
        self.cid=cid
        name=result[1]
        email=result[2]
        phone=result[3]
        plan=result[4]
        Paid =result[5]
        start =result[6]
        end=result[7]

        print("name=",name)
        print("email=",email)
        print("phone=",phone) 
        print("plan=",plan)
        print("paid=",Paid)
        print("start=",start) 
        print("end=",end) 

    #top frame design
         #icon
        self.top_image=PhotoImage(file= 'images\customer.png')
        self.top_image_label= Label(self.top, image=self.top_image,bg='#B9E9DD')
        self.top_image_label.place(x=200 ,y=40)
         #title
        self.heading=Label(self.top, text='UPDATE CUSTOMERS', font='opensans 20 bold',bg='#B9E9DD',fg='#595959' )
        self.heading.place(x=300,y=60)

#button

        self.label_name =Label(self.botom, text="name",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_name.place(x=35,y=60)
        self.entry_name=Entry(self.botom,width=30 ,bd=4)
        self.entry_name.insert(0,name)
        self.entry_name.place(x=170,y=60)

        self.label_email =Label(self.botom, text="email",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_email.place(x=35,y=100)
        self.entry_email=Entry(self.botom,width=30 ,bd=4)
        self.entry_email.insert(0,email)
        self.entry_email.place(x=170,y=100)
        
        self.label_phone =Label(self.botom, text="phone",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_phone.place(x=35,y=140)
        self.entry_phone=Entry(self.botom,width=30 ,bd=4)
        self.entry_phone.insert(0,phone)
        self.entry_phone.place(x=170,y=140)

        self.label_plan =Label(self.botom, text="plan",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_plan.place(x=35,y=180)
        self.entry_plan=Entry(self.botom,width=30 ,bd=4)
        self.entry_plan.insert(0,plan)
        self.entry_plan.place(x=170,y=180)

        self.label_paid =Label(self.botom, text="initial paid",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_paid.place(x=35,y=220)
        self.entry_paid=Entry(self.botom,width=30 ,bd=4)
        self.entry_paid.insert(0,Paid)
        self.entry_paid.place(x=170,y=220)
   
        self.label_start =Label(self.botom, text="start date",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_start.place(x=35,y=260)
        self.entry_start=Entry(self.botom,width=30 ,bd=4)
        self.entry_start.insert(0,start)
        self.entry_start.place(x=170,y=260)

        self.label_end =Label(self.botom, text="end date",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_end.place(x=35,y=300)
        self.entry_end=Entry(self.botom,width=30 ,bd=4)
        self.entry_end.insert(0,end)
        self.entry_end.place(x=170,y=300)

        self.Button= Button(self.botom,text=' UPDATE  ',font='arial 15 bold',fg='#262626',bg='#B9E9DD',command=self.update_customer)
        self.Button.place(x=200,y=400)


    def update_customer(self):

        c_id=self.cid
        name = self.entry_name.get()
        email= self.entry_email.get()
        phone = self.entry_phone.get()
        plan = self.entry_plan.get()
        paid =self.entry_paid.get()
        start =self.entry_start.get()
        end =self.entry_end.get()
        query="update customers set name=%s, email=%s , phone=%s ,plan=%s,paid=%s,start=%s, end=%s where cid=%s"
        data=(name,email,phone,plan,paid,start,end,c_id)

        try:
            cursor.execute(query,data)
            connection.commit()
            messagebox.showinfo("success","updated succcesfully")
            self.destroy()


        except EXCEPTION as e:
            print(e)              









#_addition of the details
class addcustomer(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("650x650+600+200")
        self.title("ADD CUSTOMERS")
        self.resizable(False,False)
        self.top =Frame(self , height =150 ,bg='#B9E9DD')
        self.top.pack(fill=X)
        self.botom =Frame(self , height =500 ,bg='#FCE393')
        self.botom.pack(fill=X)

    #top frame design
         #icon
        self.top_image=PhotoImage(file= 'images\customer.png')
        self.top_image_label= Label(self.top, image=self.top_image,bg='#B9E9DD')
        self.top_image_label.place(x=200 ,y=40)
         #title
        self.heading=Label(self.top, text='ADD CUSTOMERS', font='opensans 20 bold',bg='#B9E9DD',fg='#595959' )
        self.heading.place(x=300,y=60)
#button

        self.label_name =Label(self.botom, text="name",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_name.place(x=35,y=60)
        self.entry_name=Entry(self.botom,width=30 ,bd=4)
        self.entry_name.insert(0,"")
        self.entry_name.place(x=170,y=60)

        self.label_email =Label(self.botom, text="email",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_email.place(x=35,y=100)
        self.entry_email=Entry(self.botom,width=30 ,bd=4)
        self.entry_email.insert(0,"")
        self.entry_email.place(x=170,y=100)
        
        self.label_phone =Label(self.botom, text="phone",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_phone.place(x=35,y=140)
        self.entry_phone=Entry(self.botom,width=30 ,bd=4)
        self.entry_phone.insert(0,"")
        self.entry_phone.place(x=170,y=140)

        self.label_plan =Label(self.botom, text="plan",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_plan.place(x=35,y=180)
        self.entry_plan=Entry(self.botom,width=30 ,bd=4)
        self.entry_plan.insert(0,"")
        self.entry_plan.place(x=170,y=180)

        self.label_paid =Label(self.botom, text="initial paid",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_paid.place(x=35,y=220)
        self.entry_paid=Entry(self.botom,width=30 ,bd=4)
        self.entry_paid.insert(0,"")
        self.entry_paid.place(x=170,y=220)
   
        self.label_start =Label(self.botom, text="start date",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_start.place(x=35,y=260)
        self.entry_start=Entry(self.botom,width=30 ,bd=4)
        self.entry_start.insert(0,"")
        self.entry_start.place(x=170,y=260)

        self.label_end =Label(self.botom, text="end date",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_end.place(x=35,y=300)
        self.entry_end=Entry(self.botom,width=30 ,bd=4)
        self.entry_end.insert(0,"")
        self.entry_end.place(x=170,y=300)

        self.Button= Button(self.botom,text=' ADD  ',font='arial 15 bold',fg='#262626',bg='#B9E9DD',command=self.add_customers)
        self.Button.place(x=200,y=400)


    def add_customers(self):
        name = self.entry_name.get()
        email= self.entry_email.get()
        phone = self.entry_phone.get()
        plan=self.entry_plan.get()
        paid=self.entry_paid.get()
        start=self.entry_start.get()
        end=self.entry_end.get()
        if name and email and phone and plan and paid and start and end !="":
            try:
                with connection.cursor() as cursor:
                    query = "INSERT INTO customers (name,email,phone,plan,paid,start,end) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                    cursor.execute(query,(name,email,phone,plan,paid,start,end))
                    connection.commit()
                    messagebox.showinfo("success","CUSTOMER added")
                    self.destroy()
            except EXCEPTION as e:
                messagebox.showinfo("Error",str(e))

        else:
            messagebox.showerror("Error","fill all the fields",icon='warning')





#_viewing the details
class viewcustomer(Toplevel):
    def __init__(self,cid):
        Toplevel.__init__(self)

        self.geometry("650x650+600+200")
        self.title("VIEW CUSTOMER")
        self.resizable(False,False)
        self.top =Frame(self , height =150 ,bg='#B9E9DD')
        self.top.pack(fill=X)
        self.botom =Frame(self , height =500 ,bg='#FCE393')
        self.botom.pack(fill=X)

    #    fetching the data from database 
        query="select * from customers where cid ='{}'".format(cid)
        result=cursor.execute(query)
        result=cursor.fetchone()
        self.cid=cid
        name=result[1]
        email=result[2]
        phone=result[3]
        plan=result[4]
        Paid =result[5]
        start =result[6]
        end=result[7]

        print("name=",name)
        print("email=",email)
        print("phone=",phone) 
        print("plan=",plan)
        print("paid=",Paid)
        print("start=",start) 
        print("end=",end) 

    #top frame design
         #icon
        self.top_image=PhotoImage(file= 'images\customer.png')
        self.top_image_label= Label(self.top, image=self.top_image,bg='#B9E9DD')
        self.top_image_label.place(x=200 ,y=40)
         #title
        self.heading=Label(self.top, text='VIEW CUSTOMER', font='opensans 20 bold',bg='#B9E9DD',fg='#595959' )
        self.heading.place(x=300,y=60)

#button

        self.label_name =Label(self.botom, text="name",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_name.place(x=35,y=60)
        self.entry_name=Entry(self.botom,width=30 ,bd=4)
        self.entry_name.insert(0,name)
        self.entry_name.config(state='disabled')
        self.entry_name.place(x=170,y=60)

        self.label_email =Label(self.botom, text="email",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_email.place(x=35,y=100)
        self.entry_email=Entry(self.botom,width=30 ,bd=4)
        self.entry_email.insert(0,email)
        self.entry_email.config(state='disabled')
        self.entry_email.place(x=170,y=100)
        
        self.label_phone =Label(self.botom, text="phone",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_phone.place(x=35,y=140)
        self.entry_phone=Entry(self.botom,width=30 ,bd=4)
        self.entry_phone.insert(0,phone)
        self.entry_phone.config(state='disabled')
        self.entry_phone.place(x=170,y=140)

        self.label_plan =Label(self.botom, text="plan",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_plan.place(x=35,y=180)
        self.entry_plan=Entry(self.botom,width=30 ,bd=4)
        self.entry_plan.insert(0,plan)
        self.entry_plan.config(state='disabled')
        self.entry_plan.place(x=170,y=180)

        self.label_paid =Label(self.botom, text="initial paid",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_paid.place(x=35,y=220)
        self.entry_paid=Entry(self.botom,width=30 ,bd=4)
        self.entry_paid.insert(0,Paid)
        self.entry_paid.config(state='disabled')
        self.entry_paid.place(x=170,y=220)
   
        self.label_start =Label(self.botom, text="start date",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_start.place(x=35,y=260)
        self.entry_start=Entry(self.botom,width=30 ,bd=4)
        self.entry_start.insert(0,start)
        self.entry_start.config(state='disabled')
        self.entry_start.place(x=170,y=260)

        self.label_end =Label(self.botom, text="end date",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_end.place(x=35,y=300)
        self.entry_end=Entry(self.botom,width=30 ,bd=4)
        self.entry_end.insert(0,end)
        self.entry_end.config(state='disabled')
        self.entry_end.place(x=170,y=300)


  
#--------------------------------------------------------------------customer-------------------------------------------------------------#
#
#
#
#
#
#
#
#
#--------------------------------------------------------------------equipment-------------------------------------------------------------#

# events after clicking  equipment button

#_updating the details

class updateequipment(Toplevel):
    def __init__(self,eid):
        Toplevel.__init__(self)

        self.geometry("650x650+600+200")
        self.title("UPDATE EQUIPMENT")
        self.resizable(False,False)
        self.top =Frame(self , height =150 ,bg='#B9E9DD')
        self.top.pack(fill=X)
        self.botom =Frame(self , height =500 ,bg='#FCE393')
        self.botom.pack(fill=X)

    #top frame design
         #icon
        self.top_image=PhotoImage(file= 'images\customer.png')
        self.top_image_label= Label(self.top, image=self.top_image,bg='#B9E9DD')
        self.top_image_label.place(x=200 ,y=40)
         #title
        self.heading=Label(self.top, text='UPDATE EQUIPMENT', font='opensans 20 bold',bg='#B9E9DD',fg='#595959' )
        self.heading.place(x=300,y=60)

    #    fetching the data from database 
        query="select * from equipments where eid ='{}'".format(eid)
        result=cursor.execute(query)
        result=cursor.fetchone()
        self.eid=eid
        name=result[1]
        quantity=result[2]
        price=result[3]
        remark=result[4]

        print("name=",name)
        print("quantity=",quantity)
        print("price=",price) 
        print("remark=",remark)

#button
        self.label_name =Label(self.botom, text="name",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_name.place(x=49,y=40)
        self.entry_name=Entry(self.botom,width=30 ,bd=4)
        self.entry_name.insert(0,name)
        self.entry_name.place(x=150,y=40)

        self.label_quantity =Label(self.botom, text="quantity",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_quantity.place(x=49,y=80)
        self.entry_quantity=Entry(self.botom,width=30 ,bd=4)
        self.entry_quantity.insert(0,quantity)
        self.entry_quantity.place(x=150,y=80)
   
        self.label_price =Label(self.botom, text="price",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_price.place(x=49,y=120)
        self.entry_price=Entry(self.botom,width=30 ,bd=4)
        self.entry_price.insert(0,price)
        self.entry_price.place(x=150,y=120)

        self.label_remark =Label(self.botom, text="remark",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_remark.place(x=49,y=160)
        self.entry_remark=Entry(self.botom,width=30 ,bd=4)
        self.entry_remark.insert(0,remark)
        self.entry_remark.place(x=150,y=160)

        self.Button= Button(self.botom,text=' UPDATE  ',font='arial 15 bold',fg='#262626',bg='#B9E9DD',command=self.update_equipment)
        self.Button.place(x=200,y=445,)

    def update_equipment(self):

        p_id=self.eid
        name = self.entry_name.get()
        quantity= self.entry_quantity.get()
        price = self.entry_price.get()
        remark = self.entry_remark.get()
        query="update equipments set name=%s, quantity=%s , price=%s ,remark=%s where eid=%s"
        data=(name,quantity,price,remark,p_id)

        try:
            cursor.execute(query,data)
            connection.commit()
            messagebox.showinfo("success","updated succcesfully")
            self.destroy()


        except EXCEPTION as e:
            print(e)              



#_addition of the details
class addequipment(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("650x650+600+200")
        self.title("ADD EQUIPMENT")
        self.resizable(False,False)
        self.top =Frame(self , height =150 ,bg='#B9E9DD')
        self.top.pack(fill=X)
        self.botom =Frame(self , height =500 ,bg='#FCE393')
        self.botom.pack(fill=X)

    #top frame design
         #icon
        self.top_image=PhotoImage(file= 'images\customer.png')
        self.top_image_label= Label(self.top, image=self.top_image,bg='#B9E9DD')
        self.top_image_label.place(x=200 ,y=40)
         #title
        self.heading=Label(self.top, text='ADD EQUIPMENT', font='opensans 20 bold',bg='#B9E9DD',fg='#595959' )
        self.heading.place(x=300,y=60)

#button
        self.label_name =Label(self.botom, text="name",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_name.place(x=49,y=40)
        self.entry_name=Entry(self.botom,width=30 ,bd=4)
        self.entry_name.insert(0,"")
        self.entry_name.place(x=150,y=40)

        self.label_quantity =Label(self.botom, text="quantity",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_quantity.place(x=49,y=80)
        self.entry_quantity=Entry(self.botom,width=30 ,bd=4)
        self.entry_quantity.insert(0,"")
        self.entry_quantity.place(x=150,y=80)
   
        self.label_price =Label(self.botom, text="price",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_price.place(x=49,y=120)
        self.entry_price=Entry(self.botom,width=30 ,bd=4)
        self.entry_price.insert(0,"")
        self.entry_price.place(x=150,y=120)

        self.label_remark =Label(self.botom, text="remark",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_remark.place(x=49,y=160)
        self.entry_remark=Entry(self.botom,width=30 ,bd=4)
        self.entry_remark.insert(0,"")
        self.entry_remark.place(x=150,y=160)

        self.Button= Button(self.botom,text=' ADD  ',font='arial 15 bold',fg='#262626',bg='#B9E9DD',command=self.add_equipments)
        self.Button.place(x=200,y=445,)


    def add_equipments(self):
        name = self.entry_name.get()
        quantity= self.entry_quantity.get()
        price = self.entry_price.get()
        remark=self.entry_remark.get()
        if name and quantity and price and remark !="":
            try:
                with connection.cursor() as cursor:
                    query = "INSERT INTO equipments (name,quantity,price,remark) VALUES (%s,%s,%s,%s)"
                    cursor.execute(query,(name,quantity,price,remark))
                    connection.commit()
                    messagebox.showinfo("success","EQUIPMENT added")
                    self.destroy()
            except EXCEPTION as e:
                messagebox.showinfo("Error",str(e))

        else:
            messagebox.showerror("Error","fill all the fields",icon='warning')



#_viewing the details
class viewequipment(Toplevel):
    def __init__(self,eid):
        Toplevel.__init__(self)

        self.geometry("650x650+600+200")
        self.title("VIEW EQUIPMENT")
        self.resizable(False,False)
        self.top =Frame(self , height =150 ,bg='#B9E9DD')
        self.top.pack(fill=X)
        self.botom =Frame(self , height =500 ,bg='#FCE393')
        self.botom.pack(fill=X)

    #top frame design
         #icon
        self.top_image=PhotoImage(file= 'images\customer.png')
        self.top_image_label= Label(self.top, image=self.top_image,bg='#B9E9DD')
        self.top_image_label.place(x=200 ,y=40)
         #title
        self.heading=Label(self.top, text='VIEW EQUIPMENT', font='opensans 20 bold',bg='#B9E9DD',fg='#595959' )
        self.heading.place(x=300,y=60)
   
        query="select * from equipments where eid ='{}'".format(eid)
        result=cursor.execute(query)
        result=cursor.fetchone()
        self.eid=eid
        name=result[1]
        quantity=result[2]
        price=result[3]
        remark=result[4]

        print("name=",name)
        print("quantity=",quantity)
        print("price=",price) 
        print("remark=",remark)

#button
        self.label_name =Label(self.botom, text="name",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_name.place(x=49,y=40)
        self.entry_name=Entry(self.botom,width=30 ,bd=4)
        self.entry_name.insert(0,name)
        self.entry_name.config(state='disabled')
        self.entry_name.place(x=150,y=40)

        self.label_quantity =Label(self.botom, text="quantity",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_quantity.place(x=49,y=80)
        self.entry_quantity=Entry(self.botom,width=30 ,bd=4)
        self.entry_quantity.insert(0,quantity)
        self.entry_quantity.config(state='disabled')
        self.entry_quantity.place(x=150,y=80)
   
        self.label_price =Label(self.botom, text="price",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_price.place(x=49,y=120)
        self.entry_price=Entry(self.botom,width=30 ,bd=4)
        self.entry_price.insert(0,price)
        self.entry_price.config(state='disabled')
        self.entry_price.place(x=150,y=120)

        self.label_remark =Label(self.botom, text="remark",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_remark.place(x=49,y=160)
        self.entry_remark=Entry(self.botom,width=30 ,bd=4)
        self.entry_remark.insert(0,remark)
        self.entry_remark.config(state='disabled')
        self.entry_remark.place(x=150,y=160)

#--------------------------------------------------------------------equipment-------------------------------------------------------------#
#
#
#
#
#
#
#
#
#
#
#--------------------------------------------------------------------employee-------------------------------------------------------------#

# events after clicking  employee button
   
#_updating the details

class addemployee(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("650x650+600+200")
        self.title("ADD EMPLOYEE")
        self.resizable(False,False)
        self.top =Frame(self , height =150 ,bg='#B9E9DD')
        self.top.pack(fill=X)
        self.botom =Frame(self , height =500 ,bg='#FCE393')
        self.botom.pack(fill=X)



    #top frame design
         #icon
        self.top_image=PhotoImage(file= 'images\customer.png')
        self.top_image_label= Label(self.top, image=self.top_image,bg='#B9E9DD')
        self.top_image_label.place(x=200 ,y=40)
         #title
        self.heading=Label(self.top, text='ADD EMPLOYEE', font='opensans 20 bold',bg='#B9E9DD',fg='#595959' )
        self.heading.place(x=300,y=60)
   
#button
        self.label_name =Label(self.botom, text="name",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_name.place(x=35,y=40)
        self.entry_name=Entry(self.botom,width=30 ,bd=4)
        self.entry_name.insert(0,"enter the  name")
        self.entry_name.place(x=170,y=40)

        self.label_designation =Label(self.botom, text="designation",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_designation.place(x=35,y=80)
        self.entry_designation=Entry(self.botom,width=30 ,bd=4)
        self.entry_designation.insert(0,"enter the designation")
        self.entry_designation.place(x=170,y=80)
   
        self.label_salary =Label(self.botom, text="salary",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_salary.place(x=35,y=120)
        self.entry_salary=Entry(self.botom,width=30 ,bd=4)
        self.entry_salary.insert(0,"enter the salary ")
        self.entry_salary.place(x=170,y=120)

        self.label_email =Label(self.botom, text="email",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_email.place(x=35,y=160)
        self.entry_email=Entry(self.botom,width=30 ,bd=4)
        self.entry_email.insert(0,"enter the email")
        self.entry_email.place(x=170,y=160)

        self.label_phone =Label(self.botom, text="phone",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_phone.place(x=35,y=200)
        self.entry_phone=Entry(self.botom,width=30 ,bd=4)
        self.entry_phone.insert(0,"enter phone no")
        self.entry_phone.place(x=170,y=200)

        self.Button= Button(self.botom,text=' ADD  ',font='arial 15 bold',fg='#262626',bg='#B9E9DD',command=self.add_employee)
        self.Button.place(x=200,y=445,)

    def add_employee(self):
        name = self.entry_name.get()
        designation = self.entry_designation.get()
        salary = self.entry_salary.get()
        email= self.entry_email.get()
        phone=self.entry_phone.get()
        
        if name and designation and salary and email and phone !="":
            try:
                with connection.cursor() as cursor:
                    query = "INSERT INTO employees (name,designation,salary,email,phone) VALUES (%s,%s,%s,%s,%s)"
                    cursor.execute(query,(name,designation,salary,email,phone))
                    connection.commit()
                    messagebox.showinfo("success","employee added")
                    self.destroy()
            except EXCEPTION as e:
                messagebox.showinfo("Error",str(e))

        else:
            messagebox.showerror("Error","fill all the fields",icon='warning')







class updateemployee(Toplevel):
    def __init__(self,empid):
        Toplevel.__init__(self)

        self.geometry("650x650+600+200")
        self.title("UPDATE EMPLOYEE")
        self.resizable(False,False)
        self.top =Frame(self , height =150 ,bg='#B9E9DD')
        self.top.pack(fill=X)
        self.botom =Frame(self , height =500 ,bg='#FCE393')
        self.botom.pack(fill=X)

        query="select * from employees where empid ='{}'".format(empid)
        result=cursor.execute(query)
        result=cursor.fetchone()
        self.empid=empid
        name=result[1]
        designation=result[2]
        salary=result[3]
        email=result[4]
        phone=result[5]

        print("name=",name)
        print("designation=",designation)
        print("salary=",salary) 
        print("email=",email)
        print("phone=",phone)

    #top frame design
         #icon
        self.top_image=PhotoImage(file= 'images\customer.png')
        self.top_image_label= Label(self.top, image=self.top_image,bg='#B9E9DD')
        self.top_image_label.place(x=200 ,y=40)
         #title
        self.heading=Label(self.top, text='UPDATE EMPLOYEE', font='opensans 20 bold',bg='#B9E9DD',fg='#595959' )
        self.heading.place(x=300,y=60)

#button
        self.label_name =Label(self.botom, text="name",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_name.place(x=35,y=40)
        self.entry_name=Entry(self.botom,width=30 ,bd=4)
        self.entry_name.insert(0,name)
        self.entry_name.place(x=170,y=40)

        self.label_designation =Label(self.botom, text="designation",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_designation.place(x=35,y=80)
        self.entry_designation=Entry(self.botom,width=30 ,bd=4)
        self.entry_designation.insert(0,designation)
        self.entry_designation.place(x=170,y=80)
   
        self.label_salary =Label(self.botom, text="salary",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_salary.place(x=35,y=120)
        self.entry_salary=Entry(self.botom,width=30 ,bd=4)
        self.entry_salary.insert(0,salary)
        self.entry_salary.place(x=170,y=120)

        self.label_email =Label(self.botom, text="email",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_email.place(x=35,y=160)
        self.entry_email=Entry(self.botom,width=30 ,bd=4)
        self.entry_email.insert(0,email)
        self.entry_email.place(x=170,y=160)

        self.label_phone =Label(self.botom, text="phone",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_phone.place(x=35,y=200)
        self.entry_phone=Entry(self.botom,width=30 ,bd=4)
        self.entry_phone.insert(0,phone)
        self.entry_phone.place(x=170,y=200)

        self.Button= Button(self.botom,text=' UPDATE  ',font='arial 15 bold',fg='#262626',bg='#B9E9DD',command=self.update_employee)
        self.Button.place(x=200,y=445,)

    def update_employee(self):
        emp_id=self.empid
        name = self.entry_name.get()
        designation = self.entry_designation.get()
        salary = self.entry_salary.get()
        email = self.entry_email.get()
        phone = self.entry_phone.get()

        query="update employees set name=%s, designation=%s , salary=%s ,email=%s ,phone=%s where empid=%s"
        data=(name,designation,salary,email,phone,emp_id)

        try:
            cursor.execute(query,data)
            connection.commit()
            messagebox.showinfo("success","updated succcesfully")
            self.destroy()
            

        except EXCEPTION as e:
            print(e)    
        























#_viewing the details
class viewemployee(Toplevel):
    def __init__(self,empid):
        Toplevel.__init__(self)

        self.geometry("650x650+600+200")
        self.title("VIEW EMPLOYEE")
        self.resizable(False,False)
        self.top =Frame(self , height =150 ,bg='#B9E9DD')
        self.top.pack(fill=X)
        self.botom =Frame(self , height =500 ,bg='#FCE393')
        self.botom.pack(fill=X)

    #    fetching the data from database 
        query="select * from employees where empid ='{}'".format(empid)
        result=cursor.execute(query)
        result=cursor.fetchone()
        self.empid=empid
        name=result[1]
        designation=result[2]
        salary=result[3]
        email=result[4]
        phone=result[5]

        print("name=",name)
        print("designation=",designation)
        print("salary=",salary) 
        print("email=",email)
        print("phone=",phone)



    #top frame design
         #icon
        self.top_image=PhotoImage(file= 'images\customer.png')
        self.top_image_label= Label(self.top, image=self.top_image,bg='#B9E9DD')
        self.top_image_label.place(x=200 ,y=40)
         #title
        self.heading=Label(self.top, text='VIEW EMPLOYEE', font='opensans 20 bold',bg='#B9E9DD',fg='#595959' )
        self.heading.place(x=300,y=60)
        self.label_name =Label(self.botom, text="name",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_name.place(x=35,y=40)
        self.entry_name=Entry(self.botom,width=30 ,bd=4)
        self.entry_name.insert(0,name)
        self.entry_name.place(x=170,y=40)

        self.label_designation =Label(self.botom, text="designation",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_designation.place(x=35,y=80)
        self.entry_designation=Entry(self.botom,width=30 ,bd=4)
        self.entry_designation.insert(0,designation)
        self.entry_designation.place(x=170,y=80)
   
        self.label_salary =Label(self.botom, text="salary",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_salary.place(x=35,y=120)
        self.entry_salary=Entry(self.botom,width=30 ,bd=4)
        self.entry_salary.insert(0,salary)
        self.entry_salary.place(x=170,y=120)

        self.label_email =Label(self.botom, text="email",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_email.place(x=35,y=160)
        self.entry_email=Entry(self.botom,width=30 ,bd=4)
        self.entry_email.insert(0,email)
        self.entry_email.place(x=170,y=160)

        self.label_phone =Label(self.botom, text="phone",font='arial 15 bold',fg='#595959',bg='#FCE393')
        self.label_phone.place(x=35,y=200)
        self.entry_phone=Entry(self.botom,width=30 ,bd=4)
        self.entry_phone.insert(0,phone)
        self.entry_phone.place(x=170,y=200)


#--------------------------------------------------------------------employee-------------------------------------------------------------#