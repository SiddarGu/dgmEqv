import plotly.graph_objects as go
import pandas as pd

# Create dataframe with the given data
data = {'Date': ['2020-06-01', '2020-06-02', '2020-06-03', '2020-06-04', '2020-06-05', '2020-06-06', '2020-06-07', '2020-06-08', '2020-06-09', '2020-06-10', '2020-06-11', '2020-06-12', '2020-06-13', '2020-06-14', '2020-06-15', '2020-06-16', '2020-06-17', '2020-06-18', '2020-06-19', '2020-06-20'],
        'Open Price ($)': [2500, 2600, 2700, 2900, 3000, 3100, 3200, 3250, 3500, 3550, 3700, 3750, 3900, 4000, 4050, 4250, 4300, 4500, 4600, 4700],
        'Close Price ($)': [2600, 2650, 2880, 2950, 3080, 3200, 3250, 3500, 3550, 3700, 3750, 3850, 3950, 4050, 4250, 4300, 4500, 4550, 4700, 4800],
        'High Price ($)': [2700, 2800, 3000, 3100, 3200, 3300, 3400, 3600, 3700, 3800, 3900, 4000, 4100, 4200, 4350, 4450, 4600, 4700, 4800, 4900],
        'Low Price ($)': [2450, 2550, 2600, 2800, 2900, 3000, 3100, 3200, 3400, 3500, 3600, 3700, 3800, 3900, 4000, 4100, 4200, 4400, 4500, 4700]}

df = pd.DataFrame(data)

# Create the candlestick chart
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Open Price ($)'],
                                     high=df['High Price ($)'],
                                     low=df['Low Price ($)'],
                                     close=df['Close Price ($)'])])

# Set chart title and adjust layout
fig.update_layout(title='Stock Market Performance in Engineering Sector in June 2020',
                  width=800,
                  height=500,
                  margin=dict(l=50, r=50, t=50, b=50),
                  yaxis_range=[min(df['Low Price ($)'])-50, max(df['High Price ($)'])+50])

# Save the figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/139_202312302255.png')