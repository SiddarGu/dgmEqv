
import matplotlib.pyplot as plt
import numpy as np

# Restructure the data
employee_type = ["Managers", "Executives", "Analysts", "Consultants", "Administrators"]
min_salary = [3000, 4000, 3500, 2500, 2000]
q1_salary = [6000, 7500, 6500, 5500, 5000]
median_salary = [9000, 11000, 9500, 8500, 8000]
q3_salary = [12000, 14000, 12500, 11500, 11000]
max_salary = [15000, 17000, 16500, 14500, 14000]
outliers = [[], [20000], [200, 19000], [18000], [17000]]

# Create figure
fig, ax = plt.subplots(figsize=(15, 8))

# Plot data with box plot
ax.boxplot(np.array([min_salary, q1_salary, median_salary, q3_salary, max_salary]),
            labels=employee_type,
            whis=[0, 100],
            showmeans=True,
            meanline=True,
            showfliers=False)

# Plot outliers
for i, outlier in enumerate(outliers):
    if outlier:
        x = [i + 1] * len(outlier)
        ax.plot(x, outlier, 'r^', markersize=8)

# Set background grid
ax.grid(axis='y', linestyle='dotted', alpha=0.5)

# Set the title
ax.set_title('Salary Distribution in Different Types of Employees in 2021')

# Automatically resize the image
plt.tight_layout()

# Save the image
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/10_202312251315.png")

# Clear the current image state
plt.clf()