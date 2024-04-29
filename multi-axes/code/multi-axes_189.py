import matplotlib.pyplot as plt
import numpy as np

# Transform the raw data to format we can use
raw_data = [
    [2009,5500,1200,4300,1200],
    [2010,5750,1500,5000,750],
    [2011,6000,1700,5375,625],
    [2012,6250,1900,5600,650],
    [2013,6800,2000,6100,700],
    [2014,7150,2200,6500,650],
    [2015,7500,2500,6800,700],
    [2016,7900,2750,7200,700],
    [2017,8200,3000,7600,600],
    [2018,8600,3150,8000,600]
]
raw_data = np.array(raw_data)
line_labels = raw_data[:, 0]
data = raw_data[:, 1:]
data_labels = ['Number of Lawsuits Filed', 'Cost Spent (Millions)', 'Closed Cases', 'Unresolved Cases']

# Plot the data
fig = plt.figure(figsize=(24, 20))
ax1 = fig.add_subplot(111)
ax1.plot(line_labels, data[:, 0], color='tab:blue')
ax1.set_ylabel(data_labels[0], color='tab:blue')
ax1.tick_params(axis='y', colors='tab:blue')
ax1.set_title('Law and Legal Affairs: Lawsuit Activity and Costs')

ax2 = ax1.twinx()
ax2.bar(line_labels, data[:, 1], color='tab:orange', alpha=0.6)
ax2.set_ylabel(data_labels[1], color='tab:orange')
ax2.tick_params(axis='y', colors='tab:orange')

ax3 = ax1.twinx()
ax3.scatter(line_labels, data[:, 2], color='tab:green')
ax3.set_ylabel(data_labels[2], color='tab:green')
ax3.spines['right'].set_position(('outward', 60))
ax3.tick_params(axis='y', colors='tab:green')

ax4 = ax1.twinx()
ax4.fill_between(line_labels, data[:, 3], color='tab:red', alpha=0.3)
ax4.set_ylabel(data_labels[3], color='tab:red')
ax4.spines['right'].set_position(('outward', 120))
ax4.tick_params(axis='y', colors='tab:red')

fig.tight_layout()
fig.legend(
    [ax1.get_lines()[0], ax2.containers[0], ax3.collections[0], ax4.collections[0]],  
    labels=data_labels,
    loc="upper left",
    bbox_to_anchor=(0,1),
    bbox_transform=ax1.transAxes 
)

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/100_2023122292141.png')
plt.clf()
