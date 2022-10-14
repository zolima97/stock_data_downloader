from tkinter import *
from datetime import datetime
import tkinter as tk
from tkinter import ttk
from datetime import date
import pandas as pd



def run():    
    stocks = pd.read_csv("Stock_Table.csv", sep = ";").iloc[2:, :5].reset_index(drop = True)
    stocks.columns = stocks.iloc[0]
    stocks = stocks[1:]
    stocks["Country"] = stocks["Country"].fillna("Unknown")
    stocks["Category Name"] = stocks["Category Name"].fillna("Unknown")
    stocks["Category Name"] = stocks["Category Name"].map(lambda x: x.split(" ")[0])
    
    root = Tk()
    root.title("Input Datas for the Financial Analysis")
    root.geometry("570x750")
    bg = PhotoImage(file = "./background.png", master = root)
    # Show image using label
    label1 = Label( root, image = bg)
    label1.place(x = 0, y = 0)

    benchmarks_dictionary =  {"Australian Stock Exchange":"^AXJO", 
                          "World Index" : "URTH",
                         "New York Stock Exchange" : "^NYA",
                         "Standard & Poor's 500": "SPY",
                         "Nasdaq": "^IXIC",
                         "Shanghai Stock Exchange" : "000001.SS",
                         "Euronext": "IEUR",
                         "Shenzen Stock Exchange": "CNYA",
                         "Hang Seng Index": "HSI",
                          "": "URTH"  }


    def login():
        print(input_entry.get())
        return var

    def myClick():
        submission = "You succesfully submitted!\n Please now exit the window with X command"
        myLabel = Label(root, text=submission)
        myLabel.pack()

    label_input = Label(root, text= "Welcome to your customised Financial Analyzer!"
                       "\nPlease read carefully the istructions to upload the datas the tool will need!"
                         "\nAnd, overall don't forget to have fun! Matteo ;)")
    label_input.pack(padx=5, pady=5)

    label_input = Label(root, text= "Letter Start (insert a letter or a list of letters for filtering stocks)")
    label_input.pack(padx=5, pady=5)
    letters = StringVar()
    input_entry = ttk.Entry(root, textvariable = letters)
    input_entry.pack()

    
    label_input = Label(root, text= "Country Market (if you do not select any, all countries will be)")
    label_input.pack(padx=5, pady=5)
    lista = sorted(list(set(stocks["Country"])))
    country_selected = StringVar()
    country_combobox = ttk.Combobox(root, textvariable = country_selected)
    country_combobox["values"] = [m for m in lista]
    country_combobox["state"] = "readonly"
    country_combobox.pack(padx=5, pady=5)
    
    label_input = Label(root, text= "Sector Market (if you do not select any, all sectors will be")
    label_input.pack(padx=5, pady=5)
    lista = sorted(list(set(stocks["Category Name"])))
    category_selected = StringVar()
    category_combobox = ttk.Combobox(root, textvariable = category_selected)
    category_combobox["values"] = [m for m in lista]
    category_combobox["state"] = "readonly"
    category_combobox.pack(padx=5, pady=5)


    label_input = Label(root, text= "Number of stocks to download (insert a number)")
    label_input.pack(padx=5, pady=5)
    stocks_downloaded = StringVar()
    input_entry = ttk.Entry(root, textvariable = stocks_downloaded)
    input_entry.pack()
    
    label_input = Label(root, text= "Start day (insert a string with the format YYYY-mm-dd, default is: 2022-01-01)")
    label_input.pack(padx=5, pady=5)
    start_day = StringVar()
    input_entry = ttk.Entry(root, textvariable = start_day)
    input_entry.pack()

    label_input = Label(root, text= "Last day (insert a string with the format YYYY-mm-dd, default is today)")
    label_input.pack(padx=5, pady=5)
    last_day = StringVar()
    input_entry = ttk.Entry(root, textvariable = last_day)
    input_entry.pack()

    label_input = Label(root, text= "Range of days you look the percentage increase(insert a number, e.g.: 61)")
    label_input.pack(padx=5, pady=5)
    days_count = StringVar()
    input_entry = ttk.Entry(root, textvariable = days_count)
    input_entry.pack()
    
    
    label_input = Label(root, text= "Percentage increase to find in the date \n range (insert a number: if you want +100% increase, please type 100)")
    label_input.pack(padx=5, pady=5)
    percentage_increase = StringVar()
    input_entry = ttk.Entry(root, textvariable = percentage_increase)
    input_entry.pack()
    
    label_input = Label(root, text= "Benchmark(default value is: 'World Index')")
    label_input.pack(padx=5, pady=5)
    lista = list(benchmarks_dictionary.keys())
    ben_selected = StringVar()
    ben_combobox = ttk.Combobox(root, textvariable = ben_selected)
    ben_combobox["values"] = [m for m in lista]
    ben_combobox["state"] = "readonly"
    ben_combobox.pack(padx=5, pady=5)
    
    
    button = ttk.Button(root, text = "Submit", command=myClick)
    button.pack()
    
    
    root.mainloop()

    string_of_letters = letters.get()
    list_of_letters = string_of_letters.split(",")

    days_count = days_count.get()
    start_day = start_day.get()
    last_day = last_day.get()
    number_of_stocks_to_download = stocks_downloaded.get()
    percentage_increase = percentage_increase.get()
    
        #SET THE DEFAULT VALUES
    if days_count == "":
        days_count = 61
    if start_day == "":
        start_day = '2022-01-01'
    if last_day == "":
        last_day = date.today()
    if number_of_stocks_to_download == "":
        number_of_stocks_to_download = 10
    if percentage_increase == "":
        percentage_increase = 100



    country = country_selected.get()
    category = category_selected.get()
    days_count = int(days_count)
    number_of_stocks_to_download = int(number_of_stocks_to_download)
    percentage_increase = int(percentage_increase)
    perc_conversion = (percentage_increase/100)+1
    ben = ben_selected.get()

  
    return list_of_letters, country, category, days_count, start_day, last_day,number_of_stocks_to_download, percentage_increase, perc_conversion, ben, benchmarks_dictionary