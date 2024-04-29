
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels.
data_labels = ["Mathematics","Computer Science","Physics","Chemistry","Engineering","Robotics","Aerospace","Biomedical","Nanotechnology"]
data = [80,120,60,90,150,100,100,50,30]
line_labels = ["Field", "Number of Projects"]

# Plot the data with the type of rose chart.
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='polar')

# Use a loop to assign a label to each sector when you create them with `ax.bar`.
sector_angle = (2 * np.pi) / len(data)
for i, v in enumerate(data):
    ax.bar(i * sector_angle, v, width=sector_angle, label=data_labels[i], color=plt.cm.Set3(i / 10.))

# Set labels and title
ax.set_xticks([sector_angle * i for i in range(len(data))])
ax.set_xticklabels(data_labels)
ax.set_title('Number of Science and Engineering Projects in 2021')

# Create legend
ax.legend(data_labels, bbox_to_anchor=(0.7, 0.7))

# Show and save figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-082906_6.png')
plt.show()
plt.clf()