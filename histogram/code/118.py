import matplotlib.pyplot as plt
import seaborn as sns

# Given data
data_labels = ['Harvest Yield (million metric tons)']
line_labels = ['Wheat', 'Corn', 'Rice', 'Barley', 'Soybean', 'Potato', 'Cotton', 'Oats']
data = [780.0, 1080.5, 740.0, 144.5, 350.2, 380.3, 120.7, 22.5]

# Visualize the data as a histogram using seaborn
sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 8))
ax = plt.subplot(111)
sns.barplot(x=line_labels, y=data, ax=ax, palette="viridis")

# If the text length of the label is too long:
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor", wrap=True)
ax.set_ylabel('Harvest Yield (million metric tons)')
# Title of the figure
plt.title('Global Harvest Yields for Major Crops')

# Automatically resize the image
plt.tight_layout()

# Save the figure to the specified path
save_path = '/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/hancheng/histogram/png_val/118.png'
plt.savefig(save_path, format='png', dpi=300)

# Clear the current image state
plt.clf()
