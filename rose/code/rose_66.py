
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Community Services','Education and Learning','Social Services','Environment and Conservation',
               'Health and Wellness','Human Rights Protection','Animal Welfare','Poverty Alleviation']
data = [43, 97, 17, 36, 96, 60, 68, 45]
line_labels = ['Category', 'Number']

sector_angle = (2 * np.pi) / len(data_labels)

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(projection='polar'))
ax.set_title('Number of Nonprofit Organizations in Each Field')

# Create the rose chart
for i, value in enumerate(data):
    ax.bar(i * sector_angle, value, width=sector_angle, bottom=0.0,
           label=data_labels[i], color=plt.cm.Set1(i/len(data_labels)))

# Create the legend
ax.legend(bbox_to_anchor=(1.08, 1.04), loc='upper left', labels=data_labels)

# Set the ticks to the center of each sector
ax.set_xticks(np.pi/180. * np.linspace(sector_angle/2., 360.-sector_angle/2., len(data_labels), endpoint=True))
ax.set_xticklabels(data_labels)

# Set the ylim to the max of the data
ax.set_ylim(0, np.max(data))

# Remove the grid
ax.grid(False)

# Ensure the figure is tight
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_32.png')

# Clear the current image state
plt.clf()