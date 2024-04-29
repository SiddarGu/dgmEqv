import matplotlib.pyplot as plt

# Process and restructure the data
data = [
    ["Company F",10,30,50,70,100,[]],
    ["Company G",15,35,60,85,110,[120]],
    ["Company H",20,40,70,100,130,[140]],
    ["Company I",25,45,65,85,115,[5,125]],
    ["Company J",30,50,75,100,120,[150]]
]

labels, min_rev, q1_rev, median_rev, q3_rev, max_rev, outliers = zip(*data)

# Structure data for box plot
box_data = [list(a) for a in zip(min_rev, q1_rev, median_rev, q3_rev, max_rev)]
outlier_data = [list(map(int, a)) for a in outliers]

# Create a new figure and a subplot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)

# Create box plot
bplot = ax.boxplot(box_data, notch=True, vert=True, patch_artist=True, whis=1.5)

colors = ['pink', 'lightblue', 'lightgreen', 'yellow', 'red']
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)

# Plot outliers
for i, outlier in enumerate(outlier_data):
    if outlier: 
        ax.plot([i + 1] * len(outlier), outlier, "x")

# Set Title & labels 
ax.set_title('Revenue Distribution in Businesses (2022)', fontsize=12)
ax.set_xlabel('Company', fontsize=10)
ax.set_ylabel('Revenue (Million USD)', fontsize=10)

# Set x-axis labels and ensure they do not overlap
ax.set_xticks(range(1, len(labels) + 1))
ax.set_xticklabels(labels, rotation=45, wrap=True)

# Tight layout
plt.tight_layout()

# Save figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/237_202312310058.png')

# Clear figure
plt.clf()
