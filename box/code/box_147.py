import matplotlib.pyplot as plt
import numpy as np

data = [
    ["Facebook",10,20,30,40,50,[]], 
    ["Twitter",15,25,35,45,55,[120]], 
    ["Instagram",20,30,40,50,60,[1,2,3]], 
    ["LinkedIn",10,20,25,35,45,[70,75,80]], 
    ["Snapchat",5,15,25,35,45,[100]],
]

# Reshape the data
labels = [d[0] for d in data]
stats = [d[1:6] for d in data]
outliers = [d[6] for d in data]

# Create figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

# Create box plot
bp = ax.boxplot(stats, vert=False, labels=labels, patch_artist=True, notch=True, whis=1.5)

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    
# Add outliers
for i, outlier in enumerate(outliers):
    if outlier:
        x = [i + 1] * len(outlier)
        ax.plot(outlier, x, 'ro')

# Customize chart
ax.set_title('User Session Duration Distribution on Social Media Platforms (2022)', fontsize=12)
ax.set_xlabel('Session Duration (Minutes)')
ax.grid(True, linestyle='-', color='grey', alpha=0.5)
plt.setp(ax.get_xticklabels(), rotation=45)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/141_202312270030.png')
plt.clf()
