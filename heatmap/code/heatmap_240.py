
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Define data in dictionary form
data = {'Platform': ['Facebook', 'Instagram', 'Twitter', 'LinkedIn', 'Snapchat'],
        'Monthly Active Users (in millions)': [2, 1, 0.5, 0.3, 0.2],
        'Time Spent Per Day (in minutes)': [600, 450, 300, 250, 200],
        'Posts Per Minute': [4, 6, 8, 3, 10],
        'Engagement Rate (%)': ['70%', '80%', '75%', '60%', '85%'],
        'Daily Active Users (in millions)': [1.8, 1.2, 0.8, 0.5, 0.4],
        'Monthly Visitors (in millions)': [2.5, 1.8, 1, 0.9, 0.7]}

# Convert dictionary to pandas dataframe
df = pd.DataFrame(data)

# Set figure size
plt.figure(figsize=(12, 8))

# Use seaborn heatmap to plot the data
sns.heatmap(df[['Monthly Active Users (in millions)', 'Time Spent Per Day (in minutes)', 'Posts Per Minute', 'Daily Active Users (in millions)', 'Monthly Visitors (in millions)']].astype(float), annot=True, cmap='Blues')

# Set x and y labels, ticks and ticklabels
plt.xlabel('Metrics')
plt.ylabel('Social Media Platforms')
plt.xticks(np.arange(5) + 0.5, df['Platform'])
plt.yticks(np.arange(5) + 0.5, df['Platform'], rotation=45, ha='right', rotation_mode='anchor')

# Set title
plt.title('Social Media and Web Usage Statistics')

# Automatically resize the image
plt.tight_layout()

# Save figure
plt.savefig('output/final/heatmap/png/20231228-155147_35.png', bbox_inches='tight')

# Clear current image state
plt.clf()