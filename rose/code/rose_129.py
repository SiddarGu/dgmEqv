
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Electronics','Grocery','Apparel','Beauty Products','Home Furnishing','Toys','Sports Equipment','Jewelry']
data = [800,400,600,200,300,100,200,50]
line_labels = ['Product Category','Number of Items']

# Plot the data with the type of rose chart
fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')

# Create figure before plotting
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Different sectors represent different categories with the same angle
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i], color='#%06X' % np.random.randint(0, 0xFFFFFF))

ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels)

# Add legend next to the chart
ax.legend(bbox_to_anchor=(1.25, 1))

# Set the title
ax.set_title('Number of Products Available in Retail and E-commerce Stores')

# Automatically resize the image
fig.tight_layout()

# Save the image
fig.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_138.png')

# Clear the current image state at the end of the code
plt.clf()