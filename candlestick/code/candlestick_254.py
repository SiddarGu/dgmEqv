import plotly.graph_objs as go
import pandas as pd

# Define the data
data = {'Date': ['2021-01-01', '2021-02-01', '2021-03-01', '2021-04-01', '2021-05-01', '2021-06-01',
                 '2021-07-01', '2021-08-01', '2021-09-01', '2021-10-01', '2021-11-01', '2021-12-01'],
        'Opening Value ($)': [190000, 192000, 195000, 200000, 201500, 210000,
                              208000, 206000, 210000, 215000, 220000, 225000],
        'Closing Value ($)': [192000, 195000, 200000, 201500, 210000, 208000,
                              206000, 210000, 215000, 220000, 225000, 228000],
        'High Value ($)': [195000, 198000, 202000, 205000, 215000, 211000,
                           210000, 213000, 219000, 225000, 230000, 232000],
        'Low Value ($)': [188000, 190000, 194000, 198000, 200000, 203000,
                          202000, 204000, 207000, 214000, 218000, 221000]}
df = pd.DataFrame(data)

# Create the candlestick chart
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Opening Value ($)'],
                                     high=df['High Value ($)'],
                                     low=df['Low Value ($)'],
                                     close=df['Closing Value ($)'])])

# Set figure title
fig.update_layout(title="Monthly Performance of Housing Market in 2021")

# Update layout parameters
fig.update_layout(width=800, height=600)  # Set width and height to accommodate all text and chart

# Adjust y-axis range
fig.update_layout(yaxis_range=[min(df['Low Value ($)']) * 0.99, max(df['High Value ($)']) * 1.01])

# Save the figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/193_202312302255.png')