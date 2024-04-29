import matplotlib.pyplot as plt

# Restructure data
categories = ['Hydro', 'Solar', 'Wind', 'Geothermal', 'Biomass']
data = [[80,110,145,190,250], [60,95,130,175,250], [70,105,135,165,220], [30,65,90,120,150], [20,45,80,110,140]]
outliers = [[], [300], [40,260], [200], [10,160]]

# Create figure
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)

# Boxplot
bp = ax.boxplot(data, whis=1.5)

# Iterate through outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, "ro")

# Customize axes
ax.set_xticklabels(categories, rotation=45, ha='right')
ax.set_ylabel('Generation (GWh)')
ax.set_title('Power Generation Distribution by Energy Sources (2021)')
ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
ax.xaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)

fig.autofmt_xdate()
fig.tight_layout()

# Save fig and clear 
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/213_202312310058.png')
plt.clf()
