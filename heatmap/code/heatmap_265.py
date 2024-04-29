
# Generate the data
policy_area = ['Education', 'Healthcare', 'Transportation', 'Energy', 'Environment']
education_spending = [100, 120, 90, 80, 70]
healthcare_spending = [200, 180, 210, 230, 240]
transportation_funding = [150, 160, 170, 180, 190]
energy_budget = [50, 60, 70, 80, 90]
environmental_initiatives = [40, 50, 60, 70, 80]

# Create a dictionary using the data
data = {'Policy Area': policy_area,
        'Education Spending ($)': education_spending,
        'Healthcare Spending ($)': healthcare_spending,
        'Transportation Funding ($)': transportation_funding,
        'Energy Budget ($)': energy_budget,
        'Environmental Initiatives ($)': environmental_initiatives}

# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Convert the dictionary to a dataframe
df = pd.DataFrame(data)

# Set the figure size
plt.figure(figsize=(8,8))

# Plot the heatmap using seaborn
ax = sns.heatmap(data=df.set_index('Policy Area'), annot=True, cmap='Blues', fmt='g')

# Set the x and y ticks and ticklabels to be centered
ax.set_xticks(np.arange(0.5, 5.5, 1))
ax.set_yticks(np.arange(0.5, 5.5, 1))
ax.set_xticklabels(df.columns[1:], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df['Policy Area'], rotation=0, ha='center')

# Add a colorbar
cbar = ax.collections[0].colorbar
cbar.set_ticks(np.arange(0, 250, 50))
cbar.set_ticklabels(['0', '50', '100', '150', '200'])

# Set the title
ax.set_title('Government Spending by Policy Area')

# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig('output/final/heatmap/png/20231228-162116_19.png', bbox_inches='tight')

# Clear the current image state
plt.clf()