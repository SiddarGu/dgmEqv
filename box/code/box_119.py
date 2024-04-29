
import matplotlib.pyplot as plt
import numpy as np

# Restructure data
Energy_Source = ['Solar', 'Wind', 'Hydro', 'Geothermal', 'Nuclear']
Min_Usage = [50, 30, 20, 35, 40]
Q1_Usage = [90, 75, 50, 70, 80]
Median_Usage = [150, 120, 90, 100, 110]
Q3_Usage = [210, 180, 140, 130, 140]
Max_Usage = [300, 270, 220, 180, 200]
Outlier_Usage = [[], [400], [10, 300], [250, 350], [210]]

# Create figure
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)

# Plot box plot
ax.boxplot(np.array([Min_Usage, Q1_Usage, Median_Usage, Q3_Usage, Max_Usage]), labels=Energy_Source, showmeans=True, meanline=True)

# Plot outlier
for i, outlier in enumerate(Outlier_Usage):
    if len(outlier) > 0:
        ax.plot([i + 1] * len(outlier), outlier, marker='o', color='b', ls='')

# Set background grid
ax.yaxis.grid(True, ls=':', color='grey')
ax.xaxis.grid(True, ls=':', color='grey')

# Set figure title
ax.set_title('Energy Usage Distribution in Different Sources (2020)')

# Adjust layout
plt.tight_layout()

# Save figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/9_202312251315.png')

# Clear figure
plt.clf()