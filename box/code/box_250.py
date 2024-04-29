

import matplotlib.pyplot as plt
import numpy as np

# Restructure the data into two 2D lists 
data = [[1000, 10000, 20000, 30000, 50000],
        [2000, 15000, 25000, 35000, 60000],
        [3000, 12000, 22000, 32000, 55000],
        [5000, 13000, 23000, 33000, 60000],
        [4000, 11000, 21000, 31000, 45000]]
outliers = [[], [100000], [10, 12000], [70000], [50000, 60000]]

# Plot the data with the type of box plot
fig = plt.figure(figsize=(15,8))
ax = fig.add_subplot()
ax.boxplot(data, whis=1.5)

# Plot outliers manually 
for i, outlier in enumerate(outliers):
    if len(outlier) > 0:
        ax.plot(np.repeat(i+1, len(outlier)), outlier, 'o')

# Adjust the chart
ax.set_title('Settlement Amount Distribution in Legal Practices in 2020')
ax.set_xticklabels(['Personal Injury','Mediation','Bankruptcy','Corporate Law','Taxation'])
ax.set_ylabel('Settlement Amount (USD)')
ax.grid(axis='y', color='gray', alpha=0.3)
plt.xticks(rotation=20)

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the image 
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/16_202312270030.png')

# Clear the current image state
plt.clf()