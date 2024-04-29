
# Import necessary modules
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Define data as dictionary
data = {'Field': ['Business', 'Engineering', 'Medicine', 'Law', 'Psychology', 'Literature', 'Science', 'History', 'Education', 'Computer Science', 'Art', 'Music', 'Economics', 'Mathematics'], 'Students': [100, 120, 150, 200, 180, 160, 100, 130, 220, 190, 140, 120, 180, 150], 'Graduates': [80, 100, 120, 150, 140, 100, 80, 90, 180, 150, 90, 60, 140, 110], 'Professors': [30, 40, 50, 60, 80, 70, 30, 40, 90, 70, 50, 30, 60, 70]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figsize
fig, ax = plt.subplots(figsize=(10, 6))

# Calculate max total value and set ylimit and yticks
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
if max_total_value < 100:
    ylimit = 10 * np.ceil(max_total_value / 10)
elif max_total_value < 1000:
    ylimit = 100 * np.ceil(max_total_value / 100)
else:
    ylimit = 1000 * np.ceil(max_total_value / 1000)
ax.set_ylim(0, ylimit)
ax.set_yticks(np.linspace(0, ylimit, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Plot area chart
ax.stackplot(df.index, df['Students'], df['Graduates'], df['Professors'], labels=['Students', 'Graduates', 'Professors'], colors=['#4C72B0', '#55A868', '#C44E52'], alpha=0.8)

# Set xticks and xticklabels
ax.set_xlim(0, len(df.index) - 1)
ax.set_xticks(df.index)
ax.set_xticklabels(df['Field'], rotation=45, ha='right', rotation_mode='anchor', wrap=True)

# Set background grid lines
ax.grid(True, ls='--', alpha=0.5)

# Set title and legend
plt.title('Education and Academics Statistics')
ax.legend(loc='upper right')

# Automatically resize image and save
fig.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-131755_92.png', bbox_inches='tight')

# Clear current image state
plt.clf()