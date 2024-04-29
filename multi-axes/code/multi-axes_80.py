import numpy as np
import matplotlib.pyplot as plt

data_labels = ['Online Sales (in Million USD)', 'In-Store Sales (in Million USD)', 'Number of Online Shoppers (in Millions)', 'Average Spend per Online Shopper (USD)']
line_labels = ['2016', '2017', '2018', '2019', '2020', '2021']
data = np.array([[1234, 3542, 125, 445],
                 [1692, 3401, 154, 523],
                 [2028, 3265, 184, 567],
                 [2537, 3128, 218, 604],
                 [3089, 2995, 253, 640],
                 [3647, 2872, 290, 677]])

fig = plt.figure(figsize=(15, 10))
ax1 = fig.add_subplot(111)

ax1.bar(line_labels, data[:, 0], color='b', alpha=0.3, label=data_labels[0])

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], color='g', label=data_labels[1])

ax3 = ax1.twinx()
ax3.scatter(line_labels, data[:, 2], color='r', label=data_labels[2])
ax3.spines["right"].set_position(("axes", 1.1))

ax4 = ax1.twinx()
ax4.fill_between(line_labels, data[:, 3], color='purple', alpha=0.3, label=data_labels[3])
ax4.spines["right"].set_position(("axes", 1.2))

fig.autofmt_xdate()

ax1.set_ylabel(data_labels[0])
ax2.set_ylabel(data_labels[1])
ax3.set_ylabel(data_labels[2])
ax4.set_ylabel(data_labels[3])
ax1.yaxis.label.set_color('blue')
ax2.yaxis.label.set_color('green')
ax3.yaxis.label.set_color('red')
ax4.yaxis.label.set_color('purple')

ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
ax3.legend(loc='lower left')
ax4.legend(loc='lower right')

plt.title("Retail and E-commerce Trend Analysis: Online Vs In-Store Sales and customer behavior")
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/121_202312310108.png')
plt.clf()
