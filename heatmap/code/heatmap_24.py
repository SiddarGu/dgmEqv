
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Define the data
data = {'Location': ['New York City', 'Los Angeles', 'Chicago', 'Dallas', 'San Francisco', 'Miami'],
        'Median Home Price ($)': [1200000, 900000, 650000, 500000, 1500000, 800000],
        'Average Rent ($)': [2500, 2200, 1800, 1500, 3000, 2000],
        'Vacancy Rate (%)': [5, 5, 4, 3, 6, 6],
        'Median Household Income ($)': [65000, 60000, 55000, 50000, 75000, 55000]}

# Convert the data to a pandas dataframe
df = pd.DataFrame(data)

# Set the figure size
plt.figure(figsize=(10, 8))

# Create a heatmap using seaborn
ax = sns.heatmap(df.drop('Location', axis=1), annot=True, cmap='Blues')

# Set the ticks and ticklabels for both x and y axis
ax.set_xticklabels(df.columns[1:], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df['Location'], rotation=0)

# Set the title of the figure
ax.set_title('Housing Market Trends in Major Cities')

# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig('output/final/heatmap/png/20231226-140552_3.png', bbox_inches='tight')

# Clear the current image state
plt.clf()