
import plotly.graph_objects as go
import pandas as pd

df = pd.DataFrame({"Month": ["2020-05", "2020-06", "2020-07", "2020-08", "2020-09", "2020-10", "2020-11"],
                   "Average Salary ($)": [3700, 3750, 3900, 4000, 4100, 4200, 4250],
                   "Minimum Salary ($)": [2500, 2750, 3000, 3200, 3500, 3700, 4000],
                   "Maximum Salary ($)": [5000, 5500, 6000, 6500, 7000, 7500, 8000],
                   "Employee Count": [100, 200, 300, 400, 500, 600, 700]})

fig = go.Figure(data=[go.Candlestick(x=df['Month'],
                                    open=df['Minimum Salary ($)'],
                                    high=df['Maximum Salary ($)'],
                                    low=df['Minimum Salary ($)'],
                                    close=df['Average Salary ($)'])])
fig.update_layout(title_text='HR and Employee Management: Salary Overview',
                  width=1000, height=500,
                  yaxis_range=[2400, 8200])
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/3_202312251608.png')