
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels. 
# Data_labels represents the labels of each column except the first column. 
# Line_labels represents the labels of each row except the first row. 
# Data represent the numerical array in the data.
data_labels = ['Executive', 'Senior Management', 'Middle Management', 'Supervisory', 'Entry-level', 'Internship']
data = [100, 200, 400, 800, 1200, 200]
line_labels = ['Number of Employees']

# Create figure before plotting, i.e., add_subplot() follows plt.figure()
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(1,1,1, projection='polar')

# Calculate the sector angle based on the number of categories
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Plot the data with the type of rose chart
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i], color=plt.cm.Set1(i))

# Add the legend next to the chart
ax.legend(bbox_to_anchor=(1.25, 1))

# Set the number of ticks to the number of categories
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
# Set the labels for the categories
ax.set_xticklabels(data_labels, fontsize=10,rotation=90)

# Set title
plt.title('Employee Count by Job Level in Human Resources Management',fontsize=14)

# Tight the layout
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_141.png')

# Clear the current image state
plt.clf()