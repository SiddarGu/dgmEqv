import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from io import StringIO

# data
data="Category,Number of Cases,Average Case Duration (Months),Legal Fees (Dollars)\n Criminal Law,250,8,5000\n Civil Law,180,12,4000\n Family Law,300,10,4500\n Corporate Law,220,6,8000\n Intellectual Property Law,150,9,7000\n Employment Law,180,7,5500\n Immigration Law,200,11,6000\n Environmental Law,120,5,7500\n Real Estate Law,250,7,6500\n Contract Law,190,8,5500"

df = pd.read_csv(StringIO(data))
line_labels = df["Category"].values
data_labels = df.columns[1:].tolist()
data = df.values[:, 1:].astype('float')
colors = ['b', 'g', 'r', 'c', 'm', 'y']

fig = plt.figure(figsize=(22,12)) 
ax1 = fig.add_subplot(111)
fig.autofmt_xdate(rotation=45)
ax = [ax1] + [ax1.twinx() for _ in range(len(data_labels)-1)]
for ii in range(len(data_labels)-1): 
    ax[ii].spines['right'].set_position(('outward', (60*(ii))))
 
ax[0].bar(line_labels, data[:,0], color=colors[0], alpha=0.6, label=data_labels[0])
for i in range(1, len(data_labels)):
    ax[i].plot(line_labels, data[:,i], color=colors[i], marker='o', linestyle='-', label=data_labels[i])

for axs, color, label in zip(ax, colors, data_labels):
    axs.set_ylabel(label) 
    axs.yaxis.label.set_color(color)  
    axs.tick_params(axis='y', colors=color)
    axs.legend(loc='upper left')

plt.title("Legal Case Analysis: Case Load, Duration, and Costs")

plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/322_202312311430.png",
            bbox_inches='tight')
plt.clf()
