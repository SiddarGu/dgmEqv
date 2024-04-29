
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Soft Drinks', 'Coffee', 'Alcohol', 'Tea', 'Dairy Products', 'Juices', 'Snacks', 'Bakery', 'Condiments']
data = [100, 90, 80, 70, 60, 50, 40, 30, 20]
line_labels = ['Product', 'Sales']

# Plot the data with the type of rose chart
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='polar')

# Create sectors corresponding to different categories
num_categories = len(data)
sector_angle = (2 * np.pi) / num_categories

for i in range(num_categories):
    ax.bar(i * sector_angle, data[i], width=sector_angle, color=plt.cm.Set1(i / num_categories), align='edge', label=data_labels[i])

# Set the labels of each sector
ax.set_thetagrids(np.arange(num_categories) * sector_angle, data_labels, fontsize=12)
ax.grid(True)

# Add a legend next to the chart
ax.legend(loc="upper right", bbox_to_anchor=(1.2, 0.8), fontsize=12)

# Set title of the figure 
plt.title("Global Sales of Food and Beverage Products in 2021", fontsize=14)

# Save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_76.png', bbox_inches='tight')

# Clear the current image state
plt.clf()