import pandas as pd
import matplotlib.pyplot as plt

# Given Data
data_labels = ['Production Efficiency (%)', 'Number of Factories']
line_labels = ['50-60', '60-70', '70-80', '80-90', '90-95', '95-100']
data = [7, 15, 25, 30, 12, 8]

# Create DataFrame
df = pd.DataFrame(data, index=line_labels, columns=data_labels[1:])

# Plotting
fig = plt.figure(figsize=(10, 8))  # Set figure size
ax = fig.add_subplot(111)

# Plot a bar chart (Histogram)
df.plot(kind='bar', legend=False, ax=ax, color='skyblue')

# Styling
plt.title('Production Efficiency Distribution Across Manufacturing Factories')
plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=45, wrap=True)

# Automatically adjust the subplot params so that the subplot(s) fits into the figure area
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/165.png'
plt.savefig(save_path, format='png', dpi=300)  # Save with high resolution

# Clear the current figure state
plt.clf()
