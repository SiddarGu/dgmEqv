
import matplotlib.pyplot as plt
import numpy as np

# Price Distribution of Different Property Types in the Housing Market (2020)
Property_Type = np.array(['Condos', 'Townhomes', 'Single-Family Homes', 'Multi-Family Homes', 'Luxury Properties'])
Min_Price = np.array([200, 400, 500, 300, 1000])
Q1_Price = np.array([400, 600, 800, 600, 1500])
Median_Price = np.array([600, 800, 1000, 900, 2000])
Q3_Price = np.array([800, 1000, 1200, 1200, 2500])
Max_Price = np.array([1000, 1200, 1500, 1500, 3000])
outliers = [[], [2000], [3000, 6000], [1700, 2500], [6000]]
fig = plt.figure(figsize=(12,7))
ax = fig.add_subplot(111)

ax.boxplot(np.array([Min_Price, Q1_Price, Median_Price, Q3_Price, Max_Price]), labels=Property_Type, patch_artist=True, showfliers=False)

for i, outlier in enumerate(outliers):
    if len(outlier) > 0:
        ax.plot([i+1] * len(outlier), outlier, 'go', alpha=0.3, markersize=8)

ax.set_title('Price Distribution of Different Property Types in the Housing Market (2020)', fontsize=15)
ax.set_ylabel('Price (USD)', fontsize=13)

plt.xticks(rotation=45, fontsize=10, wrap=True)

plt.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/25.png', dpi=300)

plt.clf()