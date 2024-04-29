import pandas as pd
import matplotlib.pyplot as plt

# Data Preparation
data_labels = ["Yield (tons per hectare)"]
line_labels = ["Wheat", "Corn", "Rice", "Barley", "Soybean", "Potato", "Tomato", "Lettuce", "Cabbage"]
data = [3.2, 5.7, 4.1, 2.8, 2.5, 15.0, 35.6, 24.0, 40.5]

# Create DataFrame
df = pd.DataFrame(data, index=line_labels, columns=data_labels)

# Create Figure and Subplot
plt.figure(figsize=(10, 8))
ax = plt.subplot(111)

# Horizontal histogram
df.plot(kind='barh', ax=ax, legend=False)

# Title and labels
plt.title('Yield Per Hectare for Various Crops in Agriculture Production')
plt.xlabel(data_labels[0])

# Rotate labels if needed
for label in ax.get_xticklabels():
    label.set_rotation(45)
    label.set_ha('right')  # Align to the right to prevent overlapping
ax.get_yaxis().get_label().set_wrap(True)  # Wrap y-axis label

# Set grid background
ax.yaxis.grid(True)

# Prevent content from being displayed incorrectly
plt.tight_layout()

# Save Figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/5.png'
plt.savefig(save_path, bbox_inches="tight", dpi=300)

# Clear the current figure state to prevent re-plotting on the same figure
plt.clf()
