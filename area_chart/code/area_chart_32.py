
# Import modules
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create dictionary of data
data = {'Category': ['Primary School', 'Middle School', 'High School', 'College', 'Post-Graduate'],
        'Mathematics (Students)': [120, 150, 180, 200, 220],
        'Science (Students)': [150, 180, 200, 220, 250],
        'Language (Students)': [100, 130, 150, 170, 200],
        'History (Students)': [110, 140, 160, 190, 210],
        'Art (Students)': [130, 160, 180, 200, 220]}

# Process data using pandas
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(10, 8))

# Plot the data with area chart
ax.stackplot(df['Category'], df['Mathematics (Students)'], df['Science (Students)'], df['Language (Students)'], df['History (Students)'], df['Art (Students)'], labels=['Mathematics', 'Science', 'Language', 'History', 'Art'], alpha=0.7, colors=['#C44E52', '#55A868', '#4C72B0', '#8172B2', '#CCB974'])

# Set ticks and ticklabels for x axis
ax.set_xticks(np.arange(len(df.index)))
ax.set_xticklabels(df['Category'], rotation=45, ha='right', rotation_mode='anchor')

# Set ticks and ticklabels for y axis
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 100) * 100
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set grid lines
ax.grid(linestyle='--', alpha=0.3)

# Set legend
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1))

# Set title
ax.set_title('Student Enrollment by Education Level and Subject')

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig('output/final/area_chart/png/20231226-130527_17.png', bbox_inches='tight')

# Clear image state
plt.clf()