import matplotlib.pyplot as plt
import numpy as np

# Categories and corresponding data
categories = ['Personal Injury', 'Tax Law', 'Intellectual Property', 'Immigration Law', 'Estate Law']
data = [[500,1500,2500,3500,4500], [600,1600,2600,3600,4600], [700,1700,2700,3700,4700], [800,1800,2800,3800,4800], [400,1300,2200,3100,4000]]
outliers = [[0,7000], [], [5500], [20,6000], [5000]]

# Create the figure and axis
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot()

# Create the box plots
bp = ax.boxplot(data, whis=1.5)

# Style the box plots
for box in bp['boxes']:
    box.set(color='blue', linewidth=2)

for whisker in bp['whiskers']:
    whisker.set(color='green', linewidth=2)

for cap in bp['caps']:
    cap.set(color='red', linewidth=2)

for median in bp['medians']:
    median.set(color='yellow', linewidth=2)
    
# Add the outliers
for i, outlier in enumerate(outliers):
    if outlier:  # if the outlier list is not empty
        ax.plot([i + 1] * len(outlier), outlier, marker='o', linestyle='none', color='red')

# Add the labels and title
ax.set_xticklabels(categories, rotation=90)
ax.set_title('Case Amount Distribution in Different Legal Fields (2021)')
ax.set_ylabel('Case Amount (USD)')

# Show grid and set the layout
ax.grid(axis='y')
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/205_202312310058.png')

# clear the current image state
plt.clf()
