
# python code
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Data processing with dict and pandas
data = {'Company Name': ['CompanyA', 'CompanyB', 'CompanyC', 'CompanyD', 'CompanyE', 'CompanyF'],
        'Total Production (Units)': [200, 300, 400, 500, 600, 700],
        'Waste Generated (Kilograms)': [100, 150, 200, 250, 300, 350],
        'Energy Consumption (Megawatts)': [400, 500, 600, 700, 800, 900],
        'Material Usage (Tons)': [50, 75, 100, 125, 150, 175],
        'Labor Costs (Dollars)': [5000, 6000, 7000, 8000, 9000, 10000],
        'Emissions (Kilograms)': [200, 250, 300, 350, 400, 450]}

df = pd.DataFrame(data)
df = df.set_index('Company Name')

# Create the heatmap chart
fig, ax = plt.subplots(figsize=(12, 8))
heatmap = sns.heatmap(df, annot=True, cmap='Blues', linewidths=.5, ax=ax, cbar=False)

# Set ticks and ticklabels
ax.set_xticks(np.arange(0.5, len(df.columns), 1))
ax.set_yticks(np.arange(0.5, len(df.index), 1))
ax.set_xticklabels(df.columns, rotation=45, rotation_mode='anchor', ha='right')
ax.set_yticklabels(df.index, ha='center')

# Set title and labels
ax.set_title('Environmental Impact of Manufacturing Companies')
ax.set_xlabel('Company Metrics')
ax.set_ylabel('Company Name')

# Automatically resize and save the figure
fig.tight_layout()
fig.savefig('output/final/heatmap/png/20231228-134212_73.png', bbox_inches='tight')

# Clear the current image state
plt.clf()