
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create dictionary for data
data = {
    'Category': ['Patients with Chronic Conditions', 'Emergency Visits', 'Mental Health Services', 'Primary Care Visits', 'Inpatient Admissions', 'Specialty Care Visits', 'Preventive Care Visits'],
    'Number of Patients': [500, 200, 100, 300, 50, 250, 150],
    'Medication Administered': [200, 150, 50, 100, 100, 150, 50],
    'Medical Tests': [400, 150, 100, 200, 50, 150, 100],
    'Medical Procedures': [300, 100, 150, 150, 200, 200, 50],
    'Health Education': [100, 50, 50, 50, 100, 100, 200]
}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size to prevent content from being cut off
fig, ax = plt.subplots(figsize=(15, 8))

# Set x and y ticks and ticklabels with 70% probability
if np.random.randint(10) < 7:
    ax.set_xticks(np.arange(len(df.index)))
    ax.set_xticklabels(df.iloc[:, 0], rotation=45, ha='right', rotation_mode='anchor')
if np.random.randint(10) < 7:
    max_total_value = df.iloc[:, 1:].sum(axis=1).max()
    max_total_value = np.ceil(max_total_value / 100) * 100
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set background grid lines
plt.grid(axis='y', linestyle='--')

# Plot the data with area chart
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], df.iloc[:, 5], labels=['Number of Patients', 'Medication Administered', 'Medical Tests', 'Medical Procedures', 'Health Education'])

# Set legend position
plt.legend(loc='upper left')

# Set title and labels
plt.title('Healthcare Services Utilization by Category')
plt.xlabel('Category')
plt.ylabel('Number')

# Automatically resize the image
plt.tight_layout()

# Save figure as png
plt.savefig('output/final/area_chart/png/20231226-130527_4.png', bbox_inches='tight')

# Clear current image state
plt.clf()