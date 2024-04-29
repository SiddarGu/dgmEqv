import matplotlib.pyplot as plt
import ast

# Correctly parse the data
data = "Destination,Min Stay Duration (Days),Q1 Stay Duration (Days),Median Stay Duration (Days),Q3 Stay Duration (Days),Max Stay Duration (Days),Outlier Stay Duration (Days)/n Bali,3,7,10,14,21,[]/n Paris,2,5,7,10,14,[1,30]/n New York,4,7,10,14,20,[3,28]/n Sydney,3,6,9,12,16,[2,25]/n Tokyo,3,7,11,15,21,[1,30]"
data = [i.split(",") for i in data.split("/n")]
header = data.pop(0)
categories = [i[0] for i in data]
box_data = [[int(j) for j in i[1:6]] for i in data]

# Safely evaluate the outlier data
outliers = []
for i in data:
    try:
        outliers.append(ast.literal_eval(i[6]))
    except:
        outliers.append([])

# Create a boxplot
fig, ax = plt.subplots(figsize=(10, 6))
bp = ax.boxplot(box_data, vert=True, patch_artist=True, notch=True)

# Customize the boxplot colors
colors = ['pink', 'lightblue', 'lightgreen', 'red', 'purple']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Add outliers
for i, outlier in enumerate(outliers):
    if outlier:
        y = [i + 1] * len(outlier)
        ax.plot(outlier, y, 'k.', markersize=10)

# Add grid, labels, and title
ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
ax.set_xticklabels(categories)
ax.set_xlabel('Stay Duration (Days)')
ax.set_ylabel('Destination')
ax.set_title("Guests' Duration of Stay in Popular Tourist Destinations")

# Save & Clear
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/150_202312270030.png")
plt.clf()
