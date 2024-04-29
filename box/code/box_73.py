import matplotlib.pyplot as plt

# Prepare data
data = [["Department of Defense", [300,500,750,1000,1300], []],
        ["Department of Health", [200,290,350,430,520], [800]],
        ["Department of Education", [190,250,300,350,400], [500]],
        ["Department of Transportation", [150,220,300,380,420], [100,550]],
        ["Department of Veteran Affairs", [120,200,280,360,450], [50,470]]]

# Split names and budget data from the list
names, values, outliers = zip(*data)

# Create figure
fig, ax = plt.subplots(figsize=(10,6))

# Box plot
bp = ax.boxplot(values, whis=1.5)

# Plot outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, "ro")

# Create background grid
ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',alpha=0.5)

# Set y-axis label
ax.set_ylabel('Budget (Million $)')

# Set names on x-axis
ax.set_xticklabels(names, rotation=30, ha='right')

# Set figure title
plt.title('Federal Budget Distribution in Governmental Departments (2023)')

# Automatically resizes the image
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/166_202312310058.png')

# Clear current figure
plt.clf()               
