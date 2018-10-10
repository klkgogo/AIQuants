import numpy as np
import pandas as pd

#generate data
dates = pd.date_range("10/10/2018", periods = 12, freq='D')
close_prices = np.arange(len(dates))
close = pd.Series(close_prices, dates)
print(close)

#resample
print("\nresample")
close_3d = close.resample('3D')

print(close_3d)

print("\nresample to week")
close_w = close.resample('W').first()
print(close_w)

df = pd.DataFrame({"days": close, "week": close_w})
print(df)

print("\nresample to ohlc")
close_w_ohlc = close.resample('W').ohlc()
print(close_w_ohlc)


def days_to_weeks(open_prices, high_prices, low_prices, close_prices):
    """Converts daily OHLC prices to weekly OHLC prices.

    Parameters
    ----------
    open_prices : DataFrame
        Daily open prices for each ticker and date
    high_prices : DataFrame
        Daily high prices for each ticker and date
    low_prices : DataFrame
        Daily low prices for each ticker and date
    close_prices : DataFrame
        Daily close prices for each ticker and date

    Returns
    -------
    open_prices_weekly : DataFrame
        Weekly open prices for each ticker and date
    high_prices_weekly : DataFrame
        Weekly high prices for each ticker and date
    low_prices_weekly : DataFrame
        Weekly low prices for each ticker and date
    close_prices_weekly : DataFrame
        Weekly close prices for each ticker and date
    """

    # TODO: Implement Function
    open_prices_weekly = open_prices.resample('W').first()
    high_prices_weekly = high_prices.resample('W').max()
    low_prices_weekly = low_prices.resample('W').min()
    close_prices_weekly = close_prices.resample('W').last()

    return open_prices_weekly, high_prices_weekly, low_prices_weekly, close_prices_weekly