from msilib.schema import Error
import tkinter
from tkinter import *
import tkinter.messagebox 
from tkinter.ttk import *
import customtkinter
import GetCompanyData
import FundamentalAnalysis

root_tk = customtkinter.CTk()
root_tk.geometry("400x240")
root_tk.title("Fundamental Analysis Calculator")

customtkinter.set_appearance_mode("Dark")

def get_data_clicked():
    try:
        print(entry.get())
        GetCompanyData.get_company_data(entry.get())
        tkinter.messagebox.showinfo( title="Info", message="Stock annual report and price succesfuly inserted in the database")
    except:
        tkinter.messagebox.showerror("Error", "Impossible to get stock annual report and price")

def analysis_clicked():
    try:
        print(entry.get())
        FundamentalAnalysis.fundamental_analysis(entry.get())
        tkinter.messagebox.showinfo( title="Info", message="Fundamental analysis performed  and inserted in the database")
    except:
        print(Error)
        tkinter.messagebox.showerror("Error", "Impossible to perform stock fundamental analysis")


entry = customtkinter.CTkEntry(master=root_tk, width=120, height=35, corner_radius=10)
entry.place(relx=0.5, y=50, anchor=tkinter.CENTER)
entry.insert(0, "Company Ticker")


button = customtkinter.CTkButton(master=root_tk, text='Get Data', corner_radius=10, command=get_data_clicked)
button.place(relx=0.5, y=100, anchor=tkinter.CENTER)

button2 = customtkinter.CTkButton(master=root_tk, text='Analysis', corner_radius=10, command=analysis_clicked)
button2.place(relx=0.5, y=150, anchor=tkinter.CENTER)


root_tk.iconbitmap('pig.ico')
root_tk.mainloop()
