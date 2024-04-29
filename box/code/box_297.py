import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

data = []
outliers = []

# Construct 2D category list and 2D outlier list
data.append([5000,5500,6000,6500,7000])
outliers.append([4500,7500])

data.append([6000,6500,7000,7500,8000])
outliers.append([])

data.append([4000,4500,5000,5500,6000])
outliers.append([3500,6500])

data.append([3000,3500,4000,4500,5000])
outliers.append([2500,5500])

data.append([3500,4000,4500,5000,5500])
outliers.append([])

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot()

# Generate box plots for each category
bp = ax.boxplot(data, whis=1.5, vert=False, patch_artist=True, showfliers=False)

colors = ['#0A69A7', '#ED723D', '#51692F', '#B8B8B8', '#6E6E6E']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Manually add outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(outlier, [i + 1] * len(outlier), "x")

ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)

# Set labels
ax.set_xlabel('CO2 Emissions (kt) in Different Countries (2022)')
ax.set_ylabel('Countries')
plt.yticks([1, 2, 3, 4, 5], ['USA', 'China', 'India', 'Brazil', 'Russia'], rotation=0)
plt.title('Comparison of CO2 Emissions (kt) in Different Countries (2022)')

plt.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/146_202312270030.png')

plt.clf()
