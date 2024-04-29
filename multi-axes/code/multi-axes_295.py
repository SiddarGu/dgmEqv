
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Category', 'Enrollment (Thousands of Students)', 'Retention Rate (%)', 'Graduation Rate (%)', 'Dropout Rate (%)']
line_labels = ['Primary Education', 'Secondary Education', 'Vocational Education', 'Higher Education', 'Technical Education', 'Special Education']
data = np.array([[7000, 97, 95, 2],
                 [5000, 90, 83, 7],
                 [3500, 80, 60, 20],
                 [1590, 85, 71, 14],
                 [2500, 95, 88, 7],
                 [1000, 90, 75, 15]])

fig = plt.figure(figsize=(10, 8))
ax1 = fig.add_subplot(111)

# Plot bar chart
ax1.bar(line_labels, data[:, 0], color='#2ca02c', width=0.3, label=data_labels[1])
ax1.set_ylabel(data_labels[1], color='#2ca02c')
ax1.tick_params(axis='y', colors='#2ca02c')

# Plot line chart
ax2 = ax1.twinx()
ax2.spines['right'].set_position(('axes', 1.0))
ax2.plot(line_labels, data[:, 1], color='#d62728', marker='o', label=data_labels[2])
ax2.set_ylabel(data_labels[2], color='#d62728')
ax2.tick_params(axis='y', colors='#d62728')

# Plot area chart
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('axes', 1.1))
ax3.fill_between(line_labels, data[:, 2], alpha=0.3, color='#9467bd', label=data_labels[3])
ax3.set_ylabel(data_labels[3], color='#9467bd')
ax3.tick_params(axis='y', colors='#9467bd')

# Plot scatter chart
ax4 = ax1.twinx()
ax4.spines['right'].set_position(('axes', 1.2))
ax4.scatter(line_labels, data[:, 3], marker='x', color='#8c564b', label=data_labels[4])
ax4.set_ylabel(data_labels[4], color='#8c564b')
ax4.tick_params(axis='y', colors='#8c564b')

ax1.set_title('Education and Academics: Student Enrollment, Retention, and Graduation Rates')
ax1.set_xticklabels(line_labels, rotation=45, wrap=True)
ax1.set_xlabel(data_labels[0])

ax1.grid(color='#f0f0f0')

handles, labels = ax1.get_legend_handles_labels()
ax1.legend(handles[::-1], labels[::-1], bbox_to_anchor=(1, 0.5))

handles, labels = ax2.get_legend_handles_labels()
ax2.legend(handles[::-1], labels[::-1], bbox_to_anchor=(1, 0.55))

handles, labels = ax3.get_legend_handles_labels()
ax3.legend(handles[::-1], labels[::-1], bbox_to_anchor=(1, 0.95))

handles, labels = ax4.get_legend_handles_labels()
ax4.legend(handles[::-1], labels[::-1], bbox_to_anchor=(1, 1.0))

for ax in [ax2, ax3, ax4]:
    ax.autoscale(axis='y')

fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/5.png')
plt.clf()