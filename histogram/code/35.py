import pandas as pd
import matplotlib.pyplot as plt

# Data preparation
data_labels = ['Yield (metric tons)']
line_labels = ['Wheat', 'Rice', 'Corn', 'Soybeans', 'Potatoes', 'Sugarcane', 'Tomatoes', 'Barley']
data = [75, 88, 102, 94, 120, 110, 45, 58]

# Convert data to pandas DataFrame
df = pd.DataFrame(data, index=line_labels, columns=data_labels)

# Create figure and subplot
fig, ax = plt.subplots(figsize=(10, 8))

# Plot horizontal bar chart using pandas
df.plot(kind='barh', ax=ax, legend=False)

# Style the chart to make it fancy
ax.set_title('Annual Crop Yield Distribution in Agriculture Sector')
ax.set_xlabel('Yield (metric tons)')
ax.set_ylabel('Crop Type')
ax.grid(True, linestyle='--', alpha=0.7)

# Adjust the x-axis label rotation and wrap if needed
for label in ax.get_xticklabels():
    label.set_rotation(45)
    label.set_ha('right')  # Set horizontal alignment to right
ax.tick_params(axis='y', labelsize=10)

# Automatically adjust subplot params to give specified padding
plt.tight_layout()

# Save the figure with the specified absolute path
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/35.png')

# Clear the current figure's state
plt.clf()
