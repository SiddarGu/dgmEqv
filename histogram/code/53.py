import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

# Given data
data_labels = ['Yield (tons per hectare)']
line_labels = ['Wheat', 'Rice', 'Maize', 'Barley', 'Soybean', 'Potato', 'Tomato', 'Lettuce', 'Carrot']
data = [3.2, 4.1, 5.8, 2.9, 2.1, 17.5, 25.3, 3.4, 8.7]

# Transform data into DataFrame for Seaborn
df = pd.DataFrame(data, index=line_labels, columns=data_labels)

# Create figure and axis
plt.figure(figsize=(10, 8))
ax = plt.subplot()

# Create horizontal histogram using seaborn
sns.barplot(x=data_labels[0], y=df.index, data=df, orient='h', palette='viridis')

# Set title and labels
ax.set_title('Average Crop Yields in Agriculture Sector', fontsize=16)
ax.set_xlabel(data_labels[0], fontsize=14)
ax.set_ylabel('Crop Type', fontsize=14)

# Rotate x-axis labels if too long
plt.xticks(rotation=45)

# Adjust layout to prevent content from being cut off
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/53.png'
if not os.path.exists(os.path.dirname(save_path)):
    os.makedirs(os.path.dirname(save_path))

plt.savefig(save_path, dpi=300)

# Clear current figure
plt.clf()
