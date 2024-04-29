import matplotlib.pyplot as plt

# Preparing the data
data_chart = [
    ['Hotel A', [1, 3, 5, 7, 10], []],
    ['Hotel B', [2, 4, 6, 8, 11], [13, 15]],
    ['Hotel C', [1, 3, 5, 7, 9], [0, 15]],
    ['Hotel D', [2, 4, 6, 8, 12], [16]],
    ['Hotel E', [1, 3, 4, 6, 9], [12, 13, 14]],
]

main_data = [row[1] for row in data_chart]
outliers = [row[2] for row in data_chart]

labels = [row[0] for row in data_chart]

# Creating a new figure
fig = plt.figure(figsize=(12, 7))
ax = fig.add_subplot()

# Creating the box plot
bplot = ax.boxplot(main_data, vert=True, patch_artist=True, labels=labels, notch=True, whis=1.5)
colors = ['pink', 'lightblue', 'lightgreen', 'tan', 'purple']

for patch, color in zip(bplot['boxes'], colors):       
    patch.set_facecolor(color)
    
for median_line in bplot['medians']:
    median_line.set_color("black")
    
# Adding the outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, linestyle="None", color="r", marker="o")  

# Adding Grid, Title and Labels
ax.yaxis.grid(True)
ax.set_title('Guest Stay Duration Distribution in Hotels (2022)')
ax.set_xlabel('Hotel')
ax.set_ylabel('Stay Duration (Nights)')
plt.xticks(rotation=45)

# Saving the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/176_202312310058.png')

# Clearing the figure
plt.clf()
