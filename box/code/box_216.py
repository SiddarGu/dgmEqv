import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

# Restructure data
categories = ["Mathematics", "Science", "English", "History", "Geography"]
data = [[50, 65, 75, 85, 99], [45, 60, 70, 78, 98], [60, 67, 75, 80, 95], [55, 63, 73, 82, 92], [48, 62, 70, 79, 95]]
outliers = [[44, 103], [105], [], [48, 105], [40, 100]]

fig = plt.figure(figsize=(10,6))
ax1 = fig.add_subplot(111)

# Box plot
bplot = ax1.boxplot(data, vert=True, patch_artist=True, labels=categories, whis=1.5)

colors = ['pink', 'lightblue', 'lightgreen', 'orange', 'blue']
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)

# Plotting outliers
for i, outlier in enumerate(outliers):
    if outlier: # If there are outliers for this category
        ax1.plot([i + 1] * len(outlier), outlier, "ro")

# Designing Plot
ax1.set_title('Students Score Distribution in Different Subjects in 2020')
ax1.set_xlabel('Subjects')
ax1.set_ylabel('Scores')
ax1.yaxis.grid(True)  
plt.xticks(rotation=45)

# Save figure as an image
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/139_202312270030.png')

# Clear the current image state
plt.clf()
