import matplotlib.pyplot as plt
import seaborn as sns

# Given data
data_labels = ["Yield (metric tons)"]
line_labels = ["Wheat", "Corn", "Rice", "Soybeans", "Potatoes", "Tomatoes", "Apples"]
data = [3200, 2800, 2200, 1500, 2100, 2400, 1800]

# Create a new figure with specified figure size
plt.figure(figsize=(10, 7))
ax = plt.subplot()

# Create a histogram
sns.barplot(x=line_labels, y=data)

# Set aesthetic properties
ax.set_title('Crop Yield Comparison in Agriculture Sector')
ax.set_xticks(range(len(line_labels)))
ax.set_xticklabels(line_labels, rotation=45, ha="right")

# Automatically adjust subplot params so that the subplot(s) fits in to the figure area
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/shared/ADLab/datasets/chart_large_simulation_liuqi/histogram/png/7.png'
plt.savefig(save_path, format='png')

# Clear the current figure state to avoid overlap with future plots
plt.clf()
