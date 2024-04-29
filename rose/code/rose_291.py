
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data
data_labels = ['Primary Care', 'Cardiology', 'Gynecology', 'Endocrinology', 'Gastroenterology', 'Urology', 'Oncology', 'Hematology']
data = [50, 30, 40, 20, 25, 10, 35, 15]
line_labels = ['Category', 'Number']

# Plot the data with the type of rose chart
fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')
num_categories = len(data)
sector_angle = (2 * np.pi) / num_categories

# Create sectors for each category
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i], color=plt.cm.Set1(i))

# Add legend
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.0, prop={'size': 8})

# Set x-axis labels
ax.set_xticks(sector_angle * np.arange(num_categories))
ax.set_xticklabels(data_labels, fontsize=8)

# Add title
ax.set_title('Number of Patients Visiting Specialists in 2021', fontsize=14)

# Automatically resize the image
plt.tight_layout()

# Save image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-070122_99.png')

# Clear the current image state
plt.clf()