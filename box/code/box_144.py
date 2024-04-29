import matplotlib.pyplot as plt

# Define data
categories = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
numerical_values = [[6,10,13.5,18,22], [7,9.5,12,15.5,20], [2,7,11,15,20], [5,8.5,12,16.5,21], [4,8,12.5,17,23]]
outliers = [[], [24,28], [1, 30], [28.5], [2,26]] 

# Create figure
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)

# Create boxplot
bp = ax.boxplot(numerical_values, vert=False, widths=0.6, patch_artist=True, notch=True, 
                boxprops=dict(facecolor='lightblue', color='blue'),
                capprops=dict(color='blue'),
                whiskerprops=dict(color='blue'),
                flierprops=dict(color='red', markeredgecolor='red'),
                medianprops=dict(color='black'),
                whis=1.5)

# Plot outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(outlier, [i + 1] * len(outlier), "rx")

# Drawing techniques
ax.grid(True)
ax.set_yticklabels(categories, rotation=0, wrap=True)
ax.set_title('Sugar Content Distribution in Food Products of the Beverage Industry (2021)')
ax.set_xlabel('Sugar Content(grams)')

# Save figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/142_202312270030.png')

# Clear figure
plt.close(fig)
