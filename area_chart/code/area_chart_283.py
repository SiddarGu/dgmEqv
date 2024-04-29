
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define data as dictionary
data = {
    'Research Area': ['Biology', 'Chemistry', 'Physics', 'Computer Science', 'Engineering', 'Mathematics', 'Environmental Science', 'Materials Science', 'Geology'],
    'Grants Awarded': [50, 100, 150, 200, 250, 300, 350, 400, 450],
    'Publications': [100, 200, 300, 400, 500, 600, 700, 800, 900],
    'Patents': [10, 20, 30, 40, 50, 60, 70, 80, 90],
    'Citations': [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500]
}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(12, 8))

# Plot area chart
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], labels=['Grants Awarded', 'Publications', 'Patents', 'Citations'], colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'], alpha=0.8)

# Set x and y tick labels
ax.set_xticks(range(len(df.index)))
ax.set_xticklabels(df.iloc[:, 0], rotation=45, ha='right', rotation_mode='anchor')
ax.set_xlim(0, len(df.index) - 1)

# Calculate max total value and set y tick labels
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
if max_total_value < 10:
    yticks = np.linspace(0, max_total_value, 3, dtype=np.int32)
elif max_total_value < 100:
    yticks = np.linspace(0, max_total_value, np.random.choice([3, 5]), dtype=np.int32)
elif max_total_value < 1000:
    yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7]), dtype=np.int32)
else:
    yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
ax.set_yticks(yticks)

# Set grid lines
ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

# Set legend
ax.legend(loc='upper left')

# Set title
ax.set_title('Scientific Achievement in Various Fields')

# Automatically resize image
plt.tight_layout()

# Save and show plot
plt.savefig('output/final/area_chart/png/20231228-155112_51.png', bbox_inches='tight')
plt.show()

# Clear current image state
plt.clf()