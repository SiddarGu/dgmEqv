
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define data
data = {'Category': ['Residential', 'Commercial', 'Industrial', 'Agricultural', 'Public Facilities', 'Transportation', 'Mining', 'Manufacturing', 'Education', 'Healthcare', 'Government', 'Telecommunications', 'Retail', 'Hospitality', 'Energy Production'], 
        'Energy Usage (kWh)': [500, 1000, 2000, 1500, 3000, 2500, 1500, 1000, 2000, 2500, 3000, 2000, 1500, 2500, 2000], 
        'Electricity Cost ($)': [100, 200, 500, 300, 1000, 400, 500, 300, 400, 500, 1000, 400, 300, 500, 1000], 
        'Water Usage (gal)': [2000, 5000, 10000, 8000, 4000, 6000, 10000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000], 
        'Gas Usage (therm)': [100, 300, 1000, 200, 500, 400, 800, 200, 300, 500, 600, 700, 400, 600, 800]}

# Create dataframe
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig = plt.figure(figsize=(12,10))

# Set axes
ax = fig.add_subplot(111)

# Stack plot
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], colors=['#8BC6CC', '#FF7F50', '#9ACD32', '#FFD700'], alpha=0.7)

# Set labels
ax.set_xlabel('Category', fontsize=14)
ax.set_ylabel('Usage/Cost', fontsize=14)
ax.set_title('Energy and Utilities Usage and Cost by Category', fontsize=16)

# Set ticks and ticklabels
ax.set_xlim(0, len(df.index) - 1)
ax.set_xticks(np.arange(len(df.index)))
ax.set_xticklabels(df.iloc[:, 0], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticks(np.linspace(0, np.ceil(df.iloc[:, 1:].sum(axis=1).max()), np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
ax.set_yticklabels(['${}'.format(int(ytick)) for ytick in ax.get_yticks()])

# Add grid lines
ax.grid(linestyle='dashed', color='grey', alpha=0.25)

# Adjust legend position
ax.legend(loc='upper left', bbox_to_anchor=(1.0, 1.0))

# Automatically resize image
fig.tight_layout()

# Save figure
fig.savefig('output/final/area_chart/png/20231228-140159_89.png', bbox_inches='tight')

# Clear current image state
plt.clf()