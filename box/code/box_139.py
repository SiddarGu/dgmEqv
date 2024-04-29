
import matplotlib.pyplot as plt
import numpy as np

# Restructure the data into two 2D lists
data_list = [[250, 500, 750, 1000, 1500], 
             [300, 550, 800, 1100, 1700], 
             [400, 600, 850, 1200, 1800], 
             [200, 450, 700, 950, 1400], 
             [350, 550, 800, 1050, 1600]]

outliers_list = [[], [2600], [50, 2500], [2400, 2500], [2200]]
line_labels = ['Service A', 'Service B', 'Service C', 'Service D', 'Service E']
# Plot the data with the type of box plot
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
ax.boxplot(data_list, whis=1.5)

# Plot the outliers manually
for i, outlier in enumerate(outliers_list):
    if len(outlier) > 0:
        ax.plot(np.repeat(i + 1, len(outlier)), outlier, 'r*', markersize=12)

# Drawing techniques 
ax.grid(True)
ax.set_xlabel('Cloud Service')
ax.set_xticklabels(line_labels)
ax.set_ylabel('Response Time (ms)')
ax.set_title('Cloud Service Response Time Distribution in 2021')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/6_202312251608.png')
plt.cla()