import requests
import datetime
import pandas as pd
import matplotlib.pyplot as plt


class cryptoVisual:
    def __init__(self, sym, comp_sym, all_data=False, limit=1000, aggregate=1, exchange='', timeframe='histominute'):
        self.timeframe = timeframe
        self.symbol = sym
        self.comp_sym = comp_sym
        self.all_data = all_data
        self.limit = limit
        self.aggregate = aggregate
        self.exchange = exchange
        self.url = 'https://min-api.cryptocompare.com/data/{}?fsym={}&tsym={}&limit={}&aggregate={}' \
            .format(self.timeframe, self.symbol.upper(), self.comp_sym.upper(), self.limit, self.aggregate)
        if self.exchange:
            self.url += '&e={}'.format(self.exchange)
        if self.all_data:
            self.url += '&allData=true'

    def getData(self):
        print('Attempting to get Data ...')
        try:
            page = requests.get(self.url)
            data = page.json()['Data']
            dataFrame = pd.DataFrame(data)
            dataFrame['timestamp'] = [datetime.datetime.fromtimestamp(d) for d in dataFrame.time]
        except:
            print('Something went Wrong')
        else:
            return dataFrame

    def plotGraph(self):
        print('Request Initiated ...')
        data = self.getData()
        print('Data Received, Ploting into a graph ...')
        fg = plt.figure(figsize=(20, 10))
        plt.plot(data.timestamp, data.high)
        plt.title(self.symbol + ' To ' + self.comp_sym + ' Time Frequency = ' + self.timeframe, fontsize=24)
        plt.ylabel('Price In ' + self.comp_sym, fontsize=18)
        plt.xlabel('Year', fontsize=18)
        plt.show()


BTC = cryptoVisual('BTC', 'PKR', all_data=True)
BTC.plotGraph()

BTC = cryptoVisual('BTC', 'USD', all_data=True, timeframe='histohour')
BTC.plotGraph()

ETC = cryptoVisual('ETC', 'USD', all_data=True)
ETC.plotGraph()

LTC = cryptoVisual('LTC', 'USD', all_data=True)
LTC.plotGraph()
