
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Create a dictionary with the given data
data = {'Category': ['Clothing', 'Electronics', 'Home Goods', 'Beauty', 'Grocery', 'Toys', 'Sports'],
        'Total Revenue (in billions)': [100, 150, 80, 50, 200, 60, 70],
        'Online Revenue (in billions)': [30, 80, 40, 20, 50, 30, 40],
        'Traditional Revenue (in billions)': [70, 70, 40, 30, 150, 30, 30],
        'Percentage of Online Revenue': ['30%', '53.3%', '50%', '40%', '25%', '50%', '57.1%'],
        'Percentage of Traditional Revenue': ['70%', '46.7%', '50%', '60%', '75%', '50%', '42.9%']}

# Convert the dictionary into a pandas dataframe
df = pd.DataFrame(data)

# Set the figure size
plt.figure(figsize=(12, 8))

# Plot the heatmap chart using seaborn
sns.heatmap(df[['Total Revenue (in billions)', 'Online Revenue (in billions)', 'Traditional Revenue (in billions)']], annot=True, fmt='.0f', cbar=False)

# Set the x and y ticks
plt.xticks(np.arange(3), labels=['Total Revenue', 'Online Revenue', 'Traditional Revenue'], rotation=45, ha='right', rotation_mode='anchor')
plt.yticks(np.arange(len(df)), labels=df['Category'], rotation=0, wrap=True)

# Add title
plt.title('Revenue Breakdown for Retail and E-commerce Categories')

# Automatically resize the image
plt.tight_layout()

# Save the image
plt.savefig('output/final/heatmap/png/20231228-131639_1.png', bbox_inches='tight')

# Clear the current image state
plt.clf()