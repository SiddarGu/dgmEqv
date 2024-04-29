import pandas as pd
import matplotlib.pyplot as plt

# Data
data_labels = ['Yield (metric tons)']
line_labels = ['Wheat', 'Corn', 'Rice', 'Soybeans', 'Vegetables', 'Fruits', 'Cotton']
data = [850, 1230, 960, 730, 1180, 540, 590]
df = pd.DataFrame(data, index=line_labels, columns=data_labels)

# Create a figure with a single subplot
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1, 1, 1)

# Plotting the histogram
df.plot(kind='bar', ax=ax, color='skyblue', grid=True)

# Set the title
ax.set_title('Annual Crop Yields in Global Agriculture Production')

# Set rotation for x-axis labels if they're too long
for tick in ax.get_xticklabels():
    tick.set_rotation(45)
    tick.set_ha('right')
    tick.set_wrap(True)

# Automatically adjust subplot params so the subplot(s) fits into the figure area
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/0.png'
plt.savefig(save_path)

# Clear the current figure
plt.clf()
