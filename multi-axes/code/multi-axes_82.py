import matplotlib.pyplot as plt
import numpy as np

# split the data into different variables
data_labels = ['Total Sales (in millions)', 'Average Price (in thousands)', 
               'New Listings', 'Vacancy Rate (%)']
line_labels = ['2015', '2016', '2017', '2018', '2019', '2020', '2021']
data = np.array([
    [530, 175, 1200, 4.5],
    [570, 180, 1250, 3.5],
    [550, 185, 1290, 2.5],
    [590, 190, 1330, 1.7],
    [620, 195, 1350, 1.3],
    [640, 200, 1400, 1.9],
    [660, 210, 1450, 2.3]
])

# start to plot the data
fig = plt.figure(figsize=(12, 8))
ax1 = fig.add_subplot(111)

color = 'tab:red'
ax1.set_xlabel('Year')
ax1.set_ylabel(data_labels[0], color=color)
ax1.plot(line_labels, data[:, 0], color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
ax2.scatter(line_labels, data[:, 1], color='tab:blue')
ax2.set_ylabel(data_labels[1], color='tab:blue')
ax2.tick_params(axis='y', labelcolor='tab:blue')

ax3 = ax1.twinx()
ax3.scatter(line_labels, data[:, 2], color='tab:green')
ax3.set_ylabel(data_labels[2], color='tab:green')
ax3.spines['right'].set_position(('outward', 60))

ax4 = ax1.twinx()
ax4.fill_between(line_labels, 0, data[:, 3], 
                 facecolor='yellow', alpha=0.5, label=data_labels[3])
ax4.set_ylabel(data_labels[3], color='yellow')
ax4.spines['right'].set_position(('outward', 120))


plt.title('Real Estate Market Trends: Sales, Pricing, Listing and Vacancy over the years')
plt.legend(loc='upper left')
plt.grid(True)

fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/142_202312310108.png')
plt.close()
