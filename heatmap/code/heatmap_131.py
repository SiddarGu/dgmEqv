
# Solution

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# data processing
data = {'Sector': ['Residential', 'Commercial', 'Industrial', 'Agricultural', 'Transportation', 'Other'],
        'Electricity (GWh)': [1000, 1500, 2000, 500, 500, 250],
        'Natural Gas (Bcf)': [500, 750, 1000, 250, 250, 125],
        'Coal (Million Tons)': [250, 400, 500, 125, 100, 75],
        'Renewables (GWh)': [750, 1000, 1250, 350, 300, 200],
        'Nuclear (GWh)': [1000, 1250, 1500, 500, 500, 250]}

df = pd.DataFrame(data)
df = df.set_index('Sector')

# plot the heatmap chart
fig, ax = plt.subplots(figsize=(10, 8))
heatmap = sns.heatmap(df, annot=True, fmt="d", cmap='YlGnBu', cbar=True, ax=ax)
heatmap.set_title('Energy Consumption by Sector')
heatmap.set_xlabel('Energy Source')
heatmap.set_ylabel('Sector')
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-131639_37.png', bbox_inches='tight')
plt.close()

# clear the current image state
plt.clf()