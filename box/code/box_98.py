import matplotlib.pyplot as plt
import numpy as np

# Data
subjects = ['Mathematics', 'English', 'Science', 'History', 'Geography']
data = [[60,65,70,75,80], [58,68,73,78,88], [62,67,72,77,82], [57,67,72,77,87], [60,70,75,80,90]]
outliers = [[], [50,90], [55,85], [45,90], [55,95]]

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot()

# Box plotting
bp = ax.boxplot(data, whis=1.5, patch_artist=True, widths = 0.6, notch=True)

colors = ['#0000FF', '#00FF00', '#FFFF00', '#FF00FF', '#FF0000']  # Optional: change the colors
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    
ax.set_title('Score Distribution in Different Subjects (2022)')
ax.yaxis.grid(True)
ax.set_xticks([1, 2, 3, 4, 5])
ax.set_xlabel('Subject')
ax.set_ylabel('Score')
ax.set_xticklabels(subjects, rotation=45) 

# Plot outliers manually
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, 'x')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/220_202312310058.png')
plt.clf()
