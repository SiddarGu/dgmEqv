import matplotlib.pyplot as plt

# Data
data = [['Cargo Truck',2,5,8,10,15,[]], ['Airplane',1,2,4,7,12,[20,25]], ['Train',3,6,9,12,18,[]], ['Ship',10,20,30,40,50,[70,75]], ['Drone',0.5,1,1.5,2,3,[]]]
categories = [item[0] for item in data]
values = [item[1:-1] for item in data]
outliers = [item[-1] for item in data]

# Create figure and axes
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# Create boxplot
ax.boxplot(values, vert=False, widths=0.5)

# Plot outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(outlier, [i + 1] * len(outlier), 'ro')

# Set labels
ax.set_yticklabels(categories)
ax.set_xlabel('Delivery Time (Hours)')

# Set title, background grid and mirror the axes 
ax.set_title('Delivery Time Distribution in Various Types of Transportation (2021)')
ax.grid(True)
ax.yaxis.tick_right()

# Save figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/107_202312270030.png')

# Clear the current figure
plt.clf()
