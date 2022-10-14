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

import yfinance as yf
import pandas as pd
from datetime import date
from sklearn.linear_model import LinearRegression
import numpy as np
import time
import math
from datetime import datetime
import datetime
from dateutil.relativedelta import relativedelta
from tkinter import *
from tkinter import ttk
from gui import *
# Insert datas into GUI
#INITIAL PARAMETERS TO SET
'''
list_of_letters = ""
exchange = "NMS"
country = "USA"
category = "Electronic Equipment"
days_count = 61
start_day = '2022-01-01'
last_day = date.today()
number_of_stocks_to_download = 100
percentage_increase = 100
perc_conversion = (percentage_increase/100)+1
'''
def downloader(list_of_letters, country, category, days_count, start_day, last_day,number_of_stocks_to_download, percentage_increase, perc_conversion, ben):
    stocks = pd.read_csv("Stock_Table.csv", sep = ";").iloc[2:, :5].reset_index(drop = True)
    stocks.columns = stocks.iloc[0]
    stocks = stocks[1:]
    stocks["Country"] = stocks["Country"].fillna("Unknown")
    stocks["Category Name"] = stocks["Category Name"].fillna("Unknown")
    stocks["Category Name"] = stocks["Category Name"].map(lambda x: x.split(" ")[0])
    
    if country != "":
        stock_filtered = stocks[(stocks["Country"] == country)].reset_index(drop = True)
    else:
        stock_filtered = stocks
    
    if list_of_letters != "":
        tuple_letter = tuple([x.upper() for x in list_of_letters])
        stock_filtered = stock_filtered[stock_filtered['Ticker'].str.startswith(tuple_letter)]
    else:
        stock_filtered = stock_filtered
        
    if category != "":
        stock_filtered = stock_filtered[(stock_filtered["Category Name"] == category)].reset_index(drop = True)
    else:
        stock_filtered = stock_filtered

    stock_tik = stock_filtered
    stock_tik = stock_tik.reset_index(drop = True)
    stock_df = pd.DataFrame(stock_tik)
    stock_tik = stock_df
    stock_tik = stock_tik["Ticker"]
    stock_dat = pd.DataFrame([])
    counter = 0
    '''    
    rows_to_be_deleted= []
    for i in stock_filtered:
        if "." in str(i):
            rows_to_be_deleted.append(i)
    rows_series_to_be_deleted = pd.Series(rows_to_be_deleted)
    
    '''

    #dichiaro che sub_stock = stock_tik
    for indice, elem in enumerate(stock_tik[:number_of_stocks_to_download]):
        try:
            curr_el = str(elem)
            stock_df = yf.download(curr_el, 
                          start=start_day, 
                          end=last_day, 
                          progress=False)

            stock_open = pd.DataFrame(stock_df["Close"]).rename(columns = {"Close": curr_el})
        #print(curr_el)
            stock_dat = pd.merge(stock_dat, stock_open, left_index=True, right_index=True, how = "outer")
            counter += 1

            if counter % 100 == 0:
                print("we reached the number:", counter)
        except:
            continue

    stock_dat = stock_dat.dropna(how = "all", axis = 1)
    stock = stock_dat
    stock.columns = stock.columns.str.lstrip('Close_')
    print("Found ", len(stock.columns), "stocks with values")
    return stock

def analyzer(start_day, last_day, days_count, stock, perc_conversion, ben, benchmarks_dictionary):
    
    df = pd.DataFrame(columns=['Ticker', 'Long_Name', "Start_date", "End_date", 
    'Start_value', 'End_value', 'Pct','Volume_start', 'Volume_end', "marketCap_up_to_{}".format(str(date.today())),
    'Sector', 'Industry', 'Benchmark_start', 'Benchmark_end', 'pct_benchmark'])

    benchmark = yf.download(benchmarks_dictionary[ben], start=start_day, 
                              end=last_day, 
                              progress=False)["Close"]
    print(stock.columns)
    for ticker in stock.columns:
        print("I am currently scanning the ticker: ", ticker)
        tick_values = stock[ticker]
        
        volume = yf.download(ticker, start=start_day, 
                              end=last_day, 
                              progress=False)["Volume"]
        
        tick = yf.Ticker(ticker)
        if "industry" in list(tick.info.keys()):
            industry = tick.info["industry"]
        if "sector" in list(tick.info.keys()):
            sector = tick.info["sector"]
        if "longName" in list(tick.info.keys()):
            long_name = tick.info["longName"]
        if "marketCap" in list(tick.info.keys()):
            marketCap = tick.info["marketCap"]
        for key, value in tick_values.iteritems():
            #make_check
            start_value = float(tick_values.filter(like =  str(key), axis = 0).values)
            start_date = str(key)
            for i in range(days_count):
                end_date = str(key + relativedelta(days=i))
                if len(tick_values.filter(like = str(key + relativedelta(days=i)), axis = 0).values) > 0:
                    end_value = float(tick_values.filter(like = str(key + relativedelta(days=i)), axis = 0).values)
                    if end_value/start_value >= perc_conversion:
                        pct = str(round((end_value/start_value - 1)*100, 2))+ "%"
                        start_date = str(start_date).split(" ")[0]
                        end_date = str(end_date).split(" ")[0]
                        print("Ticker ", ticker," has reached a percentage change by: ", pct)

                        try:
                            volume_start = volume[start_date]
                            volume_end = volume[end_date]
                        
                        except:
                            volume_start = ""
                            volume_end = ""
                            
                        try:
                            val_ben_start = benchmark[start_date]
                            val_ben_end = benchmark[end_date]
                            pct_benchmark = str(round((val_ben_end/val_ben_start - 1)*100,2))+ "%"
                        except:
                            val_ben_start = ""
                            val_ben_end = ""
                            pct_benchmark = ""

                        data = [[ticker, long_name, start_date, end_date, start_value, end_value, pct, 
                                 volume_start, volume_end,  marketCap, sector, industry, val_ben_start, val_ben_end, 
                                 pct_benchmark]]
                        sub_df = pd.DataFrame(data, columns=['Ticker', 'Long_Name', "Start_date", "End_date", 
    'Start_value', 'End_value', 'Pct','Volume_start', 'Volume_end', "marketCap_up_to_{}".format(str(date.today())),
    'Sector', 'Industry', 'Benchmark_start', 'Benchmark_end', 'pct_benchmark'])
                        frame = [df, sub_df] 
                        df = pd.concat(frame, axis = 0).reset_index(drop = True)
                        del end_value

                    else:
                        continue
                        del end_value
        
        
    return df

def exporter(df):
    now = datetime.now()
    current_time = str(now.strftime("%d_%m_%Y__%H_%M_%S"))
    list_name = "list_of_stocks_found_"
    extension = "_.txt"
    file_name =  list_name + current_time + extension
    
    with open(r'OUTPUT/{}'.format(file_name), 'w') as fp:
        for item in set(df["Ticker"]):
            # write each item on a new line
            fp.write("%s\n" % item)
        print('Done')
        
    df_name = "analysis_of_stocks_"
    extension_csv = "_.csv"
    df_name_time = df_name + current_time + extension_csv
    df.to_csv(r'OUTPUT/{}'.format(df_name_time), sep = ",")

