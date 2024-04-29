
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Social Networking', 'Video Sharing', 'Photo Sharing', 'Web Browsing', 'Online Shopping', 'Online Gaming', 'Blogging', 'Instant Messaging', 'Streaming Music']
data = np.array([83, 73, 63, 56, 43, 36, 30, 25, 20])
line_labels = ['Social Media Usage', 'Number']

# Plot the data with the type of rose chart
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(polar=True)
sector_angle = (2 * np.pi) / len(data_labels)
for i in range(len(data_labels)):
    ax.bar(i * sector_angle, data[i], width=sector_angle, label=data_labels[i], color=plt.cm.tab10(i))
ax.legend(bbox_to_anchor=(1.0, 0.7), edgecolor='black')
ax.set_xticks(np.linspace(0, 2 * np.pi, len(data_labels)+1)[:-1])
ax.set_xticklabels(data_labels, fontsize=8, fontweight='bold', rotation=45)
ax.set_title('Popularity of Online Activities in 2020', fontsize=12, fontweight='bold')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_96.png')
plt.clf()