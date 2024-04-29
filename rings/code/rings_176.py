
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Profits', 'Overhead Costs', 'Investments', 'Revenue', 'Market Share']
data = [36, 17, 23, 14, 10]
line_labels = ['Category']

# Plot the data with the type of rings chart
fig, ax = plt.subplots(figsize=(10, 10))
cmap = plt.get_cmap('Spectral')
ax.pie(data, radius=1, colors=cmap(np.linspace(0, 1, len(data))), startangle=90, counterclock=False)

# Add a white circle to the center of the pie chart to turn it into a ring chart
circle = plt.Circle((0, 0), 0.7, color='white')
ax.add_artist(circle)

# Set legend
ax.legend(data_labels, loc='upper left')

# Set background grids
ax.grid(color='black', linestyle='dotted', linewidth=1, alpha=0.3)

# Set title
ax.set_title('Financial Insights of Businesses - 2023', fontsize=20)

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save file
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_2.png')

# Clear the current image state
plt.clf()
plt.cla()
plt.close()