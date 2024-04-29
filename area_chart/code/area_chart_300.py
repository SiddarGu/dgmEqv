
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create dictionary from data
data = {'Field': ['Astronomy', 'Geology', 'Ecology', 'Mathematics', 'Materials Science', 'Mechanical Engineering', 'Electrical Engineering', 'Computer Engineering', 'Biology', 'Physics', 'Chemistry', 'Environmental Science', 'Data Science'],
        'Physics (Publications)': [100, 70, 90, 120, 80, 110, 100, 90, 100, 110, 120, 90, 100],
        'Chemistry (Publications)': [80, 100, 120, 90, 110, 100, 120, 110, 90, 100, 110, 120, 100],
        'Biology (Publications)': [120, 150, 100, 80, 90, 110, 100, 120, 110, 90, 100, 110, 120],
        'Computer Science (Publications)': [90, 80, 70, 100, 120, 90, 110, 100, 120, 110, 90, 100, 110]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(10, 6))

# Set background grid lines
ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

# Plot the data with type of area chart
ax.stackplot(df['Field'], df['Physics (Publications)'], df['Chemistry (Publications)'], df['Biology (Publications)'], df['Computer Science (Publications)'], labels=['Physics', 'Chemistry', 'Biology', 'Computer Science'], colors=['#FFBF00', '#0080FF', '#00FF00', '#FF0000'], alpha=0.7)

# Set x and y axis ticks and ticklabels
ax.set_xlim(0, len(df.index) - 1)
ax.set_ylim(0, np.ceil(df.iloc[:, 1:].sum(axis=1).max() / 10) * 10)
ax.set_xticks(np.arange(0, len(df.index)))
ax.set_xticklabels(df['Field'], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticks(np.linspace(0, df.iloc[:, 1:].sum(axis=1).max(), np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set legend
ax.legend(loc='upper left', ncol=2)

# Automatically resize the image
plt.tight_layout()

# Add title and axis labels
plt.title('Publications in Science and Engineering Fields')
plt.xlabel('Fields')
plt.ylabel('Publications')

# Save the image
plt.savefig('output/final/area_chart/png/20231228-161902_9.png', bbox_inches='tight')

# Clear the current image state
plt.clf()