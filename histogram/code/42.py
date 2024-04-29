import matplotlib.pyplot as plt
import seaborn as sns

# Given data
data = [
    ["0-50", 12],
    ["50-100", 18],
    ["100-150", 23],
    ["150-200", 17],
    ["200-250", 10],
    ["250-300", 8],
    ["300-350", 4],
    ["350-400", 2],
    ["400-450", 1]
]

# Transforming data into three variables: data_labels, data, line_labels
data_labels = ['Revenue Range ($Million)', 'Number of Franchises']
line_labels = [item[0] for item in data]  # Extracting the Revenue Range for line_labels
data = [item[1] for item in data]  # Extracting the Number of Franchises for data

# Create figure and add subplot
plt.figure(figsize=(12, 8))
ax = plt.subplot()

# Visualize the data as a horizontal histogram using seaborn
sns.barplot(x=data, y=line_labels, orient='h', ax=ax, palette='Spectral')

# Enhancements for better visualization
ax.set_title('Revenue Distribution Among Sports and Entertainment Franchises', fontsize=14)
ax.set_xlabel(data_labels[1], fontsize=12)
ax.set_ylabel(data_labels[0], fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10, rotation=30, wrap=True)

# Adding grid (enabling y-axis gridlines only, as it's a horizontal histogram)
ax.yaxis.grid(True)

# Automatically resizing the figure
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/chart_simulation_final/histogram/png/42.png'
plt.savefig(save_path, format='png')

# Clear the current image state
plt.clf()
