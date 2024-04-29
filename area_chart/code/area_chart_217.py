
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create dictionary with data
data = {'Category': ['Philosophy', 'History', 'Sociology', 'Political Science', 'Cultural Studies'],
        '2016': [200, 250, 300, 350, 400],
        '2017': [220, 260, 320, 360, 380],
        '2018': [240, 270, 340, 380, 360],
        '2019': [260, 280, 360, 370, 340],
        '2020': [270, 290, 350, 390, 320],
        '2021': [280, 300, 370, 400, 300]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Plot data with area chart
fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(df['Category'], df['2016'], df['2017'], df['2018'], df['2019'], df['2020'], df['2021'], labels=['2016', '2017', '2018', '2019', '2020', '2021'], colors=['#B4D6E5', '#9FC1DC', '#8DB4D1', '#7DA6C6', '#6D98BB', '#5D8AB0'], alpha=0.7)

# Set ticks and ticklabels
if np.random.choice([True, False], p=[0.7, 0.3]):
  ax.set_xticks(df.index)
  ax.set_xticklabels(df['Category'], rotation=45, ha='right', rotation_mode='anchor')
  ax.set_xlim(0, len(df.index) - 1)
  max_total_value = df.iloc[:, 1:].sum(axis=1).max()
  max_total_value = np.ceil(max_total_value / 100) * 100
  ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
  ax.set_yticklabels(ax.get_yticks().astype(int))

# Add grid lines
ax.grid(color='grey', linestyle='-', linewidth=0.5, alpha=0.5)

# Adjust legend position
ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1))

# Add title
ax.set_title('Enrollment Trends in Social Sciences and Humanities')

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig('output/final/area_chart/png/20231228-145339_59.png', bbox_inches='tight')

# Clear current image state
plt.clf()