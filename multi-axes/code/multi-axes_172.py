import matplotlib.pyplot as plt
import numpy as np

# Original data and labels provided by the user
data_labels = ['Category','Research and Development Expenditure (Millions of Dollars)', 
               'Patents Filed (Thousands)', 'Average Salaries (Thousands of Dollars)', 
               'Employment (Millions of People)']
line_labels = ['Semiconductors', 'Aerospace', 'Automotive', 'Biotech', 'Robotics', 
               'IT', 'Construction', 'Energy', 'Pharmaceuticals', 'Nanotech']
data = np.array([[1940, 17.2, 90.4, 2.8],
                 [1790, 5.9, 119.2, 1.6],
                 [1200, 6.7, 74.5, 2.4],
                 [1450, 3.2, 91.8, 1.7],
                 [980, 3.1, 80.3, 1.4],
                 [1590, 18.4, 87.1, 4.2],
                 [950, 2.5, 65.9, 2.0],
                 [1400, 7.1, 102.8, 2.1],
                 [1320, 7.6, 105.6, 2.3],
                 [1150, 2.3, 83.2, 1.3]])

# Setting up the figure and primary axis
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_title("A Glimpse at the Impact of Science and Engineering on the Global Economy")
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1], color='C0')
ax.tick_params(axis='y', colors='C0')

# Bar plot for the first data series
bar_pos = np.arange(len(data))
bar_width = 0.2
bar_start = bar_pos - 0.5*(bar_width*(len(data_labels) - 2)) # Adjusted for number of series
ax.bar(bar_start, data[:, 0], width=bar_width, label=data_labels[1], color='C0')
ax.set_xticks(bar_pos)
ax.set_xticklabels(line_labels, rotation=45)

# Creating additional y-axes
for i in range(2, len(data_labels)): # Adjusted to match data size
    ax2 = ax.twinx()
    offset = 0.03 + (i-2)*0.1
    ax2.spines['right'].set_position(('axes', 1 + offset))
    ax2.set_ylabel(data_labels[i], color='C' + str(i-1))
    ax2.tick_params(axis='y', colors='C' + str(i-1))
    ax2.set_ylim(0, 1.1*np.max(data[:, i-1]))

    # Bar plot for the additional data series
    ax2.bar(bar_start + (i-1)*bar_width, data[:, i-1], width=bar_width, label=data_labels[i], color='C' + str(i-1))

fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/4.png')
plt.clf()