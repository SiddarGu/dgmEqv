
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Import data
data = {'Country':['United States','China','Russia','Japan','Germany','India'],
        'Nuclear Energy (TWh)':[800,600,450,300,400,350],
        'Hydro Energy (TWh)':[1050,900,700,500,600,550],
        'Wind Energy (TWh)':[950,800,500,400,500,450],
        'Solar Energy (TWh)':[500,300,200,150,200,150],
        'Geothermal Energy (TWh)':[150,100,75,50,75,50],
        'Biomass Energy (TWh)':[200,150,100,75,100,75]}

# Convert data into dataframe
df = pd.DataFrame(data)

# Set index as Country
df = df.set_index('Country')

# Set figure size
fig, ax = plt.subplots(figsize=(10,7))

# Plot heatmap
heatmap = sns.heatmap(df, annot=True, linewidths=.5, cmap='Blues', fmt='g')

# Set tick labels for x and y axis
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df.index, rotation=0, ha='center')

# Add title
plt.title('Energy Production by Country')

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig('output/final/heatmap/png/20231228-131639_98.png', bbox_inches='tight')

# Clear current image state
plt.clf()