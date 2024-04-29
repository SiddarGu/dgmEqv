
import matplotlib.pyplot as plt
import matplotlib.pyplot as mpl
import numpy as np

data = [[90,150,200,250,300],
        [45,75,120,180,240],
        [60,120,180,240,300],
        [15,60,90,120,180],
        [20,50,80,110,150]]
outliers = [[], [360], [20,15], [240], [270]]

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111)

categories = ['Movies','Music','Video Games','Sports','Theatre']
ax.boxplot(data, whis=1.5, labels=categories)

# Add outlier data points
for i, outlier in enumerate(outliers):
    if len(outlier) > 0:
        ax.plot(np.repeat(i+1, len(outlier)), outlier, 'ro', alpha=0.6)

# Add grid to the plot
ax.grid(True)

# Add x-axis label
ax.set_xlabel('Entertainment Type', fontsize=14, labelpad=15, fontweight='bold')
# Add y-axis label
ax.set_ylabel('Duration (Minutes)', fontsize=14, labelpad=15, fontweight='bold')
# Add title
ax.set_title('Event Duration Distribution in Sports and Entertainment in 2021', fontsize=15, fontweight="bold")

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Save the plot
plt.savefig(r'/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/45_202312270030.png')

# Clear the current image state
plt.cla()