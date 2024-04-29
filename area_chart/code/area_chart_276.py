
# Import modules
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create dictionary for data
data = {'Unit': ['Dollars ($)', 'Percentage (%)'],
        'Preventative Care': [15000, 30],
        'Primary Care': [20000, 25],
        'Specialty Care': [30000, 15],
        'Inpatient Care': [50000, 20],
        'Outpatient Care': [40000, 10]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(12, 8))

# Set x and y axis ticks and labels
ax.set_xlim(0, len(df.index) - 1)
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 100) * 100
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set background grid lines
ax.grid(color='lightgrey', linestyle='--')

# Plot data as area chart
ax.stackplot(df['Unit'], df['Preventative Care'], df['Primary Care'], df['Specialty Care'], df['Inpatient Care'], df['Outpatient Care'], labels=['Preventative Care', 'Primary Care', 'Specialty Care', 'Inpatient Care', 'Outpatient Care'], colors=['lightblue', 'lightgreen', 'orange', 'lightpink', 'yellow'], alpha=0.7)

# Set legend and position
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Set title
plt.title('Healthcare Spending by Care Type')

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig('output/final/area_chart/png/20231228-155112_4.png', bbox_inches='tight')

# Clear image state
plt.cla()
plt.clf()
plt.close()