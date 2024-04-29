import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Transform raw data into usable format
data_labels = ['GDP Growth (%)']
line_labels = ['Q1', 'Q2', 'Q3', 'Q4']
# The numerical data is organized in a nested list
data = [2.5, 3.0, 2.8, 2.4]

# Create a DataFrame for seaborn to work with
df = pd.DataFrame(data, index=line_labels, columns=data_labels)

# Initialize the figure
plt.figure(figsize=(10, 6))
ax = plt.subplot()

# Use Seaborn to plot the histogram
sns.barplot(x=line_labels, y=data, ax=ax)

# Set title, labels, and apply the 'tight_layout' for automatic resizing
plt.title('Quarterly GDP Growth Rates')
plt.xlabel('Quarter')
plt.ylabel(data_labels[0])

# If the text is too long, rotate the labels or wrap them
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")

# Enhance display with grid
ax.yaxis.grid(True)

# Tight layout for better spacing
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/shared/ADLab/datasets/chart_large_simulation_liuqi/histogram/png//162.png')

# Clear the current image state
plt.clf()
