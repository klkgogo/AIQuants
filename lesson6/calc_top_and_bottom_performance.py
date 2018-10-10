import pandas as pd

month = pd.to_datetime("02/01/2018")
close_month = pd.DataFrame(
    {
        'A': 1,
        'B': 12,
        'C': 35,
        'D': 3,
        'E': 79,
        'F': 2,
        'G': 15,
        'H': 59},
    [month])
print(close_month)

print(close_month.loc[month])


largest2 = close_month.loc[month].nlargest(2)
print(largest2)

smallest2 = close_month.loc[month].nsmallest(2)
print(smallest2)


def date_top_industries(prices, sector, date, top_n):
    """
    Get the set of the top industries for the date

    Parameters
    ----------
    prices : DataFrame
        Prices for each ticker and date
    sector : Series
        Sector name for each ticker
    date : Date
        Date to get the top performers
    top_n : int
        Number of top performers to get

    Returns
    -------
    top_industries : set
        Top industries for the date
    """
    # TODO: Implement Function

    date_prices = prices.loc[date]
    top = date_prices.nlargest(top_n)
    print(top.index)
    top_industries = sector.loc[top.index]
    return set(top_industries)


close_month = pd.DataFrame(
    {
        'A': 1,
        'B': 12,
        'C': 35,
        'D': 3,
        'E': 79},
    [month])

sector = pd.Series({'A': "Utilities", 'B': "Health Care",
'C': "Real Estate",
'D': "Real Estate",
'E': "Information Technology"})

print(date_top_industries(close_month, sector, month, 3))




