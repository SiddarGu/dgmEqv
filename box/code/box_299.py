import matplotlib.pyplot as plt

# Data
data = [['Steel',400,600,800,1000,1200,[]],
        ['Aluminum',100,200,300,400,500,[600,700]],
        ['Titanium',800,900,1000,1100,1200,[700,1300]],
        ['Copper',300,350,400,450,500,[250,600]],
        ['Carbon Fiber',1000,1200,1500,1800,2100,[2200,2300]]]

categories = [i[0] for i in data]
tensile_distribution = [i[1:-1] for i in data]
outliers = [i[-1] for i in data]

# Create figure and add subplot
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot()

# Box plot
ax.boxplot(tensile_distribution, whis=1.5)

# Plot outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, "ko")

# Settings
ax.set_xticklabels(categories, rotation=45, ha='right')
ax.set_title('Tensile Strength Distribution in Different Engineering Materials in 2025')
ax.set_ylabel('Tensile Strength (MPa)')
ax.grid()

# Save figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/154_202312310058.png')

# Clear the current figure
plt.clf()
