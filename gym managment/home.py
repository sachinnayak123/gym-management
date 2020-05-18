from tkinter import *
import datetime
from homedb import *



date=datetime.datetime.now().date()
date= str(    date)

class Application(object):
    def __init__(self,master):
        self.master = master
    #frame      
        self.top =Frame(master , height =150 ,bg='#B9E9DD')
        self.top.pack(fill=X)
        self.botom =Frame(master , height =500 ,bg='#FCE393')
        self.botom.pack(fill=X)

    #top frame design
         #title
        self.heading=Label(self.top, text=' GYM MANAGMENT', font='opensans 28 bold',bg='#B9E9DD',fg='#595959')
        self.heading.place(x=140,y=40)
        
        self.d=Label(self.top, text='by sachin nayak', font='opensans 10 bold',bg='#B9E9DD',fg='#595959' )
        self.d.place(x=440,y=85)
         #date
        self.date_label= Label(self.top, text='DATE :   '   +date ,font='arial 11 bold',fg='#595959',bg='#B9E9DD')
        self.date_label.place(x=500,y=120)

    #botom frame design
    

         #icon
        self.botom_image=PhotoImage(file= 'images\gym.png')
        self.botom_image_label= Label(self.botom, image=self.botom_image,bg='#FCE393')
        self.botom_image_label.place(x=350 ,y=50)  


         #buttons
        self.planButton= Button(self.botom,       text='    PLANS                  ',font='arial 15 bold',fg='#262626',bg='#B9E9DD', command=self.My_Plans)
        self.planButton.place(x=6,y=60,)

        self.customersButton= Button(self.botom,  text='    CUSTOMERS        ',font='arial 15 bold',fg='#262626',bg='#B9E9DD',command=self.My_Customers)
        self.customersButton.place(x=6,y=120)        

        self.employessButton= Button(self.botom,  text='    EMPLOYESS         ',font='arial 15 bold',fg='#262626',bg='#B9E9DD',command=self.My_Employess)
        self.employessButton.place(x=6,y=180)

        self.equipmentsButton= Button(self.botom, text='    EQUIPMENTS        ',font='arial 15 bold',fg='#262626',bg='#B9E9DD',command=self.My_Equipment)
        self.equipmentsButton.place(x=6,y=240)

        self.dietchartButton= Button(self.botom,  text='    DIET CHART          ',font='arial 15 bold',fg='#262626',bg='#B9E9DD',command=self.My_Dietchart)
        self.dietchartButton.place(x=6,y=300)

    def My_Plans(self):
        plan = MyPlans()

    def My_Employess(self):
        employee = MyEmployess() 

    def My_Customers(self):
        customer = MyCustomers()  

    def My_Equipment(self):
        equipment = MyEquipment()

    def My_Dietchart(self):
        diet = MyDietchart()

def main():
    root=Tk()
    app=Application(root)
    root.title("HOME")
    root.geometry("650x550+350+200")
    root.resizable(False,False)
    root.mainloop()

if __name__=="__main__":
    main()


      
