import matplotlib.pyplot as plt

# Given data
data_labels = ['CO2 Emissions (Metric Tons per Capita)']
line_labels = ['0-5', '5-10', '10-15', '15-20', '20-25', '25-30', '30-35', '35-40', '40-45']
data = [30, 45, 60, 50, 35, 20, 15, 5, 2]

# Figure setup
plt.figure(figsize=(10, 8))
ax = plt.subplot(111)

# Vertical Histogram
ax.bar(line_labels, data, color='skyblue')

# Add grid, title, and adjust layout
ax.grid(True, linestyle='--', which='major', color='grey', alpha=.25)
plt.title('Global Distribution of Carbon Dioxide Emissions Per Capita', fontsize=14)

# Handling long label texts
ax.set_xticklabels(line_labels, rotation=45, ha='right')
ax.set_ylabel('Country')
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/hancheng/histogram/png_val/92.png'
plt.savefig(save_path)

# Clear the current figure state
plt.clf()
