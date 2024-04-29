import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

# Data Preparation
data_labels = ["Years Active/Number of Works"]
line_labels = ["0-1700", "1701-1800", "1801-1900", "1901-1950", "1951-2000", "2001-2023"]
data = [0, 150, 300, 450, 600, 550]

# Create a DataFrame from the data
df = pd.DataFrame(data, index=line_labels, columns=data_labels)

# Initialize the matplotlib figure
plt.figure(figsize=(12, 8))
ax = plt.subplot()

# Create a horizontal bar plot
sns.barplot(x=data_labels[0], y=df.index, data=df, orient='h')

# Add a grid to the background
ax.set_axisbelow(True)
plt.grid(axis='x', linestyle='-', linewidth=0.5, color='gray')

# Set the title of the plot
plt.title('Historical Artwork Production by Movement Period')

# Set rotation or text wrapping for xticklabels if needed
plt.xticks(rotation=45, ha='right', wrap=True)

# Use tight layout to resize the image
plt.tight_layout()

# Define the path for saving the image
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/211.png'

# Ensure the directory exists
os.makedirs(os.path.dirname(save_path), exist_ok=True)

# Save the figure
plt.savefig(save_path)

# Clear the current figure state after saving the image
plt.clf()

