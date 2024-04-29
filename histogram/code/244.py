import pandas as pd
import matplotlib.pyplot as plt

# Create the data
data_labels = ['Annual Yield (million metric tons)']
line_labels = ['Cereals', 'Vegetables', 'Fruits', 'Oilseeds', 'Pulses', 'Nuts', 'Spices', 'Coffee']
data = [218.5, 411.2, 370.3, 125.4, 81.9, 46.8, 17.5, 8.9]

# Transform data into a DataFrame
df = pd.DataFrame(data, index=line_labels, columns=data_labels)

# Create a figure object and add a subplot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)

# Plot the data
df.plot(kind='bar', ax=ax, color='skyblue', grid=True)

# Set title and labels
ax.set_title('Global Annual Yield of Key Agricultural Products', fontsize=16)
ax.set_xlabel('Crop Type', fontsize=12)
ax.set_ylabel('Annual Yield (million metric tons)', fontsize=12)

# Manage the labels to prevent overlapping
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', wrap=True)

# Tight layout to adjust spacing
plt.tight_layout()

# Save figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/244.png'
plt.savefig(save_path, dpi=300)

# Clear the current figure state
plt.clf()
