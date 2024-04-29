
import plotly.graph_objects as go
import pandas as pd

data = [['2019-04-26',750,780,800,720],
        ['2019-04-27',770,800,830,750],
        ['2019-04-28',740,780,810,700],
        ['2019-04-29',780,820,840,760],
        ['2019-04-30',800,850,870,780],
        ['2019-05-01',820,870,900,780],
        ['2019-05-02',840,880,910,800],
        ['2019-05-03',860,900,930,820],
        ['2019-05-04',880,920,950,840]]

df = pd.DataFrame(data, columns = ['Date','Open Price ($)','Closing Price ($)','High Price ($)','Low Price ($)']) 

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open Price ($)'],
                high=df['High Price ($)'],
                low=df['Low Price ($)'],
                close=df['Closing Price ($)'])])
fig.update_layout(title_text='Law and Legal Affairs Stock Performance - Weekly Overview',
                  xaxis_rangeslider_visible=False,
                  xaxis_title="Date",
                  yaxis_title="Price ($)",
                  width=650,
                  height=400)
fig.write_image("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/12_202312251608.png")