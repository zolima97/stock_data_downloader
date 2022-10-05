#!/usr/bin/env python
# coding: utf-8

# Hi matteozoli893, I am after a custom stock scan/screener for a personal project of mine.
# 
# The purpose of the screener is to scan the entire market, and identify stocks that, at any point in time, ---made a move of 100% or more in a period of 2 months or less---.
# 
# I would like to emphasise that this is a historical scan and it needs to scan the stocks entire chart to find the above criteria.
# 
# I would also like the screener to be customisable, so that the % and time periods can be changed. And also to be able to select any market.
# 
# I currently use TradingView, so I am hoping for something compatible with the platform.

# In[1]:


import yfinance as yf
import pandas as pd
from datetime import date
from datetime import datetime
from sklearn.linear_model import LinearRegression
import numpy as np
import time
import math
from datetime import datetime
import datetime

from dateutil.relativedelta import relativedelta
from tkinter import *
from tkinter import ttk


# In[23]:


from gui import *


# Insert datas into GUI

# In[27]:


root = Tk()
root.title("Input Datas")
root.geometry("600x600")

def login():
    print(input_entry.get())
    return var

label_input = Label(root, text= "exchange")
label_input.pack(padx=5, pady=5)
exchange = StringVar()
input_entry = ttk.Entry(root, textvariable = exchange)
input_entry.pack()
button = ttk.Button(root, text = "submit")
button.pack()

label_input = Label(root, text= "country")
label_input.pack(padx=5, pady=5)
country = StringVar()
input_entry = ttk.Entry(root, textvariable = country)
input_entry.pack()
button = ttk.Button(root, text = "submit")
button.pack()

label_input = Label(root, text= "days count")
label_input.pack(padx=5, pady=5)
days_count = StringVar()
input_entry = ttk.Entry(root, textvariable = days_count)
input_entry.pack()
button = ttk.Button(root, text = "submit")
button.pack()

label_input = Label(root, text= "start day")
label_input.pack(padx=5, pady=5)
start_day = StringVar()
input_entry = ttk.Entry(root, textvariable = start_day)
input_entry.pack()
button = ttk.Button(root, text = "submit")
button.pack()

label_input = Label(root, text= "last day")
label_input.pack(padx=5, pady=5)
last_day = StringVar()
input_entry = ttk.Entry(root, textvariable = last_day)
input_entry.pack()
button = ttk.Button(root, text = "submit")
button.pack()

label_input = Label(root, text= "number of stocks to download")
label_input.pack(padx=5, pady=5)
stocks_downloaded = StringVar()
input_entry = ttk.Entry(root, textvariable = stocks_downloaded)
input_entry.pack()
button = ttk.Button(root, text = "submit")
button.pack()

label_input = Label(root, text= "percentage_increase")
label_input.pack(padx=5, pady=5)
percentage_increase = StringVar()
input_entry = ttk.Entry(root, textvariable = percentage_increase)
input_entry.pack()
button = ttk.Button(root, text = "submit")
button.pack()

root.mainloop()

exchange = exchange.get()
country = country.get()
days_count = days_count.get()
start_day = start_day.get()
last_day = last_day.get()
number_of_stocks_to_download = stocks_downloaded.get()
percentage_increase = int(percentage_increase.get())
    


# In[28]:


country


# In[334]:


#INITIAL PARAMETERS TO SET
start_time = datetime.now()

exchange = "NMS"
country = "USA"
days_count = 61
start_day = '2022-01-01'
last_day = date.today()
number_of_stocks_to_download = 100

percentage_increase = 100
perc_conversion = (percentage_increase/100)+1


# In[335]:


stocks = pd.read_excel("yticker.xlsx", sheet_name=0).iloc[2:, :5].reset_index(drop = True)
stocks.columns = stocks.iloc[0]
stocks = stocks[1:]
stock_filtered = stocks[(stocks["Country"] == country) & (stocks["Exchange"] == exchange)].reset_index(drop = True)

rows_to_be_deleted= []
for i in stock_filtered:
    if "." in str(i):
        rows_to_be_deleted.append(i)

rows_series_to_be_deleted = pd.Series(rows_to_be_deleted)
stock_tik = stock_filtered[~stock_filtered.isin(rows_series_to_be_deleted)]

stock_tik = stock_tik.reset_index(drop = True)

stock_df = pd.DataFrame(stock_tik)

stock_tik = stock_df
stock_tik = stock_tik["Ticker"]


# In[336]:


stock_list = []
stock_dat = pd.DataFrame(stock_list)
counter = 0

#dichiaro che sub_stock = stock_tik
for indice, elem in enumerate(stock_tik[:number_of_stocks_to_download]):
    if (indice+1 < len(stock_tik[:]) and indice - 1 >= 0):
        prev_el = str(stock_tik[:][indice-1])
        curr_el = str(elem)
        stock_df = yf.download(curr_el, 
                          start=start_day, 
                          end=last_day, 
                          progress=False)
        
        stock_open = pd.DataFrame(stock_df["Close"])
        #print(curr_el)
        stock_dat = pd.merge(stock_dat, stock_open, left_index=True, right_index=True, how = "outer", suffixes=('_'+ prev_el, '_'+ curr_el))
        counter += 1
        
        if counter % 100 == 0:
            print("we reached the number:", counter)

stock_dat = stock_dat.dropna(how = "all", axis = 1)
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))


# In[337]:


stock = stock_dat
stock.columns = stock.columns.str.lstrip('Close_')


# In[351]:


df = pd.DataFrame(columns=['Ticker', "Start_date", "End_date", 'Start_value', 'End_value', 'Pct'])

for ticker in stock.columns[:]:
    tick_values = stock[ticker]
    for key, value in tick_values.iteritems():
        #make_check
        start_value = float(tick_values.filter(like =  str(key), axis = 0).values)
        start_date = str(key)
        for i in range(days_count):
            end_date = str(key + relativedelta(days=i))
            if len(tick_values.filter(like = str(key + relativedelta(days=i)), axis = 0).values) > 0:
                end_value = float(tick_values.filter(like = str(key + relativedelta(days=i)), axis = 0).values)
                print(ticker, start_value, end_value)
                if end_value/start_value >= perc_conversion:
                    pct = (end_value/start_value - 1)*100
                    data = [[ticker, start_date, end_date, start_value, end_value, pct]]
                    sub_df = pd.DataFrame(data, columns=['Ticker', "Start_date", "End_date", 'Start_value', 'End_value', 'Pct'])
                    frame = [df, sub_df] 
                    df = pd.concat(frame, axis = 0).reset_index(drop = True)
                    del end_value

                else:
                    continue
                    del end_value


# In[353]:


df.to_csv("test_stocks.csv", sep = ";")

