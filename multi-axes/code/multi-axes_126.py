import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.ticker as ticker

# First, we need to process the given input

from io import StringIO

text = 'Year,Box Office Revenue (Millions),TV Ratings (Millions),Social Media Engagement (Likes & Shares)\n 2015,3405,140,200000\n 2016,3580,147,210000\n 2017,3850,168,230000\n 2018,4170,180,245000\n 2019,4550,205,280000\n 2020,3650,220,340000\n 2021,3900,215,380000'
data = pd.read_csv(StringIO(text))
data_labels = list(data.columns)[1:]
line_labels = list(data.iloc[:, 0])
data = data.iloc[:, 1:].values

colors = ['r', 'g', 'b', 'y']
plot_types = ['line', 'bar', 'scatter', 'area']
fig = plt.figure(figsize=(20, 10))
ax1 = fig.add_subplot(111)

# Plotting first column
ax1.plot(line_labels, data[:,0], color=colors[0])
ax1.set_ylabel(data_labels[0], color=colors[0])
ax1.yaxis.label.set_color(colors[0])
ax1.tick_params(axis='y', colors=colors[0])

ax1.spines['right'].set_position(('outward', 60))
ax1.yaxis.set_major_locator(ticker.AutoLocator())

ax_list = [ax1]

# Plotting other columns
for i in range(1, len(data_labels)):
    ax = ax1.twinx()
    ax.spines['right'].set_position(('outward', 60*(i+1)))
    ax.yaxis.set_major_locator(ticker.AutoLocator())

    if plot_types[i] == 'bar':
        ax.bar(line_labels, data[:,i], color=colors[i], alpha=0.5)
    elif plot_types[i] == 'scatter':
        ax.scatter(line_labels, data[:,i], color=colors[i])
    elif plot_types[i] == 'line':
        ax.plot(line_labels, data[:,i], color=colors[i])
    else:
        ax.fill_between(line_labels, data[:,i], color=colors[i], alpha=0.5)

    ax.set_ylabel(data_labels[i], color=colors[i])
    ax.yaxis.label.set_color(colors[i])
    ax.tick_params(axis='y', colors=colors[i])

    ax_list.append(ax)

plt.title('Trends in Sports and Entertainment: Revenue, Viewership, and Engagement')
plt.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/69_2023122292141.png')
plt.show()
