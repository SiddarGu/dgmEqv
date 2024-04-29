
# Import necessary modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create the data dictionary
data = {'Year': [2016, 2017, 2018, 2019, 2020],
        'Coal (kWh)': [500, 480, 450, 420, 400],
        'Natural Gas (kWh)': [750, 800, 850, 900, 950],
        'Nuclear (kWh)': [1000, 950, 900, 850, 800],
        'Hydro (kWh)': [1200, 1250, 1300, 1350, 1400],
        'Solar (kWh)': [500, 600, 750, 900, 1050],
        'Wind (kWh)': [300, 350, 400, 450, 500]}

# Convert dictionary to dataframe
df = pd.DataFrame(data)

# Set the index to be the 'Year' column
df.set_index('Year', inplace=True)

# Set the figure size
plt.figure(figsize=(10, 8))

# Plot the heatmap using seaborn
sns.heatmap(df, cmap='YlGnBu')

# Set the tick labels and positions for both axes
plt.xticks(np.arange(6), df.columns, fontsize=12, ha='center', rotation=45, rotation_mode='anchor')
plt.yticks(np.arange(5), df.index, fontsize=12, va='center')

# Add a title to the figure
plt.title('Electricity Generation by Source and Year', fontsize=14)

# Automatically resize the figure and save it
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-134212_83.png', bbox_inches='tight')

# Clear the figure
plt.clf()