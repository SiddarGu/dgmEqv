import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator
import pandas as pd

# preprocess data
raw_data = '''Quarter,Total Revenue (Millions),Operating Expenses (Millions),Net Profit (Millions),Number of Employees
 Q1 2020,1000,400,300,2000
 Q2 2020,1100,420,330,2100
 Q3 2020,1200,470,370,2100
 Q4 2020,1400,550,400,2200
 Q1 2021,1500,600,450,2300
 Q2 2021,1600,640,480,2300
 Q3 2021,1700,680,520,2350
 Q4 2021,1800,740,560,2400'''

# create DataFrame
data_df = pd.DataFrame([x.split(',') for x in raw_data.split('\n')])

# assign column headers
data_df.columns = data_df.iloc[0]
data_df.drop(0, inplace=True)

# create variables
data_labels = list(data_df.columns[1:])
line_labels = data_df['Quarter'].values
data = data_df[data_df.columns[1:]].values.astype('float')

# colors
color = ['b', 'g', 'r', 'm']
plot_types = [ 'line' , 'bar', 'line' , 'scatter']

# create figure, set size
fig = plt.figure(figsize=(30, 15))
ax1 = fig.add_subplot(111)
ax1.plot(line_labels, data[:, 0], color=color[0], label=data_labels[0])
ax1.set_ylabel(data_labels[0], color=color[0])
plt.title('Business and Finance Performance Analysis from Q1 2020 to Q4 2021')

# initiate axes
axes = [ax1]
for i in range(1, len(data_labels)):
    ax = ax1.twinx()
    axes.append(ax)

for ax, color, data_label, plot_type, data_column in zip(axes, color, data_labels, plot_types, data.T):
    ax.set_ylabel(data_label, color=color)
    ax.tick_params(axis='y', colors=color)
    ax.yaxis.set_major_locator(AutoLocator())
    ax.spines['right'].set_position(('outward', 70 * (data_labels.index(data_label))))

    if plot_type == 'bar':
        ax.bar(line_labels, data_column, color=color, alpha=0.3, label=data_label, align='center')
    elif plot_type == 'scatter':
        ax.scatter(line_labels, data_column, color=color, label=data_label)
    else:  # line
        ax.plot(line_labels, data_column, color=color, label=data_label)

# legends
handles, labels = [], []
for ax in axes:
    for h, l in zip(*ax.get_legend_handles_labels()):
        handles.append(h)
        labels.append(l)

plt.legend(handles, labels, loc='upper right', bbox_to_anchor=(1.15, 1))

plt.grid()
plt.tight_layout()

# save figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/79_2023122292141.png')

# clear current figure
plt.clf()
