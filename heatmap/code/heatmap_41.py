
# Import necessary modules 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Define data 
data = {'Organization': ['Charity A', 'Charity B', 'Charity C', 'Charity D', 'Charity E'], 
        'Total Donations (in millions)': [25, 50, 20, 40, 30], 
        'Donor Retention Rate (%)': [80, 75, 90, 70, 85], 
        'Volunteer Participation (%)': [50, 40, 60, 45, 55], 
        'Impact Score': [90, 85, 95, 80, 88], 
        'Transparency Score': [85, 80, 90, 75, 83]}

# Convert data to dataframe 
df = pd.DataFrame(data)

# Set figure size 
plt.figure(figsize=(10,6))

# Plot heatmap chart 
ax = sns.heatmap(df.set_index('Organization'), annot=True, cmap='Blues', cbar=True)

# Set ticks and labels for x and y axis 
plt.xticks(np.arange(5)+0.5, df.columns[1:], rotation=45, ha='right', rotation_mode='anchor')
plt.yticks(np.arange(5)+0.5, df['Organization'], rotation=0)

# Set ticklabels in the center of rows and columns 
# ax.set_xticklabels(df['Organization'], ha='center')
ax.set_yticklabels(df['Organization'], va='center')

# Set title 
plt.title('Charity Performance Metrics')

# Resize image and save figure 
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-124154_26.png', bbox_inches='tight')

# Clear current image state 
plt.clf()