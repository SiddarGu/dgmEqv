import matplotlib.pyplot as plt

# Creating data structure
data = [
['Child Law', [400,1000,1500,2000,2500], []],
['Property Law', [300,800,1200,2000,3000], [4000,5000]],
['Maritime Law', [500,1200,1700,2200,2700], []],
['Immigration Law', [600,1100,1600,2500,3500], [4500]],
['Tax Law', [700,1500,2000,2900,3700], [4500,5000]],  
]

labels, data, outliers = zip(*data)

# Creating figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# Plotting data
ax.boxplot(data, widths=0.5, vert=False, whis=1.5, patch_artist=True, medianprops={'linewidth': 2})

# Plotting outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(outlier, [i + 1] * len(outlier), "ro", ms=5)

# Setting properties
ax.set_yticklabels(labels, fontsize=10)
ax.set_xlabel('Fees ($)', fontsize=10)
ax.set_title('Legal Fees Distribution in Different Law Areas', fontsize=12)
ax.grid(True)

# Saving figure and clearing image
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/87_202312270030.png')
plt.clf()
