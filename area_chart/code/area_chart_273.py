


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create dictionary with data
data = {'Measurement': ['Nurse', 'Doctor', 'Surgeon', 'Therapist', 'Technician', 'Administrator', 'Assistant', 'Pharmacist', 'Dentist', 'Nutritionist', 'Radiologist', 'Optometrist', 'Chiropractor'], 'Healthcare Professionals (Total)': [400, 300, 200, 100, 50, 75, 100, 150, 75, 50, 100, 50, 50], 'Healthcare Professionals (Male)': [200, 150, 100, 50, 25, 30, 50, 75, 40, 25, 50, 25, 25], 'Healthcare Professionals (Female)': [200, 150, 100, 50, 25, 45, 50, 75, 35, 25, 50, 25, 25]}

# Process data using pandas
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
plt.figure(figsize=(10, 6))

# Calculate max total value
max_total_value = np.ceil(df.iloc[:, 1:].sum(axis=1).max() / 10) * 10

# Set x and y axis limits
plt.xlim(0, len(df.index) - 1)
plt.ylim(0, max_total_value)

# Set random background grid lines
plt.grid(alpha=0.3)

# Set x and y axis ticks and ticklabels
if np.random.rand() > 0.3:
    plt.xticks(np.arange(len(df.index)), df['Measurement'], rotation=45, ha='right', rotation_mode='anchor')
else:
    plt.xticks(np.arange(len(df.index)), df['Measurement'])
if np.random.rand() > 0.3:
    plt.yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
else:
    plt.yticks(np.linspace(0, max_total_value, 5, dtype=np.int32))

# Plot stacked area chart
ax = plt.stackplot(df['Measurement'], df['Healthcare Professionals (Total)'], df['Healthcare Professionals (Male)'], df['Healthcare Professionals (Female)'], colors=['#0072BD', '#D95319', '#EDB120'], alpha=0.7)

# Set legend
plt.legend(ax, ['Total', 'Male', 'Female'], loc='lower left')

# Set title
plt.title('Distribution of Healthcare Professionals by Gender')

# Automatically resize and save image
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-155112_37.png', bbox_inches='tight')

# Clear image state
plt.clf() 