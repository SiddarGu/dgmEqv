
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Import data
data = {'Category': ['Corporate Law', 'Criminal Law', 'Family Law', 'Intellectual Property Law', 'Environmental Law', 'Personal Injury Law', 'Employment Law', 'Real Estate Law', 'Civil Rights Law'],
        'Number of Lawyers': [100, 150, 50, 75, 25, 100, 75, 50, 25],
        'Number of Cases Filed': [250, 500, 100, 200, 50, 300, 150, 100, 50],
        'Number of Cases Won': [200, 400, 75, 175, 30, 250, 100, 80, 40],
        'Number of Clients': [150, 300, 50, 100, 25, 200, 75, 50, 30],
        'Average Case Duration': ['2.5 years', '5 years', '1 year', '3 years', '2 years', '2 years', '1.5 years', '2 years', '1 year'],
        'Win Rate (%)': ['80%', '70%', '75%', '82%', '60%', '83%', '67%', '80%', '80%']}

# Convert data to dataframe
df = pd.DataFrame(data)

# Set figure size
fig, ax = plt.subplots(figsize=(12, 8))

# Create heatmap chart using seaborn
sns.heatmap(df[['Number of Lawyers', 'Number of Cases Filed', 'Number of Cases Won', 'Number of Clients']].transpose(), annot=True, cmap='Blues', fmt='g', linewidth=0.5, cbar_kws={'label': 'Number of People'})

# Set x and y ticks and tick labels
ax.set_xticks(np.arange(len(df['Category']))+0.5)
ax.set_yticks(np.arange(4)+0.5)
ax.set_xticklabels(df['Category'], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(['Number of Lawyers', 'Number of Cases Filed', 'Number of Cases Won', 'Number of Clients'], rotation=0, ha='center')

# Set title
plt.title('Legal Metrics by Practice Area')

# Automatically resize image before saving
plt.tight_layout()

# Save image
plt.savefig('output/final/heatmap/png/20231228-131639_17.png', bbox_inches='tight')

# Clear current image state
plt.clf()