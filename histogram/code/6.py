import pandas as pd
import matplotlib.pyplot as plt

# Given data
data_labels = ['Weekly Hours of Operation', 'Number of Facilities']
line_labels = ['0-20', '20-40', '40-60', '60-80', '80-100', '100-120', '120-140', '140-160']
data = [5, 15, 20, 25, 18, 12, 8, 2]

# Creating a DataFrame using the given data
df = pd.DataFrame(data, index=line_labels, columns=data_labels[1:])

# Creating the figure and the histogram
plt.figure(figsize=(10, 8))
ax = plt.subplot()

# Plot horizontal histogram
df.plot(kind='barh', ax=ax, legend=False, color='skyblue')

# Setting the title, xlabel and grid
ax.set_title('Operating Hours of Sports and Entertainment Facilities')
ax.set_xlabel('Number of Facilities')
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Enabling the rotation and text wrapping of tick labels
ax.set_yticklabels(line_labels, rotation=45, wrap=True)

# Prevent content from being displayed improperly
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/6.png')

# Clear the current image state
plt.clf()
