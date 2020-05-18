from tkinter import *
from after_click_event import *
import os # for importing the image from the path
from PIL import Image, ImageTk  #module to put image in tkinter
import pymysql
connection= pymysql.connect("localhost","root","123sachin","gym")
cursor=connection.cursor()



#-----------------------------------------------------------------------MY-plans------------------------------------------------------------#

class MyPlans(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("650x650+600+200")
        self.title("PLANS")
        self.resizable(False,False)

        self.top =Frame(self , height =150 ,bg='#B9E9DD')
        self.top.pack(fill=X)
        self.botom =Frame(self , height =500 ,bg='#FCE393')
        self.botom.pack(fill=X)

    #top frame design
         #icon
        self.top_image=PhotoImage(file= 'images\plan.png')
        self.top_image_label= Label(self.top, image=self.top_image,bg='#B9E9DD')
        self.top_image_label.place(x=200 ,y=40)
         #title
        self.heading=Label(self.top, text='  PLANS ', font='opensans 20 bold',bg='#B9E9DD',fg='#595959' )
        self.heading.place(x=300,y=60)



  #listbox
        self.listBox = Listbox(self.botom ,width=60,height=35,bg='#fdecb4' )
        self.listBox.grid(row=0,column=0,padx=(40,0))
    
        #scrollbar
        self.scroll = Scrollbar(self.botom,orient=VERTICAL)
        self.scroll.grid(row=0,column=1, sticky=N+S)

        self.scroll.config(command=self.listBox.yview)
        self.listBox.config(yscrollcommand=self.scroll.set)


        plan = cursor.execute("SELECT * FROM plans")
        plan=cursor.fetchall()
       
        count=0
        for plans in plan:
            self.listBox.insert(count,str(plans[0])+".  "+plans[1])
            count +=1

        #buttons
        btnadd1= Button(self.botom ,text='ADD',width=12,font='sans 12 bold',fg='#262626',bg='#B9E9DD',command=self.add_plan)
        btnadd1.grid(row=0,column=2,padx=50,pady=50 ,sticky=N)

        btnupdate2= Button(self.botom ,text='UPDATE',width=12,font='sans 12 bold',fg='#262626',bg='#B9E9DD',command=self.update_plan)
        btnupdate2.grid(row=0,column=2,padx=0,pady=90, sticky=N)

        btnview3= Button(self.botom ,text='VIEW',width=12,font='sans 12 bold',fg='#262626',bg='#B9E9DD',command=self.view_plan)
        btnview3.grid(row=0,column=2,padx=0,pady=130 ,sticky=N)

        btndelete4= Button(self.botom ,text='DELETE',width=12,font='sans 12 bold',fg='#262626',bg='#B9E9DD',command=self.delete_plan)
        btndelete4.grid(row=0,column=2,padx=0,pady=170 ,sticky=N)
    

    
    def add_plan(self):
        add = addplan()
    def update_plan(self):  
        selected_item= self.listBox.curselection()
        plan=self.listBox.get(selected_item)
        pid=plan.split(".")[0]
        update = updateplan(pid)


    def view_plan(self):

        selected_item= self.listBox.curselection()
        plan=self.listBox.get(selected_item)
        pid=plan.split(".")[0]        
        view = viewplan(pid)
    
    def delete_plan(self):
        selected_item= self.listBox.curselection()
        plan=self.listBox.get(selected_item)
        pid=plan.split(".")[0]  

        query="delete from plans where pid={}".format(pid)
        answer= messagebox.askquestion("warning","are you sure you want to delete")
        if answer =='yes':
            try:
                cursor.execute(query)
                connection.commit()
                messagebox.showinfo("succes","deleted")
                self.destroy()
            except EXCEPTION as e:
                messagebox.showinfo("Info",str(e))



#-----------------------------------------------------------------------MY-plans------------------------------------------------------------#









#-----------------------------------------------------------------------MY-customer------------------------------------------------------------#




class MyCustomers(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("650x650+600+200")
        self.title("CUSTOMERS")
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
        self.heading=Label(self.top, text='CUSTOMERS', font='opensans 20 bold',bg='#B9E9DD',fg='#595959' )
        self.heading.place(x=300,y=60)
   

        #listbox
        self.listBox = Listbox(self.botom ,width=60,height=35,bg='#fdecb4')
        self.listBox.grid(row=0,column=0,padx=(40,0))

        customer = cursor.execute("SELECT * FROM customers")
        customer =cursor.fetchall()
       
        count=0
        for customers in customer:
            self.listBox.insert(count,str(customers[0])+".  "+customers[1])
            count +=1

    
        #scrollbar
        self.scroll = Scrollbar(self.botom,orient=VERTICAL)
        self.scroll.grid(row=0,column=1, sticky=N+S)

        self.scroll.config(command=self.listBox.yview)
        self.listBox.config(yscrollcommand=self.scroll.set)

 
        #buttons
        btnadd= Button(self.botom ,text='ADD',width=12,font='sans 12 bold',fg='#262626',bg='#B9E9DD', command=self.add_customer)
        btnadd.grid(row=0,column=2,padx=50,pady=50 ,sticky=N)

        btnupdate= Button(self.botom ,text='UPDATE',width=12,font='sans 12 bold',fg='#262626',bg='#B9E9DD',command=self.update_customer)
        btnupdate.grid(row=0,column=2,padx=0,pady=90, sticky=N)

        btnview= Button(self.botom ,text='VIEW',width=12,font='sans 12 bold',fg='#262626',bg='#B9E9DD',command=self.view_customer)
        btnview.grid(row=0,column=2,padx=0,pady=130 ,sticky=N)

        btndelete= Button(self.botom ,text='DELETE',width=12,font='sans 12 bold',fg='#262626',bg='#B9E9DD',command=self.delete_customer)
        btndelete.grid(row=0,column=2,padx=0,pady=170 ,sticky=N)


    def add_customer(self):
        add = addcustomer()

    def update_customer(self):
        selected_item= self.listBox.curselection()
        plan=self.listBox.get(selected_item)
        cid=plan.split(".")[0]
        update = updatecustomer(cid)


    def view_customer(self):
        selected_item= self.listBox.curselection()
        plan=self.listBox.get(selected_item)
        cid=plan.split(".")[0]
        view = viewcustomer(cid)

    def delete_customer(self):
        selected_item= self.listBox.curselection()
        customer=self.listBox.get(selected_item)
        cid=customer.split(".")[0]  

        query="delete from customers where cid={}".format(cid)
        answer= messagebox.askquestion("warning","are you sure you want to delete")
        if answer =='yes':
            try:
                cursor.execute(query)
                connection.commit()
                messagebox.showinfo("succes","deleted")
                self.destroy()
            except EXCEPTION as e:
                messagebox.showinfo("Info",str(e))
       

#-----------------------------------------------------------------------MY-customer------------------------------------------------------------#











#-----------------------------------------------------------------------MY-equi[ment------------------------------------------------------------#





class MyEquipment(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("650x650+600+200")
        self.title("EQUIPMENTS")
        self.resizable(False,False)

        self.top =Frame(self , height =150 ,bg='#B9E9DD')
        self.top.pack(fill=X)
        self.botom =Frame(self , height =500 ,bg='#FCE393')
        self.botom.pack(fill=X)

    #top frame design
         #icon
        self.top_image=PhotoImage(file= 'images\equipment.png')
        self.top_image_label= Label(self.top, image=self.top_image,bg='#B9E9DD')
        self.top_image_label.place(x=200 ,y=40)
         #title
        self.heading=Label(self.top, text='  EQUIPMENTS', font='opensans 20 bold',bg='#B9E9DD',fg='#595959' )
        self.heading.place(x=300,y=60)


  #listbox
        self.listBox = Listbox(self.botom ,width=60,height=35 ,bg='#fdecb4')
        self.listBox.grid(row=0,column=0,padx=(40,0))
    
        #scrollbar
        self.scroll = Scrollbar(self.botom,orient=VERTICAL)
        self.scroll.grid(row=0,column=1, sticky=N+S)

        self.scroll.config(command=self.listBox.yview)
        self.listBox.config(yscrollcommand=self.scroll.set)

        equipment = cursor.execute("SELECT * FROM equipments")
        equipment = cursor.fetchall()
       
        count=0
        for equipments in equipment:
            self.listBox.insert(count,str(equipments[0])+".  "+equipments[1])
            count +=1
 
        #buttons
        btnadd5= Button(self.botom ,text='ADD',width=12,font='sans 12 bold',fg='#262626',bg='#B9E9DD',command=self.add_equipment)
        btnadd5.grid(row=0,column=2,padx=50,pady=50 ,sticky=N)

        btnupdate6= Button(self.botom ,text='UPDATE',width=12,font='sans 12 bold',fg='#262626',bg='#B9E9DD',command=self.update_equipment)
        btnupdate6.grid(row=0,column=2,padx=0,pady=90, sticky=N)

        btnview7= Button(self.botom ,text='VIEW',width=12,font='sans 12 bold',fg='#262626',bg='#B9E9DD',command=self.view_equipment)
        btnview7.grid(row=0,column=2,padx=0,pady=130 ,sticky=N)

        btndelete8= Button(self.botom ,text='DELETE',width=12,font='sans 12 bold',fg='#262626',bg='#B9E9DD',command=self.delete_equipment)
        btndelete8.grid(row=0,column=2,padx=0,pady=170 ,sticky=N)

    def add_equipment(self):
        add = addequipment()
        
    def update_equipment(self):
        selected_item= self.listBox.curselection()
        equipment=self.listBox.get(selected_item)
        eid=equipment.split(".")[0]
        update = updateequipment(eid) 

    def view_equipment(self):
        selected_item= self.listBox.curselection()
        equipment=self.listBox.get(selected_item)
        eid=equipment.split(".")[0]
        view = viewequipment(eid)

    def delete_equipment(self):
        selected_item= self.listBox.curselection()
        equipment=self.listBox.get(selected_item)
        eid=equipment.split(".")[0]  

        query="delete from equipments where eid={}".format(eid)
        answer= messagebox.askquestion("warning","are you sure you want to delete")
        if answer =='yes':
            try:
                cursor.execute(query)
                connection.commit()
                messagebox.showinfo("succes","deleted")
                self.destroy()
            except EXCEPTION as e:
                messagebox.showinfo("Info",str(e))



#-----------------------------------------------------------------------MY-equipment------------------------------------------------------------#








#-----------------------------------------------------------------------MY-employee------------------------------------------------------------#

class MyEmployess(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("650x650+600+200")
        self.title("EMPLOYESS")
        self.resizable(False,False)

        self.top =Frame(self , height =150 ,bg='#B9E9DD')
        self.top.pack(fill=X)
        self.botom =Frame(self , height =500 ,bg='#FCE393')
        self.botom.pack(fill=X)

    #top frame design
         #icon
        self.top_image=PhotoImage(file= 'images\employee.png')
        self.top_image_label= Label(self.top, image=self.top_image,bg='#B9E9DD')
        self.top_image_label.place(x=200 ,y=40)
         #title
        self.heading=Label(self.top, text='    EMPLOYESS', font='opensans 20 bold',bg='#B9E9DD',fg='#595959' )
        self.heading.place(x=300,y=60)


  #listbox
        self.listBox = Listbox(self.botom ,width=60,height=35,bg='#fdecb4' )
        self.listBox.grid(row=0,column=0,padx=(40,0))
    
        #scrollbar
        self.scroll = Scrollbar(self.botom,orient=VERTICAL)
        self.scroll.grid(row=0,column=1, sticky=N+S)

        self.scroll.config(command=self.listBox.yview)
        self.listBox.config(yscrollcommand=self.scroll.set)

        employee = cursor.execute("SELECT * FROM employees")
        employee=cursor.fetchall()
       
        count=0
        for employees in employee:
            self.listBox.insert(count,str(employees[0])+".  "+employees[1])
            count +=1

 
        #buttons
        btnadd9= Button(self.botom ,text='ADD',width=12,font='sans 12 bold',fg='#262626',bg='#B9E9DD',command=self.add_employee)
        btnadd9.grid(row=0,column=2,padx=50,pady=50 ,sticky=N)

        btnupdate10= Button(self.botom ,text='UPDATE',width=12,font='sans 12 bold',fg='#262626',bg='#B9E9DD',command=self.update_employee)
        btnupdate10.grid(row=0,column=2,padx=0,pady=90, sticky=N)

        btnview11= Button(self.botom ,text='VIEW',width=12,font='sans 12 bold',fg='#262626',bg='#B9E9DD',command=self.view_employee)
        btnview11.grid(row=0,column=2,padx=0,pady=130 ,sticky=N)

        btndelete12= Button(self.botom ,text='DELETE',width=12,font='sans 12 bold',fg='#262626',bg='#B9E9DD',command=self.delete_employee)
        btndelete12.grid(row=0,column=2,padx=0,pady=170 ,sticky=N)

    def add_employee(self):
        add = addemployee()
    def update_employee(self):
        selected_item= self.listBox.curselection()
        plan=self.listBox.get(selected_item)
        empid=plan.split(".")[0]
        update = updateemployee(empid)


    def view_employee(self):
        selected_item= self.listBox.curselection()
        plan=self.listBox.get(selected_item)
        empid=plan.split(".")[0]
        view = viewemployee(empid)

    def delete_employee(self):
        selected_item= self.listBox.curselection()
        plan=self.listBox.get(selected_item)
        empid=plan.split(".")[0]  

        query="delete from employees where empid={}".format(empid)
        answer= messagebox.askquestion("warning","are you sure you want to delete")
        if answer =='yes':
            try:
                cursor.execute(query)
                connection.commit()
                messagebox.showinfo("succes","deleted")
                self.destroy()
            except EXCEPTION as e:
                messagebox.showinfo("Info",str(e))





#----------------------------------------------------------------------MY-employee------------------------------------------------------------#











#----------------------------------------------------------------------MY--diet chart------------------------------------------------------------#



class MyDietchart(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("950x950+800+400")
        self.title("DIET CHART")
        self.resizable(False,False)

        self.top =Frame(self , height =150 ,bg='#B9E9DD')
        self.top.pack(fill=X)
        self.botom =Frame(self , height =900 ,bg='#FCE393')
        self.botom.pack(fill=X)

    #top frame design
         #icon
        self.top_image=PhotoImage(file= 'images\diet.png')
        self.top_image_label= Label(self.top, image=self.top_image,bg='#B9E9DD')
        self.top_image_label.place(x=200 ,y=40)
         #title
        self.heading=Label(self.top, text='  DIET CHART', font='opensans 20 bold',bg='#B9E9DD',fg='#595959' )
        self.heading.place(x=300,y=60)

     #bottome fram design
        self.botom_image = PhotoImage(file="images\chart.png")  
        self.botom_image_label= Label(self.botom, image=self.botom_image,bg='#FCE393')
        self.botom_image_label.place(x=0 ,y=0)



      


#-----------------------------------------------------------------------MY-diet chart------------------------------------------------------------#