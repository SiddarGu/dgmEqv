import matplotlib.pyplot as plt

#Data
cities = ['Los Angeles', 'New York', 'San Francisco', 'Chicago', 'Miami', 'Houston']
data = [[500,800,1100,1400,1700], [700,1000,1300,1600,1900], [1000,1300,1600,1900,2200],
        [400,700,1000,1300,1600], [300,600,900,1200,1500], [200,500,800,1100,1400]]
outliers = [[], [400, 2500], [], [2000], [2600], [1800]]

#Create figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

#Make box plot
bp = ax.boxplot(data, patch_artist=True, notch=True, vert=0)

colors = ['pink', 'lightblue', 'lightgreen', 'tan', 'lightyellow', 'lightgray']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

#Plot outliers manually
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(outlier, [i + 1] * len(outlier), 'x')

#Set labels
ax.set_yticklabels(cities)
plt.xlabel('House Price (in Thousands)')
ax.set_title('House Price Distribution in Various U.S Cities (2022)')

# Enable Grid
plt.grid(True)

#Save figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/70_202312270030.png')

plt.clf()  # Clear the current figure
