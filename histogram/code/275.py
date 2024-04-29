import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

# Prepare Data
data_labels = ["Yield (metric tons per hectare)"]
line_labels = ["Wheat", "Corn", "Rice", "Soybeans", "Potatoes", "Tomatoes", "Barley", "Oats"]
data = [3.5, 6.8, 4.1, 2.9, 22.0, 25.6, 3.0, 2.4]

df = pd.DataFrame(data, index=line_labels, columns=data_labels)

# Create a larger figure to prevent content from being displayed poorly
plt.figure(figsize=(10, 8))
ax = plt.subplot(111)

# Plot histogram
sns.barplot(x=df.index, y=df["Yield (metric tons per hectare)"], ax=ax, palette='viridis')

# Set the rotation of the x-axis labels if needed
plt.xticks(rotation=45, ha='right', wrap=True)

# Set grid, labels, and title
ax.grid(True, which='both', axis='y', linestyle='--', linewidth=0.7)
plt.xlabel('Crop Type')
plt.ylabel('Yield (metric tons per hectare)')
plt.title('Average Crop Yields in Agriculture Sector')

# Tight layout to automatically adjust the size
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/demo/histogram/png/625.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)  # Ensure directory exists
plt.savefig(save_path, format='png')

# Clear the current figure state
plt.clf()
