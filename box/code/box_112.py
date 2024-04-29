import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Basketball', 'Baseball', 'Football', 'Soccer', 'Tennis']
data = [[60,85,100,115,140], [4,6,9,12,19], [7,12,17,22,28], [1,2,3,4,5], [1,3,6,8,10]]
outliers_data = [[], [2,23], [40], [0,7], [12]]

# Create figure and add subplot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)

# Boxplot
bp = ax.boxplot(data, whis=1.5, patch_artist=True, notch=True, vert=1)

colors = ['pink', 'lightblue', 'lightgreen', 'lightyellow', 'lightgray']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Plot outliers
for i, outlier in enumerate(outliers_data):
    if outlier: # if there are outliers for that category        
        ax.plot([i + 1] * len(outlier), outlier, 'ko')

# Formatting
ax.set(xticks= np.arange(1,len(categories)+1), xticklabels=categories, title='Score Distribution in Various Sport Categories (2021)', ylabel='Scores')
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor", wrap=True)
ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)

# Mirrored axes
ax.yaxis.tick_left()
ax.yaxis.set_label_position("left")
ax.xaxis.tick_bottom()
ax.xaxis.set_label_position('bottom') 

# Save figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/230_202312310058.png')

# Clear Image
plt.clf()
