import matplotlib.pyplot as plt

# the given data
data = [
["Charity A", [50,200,500,800,1500], []],
["Charity B", [100,300,700,1100,2000], [4000]],
["Charity C", [80,240,600,960,1800], [20,25]],
["Charity D", [50,150,400,650,1200], [2500]],
["Charity E", [100,200,500,900,1400], [3000]]
]

# separating the data into necessary parts
labels = [i[0] for i in data]
values = [i[1] for i in data]
outliers = [i[2] for i in data]

fig = plt.figure(figsize = (10,5))

# create a subplot
ax = fig.add_subplot()

# creating the boxplot
bp = ax.boxplot(values, vert = False, patch_artist=True, whis = 1.5)
for flier in bp['fliers']:
    flier.set(marker='o', color='red', alpha=0.5)

# plot the outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(outlier, [i + 1] * len(outlier), marker='o', linestyle='none', color='r', markersize=3)

# setting the labels
ax.set_yticklabels(labels, rotation=45)

# setting the title of the axes
ax.set_xlabel("Donation Amount (USD)")
ax.set_ylabel("Charities")
ax.set_title("Donation Distribution in Charities and Nonprofit Organizations (2023)")

plt.grid(True)

# save the plot as a file
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/88_202312270030.png', format = 'png', dpi = 300)

plt.show()

# clear current figure
plt.clf()
