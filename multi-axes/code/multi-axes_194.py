import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from io import StringIO

# Store your chart data in a pandas dataframe
raw_data = '''Month,Hotel Occupancy Rate (%),Total Visitors (Millions),Average Daily Rate (Dollars),Revenue Per Available Room (Dollars)
January,75,2.1,150,112.5
February,79,2.4,155,122.45
March,84,2.8,160,134.4
April,80,2.5,165,132
May,85,3.0,170,144.5
June,88,3.5,175,154
July,89,3.5,180,160.2
August,87,3.3,185,160.95
September,82,2.9,185,151.7
October,78,2.5,190,148.2
November,76,2.3,195,148.2
December,82,2.7,200,164'''
df = pd.read_csv(StringIO(raw_data))

line_labels = df.iloc[:, 0]
data_labels = df.columns[1:]
data = df.iloc[:, 1:].values

fig = plt.figure(figsize=(20,10))
ax1 = fig.add_subplot(111)
ax1.plot(line_labels, data[:,0], label=data_labels[0], color='b')
ax1.set_xlabel('Months')
ax1.set_ylabel(data_labels[0])
ax1.yaxis.label.set_color('b')

ax2 = ax1.twinx()
ax2.bar(line_labels, data[:,1], label=data_labels[1], color='g', alpha=0.6, align='center')
ax2.set_ylabel(data_labels[1])
ax2.yaxis.label.set_color('g')

ax3 = ax1.twinx()
ax3.fill_between(line_labels, 0, data[:,2], label=data_labels[2], color='r', alpha=0.3)
ax3.set_ylabel(data_labels[2])
ax3.spines['right'].set_position(('outward', 60))
ax3.yaxis.label.set_color('r')

ax4 = ax1.twinx()
ax4.scatter(line_labels, data[:,3], label=data_labels[3], color='c')
ax4.set_ylabel(data_labels[3])
ax4.spines['right'].set_position(('outward', 120))
ax4.yaxis.label.set_color('c')

fig.autofmt_xdate() 
fig.legend(bbox_to_anchor=(1.1, 1), loc='upper left')
plt.title('Tourism and Hospitality Trends: Occupancy, Visitors, and Revenue Metrics')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/97_2023122292141.png', bbox_inches='tight')
plt.clf() # clear figure
