
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels. 
data_labels = ["Taxation", "Infrastructure", "Education", "Social Welfare", "Health Care"] 
data = [20, 17, 25, 18, 20]
line_labels = ["Category", "ratio"]

# Create figure before plotting 
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(1,1,1)

# Plot the data with the type of rings chart 
ax.pie(data, labels=data_labels, counterclock=False, startangle=90, 
       wedgeprops={'edgecolor':'black', 'linewidth':1.3}, autopct='%.1f%%')

# To change the pie chart into a ring chart 
inner_circle = plt.Circle((0,0), 0.7, color='white')
ax.add_artist(inner_circle)

# For the plot of legend
ax.legend(data_labels, loc="upper left")

# Drawing techniques such as background grids can be used.
ax.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)

# The title of the figure
plt.title("Public Policy Impact - 2023")

# Automatically resize the image by tight_layout()
plt.tight_layout()

# The image must be saved
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231225-122818_16.png')

# Clear the current image state at the end of the code
plt.clf()