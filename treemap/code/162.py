import matplotlib.pyplot as plt
import squarify

# Given data
data_labels = ['Usage Share (%)']
line_labels = ['Social Media', 'Online Shopping', 'Streaming Services', 'Gaming',
               'Online News', 'Cloud Services', 'Remote Work', 'E-Learning']
data = [25, 18, 17, 16, 9, 8, 4, 3]

# Colors for each sector (optional, but makes the chart more interesting)
colors = plt.cm.Spectral([float(i) / max(data) for i in data])

# Plotting the treemap
plt.figure(figsize=(12, 8))
squarify.plot(sizes=data, label=line_labels, color=colors, alpha=0.8, text_kwargs={'wrap': True})

# Title of the figure
plt.title('Online Usage Distribution Across Internet Activities in 2023', fontsize=14)

# Removing the axis lines
plt.axis('off')

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()

# Save the image to the absolute path
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/1116.png')

# Clear the current image state
plt.clf()
