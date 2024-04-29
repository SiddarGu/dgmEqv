
# Import necessary modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create a dictionary for the data
data = {'Subject': ['Political Science', 'Psychology', 'Economics', 'Sociology', 'History'],
        '2019': [200, 150, 180, 130, 250],
        '2020': [220, 170, 200, 150, 280],
        '2021': [240, 190, 220, 170, 300],
        '2022': [250, 200, 230, 180, 310],
        '2023': [270, 220, 250, 200, 330]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Create area chart using ax.stackplot()
fig, ax = plt.subplots(figsize=(10, 6))
ax.stackplot(df['Subject'], df['2019'], df['2020'], df['2021'], df['2022'], df['2023'], labels=['2019', '2020', '2021', '2022', '2023'], colors=['#ff8c00', '#f4a460', '#ffa07a', '#ff7f50', '#cd5c5c'], alpha=0.8)

# Set x and y axis ticks and ticklabels
ax.set_xticks(np.arange(len(df.index)))
ax.set_xticklabels(df['Subject'], rotation=45, ha='right', rotation_mode='anchor')

# Calculate max total value and set suitable ylim range and yticks
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 100) * 100
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set background grid lines
ax.grid(color='#d3d3d3', linestyle='dashed', linewidth=0.5)

# Set legend and legend position
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Set title and labels
ax.set_title('Student Enrollment in Social Sciences and Humanities')
ax.set_xlabel('Subject')
ax.set_ylabel('Number of Students')

# Automatically resize image and save
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-145339_46.png', bbox_inches='tight')

# Clear current image state
plt.clf()