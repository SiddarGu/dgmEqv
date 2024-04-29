
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create dictionary of data
data = {'Category': ['2019', '2020', '2021', '2022', '2023'], 'Executive (Employees)': [50, 55, 60, 65, 70], 'Senior Management (Employees)': [100, 110, 120, 130, 140], 'Middle Management (Employees)': [200, 210, 220, 230, 240], 'Junior Management (Employees)': [300, 310, 320, 330, 340], 'Frontline Staff (Employees)': [400, 425, 450, 475, 500]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size and probability of setting ticks and ticklabels
fig, ax = plt.subplots(figsize=(9, 6))
prob = np.random.choice([True, False], p=[0.7, 0.3])

# Plot the data with area chart
ax.stackplot(df['Category'], df['Executive (Employees)'], df['Senior Management (Employees)'], df['Middle Management (Employees)'], df['Junior Management (Employees)'], df['Frontline Staff (Employees)'], colors=['#7AB4C9', '#E9CD8E', '#F4A6A6', '#C9E9B5', '#B5E1E6'], alpha=0.8)
ax.set_title('Employee Distribution by Seniority from 2019 to 2023')

# Set ticks and ticklabels for x axis
ax.set_xlim(0, len(df.index) - 1)
if prob:
    ax.set_xticks(np.arange(len(df['Category'])))
    if len(df['Category'][0]) > 6:
        ax.set_xticklabels(df['Category'], rotation=45, ha='right', rotation_mode='anchor')
    else:
        ax.set_xticklabels(df['Category'])
else:
    ax.set_xticklabels([])

# Calculate and set suitable ylime range and yticks
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
if max_total_value < 10:
    max_total_value = 10
elif max_total_value < 100:
    max_total_value = np.ceil(max_total_value / 10) * 10
elif max_total_value < 1000:
    max_total_value = np.ceil(max_total_value / 100) * 100
else:
    max_total_value = np.ceil(max_total_value / 1000) * 1000
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set ticks and ticklabels for y axis
if prob:
    ax.set_ylabel('Number of Employees')
else:
    ax.set_yticklabels([])
    
# Add background grid lines
ax.grid(linestyle='--')

# Add legend and adjust its position
leg = ax.legend(['Executive', 'Senior Management', 'Middle Management', 'Junior Management', 'Frontline Staff'], loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=5)

# Automatically resize image and save
fig.tight_layout()
plt.savefig('output/final/area_chart/png/20231226-103019_11.png', bbox_inches='tight')

# Clear image state
plt.clf()