from tkinter import *
from tkinter.ttk import *

window = Tk()

window.title("Stock Fundamental Analysis")

window.geometry('350x200')

Tickerlbl = Label(window, text="Company Ticker")
""" CompanyName = Label(window, text="Company Name")
Currency= Label(window, text="Currency")
CurrentPrice=Label(window, text="CurrentPrice")

ReferencePrice2020=Label(window, text="Reference Price 2020")
ReferencePrice2019=Label(window, text="Reference Price 2019")
ReferencePrice2018=Label(window, text="Reference Price 2018")
ReferencePrice2017=Label(window, text="Reference Price 2017") """

#Sector = Label(window, text="Sector")


Tickerlbl.grid(column=1, row=0)
""" CompanyName.grid(column=0, row=1)
Currency.grid(column=0, row=2)
CurrentPrice.grid(column=0, row=3)
ReferencePrice2020.grid(column=0, row=4)
ReferencePrice2019.grid(column=0, row=5)
ReferencePrice2018.grid(column=0, row=6)
ReferencePrice2017.grid(column=0, row=7) """

""" Sector.grid(column=0, row=9) """

Tickertxt = Entry(window,width=20)
""" CompanyNametxt=Entry(window,width=20)

Currencytxt=Entry(window,width=20)
CurrentPricetxt=Entry(window,width=20)
ReferencePrice2020txt=Entry(window,width=20)
ReferencePrice2019txt=Entry(window,width=20)
ReferencePrice2018txt=Entry(window,width=20)
ReferencePrice2017txt=Entry(window,width=20)
 """

""" Sectortxt = Combobox(window,width=20)
Sectortxt['values']= ('Banking', 
                    'Automotive',
                    'REIT',
                    'IT Consulting',
                    'E-Commerce',
                    'Telecom',
                    'Airport',
                    'Other Transport',
                    'Facilities Maintenance',
                    'Energy',
                    'Oil and Gas',
                    'Electronics',
                    'Software',
                    'Food',
                    'Health',
                    'Supermarket') """

Tickertxt.grid(column=1, row=1)
""" CompanyNametxt.grid(column=1, row=1)
Currencytxt.grid(column=1, row=2)
CurrentPricetxt.grid(column=1, row=3)
ReferencePrice2020txt.grid(column=1, row=4)
ReferencePrice2019txt.grid(column=1, row=5)
ReferencePrice2018txt.grid(column=1, row=6)
ReferencePrice2017txt.grid(column=1, row=7)
Sectortxt.grid(column=1, row=9) """

def clicked():

    #res = "Hello " + txt.get()
    print(Tickertxt.get())
    """ print(Sectortxt.get()) """

    #Tickerlbl.configure(text= res)

btn = Button(window, text="Get Data", command=clicked)
btn2 = Button(window, text="Analysis", command=clicked)

btn.grid(column=1, row=4)
btn2.grid(column=1, row=5)

window.mainloop()