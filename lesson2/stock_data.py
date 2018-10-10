
#read as string
with open("prices.csv", "r") as file:  #不需要调用close方法
    prices = file.read()
print(prices)

#read to a dataframe

import pandas as pd

prices_df = pd.read_csv("prices.csv",  names=['ticker', 'date', 'open', 'high', 'low', 'close', 'volume', 'adj_close', 'adj_volume'])
print(prices_df)

#计算中位数
print("\n计算中位数")
print(prices_df.median())

print("\n按ticker分组:")
for d in prices_df.groupby('ticker'):
    print('-------group -------')
    print(d)

print("\n按ticker分组计算中位数")
print(prices_df.groupby('ticker').median())


#切片

print("\n切片0：16")
print(prices_df.iloc[:16])

#privot
print("\npivot open:")
open_price = prices_df.pivot(index='date', columns="ticker", values="open")
print(open_price)

print("\npivot open 2:")
open_price = prices_df.pivot(index='date', columns="ticker")['open']
print(open_price)

print("\nopen_price mean:")
print(open_price.mean())
print(type(open_price))

print("\nmean of each date")
print(open_price.T)
print(open_price.T.mean())


def csv_to_close(csv_filepath, field_names):
    """Reads in data from a csv file and produces a DataFrame with close data.

    Parameters
    ----------
    csv_filepath : str
        The name of the csv file to read
    field_names : list of str
        The field names of the field in the csv file

    Returns
    -------
    close : DataFrame
        Close prices for each ticker and date
    """

    # TODO: Implement Function
    prices_df = pd.read_csv(csv_filepath, names=field_names)

    close_prices = prices_df.pivot(index="date", columns="ticker", values='close')

    return close_prices

print(csv_to_close("prices.csv", ['ticker', 'date', 'open', 'high', 'low', 'close', 'volume', 'adj_close', 'adj_volume']))