import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# data processing
data_labels = ['Number of Students', 'Enrollment Rate (%)', 'Graduation Rate (%)', 'Dropout Rate (%)']
line_labels = ['Arts and Humanities', 'Business and Economics', 'Engineering and Technology', 'Health Sciences', 'Social Sciences', 'Natural Sciences', 'Computer Science', 'Education', 'Languages and Literature', 'Psychology and Sociology', 'Mathematics and Statistics', 'Physical Education and Sports', 'Design and Architecture', 'Law and Legal Studies', 'Medicine and Health Care']
data = np.array([
[5000,80,70,10],
[6000,90,80,5],
[7000,80,75,8],
[8000,85,75,6],
[9000,85,80,7],
[10000,90,85,4],
[11000,95,90,3],
[12000,95,90,2],
[13000,80,70,5],
[14000,85,75,4],
[15000,90,85,3],
[16000,95,90,2],
[17000,90,85,4],
[18000,85,80,5],
[19000,95,90,2]
])

fig = plt.figure(figsize=(24, 8))
ax1 = fig.add_subplot(111)
plot_types = ['bar', 'plot', 'plot', 'scatter']

colors = ['b', 'r', 'g', 'k']
x = np.arange(len(line_labels))

ax1.bar(x, data[:, 0], color=colors[0], alpha=0.6)
ax1.set_ylabel(data_labels[0])
ax1.yaxis.label.set_color(colors[0])
ax1.tick_params(axis='y', colors=colors[0])
ax1.set_title('Education and Academics: Student Enrollment, Graduation, and Dropout Rates')

for i in range(1, data.shape[1]):
    axn = ax1.twinx()
    axn.spines['right'].set_position(('outward', 60*(i-1)))
    axn.set_ylabel(data_labels[i])
    axn.yaxis.label.set_color(colors[i % len(colors)])
    axn.tick_params(axis='y', colors=colors[i % len(colors)])

    if plot_types[i] == 'bar':
        axn.bar(x + 0.1*i, data[:, i], width=0.1, color=colors[i % len(colors)], alpha=0.6)
    elif plot_types[i] == 'plot':
        axn.plot(x, data[:, i], color=colors[i % len(colors)])
    elif plot_types[i] == 'scatter':
        axn.scatter(x, data[:, i], color=colors[i % len(colors)])

ax1.set_xticks(x)
ax1.set_xticklabels(line_labels, rotation=45, ha='right')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/325_202312311430.png')
plt.clf()
