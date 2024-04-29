
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels.
data_labels = ['Web Design', 'Network Security', 'Cloud Computing', 'Online Advertising', 'Mobile Applications', 'Big Data', 'Web Analytics', 'Machine Learning']
data = [70, 90, 50, 80, 60, 40, 20, 10]
line_labels = ['Category','Number']

# Plot the data with the type of rose chart
fig = plt.figure(figsize=(15,15))
ax = fig.add_subplot(111, projection='polar')

# Different sectors represent different categories with the same angle
sector_angle = (2 * np.pi) / len(data_labels)

# assign a different color to each sector
for i in range(len(data_labels)):
    ax.bar([i*sector_angle], [data[i]], width=sector_angle, label=data_labels[i], color=plt.cm.Reds(i/len(data_labels)))

# reposition the legend so that it does not cover any part of the chart
ax.legend(bbox_to_anchor=(1.2, 1.2), title='Category')

# Ensure that the number of ticks set with `ax.set_xticks()`
angles = [i*sector_angle for i in range(len(data_labels))]
ax.set_xticks(angles)

# set each category label at the center of its corresponding sector
ax.set_xticklabels(data_labels, fontsize=12, horizontalalignment='center', wrap=True)

ax.set_title('Frequency of Technologies Used in Social Media and the Web in 2021', fontsize=20)

# Save the image
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_1.png')

# Clear the current image state
plt.clf()