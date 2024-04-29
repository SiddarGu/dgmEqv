
# Import necessary modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define data as dictionary
data = {'Category': ['0-18 Years', '19-35 Years', '36-50 Years', '51-65 Years', '66+ Years'],
        'Primary Care (Millions)': [20, 25, 30, 35, 40],
        'Specialty Care (Millions)': [10, 15, 20, 25, 30],
        'Emergency Care (Millions)': [5, 8, 10, 15, 20],
        'Mental Health (Millions)': [3, 5, 8, 10, 15],
        'Dental Care (Millions)': [8, 10, 15, 20, 25]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size and probability for ticks and ticklabels
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, len(df.index) - 1)
ax.set_yticks(np.linspace(0, df.iloc[:, 1:].sum(axis=1).max(), np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Calculate max total value and set ylim
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
if max_total_value < 10:
    ax.set_ylim(0, 10)
elif max_total_value < 100:
    ax.set_ylim(0, np.ceil(max_total_value/10) * 10)
elif max_total_value < 1000:
    ax.set_ylim(0, np.ceil(max_total_value/100) * 100)
else:
    ax.set_ylim(0, np.ceil(max_total_value/1000) * 1000)

# Set background grid lines
ax.grid(color='gray', linestyle=':', linewidth=0.5, alpha=0.5)

# Plot area chart
ax.stackplot(df['Category'], df['Primary Care (Millions)'], df['Specialty Care (Millions)'], df['Emergency Care (Millions)'], df['Mental Health (Millions)'], df['Dental Care (Millions)'], labels=['Primary Care', 'Specialty Care', 'Emergency Care', 'Mental Health', 'Dental Care'], colors=['#7199cf', '#4fc4aa', '#e1a7a2', '#e8d174', '#b5a8b1'], alpha=0.8)

# Set legend position and labels
ax.legend(loc='upper right')
ax.yaxis.label.set_text('Cost (Millions)')

# Set x and y labels
ax.set_xlabel('Age Group')
ax.set_ylabel('Healthcare Utilization')

# Set title
ax.set_title('Healthcare Utilization by Age Group')

# Automatically resize image and save
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-131755_59.png', bbox_inches='tight')

# Clear current image state
plt.clf()