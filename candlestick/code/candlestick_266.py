
import plotly.graph_objects as go
import pandas as pd

data = [['2019-07-01',122,124,128,119],['2019-07-08',124,127,130,121],['2019-07-15',126,127,129,118],['2019-07-22',121,118,123,115],['2019-07-29',123,125,127,122],['2019-08-05',125,128,130,122],['2019-08-12',127,124,129,120],['2019-08-19',123,126,128,122]]

df = pd.DataFrame(data,columns=['Date','Opening Price ($)','Closing Price ($)','High Price ($)','Low Price ($)'])

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Opening Price ($)'],
                high=df['High Price ($)'],
                low=df['Low Price ($)'],
                close=df['Closing Price ($)'])])

fig.update_layout(title_text="Financial Trend of Tourism and Hospitality Industry - Monthly Overview",
    yaxis_range=[min(df['Low Price ($)'])-10, max(df['High Price ($)'])+10],
    width=1200,
    height=800,
    font=dict(
        family="Courier New, monospace",
        size=14,
        color="#7f7f7f"
    )
)

fig.write_image("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/7_202312270043.png")