

# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create data dictionary 
data = {'Platform': ['Facebook', 'Twitter', 'Instagram', 'Pinterest', 'LinkedIn'],
        'Number of Active Users (Millions)': [2600, 850, 1000, 500, 700],
        'User Engagement (Hours per Month)': [5, 4, 6, 5, 3],
        'Daily Visits (Millions)': [400, 300, 350, 200, 250],
        'Total Posts (Millions)': [350, 250, 300, 150, 200],
        'Ad Revenue (Millions)': [100, 75, 80, 50, 60]
       }

# Create pandas dataframe 
df = pd.DataFrame(data)

# Set figure size 
plt.figure(figsize=(10, 8))

# Create heatmap using seaborn 
sns.heatmap(df.iloc[:, 1:], annot=True, cmap='Blues', cbar=False, linewidths=0.5)

# Set x and y ticks and labels 
plt.xticks(ticks=np.arange(5)+0.5, labels=['Number of Active Users (Millions)', 'User Engagement (Hours per Month)', 'Daily Visits (Millions)', 'Total Posts (Millions)', 'Ad Revenue (Millions)'], rotation=45, ha='right', rotation_mode='anchor', wrap=True)
plt.yticks(ticks=np.arange(5)+0.5, labels=['Facebook', 'Twitter', 'Instagram', 'Pinterest', 'LinkedIn'], rotation=0, ha='right', rotation_mode='anchor', wrap=True)

# Set title 
plt.title('Social Media and Web Analytics')

# Automatically resize image and save 
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-155147_53.png', bbox_inches='tight')

# Clear figure 
plt.clf()