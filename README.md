# FINANCE PROJECTS

Starting from a throughful list of tickers, this code is able to retrieve the information about the stocks, such as price, capitalization, P/E since their inception

In this repository we have a file called "download_stocks_etfs", we have a script that is already set to use the tickers from a file with all the denomination of Yahoo Tickers,
abd retrieve the information (price, capitalization, P/E).
Pay attention to the following: 
- p/e ratio column refers primarly to the variable from yahoo finance called "TRailing PE", and when this occurs being missing, the variable is "Revenues per share"
- The output files are saved in a .parquet format
- All the values of the stocks refers to a the close price
- The top 75% of stocks with capitalization are kept, while others are filtered out
- The stocks having no capitalization values registered are dropped
- The naan values are replaced with the first value occurring
- All the stocks with .X are deleted


In the file gold digger, we have a tool that use the file of input with data of stocks in order to find the most performing stocks, according to a given timeframe, based
on the percentage change of value of stock, and also is computed for each stock the corresponding coefficient according to a simple Linear Regression Model (aka, the highest thje value, 
the faster is the pace the stocks has made money$$), in this sense the coefficient works as a predictor.
