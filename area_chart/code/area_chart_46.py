
# Import modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define data
data = {'Category': ['Advertising', 'Influencers', 'Branding', 'Customer Service', 'Analytics', 'Content Creation', 'E-commerce', 'Events', 'Public Relations', 'Recruitment', 'Sales', 'Social Listening', 'User Engagement'],
        'Facebook (Posts)': [100, 200, 150, 200, 130, 180, 150, 180, 130, 250, 120, 180, 150],
        'Instagram (Posts)': [150, 180, 200, 180, 100, 120, 180, 150, 100, 130, 100, 200, 180],
        'Twitter (Posts)': [120, 250, 100, 120, 150, 200, 130, 100, 150, 100, 200, 150, 130],
        'LinkedIn (Posts)': [200, 150, 180, 150, 200, 150, 200, 200, 180, 200, 180, 100, 200],
        'YouTube (Posts)': [250, 120, 130, 250, 180, 130, 100, 170, 200, 150, 150, 250, 100]}

# Convert data to dataframe
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(12, 8))

# Calculate max total value
max_total_value = df.iloc[:, 1:].sum(axis=1).max()

# Set y limits and ticks
ax.set_ylim(0, np.ceil(max_total_value / 100) * 100)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Plot area chart
ax.stackplot(df['Category'], df.iloc[:, 1:].T, labels=df.columns[1:], colors=['#F8766D', '#7CAE00', '#00BFC4', '#C77CFF', '#619CFF'], alpha=0.7)

# Set grid lines
ax.grid(linestyle='--', alpha=0.5)

# Set legend
ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1))

# Set x and y labels
ax.set_xlabel('Category')
ax.set_ylabel('Posts')

# Set x ticks and tick labels
ax.set_xticks(np.arange(len(df.index)))
ax.set_xticklabels(df['Category'], rotation=45, ha='right', rotation_mode='anchor')

# Set title
ax.set_title('Social Media and the Web Usage by Category')

# Automatically adjust spacing
fig.tight_layout()

# Save figure
fig.savefig('output/final/area_chart/png/20231228-131755_2.png', bbox_inches='tight')

# Clear current image state
plt.clf()