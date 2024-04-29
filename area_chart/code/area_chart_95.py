
# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Generate data dictionary
data = {
    'Category': ['Technology', 'Fashion', 'Food', 'Travel', 'Art', 'Music', 'Health', 'Fitness', 'Beauty', 'Education', 'Entertainment', 'Business', 'News'],
    'Facebook (Posts)': [500, 200, 350, 250, 300, 450, 350, 400, 300, 250, 200, 400, 300],
    'Twitter (Posts)': [400, 300, 250, 350, 400, 300, 200, 250, 400, 350, 300, 250, 250],
    'Instagram (Posts)': [300, 500, 200, 300, 200, 200, 400, 350, 200, 300, 400, 300, 400],
    'Linkedin (Posts)': [450, 400, 400, 200, 250, 350, 250, 300, 350, 400, 250, 350, 200],
    'YouTube (Videos)': [350, 250, 300, 450, 350, 250, 300, 200, 250, 200, 350, 200, 350]
}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(10, 6))

# Set background grid lines
ax.grid(color='lightgrey', linestyle='-', linewidth=0.5)

# Plot data with area chart
ax.stackplot(df['Category'], df['Facebook (Posts)'], df['Twitter (Posts)'], df['Instagram (Posts)'], df['Linkedin (Posts)'], df['YouTube (Videos)'], labels=['Facebook', 'Twitter', 'Instagram', 'Linkedin', 'YouTube'], alpha=0.8)

# Set x and y axis ticks and ticklabels
ax.set_xticks(np.arange(len(df.index)))
ax.set_xticklabels(df['Category'], rotation=45, ha='right', rotation_mode='anchor')

# Set y axis range and ticks
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
if max_total_value > 1000:
    max_total_value = np.ceil(max_total_value / 1000) * 1000
elif max_total_value > 100:
    max_total_value = np.ceil(max_total_value / 100) * 100
else:
    max_total_value = np.ceil(max_total_value / 10) * 10

ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set legend
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Set title
plt.title('Social Media and the Web Post and Video Statistics')

# Automatically resize the image
plt.tight_layout()

# Save figure
plt.savefig('output/final/area_chart/png/20231228-131755_81.png', bbox_inches='tight')

# Clear the current image state
plt.clf()
plt.close()