
import matplotlib.pyplot as plt 
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Charitable Organizations', 'Animal Welfare Organizations', 'Education Organizations', 'Environmental Organizations', 'Human Rights Organizations', 'Poverty Relief Organizations', 'Health Organizations']
data = [90, 70, 50, 40, 30, 20, 10]
line_labels = ['Category', 'Number of Organizations']

# Create figure before plotting
fig = plt.figure(figsize=(10, 10))

# Plot the data with the type of rose chart
ax = fig.add_subplot(111, projection='polar')

# Get number of categories and calculate sector angle
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Plot sectors corresponding to different categories
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, bottom=0.0, color=plt.cm.Set1(i))
    ax.set_xticklabels(data_labels, rotation=30)

# Add legend
ax.legend(data_labels, bbox_to_anchor=(1.1, 0.95))

# Set title
ax.set_title('Number of Nonprofit Organizations by Category in 2021')

# Tighten layout and save figure
plt.tight_layout()
fig.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-070122_88.png')

# Clear current image state
plt.close()