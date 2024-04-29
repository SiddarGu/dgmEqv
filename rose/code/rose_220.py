
import matplotlib.pyplot as plt
import numpy as np

# transform the given data into three variables: data_labels, data, line_labels
data_labels = ['General Medicine', 'Specialized Medicine', 'Surgery', 'Pediatrics', 'Psychiatry', 'Orthopedics', 'Dermatology', 'Neurology']
data = [82, 97, 60, 17, 36, 96, 60, 68]
line_labels = ['Category', 'Number of Visits']

# plot the data with the type of rose chart
plt.figure(figsize=(12, 8))
ax = plt.subplot(111, polar=True)
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

ax.set_theta_direction(-1)
ax.set_theta_zero_location('N')

# draw each sector according to the data
colors = plt.cm.Set3(np.linspace(0, 1, num_categories))
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, color=colors[i], label=data_labels[i])

# set labels and ticks
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=10)
ax.set_yticks([])

# set the title and legend
plt.title('Number of Patient Visits at Healthcare Facilities by Specialty', fontsize=15, y=1.1)
ax.legend(data_labels, bbox_to_anchor=(1.2, 1.15), fontsize=10)

# adjust the display
plt.tight_layout()

# save the figure
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-032010_33.png')

# clear the current image state
plt.clf()