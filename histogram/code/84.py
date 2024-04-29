import matplotlib.pyplot as plt
import seaborn as sns

# Extracting data into variables
data_labels = ['Occupancy Rate (%)', 'Number of Hotels']
line_labels = ['0-20', '20-40', '40-60', '60-80', '80-100']
data = [4, 6, 15, 25, 10]

# Setting the style
sns.set(style="whitegrid")

# Creating the figure and a subplot
plt.figure(figsize=(10, 8))
ax = plt.subplot()

# Plotting the histogram
sns.barplot(x=line_labels, y=data, palette="viridis")

# Rotating the x labels if needed and enabling wrapping
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')

# Setting the title
plt.title('Hotel Occupancy Rate Distribution in a Tourist City')

# Applying tight_layout to automatically adjust subplot params
plt.tight_layout()

# Save the image
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/84.png'
plt.savefig(save_path, dpi=300)

# Clear the current figure
plt.clf()
