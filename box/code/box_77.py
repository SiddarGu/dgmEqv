import matplotlib.pyplot as plt

# Restructuring the data
categories = ['HelpAid', 'Childcare Worldwide', 'LoveEarth', 'Peaceful Start', 'GreenFuture']
data = [[150,300,450,600,800], [200,400,600,800,1000], [100,200,300,400,500], [50,150,250,350,450], [300,500,700,900,1000]]
outliers = [[], [50,1500], [50,750], [1000], [50]]

# Creating the figure
fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111)

# Plotting the boxplot
bplot = ax.boxplot(data, vert=True, patch_artist=True, labels=categories, notch=True, medianprops={'linewidth': 2})

# Coloring the boxes
colors = ['red', 'blue', 'green', 'yellow', 'magenta']
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)

for cap in bplot['caps']:
    cap.set(color='grey', linewidth=2)

# Plotting outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, "ro")

# Styling the plot
plt.grid(axis='y', linestyle='--', linewidth=0.5)

plt.title('Donation Distribution in Charity and Nonprofit Organizations (2022)')
plt.ylabel('Donation ($)')
plt.xticks(rotation=30)

# Save figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/68_202312270030.png')
plt.clf()
