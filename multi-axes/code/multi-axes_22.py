
import matplotlib.pyplot as plt 
import numpy as np 

# Transform the given data
data_labels = ['Enrolment Rate (%)', 'Graduation Rate (%)', 'Dropout Rate (%)', 'Average GPA']     
line_labels = ['Primary Education', 'Secondary Education', 'College Education', 'Postgraduate Education']  
data = np.array([[90.5, 72.2, 5.3, 3.1], 
                 [75.1, 59.1, 7.4, 3.3], 
                 [45.6, 36.4, 4.8, 3.6], 
                 [35.2, 25.7, 2.5, 3.9]])

# Create figure
plt.figure(figsize=(10, 8))
ax1 = plt.subplot(111)

bar_pos = np.arange(len(data))
bar_width = 0.2
bar_start = bar_pos - 0.5*(bar_width*(len(data_labels) - 2)) # Adjusted for number of series

# Plot the data
ax1.bar(bar_start, data[:, 0], label=data_labels[0], width=0.2, color='cornflowerblue', alpha=0.7)
ax2 = ax1.twinx()
ax2.bar(bar_start + bar_width, data[:, 1], label=data_labels[1], width=0.2, color='orchid', alpha=0.7)
ax3 = ax1.twinx()
ax3.bar(bar_start + 2 * bar_width, data[:, 2], label=data_labels[2], width=0.2, color='lightseagreen', alpha=0.7)
ax4 = ax1.twinx()
ax4.plot(bar_start + bar_width, data[:, 3], label=data_labels[3], color='palevioletred', marker='o')
ax1.set_xticks(bar_pos)
ax1.set_xticklabels(line_labels, rotation=45)

# Position the y-axes
ax3.spines["right"].set_position(("axes", 1.1))
ax4.spines["right"].set_position(("axes", 1.2))

# Label all axes
ax1.set_ylabel(data_labels[0], color="cornflowerblue")
ax2.set_ylabel(data_labels[1], color="orchid")
ax3.set_ylabel(data_labels[2], color="lightseagreen")
ax4.set_ylabel(data_labels[3], color="palevioletred")

# Draw background grids
ax1.grid(linestyle='--')
ax2.grid(linestyle='--')
ax3.grid(linestyle='--')

# Autolocator
ax1.yaxis.set_major_locator(plt.MaxNLocator(10))
ax2.yaxis.set_major_locator(plt.MaxNLocator(10))
ax3.yaxis.set_major_locator(plt.MaxNLocator(10))
ax4.yaxis.set_major_locator(plt.MaxNLocator(10))

# Show legends
ax1.legend(bbox_to_anchor=(1.0, 0.85))
ax2.legend(bbox_to_anchor=(1.0, 0.8))
ax3.legend(bbox_to_anchor=(1.0, 0.75))
ax4.legend(bbox_to_anchor=(1.0, 0.7))

# Set the title
plt.title('Educational Enrolment, Graduation, and Dropout Rates Analysis')

# Resize the image
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/5_2023122261325.png')

# Clear the current image state
plt.clf()