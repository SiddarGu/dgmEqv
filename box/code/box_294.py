import matplotlib.pyplot as plt

# Data
categories = ['Paintings', 'Sculptures', 'Photography', 'Digital Art', 'Mixed Media']
numbers = [[2000, 5000, 7500, 10000, 15000],
           [2500, 6000, 8500, 12000, 18000],
           [1800, 4500, 6500, 9000, 13000],
           [1500, 4000, 5500, 7000, 10000],
           [2200, 5500, 8000, 10500, 14500]]
outliers = [[], [22200], [15500], [], [16500]]

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# Boxplot
ax.boxplot(numbers, vert=False, whis=1.5, widths = 0.3,
           patch_artist=True, medianprops = dict(linewidth=2.5, color='firebrick'),
           boxprops = dict(linewidth=2.5, color='black', facecolor = 'blue', alpha =.6))

# Outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(outlier, [i + 1] * len(outlier), 'ro')

# Setting up the title and labels
ax.set_title('Artwork Pricing Analysis across Different Categories (2020-2021)')
ax.set_xlabel('Price (USD)')
ax.set_ylabel('Art Category')
ax.set_yticklabels(categories)

ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/114_202312270030.png')

plt.close()
