import matplotlib.pyplot as plt
import numpy as np

data = np.array([
    [1200, 365, 30, 4570],
    [3000, 180, 20, 6410],
    [1500, 120, 40, 3590],
    [500, 540, 50, 7280],
    [1350, 365, 45, 8590],
    [2300, 90, 20, 3600],
    [1100, 440, 60, 9500],
    [1800, 270, 50, 5040],
    [2800, 180, 35, 2680],
    [950, 400, 55, 5490],
    [1540, 220, 35, 3570]
])

data_labels = ['Case Load (Numbers)', 'Average Resolution Time (Days)', 'Successful Appeals (Percent)', 'Legal Cost(Thousands of Dollars)']
line_labels = ['Criminal', 'Civil', 'Labor', 'Intellectual Property', 'Corporate', 'Real Estate', 'Medical Malpractice', 'Personal Injury', 'Property', 'Environment Law', 'Insurance Law']

fig = plt.figure(figsize=(25,15))
ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:, 0], color = 'blue', alpha = 0.7)
ax1.set_ylabel(data_labels[0], color = 'blue')
ax1.tick_params(axis='y', colors='blue')

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], color = 'red')
ax2.set_ylabel(data_labels[1], color = 'red')
ax2.tick_params(axis='y', colors='red')

ax3 = ax1.twinx()
ax3.scatter(line_labels, data[:, 2], color = 'green')
ax3.set_ylabel(data_labels[2], color = 'green')
ax3.spines['right'].set_position(('outward', 60))
ax3.tick_params(axis='y', colors='green')

ax4 = ax1.twinx()
ax4.fill_between(line_labels, 0, data[:, 3], color = 'purple', alpha=0.5)
ax4.set_ylabel(data_labels[3], color = 'purple')
ax4.spines['right'].set_position(('outward', 120))
ax4.tick_params(axis='y', colors='purple')

fig.autofmt_xdate(rotation = 45)
plt.title('Legal Affairs Analysis: Case Load and Resolutions Trends')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/257_202312311051.png')
plt.close(fig)
