







# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Set data as a dictionary
data = {'Category': ['History', 'Sociology', 'Psychology', 'Economics', 'Political Science', 'Education', 'Anthropology', 'Communications'],
        'Number of Publications': [500, 700, 800, 1000, 600, 900, 400, 300],
        'Number of Citations': [15000, 25000, 30000, 35000, 20000, 40000, 10000, 7500],
        'Number of Authors': [800, 1000, 1200, 1500, 900, 1400, 600, 500],
        'Number of Collaborations': [2000, 3000, 3500, 4000, 2500, 3750, 1500, 1250],
        'Number of Journals': [40, 45, 50, 55, 42.5, 52.5, 35, 30]}

# Convert data to pandas dataframe
df = pd.DataFrame(data)

# Set figure size
plt.figure(figsize=(10, 8))

# Plot heatmap chart using pcolor
plt.pcolor(df[['Number of Publications', 'Number of Citations', 'Number of Authors', 'Number of Collaborations', 'Number of Journals']], cmap='YlOrRd')

# Set x and y ticks and labels
plt.xticks(np.arange(len(['Number of Publications', 'Number of Citations', 'Number of Authors', 'Number of Collaborations', 'Number of Journals'])) + 0.5, ['Number of Publications', 'Number of Citations', 'Number of Authors', 'Number of Collaborations', 'Number of Journals'], rotation=45, ha='right', rotation_mode='anchor')
plt.yticks(np.arange(len(data['Category'])) + 0.5, data['Category'])

# Add colorbar
cb = plt.colorbar()
cb.ax.tick_params(labelsize=12)

# Add values to each cell if no colorbar
if np.random.choice([True, False], p=[0.4, 0.6]):
    for y in range(len(data['Category'])):
        for x in range(len(data['Category'])):
            plt.text(x+0.5, y+0.5, f"{data['Number of Journals'][y]}", ha='center', va='center', color='black', fontsize=12)

# Set title
plt.title("Research Trends in Social Sciences and Humanities", fontsize=16)

# Automatically resize image and save figure
plt.tight_layout()
plt.savefig("output/final/heatmap/png/20231228-134212_42.png", bbox_inches='tight')

# Clear current image state
plt.clf()