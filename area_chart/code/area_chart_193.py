
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data as a dictionary
data = {'Category': ['Elementary School', 'Middle School', 'High School', 'Undergraduate', 'Graduate', 'Doctorate'],
        'Science (Students)': [200, 150, 100, 200, 150, 180],
        'Arts (Students)': [150, 180, 200, 180, 200, 150],
        'Mathematics (Students)': [180, 200, 250, 150, 100, 100],
        'History (Students)': [130, 150, 180, 130, 250, 200],
        'Language (Students)': [250, 250, 150, 100, 120, 170],
        'Music (Students)': [100, 120, 130, 150, 180, 120]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Create figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Set background grid lines
ax.grid(color='#D3D3D3', linestyle='-', linewidth=0.5, alpha=0.5)

# Plot data as stacked area chart
ax.stackplot(df['Category'], df.iloc[:, 1:], labels=df.columns[1:], colors=['#0B7C83', '#FBAF00', '#E03B8B', '#BCA0DC', '#F5A521', '#6C6C6C'],
             alpha=0.8)

# Set x and y axis ticks and ticklabels
if np.random.randint(0, 100) < 70:
    ax.set_xlim(0, len(df.index) - 1)
    ax.set_xticks(np.arange(0, len(df.index)))
    ax.set_xticklabels(df['Category'], fontsize=12, rotation=45, ha='right', rotation_mode='anchor')

    # Calculate and set y axis tick values
    max_total_value = df.iloc[:, 1:].sum(axis=1).max()
    if max_total_value < 10:
        max_total_value = 10
    elif max_total_value < 100:
        max_total_value = np.ceil(max_total_value / 10) * 10
    elif max_total_value < 1000:
        max_total_value = np.ceil(max_total_value / 100) * 100
    else:
        max_total_value = np.ceil(max_total_value / 1000) * 1000
    ax.set_ylim(0, max_total_value)
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
    ax.set_yticklabels(list(map(str, np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))), fontsize=12)

# Set legend and title
ax.legend(loc='upper left')
ax.set_title('Student Enrollment across Education Levels', fontsize=16)

# Automatically resize the image
fig.tight_layout()

# Save and clear the figure
plt.savefig('output/final/area_chart/png/20231228-145339_26.png', bbox_inches='tight')
plt.clf()