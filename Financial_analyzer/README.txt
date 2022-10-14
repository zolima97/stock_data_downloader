Hi! I am Matteo and this is the project!

MAIN IDEA
With this documentation you are having access to a data science project in finance. The objective of the program is to scout stocks across all the markets in every time period (according to datas availability) that have performed a certain increse/decrease of stock value in a given data range, counted as number of days, comparing the performance with one given benchmark. In the end you will be able to tell which stocks have performed according to details you have given.

WHAT YOU NEED
Before running the program, please be sure to have installed python (at least 3.6 version), and be sure to have either an IDE for running the script or being aware how to run a program via command line on terminal. Also be sure to have installed the following python packages:
- tkinter 
- yfinance
- pandas
- datetime 
- time
- math
- dateutil.relativedelta

COMPOSITION OF FILES
This project is composed by:
	INPUT:
		- Stock_table.csv -> this works as big dictionary of all the available tickers in the global markets associated with country, and exchange market. They are more than 100.000 stocks
	EXECUTION:
		- main.py -> this is the "manager" of the other scripts. Launch it and program will work and execute the scripts automatically
		- gui.py -> this script launches the graphical interface you will insert the data in 
		- calculator.py -> this is the very juice of the project. Here is where the magic happens. stocks are downloaded and analysed according to what you have stated in the graphical interface. Eventually, the output is exported into lista_ticker.txt and analysis_of_stocks.csv
	OUTPUT:
		- lista_ticker.txt -> it collect the list of stocks found with the prerequisites you gave in the beginning
		- analysis_of_stocks.csv -> output dataframe showing occurrences every time a stock hit or overcame the percentage given. The dataframe includes: name of the ticker, the name of the company, the start and end date when the percentage change occurred, the start and end value when the percentage change occurred, the percentage change, the volume of the stock when the percentage started and the volume ended, the market capitalisation of the stock updated to the day you are running the script, the sector of the stock, the industry of the stock, the value of the benchmark for the same starting and end date, the percentage change of the benchmark in the same given range of time of the stock  

	APPENDIX
	- sky.png -> image used in gui.py

INSTRUCTIONS
This is a python script you can directly execute either on an IDE (for example Jupiter Notebook, Visual Studio Code, Pycharm, Spider etc.) or directly on the terminal (the command line). 

You have to execute ONLY the script called "main.py".
 
If you want to run on your terminal, firstly be sure you have installed python. Then you simply have to locate on the specific path of the main.py (please check the path you are in. E.g.: User/Desktop/Folder/Folder2/Financial_analyzer). Then type in the terminal "ipython" and execute. Then open the file main.py and get the code (also via txt file). Copy and paste it on the terminal. Execute it. A graphic interface will appear. Please read carefully and insert datas in the format as requested. The format is very important: attain to it and program will not crash. However, do not worry to not insert datas in the box, since there are default values already.
Datas you will be asked to insert in the interface are:
- Country Market (default: USA)
- Number of stocks to download (default: 10). Use a very large number to scout all the available stocks for that market (e.g.: 10000)
- Start Day (default: 2022-01-01)
- Last Day (default: the day you run the script)
- Range of days (default:61)
- Percentage increase/decrease (default: 100%), do not insert the % sign
- Benchmark (default is World Index)
Once you are done with the input datas, click the submit button. Then it appears "You successfully submitted...." You have to exit the interface by clicking the X button. 
The script will start to run and you just have to seat back and relax. The task might be time consuming, depending on how many stock you want to analyse etc.
When in the terminal will appear the writing "Done", your output is ready and you can check it out by clicking the files "lista_ticker.txt" and "analysis_of_stocks.csv"


For more information, you can also look at the quick video tutorial I attach to this project.
Bye and enjoy! ;)
