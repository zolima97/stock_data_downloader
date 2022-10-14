#!/usr/bin/env python
# coding: utf-8

# From this script you can launch the functions related to other files.
# Once you start it, a GUI will appear with variables to insert. Please use the characters as specified and submit

# In[1]:


from gui import *
from calculator import *
from tkinter import *
import tkinter as tk
from tkinter import ttk
import yfinance as yf
import pandas as pd


# In[2]:


def main():
    list_of_letters, country, category, days_count, start_day, last_day,number_of_stocks_to_download, percentage_increase, perc_conversion, ben, benchmarks_dictionary = run()
    print("Recap of the parameters selected:,"
          "\n Letters used: ", list_of_letters,
          "\n Country filtered: ", country,
          "\n Category filtered: ", category,
          "\nNumber of total days to count: ", days_count,
          "\n Start Day of the analysis: ", start_day, 
          "\nLast day of the analysis: ",last_day,
          "\nNumber of stocks to analyze: ",number_of_stocks_to_download, 
          "\nTotal Percentage change between start date and last day: ",percentage_increase)
    print("Datas are loaded correctly")
    stock = downloader(list_of_letters, country, category, days_count, start_day, last_day,number_of_stocks_to_download, percentage_increase, perc_conversion, ben)
    print("Stocks are downloaded correctly")
    df = analyzer(start_day, last_day, days_count, stock, perc_conversion, ben, benchmarks_dictionary)
    print("df is ready to export")
    exporter(df)
    return df, stock


# In[ ]:


if __name__ == "__main__":
    main()

