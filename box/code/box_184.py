import matplotlib.pyplot as plt

# Data
data = [["HealthCare", [20, 35, 55, 70, 95], []], 
        ["IT", [10, 60, 90, 110, 140], [150, 180]], 
        ["Retail", [30, 40, 55, 65, 80], [90, 100]], 
        ["FMCG", [25, 35, 50, 70, 85], [95]], 
        ["Manufacturing", [15, 45, 55, 65, 80], [90]]]

labels = [item[0] for item in data]
values = [item[1] for item in data]
outliers = [item[2] for item in data]

# Create figure and add subplot
fig = plt.figure(figsize=(15, 10)) 
ax = fig.add_subplot()

# Plotting the data
bp = ax.boxplot(values, notch=True, vert=1, patch_artist=True, whis=1.5)

colors = ['pink', 'lightblue', 'lightgreen', 'tan', 'plum']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Plotting the outliers
for i, outlier in enumerate(outliers, start=1):
    if outlier:
        ax.plot([i] * len(outlier), outlier, "ro")

# Adding labels and title
ax.set_xticklabels(labels, rotation=45)  
ax.set_title('Profit Distribution Across Various Business Sectors (2020 - 2021)')
ax.set_xlabel('Business Sector')
ax.set_ylabel('Profit (Million USD)')

# Show grid
ax.yaxis.grid(True)
ax.xaxis.grid(True)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/152_202312310058.png')
plt.clf()
