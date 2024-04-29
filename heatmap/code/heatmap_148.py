
import matplotlib
matplotlib.use('agg')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Process data
data = {
    'Research Area': ['Calculus', 'Structural Engineering', 'Artificial Intelligence', 'Genetics', 'Organic Chemistry', 'Quantum Mechanics'],
    'Mathematics': [30, 10, 50, 5, 5, 40],
    'Civil Engineering': [90, 35, 15, 10, 5, 10],
    'Computer Science': [70, 50, 80, 10, 5, 5],
    'Biology': [20, 5, 10, 40, 20, 5],
    'Chemistry': [10, 20, 5, 50, 80, 10],
    'Physics': [40, 30, 10, 20, 10, 90]
}

df = pd.DataFrame(data)
df.set_index('Research Area', inplace=True)

# Create figure and axes
fig, ax = plt.subplots(figsize=(10, 8))

# Plot heatmap
if np.random.random() < 0.7:
    sns.heatmap(df, annot=True, cmap='Blues', fmt='g', ax=ax) # Use seaborn heatmap
else:
    ax.imshow(df, cmap='Blues') # Use imshow or pcolor

# Set ticks and ticklabels
ax.set_xticks(np.arange(6) + 0.5)
ax.set_yticks(np.arange(6) + 0.5)
ax.set_xticklabels(df.columns, rotation=45, rotation_mode='anchor', ha='right')
ax.set_yticklabels(df.index, rotation=0, rotation_mode='anchor', ha='right')

# Set ticks and ticklabels in the center
ax.tick_params(axis='both', which='both', length=0, width=0, pad=12)
plt.setp(ax.get_xticklabels(), ha='center', wrap=True)
plt.setp(ax.get_yticklabels(), va='center', wrap=True)

# Add colorbar
if np.random.random() < 0.4:
    plt.colorbar()

# Set title
ax.set_title('Interdisciplinary Fields in Science and Engineering')

# Remove extra whitespace
plt.tight_layout()

# Save figure
plt.savefig('output/final/heatmap/png/20231228-131639_67.png', bbox_inches='tight')

# Clear current image state
plt.clf()