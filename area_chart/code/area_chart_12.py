
# Import necessary modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set data as dictionary
data = {'Gender': ['Male', 'Female', 'Other'], 'Total Visits': [350, 450, 20], 'New Patients': [150, 200, 10], 'Follow-up Visits': [200, 250, 10]}

# Convert dictionary to dataframe
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(10, 6))

# Set background grid lines
ax.grid(color='lightgrey', linestyle='--', linewidth=1, alpha=0.5)

# Set area chart
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], labels=['Total Visits', 'New Patients', 'Follow-up Visits'], colors=['#98C1D9', '#E0FBFC', '#EE6C4D'], alpha=0.8)

# Set legend and position
ax.legend(loc='upper left')

# Set ticks and ticklabels for x axis
ax.set_xticks(np.arange(len(df.index)))
ax.set_xticklabels(df.iloc[:, 0])

# Set rotation for x axis
plt.setp(ax.get_xticklabels(), ha='right', rotation=45, rotation_mode='anchor')

# Set ticks and ticklabels for y axis
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value/100) * 100
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set title
plt.title('Patient Demographics and Visits by Gender')

# Set y label
plt.ylabel('Visits')

# Set x label
plt.xlabel('Gender')

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig('output/final/area_chart/png/20231226-103019_20.png', bbox_inches='tight')

# Clear the current image state
plt.clf()