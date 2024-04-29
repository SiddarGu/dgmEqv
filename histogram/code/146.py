import matplotlib.pyplot as plt

# Variables from the data
data_labels = ['50-60', '60-70', '70-80', '80-90', '90-100']
data = [4, 10, 35, 45, 6]
line_labels = ['Life Expectancy (Years)', 'Number of Countries']

# Creating a figure with larger figsize to prevent content from being squeezed
plt.figure(figsize=(12, 7))

# Create an axis instance
ax = plt.subplot()

# Plotting the data using a horizontal bar chart
ax.barh(data_labels, data, align='center', color='skyblue', edgecolor='black')

# Adding the grid, title, and labels
plt.grid(linestyle='--', linewidth=0.5)
plt.title('Global Life Expectancy Distribution')

# Set the label rotation or wrapping if too long
ax.set_yticklabels(data_labels, wrap=True)
ax.set_xlabel('Number of Countries')

# Automatically adjust subplot params so the subplot(s) fits into the figure area
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/hancheng/histogram/png_val/146.png'
plt.savefig(save_path, format='png')

# Clear the current figure state to ensure no overlap on future plots
plt.clf()
