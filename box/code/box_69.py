import matplotlib.pyplot as plt

product_names = ['Whole Grain Bread', 'Red Wine', 'White Meat', 'Blue Cheese', 'Organic Apples']
data = [[3,3.5,4,4.5,5], [15,20,25,30,35], [5,7,9,11,15], [6,7.5,9,10.5,12], [2,2.5,3,4,5]]
outliers = [[], [45,50], [], [15], [10]]

fig, ax = plt.subplots(figsize=(12, 8))
ax.boxplot(data, widths=0.5, patch_artist=True, notch=True, vert=True, whis=1.5)
ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, "x")

ax.set_title('Price Distribution of Selected Food and Beverage Products (2022)')
ax.set_ylabel('Price ($)')
ax.set_xticks([1, 2, 3, 4, 5])
ax.set_xticklabels(product_names, rotation=45, ha='right')

fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/150_202312310058.png')
plt.clf()
