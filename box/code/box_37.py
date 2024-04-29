
import matplotlib.pyplot as plt
import numpy as np

# Restructure the data
retail_type = ['Grocery Shopping', 'Clothing Shopping', 'Online Shopping', 'Home Appliance', 'Home Decoration']
min_spend = [10, 20, 15, 25, 15]
Q1_spend = [30, 50, 40, 60, 50]
median_spend = [50, 80, 65, 90, 80]
Q3_spend = [70, 110, 90, 120, 110]
max_spend = [100, 150, 120, 170, 140]
outliers = [[], [200], [130, 160], [190], [180]]

# Plotting
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
ax.set_title('Spending Distribution in Retail Types in 2021')
ax.set_ylabel('Spending ($)')

# Transform the data into a 2D list
data = [min_spend, Q1_spend, median_spend, Q3_spend, max_spend]
data = np.array(data).T.tolist()

# Plot the box plot
ax.boxplot(data, showmeans=True, meanline=True)

# Plot the outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, 'ro')

# Drawing techniques
ax.grid(linestyle='--', alpha=0.5)

# Add labels
ax.set_xticklabels(retail_type, rotation=45, ha='right', wrap=True)

# Resize the image
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/14_202312251520.png')

# Clear current image state
plt.clf()