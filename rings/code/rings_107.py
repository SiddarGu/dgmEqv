
import matplotlib.pyplot as plt
import numpy as np
import math

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Legal Compliance', 'Regulatory Framework', 'Risk Management', 'Compliance Enforcement', 'Professional Ethics']
data = np.array([37, 23, 16, 17, 7])
line_labels = ['Category', 'ratio']

# Plot the data with the type of rings chart
fig, ax = plt.subplots(figsize=(10, 5))

# Create only one pie chart using the `ax.pie()` method
ax.pie(data, startangle=90, counterclock=False, labels=data_labels, 
       autopct='%1.1f%%', pctdistance=0.8, labeldistance=1.1)

# Change the pie chart into a ring chart in your code
inner_circle = plt.Circle((0,0),0.7, color='white')
ax.add_artist(inner_circle)

# For the plot of legend
ax.legend(data_labels, loc='upper center', bbox_to_anchor=(0.5, -0.1),
          fancybox=True, shadow=True, ncol=2)

# Drawing techniques such as background grids can be used
ax.grid(True)

# The title of the figure 
ax.set_title('Law and Legal Affairs Overview - 2023', fontsize=20)

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_58.png')

# Clear the current image state
plt.clf()