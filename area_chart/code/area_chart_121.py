
# Import necessary modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define data as dictionary
data = {'Category': ['Children', 'Teenagers', 'Adults', 'Elderly'],
        'Average Age (Years)': [10, 15, 25, 70],
        'Average BMI (kg/m2)': [15, 20, 25, 30],
        'Average Blood Pressure (mmHg)': [100, 110, 120, 130],
        'Average Cholesterol (mg/dL)': [150, 170, 180, 190],
        'Average Blood Sugar (mg/dL)': [50, 60, 70, 80]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Create figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Stackplot the data
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1:].T,
             labels=df.iloc[:, 1:].columns,
             colors=['#E3D9FF', '#BFA6FF', '#8C73FF', '#5C3BFF', '#4019FF'],
             alpha=0.9)

# Set background grid lines
ax.grid(axis='y', linestyle='-', color='#EEEEEE')

# Set x and y axis ticks and ticklabels
# if np.random.random() > 0.3:
ax.set_xticks(np.arange(len(df.iloc[:, 0])))
ax.set_xticklabels(df.iloc[:, 0])
# else:
#     ax.set_xticks([])
#     ax.set_xticklabels([])

# if np.random.random() > 0.3:
# max_total_value = df.iloc[:, 1:].sum(axis=1).max()
# max_total_value = np.ceil(max_total_value/10) * 10

# ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
# ax.set_yticklabels(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
# else:
#     ax.set_yticks([])
#     ax.set_yticklabels([])

# Set axis limits
ax.set_xlim(0, len(df.iloc[:, 0]) - 1)

# Set legend
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1), frameon=False)

# Set title
ax.set_title('Health Statistics by Age Group')

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig('output/final/area_chart/png/20231228-140159_32.png', bbox_inches='tight')

# Clear current image state
plt.clf()