

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Process the data
data = {'Category': ['Patient Satisfaction', 'Quality of Care', 'Cost Efficiency'],
        'Hospital': [85, 90, 85],
        'Clinic': [90, 92, 90],
        'Pharmacy': [95, 88, 95],
        'Lab': [88, 90, 90],
        'Insurance Company': [90, 95, 90],
        'Physician': [92, 98, 88]}

df = pd.DataFrame(data)
df = df.set_index('Category')

# Plot the chart
fig, ax = plt.subplots(figsize=(10, 6))
heatmap = sns.heatmap(df, annot=True, cmap='Blues', cbar=False)

# Set the ticks and ticklabels
ax.set_xticks([0.5, 1.5, 2.5, 3.5, 4.5, 5.5])
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticks([0.5, 1.5, 2.5])
ax.set_yticklabels(df.index, rotation=0)

# Set the ticks and ticklabels in the center
ax.set_xticklabels(df.columns, rotation=45, ha='center', rotation_mode='anchor')
ax.set_yticklabels(df.index, rotation=0, va='center')

# Set the title
ax.set_title('Healthcare Performance Comparison')

# Automatically resize the image
plt.tight_layout()

# Save the image
plt.savefig('output/final/heatmap/png/20231228-124154_65.png', bbox_inches='tight')

# Clear the image state
plt.clf()