import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoLocator


# Data Preparation
raw_data = """Category,Donation Amount (USD),Number of Donors,Number of Volunteers
Educational Institutions,500000,1000,200
Healthcare Services,250000,500,150
Environmental Conservation,150000,300,100
Social Services,400000,800,250
Animal Welfare,200000,400,150
Arts and Culture,300000,600,200
Disaster Relief,450000,900,300
Community Development,350000,700,250
International Aid,600000,1200,400 """

lines = raw_data.split('\n')

data_labels = lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in lines[1:]]

data = [list(map(int, line.split(',')[1:])) for line in lines[1:]]
data = np.array(data)

colors = ['b', 'g', 'r']

fig = plt.figure(figsize=(15, 10))
ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:, 0], width=0.6, alpha = 0.75, color=colors[0])
ax1.set_ylabel(data_labels[0], color=colors[0])
ax1.tick_params(axis='y', labelcolor=colors[0])
ax1.set_xlabel('Category')
ax1.set_xticklabels(line_labels, rotation=45)

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], color=colors[1])
ax2.set_ylabel(data_labels[1], color=colors[1])
ax2.tick_params(axis='y', labelcolor=colors[1])

if data.shape[1] > 2:
    ax3 = ax1.twinx()
    ax3.plot(line_labels, data[:, 2], color=colors[2])
    ax3.set_ylabel(data_labels[2], color=colors[2])
    ax3.tick_params(axis='y', labelcolor=colors[2])
    ax3.spines['right'].set_position(('outward', 60))

ax1.yaxis.set_major_locator(AutoLocator())
ax2.yaxis.set_major_locator(AutoLocator())
if data.shape[1] > 2: ax3.yaxis.set_major_locator(AutoLocator())

plt.title("Charitable Organization Overview: Donations, Supporters, and Volunteers")
fig.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/314_202312311430.png", dpi=300)
plt.close(fig)
