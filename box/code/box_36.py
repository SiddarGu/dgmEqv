
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[500,1000,2000,3000,4000],
                 [600,1200,2200,3200,5000],
                 [400,1100,1800,2500,3500],
                 [300,900,1500,2100,3000],
                 [450,1300,1900,2700,3800]])
outliers = [[], [7000], [200, 8000], [4500, 7000], [1800]]

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
ax.set_title('Housing Price Distribution in Different Areas in 2021')
ax.boxplot(data.T, labels=['Central','West','North','East','South'],
           notch=True, sym='b+', vert=True, whis=1.5,showmeans=True)
# Plot outliers manually
for i, outlier in enumerate(outliers):
    if len(outlier) > 0:
        ax.plot(np.repeat(i + 1, len(outlier)), outlier, 'ro', alpha=0.6)

ax.set_ylabel('Price (USD)')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/20.png')
plt.clf()