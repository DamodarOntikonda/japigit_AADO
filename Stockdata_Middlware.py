import sys

from alpha_vantage.timeseries import TimeSeries

API_KEY = '7YVE9DLCGCNJKT9S'

def getStockdata(symbol):

    try:
        print("Collecting info....")

        ts = TimeSeries(key=API_KEY, output_format='pandas')

        data, meta_data = ts.get_intraday(symbol=symbol, interval='1min', outputsize='full')

        return str(data.tail(1).iloc[0]['4. close'])

    except:
        return "not found"

def main():

    output_file = open('japi.out', 'w')    
    while 1:
        userInput = input("Enter Stock Symbol or EXIT to exit: ").upper()

        if userInput != "EXIT":

            serverData = 'The current price of {} is {}\n'.format(userInput, getStockdata(userInput))

            print(serverData)

            output_file.write(serverData)

        else:
            output_file.close()
            sys.exit("\nStock Quotes retrieved successfully!\n")
        #output_file.close()

main()