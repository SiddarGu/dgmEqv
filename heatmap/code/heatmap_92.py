
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Define data as a dictionary
data = {'Category': ['Clothing', 'Electronics', 'Home Goods', 'Beauty', 'Toys', 'Groceries'],
       'Revenue (in Million)': [100, 150, 50, 70, 40, 200],
       'Profit (in Million)': [20, 30, 10, 15, 8, 40],
       'Sales (in Million)': [80, 120, 40, 50, 30, 160],
       'Customers (in Million)': [10, 15, 5, 8, 4, 20],
       'Average Order Value ($)': [50, 40, 45, 55, 35, 45]}

# Convert data into a pandas dataframe
df = pd.DataFrame(data)

# Set the figure size
plt.figure(figsize=(10,8))

# Create the heatmap using seaborn
sns.heatmap(df.iloc[:,1:], annot=True, cmap='Blues', cbar=False)

# Set ticks and ticklabels for x and y axis
plt.xticks(np.arange(5)+0.5, labels=df.columns[1:], rotation=45, ha='right', rotation_mode='anchor')
plt.yticks(np.arange(6)+0.5, labels=df['Category'], rotation=0, ha='right', rotation_mode='anchor')

# Set title and labels
plt.title('Retail Performance by Category')
plt.xlabel('Metrics')
plt.ylabel('Category')

# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig('output/final/heatmap/png/20231228-124154_89.png', bbox_inches='tight')

# Clear the current image state
plt.clf() 