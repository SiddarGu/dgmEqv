import matplotlib.pyplot as plt

# data
category_useful_values = [
    ['Electronics', [1,3,5,7,10]],
    ['Clothing', [2,4,6,8,11]],
    ['Books', [1,2,4,6,8]],
    ['Furniture', [5,7,10,13,16]],
    ['Beauty Products', [2,3,4,5,7]]
]

category_outliers_values = [
    ['Electronics', []],
    ['Clothing', [13,15]],
    ['Books', [0.5,11]],
    ['Furniture', [18,20]],
    ['Beauty Products', [9]]
]

# Figure initialization
fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111)

# For each category, make a box plot
for i, cat_values in enumerate(category_useful_values):
    ax.boxplot(cat_values[1], positions=[i+1], vert=False, patch_artist=True,
               boxprops=dict(facecolor='cornflowerblue', color='black'),
               capprops=dict(color='black'),
               whiskerprops=dict(color='black'), medianprops=dict(color='black'),
               whis=1.5)

# Convert labels list into a tuple for 'set_yticklabels' function
labels = tuple(i[0] for i in category_useful_values)

ax.set_yticklabels(labels)
ax.set_xlabel("Delivery Time (Days)")
ax.set_ylabel("Product Category")
ax.set_title("Delivery Time Distribution in E-commerce Product Categories (2022)")
ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
               alpha=0.5)
ax.set_axisbelow(True)

# custom y-axis settings
ax.get_yaxis().set_tick_params(which='major', direction='out')

# Plotting outliers using scatter
# plotting random outliers
for i, outlier in enumerate(category_outliers_values):
    if outlier[1]:
        ax.scatter(outlier[1], [i + 1] * len(outlier[1]), color='Tomato', alpha= 0.5)

plt.tight_layout() # Automatically resize the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/94_202312270030.png')
plt.clf() # clear the current image state
