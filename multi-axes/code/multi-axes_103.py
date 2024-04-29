import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoLocator

# Given data
given_data = "Year, Number of Graduates (Thousands), Average Tuition Fee ($), Student Loans Taken (%), Employment Rate (%)/n 2015, 2642, 9800, 80,85/n 2016, 2791, 10060, 81,87/n 2017, 2857, 10430, 83,88/n 2018, 2919, 10710, 85,89/n 2019, 2986, 11000, 87,90/n 2020, 3057, 11300, 88,88/n 2021, 3122, 11610, 89,87"

# Transforming data
given_data = [i.split(',') for i in given_data.split('/n') if i]
data_labels = given_data[0]
line_labels = [i[0] for i in given_data[1:]]
data = np.array([list(map(int, i[1:])) for i in given_data[1:]])

# Plotting
fig = plt.figure(figsize=(25, 15))
ax = fig.add_subplot(111)

p1, = ax.plot(line_labels, data[:, 0], color='b', marker='o', linestyle='-')
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1], color='b')
ax.tick_params(axis='y', colors='b')

ax2 = ax.twinx()
p2 = ax2.bar(line_labels, data[:, 1], color='g', alpha=0.6)
ax2.set_ylabel(data_labels[2], color='g')
ax2.tick_params(axis='y', colors='g')

ax3 = ax.twinx()
ax3.spines['right'].set_position(('outward', 60))      
p3 = ax3.scatter(line_labels, data[:, 2], color='r', marker='x')
ax3.set_ylabel(data_labels[3], color='r')
ax3.tick_params(axis='y', colors='r')

ax4 = ax.twinx()
ax4.spines['right'].set_position(('outward', 120))   
p4, = ax4.plot(line_labels, data[:, 3], color='c', marker='s', linestyle=':')
ax4.set_ylabel(data_labels[4], color='c')
ax4.tick_params(axis='y', colors='c')

plt.title('Yearly Trends in Graduates, Tuition, Loans, and Employment')

leg = plt.legend([p1, p2, p3, p4], 
                 [l.lstrip() for l in data_labels[1:]],
                 loc='upper left',
                 bbox_to_anchor=(1.15, 1))

for ax in [ax, ax2, ax3, ax4]:
    ax.yaxis.set_major_locator(AutoLocator())
    ax.grid(True)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/101_2023122292141.png')
plt.close()
