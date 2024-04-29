import matplotlib.pyplot as plt

# Data provided
data = [[3000,4000,4500,5000,6000],[4000,5000,5500,6000,7000],
        [5000,6000,6500,7000,8000],[6000,7000,7500,8000,9000],
        [7000,8000,8500,9000,10000]]
outliers = [[],[8000],[7500,9000],[10500],[11000]]
age_group = ["<25", "25-30", "31-35", "36-40", ">41"]

# Creating the boxplot
fig, ax = plt.subplots(figsize=(10, 8))

# Plot each boxplot separately
positions = range(1, len(age_group) + 1)  # Set positions for boxplots
for i, (age, pos) in enumerate(zip(data, positions)):
    ax.boxplot(age, positions=[pos], whis=1.5, widths=0.6)
    # Plotting outliers for each age group
    if len(outliers[i]) > 0:
        ax.plot([pos] * len(outliers[i]), outliers[i], "ro")

# Adding grid, labels, and title
ax.grid(color='gray', linestyle='--', linewidth=1, axis='y', alpha=0.7)
ax.set_ylabel("Salary (USD)")
ax.set_title("Salary Distribution of Employees in Different Age Groups (2020)")
ax.set_xticklabels(age_group)

# Adjust layout and save the figure
plt.tight_layout()
# Save the image
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/48_202312251608.png")

# Clear the current image state
plt.clf()