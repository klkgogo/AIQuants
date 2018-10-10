import pandas as pd

close = pd.DataFrame(
    {
        'ABC': [1, 5, 3, 6, 2],
        'EFG': [12, 51, 43, 56, 22],
        'XYZ': [35, 36, 36, 36, 37],},
    pd.date_range('10/01/2018', periods=5, freq='D'))

print(close)

print("\nleft shift")
print(close.shift(-1))

print("\nright shift")
print(close.shift(1))

print("\nclose_delta")
close_delta = close - close.shift(1)
print(close_delta)


def calculate_returns(close):
    """
    Compute returns for each ticker and date in close.

    Parameters
    ----------
    close : DataFrame
        Close prices for each ticker and date

    Returns
    -------
    returns : DataFrame
        Returns for each ticker and date
    """
    # TODO: Implement Function
    returns = (close - close.shift(1)) / close.shift(1)

    return returns


returns = calculate_returns(close)
print(returns)
