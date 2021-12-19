from pycoingecko import CoinGeckoAPI as cg
import pandas as pd
import datetime
import plotly.graph_objects as go
bitcoin_data = cg().get_coin_market_chart_by_id(
    id="bitcoin", vs_currency="usd", days=30)
print(bitcoin_data)
price = bitcoin_data["prices"]
print(price[0:3])
price_table = pd.DataFrame(price, columns=['TimeStamp', 'Price'])
print(price_table.head)
price_table['date'] = price_table['TimeStamp'].apply(
    lambda d: datetime.date.fromtimestamp(d/1000.0))
candlestick_data = price_table.groupby(price_table.date, as_index=False).agg({
    "Price": ['min', 'max', 'first', 'last']})
fig = go.Figure(data=[go.Candlestick(x=candlestick_data['date'],
                open=candlestick_data['Price']['first'],
                high=candlestick_data['Price']['max'],
                low=candlestick_data['Price']['min'],
                close=candlestick_data['Price']['last'])
                      ])

fig.update_layout(xaxis_rangeslider_visible=False)

fig.show()
