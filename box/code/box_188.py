import matplotlib.pyplot as plt

# Define the data
data = [["Solar", 200, 450, 700, 950, 1200, [1500]],
        ["Wind", 150, 300, 450, 600, 800, [1300]], 
        ["Hydro", 100, 250, 400, 550, 700, [900]],
        ["Geothermal", 50, 150, 250, 350, 450, [65,600]],
        ["Nuclear", 300, 650, 1000, 1350, 1700, [2250]]]

# Reformat the data
box_data = [[a[1], a[2], a[3], a[4], a[5]] for a in data]
outliers = [a[6] for a in data]

# Create the figure
fig = plt.figure(figsize = (10, 5))
ax1 = fig.add_subplot(111)

# boxplot
bplot = ax1.boxplot(box_data, vert=0, patch_artist=True, notch=True, whis=1.5)

colors = ['#0000FF', '#00FF00', '#FFFF00', '#FF00FF', '#800000']
for i in range(len(colors)):
    bplot['boxes'][i].set_facecolor(colors[i])

for i, outlier in enumerate(outliers):
    if outlier:
        ax1.plot(outlier, [i + 1] * len(outlier), "ko")

ax1.set_yticklabels([a[0] for a in data], wrap=True)
ax1.set_xlabel('Production (MW)')
ax1.grid(True)
plt.title("Energy Production Distribution in Different Energy Sources (2022)")

# Save the figure
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/129_202312270030.png")

# Clear current figure
plt.clf()
