
import plotly.graph_objects as go
import pandas as pd

data = [['2019-11-01',215.2,214.4,219.6,208.1],
        ['2019-11-08',212.7,213.2,216.9,210.4],
        ['2019-11-15',211,216.1,219.6,208.2],
        ['2019-11-22',215.5,214.9,219.2,211.7],
        ['2019-11-29',215.2,217.9,220.3,213.4],
        ['2019-12-06',219,219.2,224.2,214.2],
        ['2019-12-13',220.3,223.2,224.8,218.2],
        ['2019-12-20',221.9,221.5,226.3,217.1],
        ['2019-12-27',221.2,223.2,226,218.5]]

df = pd.DataFrame(data, columns = ['Date','Open','Close','High','Low'])

# Create figure
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])

# Set title
fig.update_layout(title_text="Weekly Performance of Healthcare and Health Industry Stock Prices",
                  font_size=8,
                  width=800,
                  height=600,
                  yaxis_range=[200,230])

# Write image
fig.write_image("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/9_202312251608.png")