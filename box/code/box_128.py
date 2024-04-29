import matplotlib.pyplot as plt

# restructuring data into two lists
data = [["Electronics", 50, 150, 200, 250, 350], 
        ["Clothing", 100, 200, 250, 325, 475], 
        ["Groceries", 75, 180, 225, 275, 350], 
        ["Furniture", 55, 145, 200, 255, 330], 
        ["Appliances", 80, 160, 220, 290, 380]]
outliers = [[], [30, 545], [15, 400], [10, 370], [420]]

# Extract sales data for each category
categories = [item[0] for item in data]
sales_data = [item[1:] for item in data]

fig = plt.figure(figsize=(10, 6)) 
ax = fig.add_subplot(111) 

# Creating boxplots with custom settings
bp = ax.boxplot(sales_data, patch_artist=True, notch=True, vert=1, whis=1.5)

# Setting colors for each boxplot
colors = ['#0000FF', '#00FF00', '#FFFF00', '#FF00FF', '#00FFFF']
for patch, color in zip(bp['boxes'], colors):
    patch.set(facecolor=color)

# Manually plotting the outliers for each category
for i, outlier in enumerate(outliers):
    if outlier:  # Only plot if the list is not empty
        ax.plot([i + 1] * len(outlier), outlier, "ro")

# Adding grid, titles, and labels
ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
ax.set_axisbelow(True)
ax.set_title('Sales Distribution in Different Product Categories in Retail and E-commerce (2020)')
ax.set_xlabel('Product Category')
ax.set_ylabel('Sales (in Thousands)')

# Setting custom x-axis labels
ax.set_xticklabels(categories, rotation=45, ha="right")

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/169_202312310058.png')
plt.close(fig)
