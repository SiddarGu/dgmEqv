import matplotlib.pyplot as plt

# Preparation of data
categories = ["Clothes", "Electronics", "Beauty & Health", "Groceries", "Books"]
data = [[15, 40, 60, 75, 99], [30, 60, 100, 150, 220], [20, 50, 90, 140, 200], [50, 80, 120, 160, 210], [10, 30, 50, 70, 90]]
outliers = [[], [350, 400], [10, 25], [300, 320, 350], [5, 7, 9]]

# Create figure and add subplot
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot()

# Clear current axis and set grid
ax.cla()  
ax.grid(True)

# Box plotting for each category
ax.boxplot(data, whis=1.5, vert = False, patch_artist = True, widths = 0.5)

plt.yticks([i + 1 for i, _ in enumerate(categories)], categories)

# Plotting outliers manually for each category
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(outlier, [i + 1] * len(outlier), "ro")

# Setting labels for y-axis
ax.set_ylabel('Sales (Thousands)')

# Setting title for the figure
plt.title('Sales Distribution in Different Retail and E-commerce Product Categories (2020)')

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/106_202312270030.png')

# Clear the current image state
plt.clf()
