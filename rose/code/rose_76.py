
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Music', 'Visual Arts', 'Performing Arts', 'Literature', 
               'Creative Arts', 'Architecture', 'Cinema', 'Photography', 'Dance']
data = [120, 90, 100, 75, 60, 50, 40, 30, 20]
line_labels = ['Category', 'Number of Arts']

# Create figure and plot data with type of rose chart
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(1, 1, 1, polar=True)
ax.set_title('Number of Arts Practices by Category in 2021')

# Calculate sector angle and draw sectors
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, 
           label=data_labels[i], color='C'+str(i))
    
# Set ticks to match categories
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, rotation=90)

# Position legend outside of chart area
ax.legend(bbox_to_anchor=(1.3, 1), frameon=False)

# Adjust font size and color
for tick in ax.xaxis.get_ticklabels():
    tick.set_fontsize(15)
    tick.set_color('black')
for tick in ax.yaxis.get_ticklabels():
    tick.set_color('black')

# Automatically resize the image
plt.tight_layout()

# Save image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_5.png')

# Clear current image
plt.clf()