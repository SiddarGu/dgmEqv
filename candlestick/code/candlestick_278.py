import plotly.graph_objects as go

# Data
data = [
    ['2020-01-01', 50000, 52000, 54000, 49000],
    ['2020-02-01', 51000, 53000, 55000, 50000],
    ['2020-03-01', 52000, 54000, 56000, 51000],
    ['2020-04-01', 53000, 55000, 57000, 52000],
    ['2020-05-01', 54000, 56000, 58000, 53000],
    ['2020-06-01', 55000, 57000, 59000, 54000],
    ['2020-07-01', 56000, 58000, 60000, 55000],
    ['2020-08-01', 57000, 59000, 61000, 56000],
    ['2020-09-01', 58000, 60000, 62000, 57000],
    ['2020-10-01', 59000, 61000, 63000, 58000],
    ['2020-11-01', 60000, 62000, 64000, 59000],
    ['2020-12-01', 61000, 63000, 65000, 60000]
]

# Extracting data
dates = [row[0] for row in data]
open_salary = [row[1] for row in data]
close_salary = [row[2] for row in data]
high_salary = [row[3] for row in data]
low_salary = [row[4] for row in data]

# Creating candlestick chart
fig = go.Figure(data=[go.Candlestick(x=dates,
                                     open=open_salary,
                                     close=close_salary,
                                     high=high_salary,
                                     low=low_salary)])

# Updating layout
fig.update_layout(
    title='Salary Range Trend in Human Resources and Employee Management 2020',
    width=800,
    height=600,
    margin=dict(l=50, r=50, b=50, t=50),
    xaxis=dict(
        title='Date',
        tickangle=-45,
        showline=True,
        linewidth=1,
        linecolor='black',
        mirror=True
    ),
    yaxis=dict(
        title='Salary ($)',
        showline=True,
        linewidth=1,
        linecolor='black',
        mirror=True
    )
)

# Saving the figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/82_202312302255.png')