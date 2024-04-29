

# 20231228-124154_32.png
import pandas as pd
import matplotlib.pyplot as plt

# Preprocess data
data = {'Topic': ['Intellectual Property', 'Employment Law', 'Criminal Law', 'Contract Law', 'Tax Law'],
        'Number of Lawsuits': [100, 200, 150, 125, 75],
        'Number of Legal Advisers': [25, 50, 75, 100, 50],
        'Number of Legal Documents': [500, 1000, 750, 650, 400],
        'Number of Court Cases': [450, 900, 600, 500, 300],
        'Number of Lawyers': [300, 600, 500, 400, 200]}

df = pd.DataFrame(data)
df.set_index('Topic', inplace=True)

# Plot heatmap
fig, ax = plt.subplots(figsize=(10, 8))
heatmap = ax.pcolor(df, cmap='OrRd')

# Set ticks and tick labels
ax.set_xticks([x + 0.5 for x in range(len(df.columns))])
ax.set_yticks([y + 0.5 for y in range(len(df.index))])
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df.index, rotation=0, ha='right', rotation_mode='anchor', wrap=True)

# Set ticks and tick labels in the center
ax.set_xticks([x + 0.5 for x in range(len(df.columns))], minor=True)
ax.set_yticks([y + 0.5 for y in range(len(df.index))], minor=True)
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor', minor=True)
ax.set_yticklabels(df.index, rotation=0, ha='right', rotation_mode='anchor', wrap=True, minor=True)
ax.tick_params(axis='both', which='both', length=0)

# Set colorbar
plt.colorbar(heatmap)

# Set title
ax.set_title('Legal Activity and Representation')

# Automatically resize and save
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-124154_32.png', bbox_inches='tight')

# Clear image state
plt.clf()