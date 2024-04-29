
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels.
data_labels = ['Homelessness', 'Food Insecurity', 'Education', 'Environment', 'Human Rights', 'Animal Welfare', 'Health', 'Poverty']
line_labels = ['Category', 'Number']
data = np.array([[42, 50, 54, 70, 34, 20, 45, 60]])

# Plot the data with the type of rose chart.
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

for i in range(num_categories):
    ax.bar(sector_angle * i, data[0,i], width=sector_angle, bottom=0.0, color=f'C{i}', label=data_labels[i])

# Set ticks to match number of categories
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels)

# Add legend
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

# Add title
plt.title('Number of Nonprofit Organizations Addressing Each Cause in 2021')

# Resize the image
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-112325_51.png')

# Clear the current image state
plt.clf()