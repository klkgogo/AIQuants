import numpy as np

"""
For the positions(持仓), let's say we want to buy one share of stock when the price 
is above 2 dollars and the buy 3 more shares when it's above 4 dollars.
We'll first need to generate the signal for these two positions.
"""
prices = np.array([1, 3, -2, 9, 5, 7, 2])
print(prices)

signal_one = prices > 2
signal_three = prices > 4

print(signal_one)
print(signal_three)

signal_one = signal_one.astype(np.int)
signal_three = signal_three.astype(np.int)
print(signal_one)
print(signal_three)

pos_one = signal_one * 1
pos_three = signal_three * 3
print(pos_one)
print(pos_three)

long_pos = pos_one + pos_three
print(long_pos)


def generate_positions(prices):
    """
    Generate the following signals:
     - Long 30 share of stock when the price is above 50 dollars
     - Short 10 shares when it's below 20 dollars

    Parameters
    ----------
    prices : DataFrame
        Prices for each ticker and date

    Returns
    -------
    final_positions : DataFrame
        Final positions for each ticker and date
    """
    # TODO: Implement Function
    long_signal = prices > 50
    short_signal = prices < 20
    long_pos = long_signal.astype(np.int) * 30
    short_pos = short_signal.astype(np.int) * -10
    pos = long_pos + short_pos

    return pos


prices = np.array([10, 30, 2, 90, 50, 70, 2])
print(generate_positions(prices))