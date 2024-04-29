
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data as dictionary
data = {'Category': ['Clothing', 'Electronics', 'Beauty & Personal Care', 'Home & Garden', 'Sports & Fitness', 'Health & Wellness', 'Toys & Games', 'Food & Beverage', 'Automotive', 'Travel & Tourism', 'Entertainment', 'Other'], 'E-commerce Sales ($)': [10000, 8000, 5000, 6000, 4000, 3000, 3500, 4500, 2500, 3000, 2000, 1500], 'Retail Sales ($)': [8000, 7000, 6000, 5000, 3500, 4500, 3000, 4000, 3000, 2500, 3000, 2000]}

# Process data using pandas
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Plot the data as an area chart
fig, ax = plt.subplots(figsize=(10, 6)) # Set figure size

# Set background grid lines
ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

# Set x and y axis ticks and ticklabels
# if np.random.choice([0, 1], p=[0.3, 0.7]): # 70% probability of setting ticks and ticklabels
#     ax.set_xlim(0, len(df.index) - 1) # Set x axis limit
#     ax.set_yticks(np.linspace(0, df.iloc[:, 1:].sum(axis=1).max(), np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)) # Set y axis ticks
#     ax.set_yticklabels(np.linspace(0, df.iloc[:, 1:].sum(axis=1).max(), np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)) # Set y axis ticklabels

# Set suitable colors and transparency
colors = ['#8dd3c7', '#ffffb3'] # Set colors
alpha = 0.8 # Set transparency

# Plot the data
ax.stackplot(df['Category'], df['E-commerce Sales ($)'], df['Retail Sales ($)'], labels=df.columns[1:], colors=colors, alpha=alpha)

# Set legend
ax.legend(loc='upper left', bbox_to_anchor=(1, 1)) # Adjust position of legend to avoid overlapping

# Set title
ax.set_title('Revenue Comparison between E-commerce and Retail Sales in Various Categories', fontsize=14)
plt.xticks(rotation=45, ha='right', rotation_mode='anchor')
# Automatically resize image
fig.tight_layout()

# Save the chart as a png file
fig.savefig('output/final/area_chart/png/20231228-140159_99.png', bbox_inches='tight')

# Clear current image state
plt.clf()