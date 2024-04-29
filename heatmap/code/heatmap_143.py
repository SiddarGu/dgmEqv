
# Import the necessary modules
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Define the data
data = {'Utility': ['Green Energy Co.', 'Power Solutions Inc.', 'Energy Innovations Ltd.', 'Sustainable Utilities Corp.'],
        'Electricity Usage (kWh)': [500, 700, 600, 550],
        'Natural Gas Usage (m3)': [300, 400, 350, 400],
        'Water Usage (Liters)': [600, 800, 650, 700],
        'Waste Production (kg)': [100, 150, 120, 130],
        'Renewable Energy Usage (%)': [75, 65, 80, 70],
        'Carbon Emissions (tons)': [50, 60, 45, 55]
        }

# Convert the data into a pandas dataframe
df = pd.DataFrame(data)

# Set the utility column as the index
df.set_index('Utility', inplace=True)

# Plot the heatmap chart using seaborn
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(df, annot=True, cmap='Oranges')

# Set the ticks and ticklabels for the x and y axis
ax.set_xticks(np.arange(0.5, len(df.columns), 1))
ax.set_yticks(np.arange(0.5, len(df.index), 1))
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df.index, rotation=0, ha='right', rotation_mode='anchor')

# Set the title
ax.set_title('Energy and Utilities Usage and Impact')

# Automatically resize the image and save it
fig.tight_layout()
fig.savefig('output/final/heatmap/png/20231228-131639_6.png', bbox_inches='tight')

# Clear the current image state
plt.clf()