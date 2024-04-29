import matplotlib.pyplot as plt

# Data Preparation
charity_data = [
    ['Charity A', [100, 500, 800, 1200, 2000], []],
    ['Charity B', [200, 600, 950, 1320, 2100], [50, 3000]],
    ['Charity C', [150, 550, 850, 1250, 1800], [4000]],
    ['Charity D', [120, 510, 810, 1100, 1600], [2600, 2800]],
    ['Charity E', [300, 800, 1200, 1600, 2300], [3500]]
]

# Extract Only Numerical Data and Outliers
data =[item[1] for item in charity_data]
outliers = [item[2] for item in charity_data]

# Figure Preparation
plt.figure(figsize=(12, 6))
ax = plt.subplot()

# Box Plot
bp = ax.boxplot(data, whis=1.5)

# Overlay the Outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, "ro")

# Axes Configurations
ax.set_xticklabels([item[0] for item in charity_data], rotation=45, ha='right')
ax.set_ylabel('Donation Amount (USD)')
ax.grid(True)

# Figure Configurations
plt.title('Donation Amount Distribution in Charities and Nonprofit Organizations (2019-2021)')
plt.tight_layout()

# Save Figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/171_202312310058.png')

# Clear Figure
plt.clf()
