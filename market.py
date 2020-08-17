'''
Jose D. Santiago
May 1,2020
Python 2.7 Script to get Stock Market Data of NASDAQ companies
'''

#Import Libraries
try:
    import argparse
    import sys
    import yfinance as yf
    import matplotlib.pyplot as plt
    from datetime import date
    from pprint import pprint
except Exception as e:
    print('Some Modules are Missing {}'.format(e))

#Creathe the Parser 
parser = argparse.ArgumentParser(description='Get Stock Data and return prediction')
#Arguments of Parser
parser.add_argument('-s','--stock',metavar='',required=True, help='Stock Symbol' )
parser.add_argument('-e','--evaluation',action='store_true',help='Evaluation of Stock')
parser.add_argument('-r','--recommendations',action='store_true',help='Recommendation of Stock')
parser.add_argument('-p','--price',action='store_true',help='Return Stock Price')
parser.add_argument('-g','--graph',action='store_true',help='Return Stock Graph')
parser.add_argument('-v','--verbose',action='store_true',help='Return Stock Information')
#Execute parse
args = parser.parse_args()

#Function to graph data
def graph_stock(stock):
    data = yf.download(stock,period='1day',interval='1m')
    #data = yf.download('HTZ','2020-03-31',date.today())
    #Plot the close prices
    data.Close.plot()
    plt.show()

#Function to Analyze Data
def analyze_stock(stock):
    print stock.recommendations

#Function to Print Yahoo Recommendations
def stock_recommendation(stock):
    print stock.recommendations

#Function to Print Stock Info
def info_stock(stock):
    pprint(stock.info)

#Function to Print Live Stock Price
def getstock_price(stock):
    hist = stock.history(period='1day')
    price = hist['Close']
    print price[0]
    #data = yf.download('HTZ',period='1day',interval='1m')

#Main Function
def main():
    #Set Variables
    stock = yf.Ticker(args.stock)
    if args.verbose:
        info_stock(stock)
    if args.price:
        getstock_price(stock)
    if args.graph:
        graph_stock(args.stock)
    if args.evaluation:
        analyze_stock(stock)
    if args.recommendations:
        stock_recommendation(stock)

if __name__== "__main__":
    main()
