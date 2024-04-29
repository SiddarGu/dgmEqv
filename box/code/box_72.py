import matplotlib.pyplot as plt
import numpy as np

# Predefined data
data = [("New York",[250000,300000,400000,500000,600000],[]),
        ("Los Angeles",[200000,300000,350000,450000,550000],[700000,800000]),
        ("Chicago",[150000,250000,300000,350000,400000],[500000]),
        ("Miami",[200000,250000,300000,350000,450000],[550000]),
        ("Seattle",[250000,300000,400000,500000,600000],[])]

# Data restructuring
categories, values, outliers = zip(*data)
values = np.array(values).T
outliers = [list(map(int, outlier)) for outlier in outliers]

# Figure creation
fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot(111)

# Box plotting
ax.boxplot(values, widths=0.4, whis=1.5, patch_artist=True,
           boxprops=dict(facecolor="cornflowerblue", color="k"),
           capprops=dict(color="k"),
           whiskerprops=dict(color="k"),
           flierprops=dict(color="r", markeredgecolor="r"),
           medianprops=dict(color="navy"))

# Outlier plotting
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, "ro")

# Styling
plt.xticks(np.arange(1, len(categories) + 1), categories, rotation='vertical')
ax.set_title('Distribution of House Prices in Different Cities (2022)')
ax.set_ylabel('House Price ($)')
ax.grid(True)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/227_202312310058.png')
plt.close(fig)
