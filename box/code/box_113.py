import matplotlib.pyplot as plt
import numpy as np

# Restructure the data into two 2D lists
data = [["Red Cross",50,250,500,750,1000,[]],
        ["Animal Welfare",100,300,550,800,1050,[2000]],
        ["Save the Children",75,350,600,850,1100,[50,2500]],
        ["Greenpeace",50,200,400,600,800,[1500]],
        ["Unicef",100,500,800,1100,1400,[]]]

values = [d[1:6] for d in data]  # box plot values
outliers = [d[6] for d in data]   # potential outliers

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# Plot boxplots
bp = ax.boxplot(values, patch_artist=True, notch=True, whis=1.5)

# Look for outliers and plot them
for i, outlier in enumerate(outliers):
    if outlier:  # only plot if there are outliers for this category
        x = np.array([i + 1] * len(outlier))  # correct x-coordinate for the category
        ax.plot(x, outlier, 'rX')

ax.set_title('Donation Distribution in Nonprofit Organizations in 2022')
ax.set_xlabel('Organization Name')
ax.set_ylabel('Donation Amount($)')
plt.xticks([1, 2, 3, 4, 5], [d[0] for d in data], rotation=45)
plt.grid(True)
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/203_202312310058.png', dpi=300, bbox_inches='tight')

# Clear current image state
plt.clf()
