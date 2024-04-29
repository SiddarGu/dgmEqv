import matplotlib.pyplot as plt

# Data restructuring
data = [['Burger', 2, 5, 7, 10, 12], ['Pizza', 5, 10, 15, 20, 25], ['Pasta', 7, 12, 17, 22, 27], 
        ['Coffee', 1, 3, 5, 7, 9], ['Smoothie', 3, 6, 8, 10, 12]]
outliers = [[], [1, 30], [35], [12, 15], [18]]

# Creating a figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# Plotting boxplot
ax.boxplot([item[1:] for item in data], whis=1.5)

# Iterating through outliers and plotting them
for i, out in enumerate(outliers):
    if out:
        ax.plot([i + 1] * len(out), out, "ro")

# Setting background grid
ax.grid(True)

# Setting title and labels
plt.title('Preparation Time Distribution for Typical Food and Beverage Products in 2021', fontsize=12)
plt.ylabel('Preparation Time (Minutes)')
ax.set_xticklabels([item[0] for item in data], rotation=20)

# Automatically resize the image
plt.tight_layout()

# save the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/216_202312310058.png')

# clear the current figure
plt.clf()
