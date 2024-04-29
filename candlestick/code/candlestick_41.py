
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

data = {'Date':['2020-11-16','2020-11-23','2020-11-30','2020-12-07','2020-12-14','2020-12-21','2020-12-28'],
        'Opening Price (USD)':[30.2,30.5,30.2,32.1,35.0,34.5,36.0],
        'Closing Price (USD)':[29.7,32.0,33.0,34.0,33.7,37.2,37.2],
        'High Price (USD)':[31.2,33.0,35.5,36.0,36.2,38.2,39.3],
        'Low Price (USD)':[28.4,29.0,29.2,30.5,31.3,33.2,35.5]}
df = pd.DataFrame(data)

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Opening Price (USD)'],
                high=df['High Price (USD)'],
                low=df['Low Price (USD)'],
                close=df['Closing Price (USD)'])])

fig.update_layout(title='The Financial Trend in Government and Public Policy Over One Month',
            yaxis_range=[min(df['Low Price (USD)']),max(df['High Price (USD)'])],
            width=800,
            height=600)

fig.write_image("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/10_202312252244.png")