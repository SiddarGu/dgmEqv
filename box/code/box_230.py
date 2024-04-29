import matplotlib.pyplot as plt

# Raw data
data_string = '''Education Policy,10,20,30,40,50,[]
Health Policy,15,25,35,45,55,[5,60]
Environmental Policy,20,30,40,50,60,[10,70]
Immigration Policy,5,15,25,35,45,[2,55]
Defense Policy,10,22,34,46,58,[1,65]'''

# Parse the raw data
categories = []
box_data = []
outliers_data = []
for row in data_string.split("\n"):
    vals = row.split(",")
    categories.append(vals[0])
    box_data.append(list(map(int, vals[1:6])))
    outliers_data.append([int(x) for x in vals[6][1:-1].split() if x])

# Create a figure and a subplot
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# Plot the boxplot
ax.boxplot(box_data, whis=1.5)

# Plot the outliers
for i, outliers in enumerate(outliers_data):
    if outliers:
        x = [i + 1] * len(outliers)
        ax.plot(x, outliers, 'ro')

# Set labels and title
ax.set_xticklabels(categories, rotation=25, ha='right')
ax.set_ylabel('Approval Time (Days)')
plt.title('Approval Time Distribution in Different Policy Areas (2021)')

# Make the plot more appealing
ax.yaxis.grid(True)
ax.xaxis.grid(False)

# Resize the image
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/156_202312310058.png')

# Clear the current image state
plt.clf()
