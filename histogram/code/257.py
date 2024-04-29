import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

# Data
data = {
    'Crime Type': ['Theft', 'Burglary', 'Fraud', 'Assault', 'Drug-related', 'Homicide', 'Cybercrime', 'Property Damage', 'Vandalism', 'Public Intoxication'],
    'Number of Cases': [890, 700, 450, 550, 480, 150, 350, 300, 220, 190]
}

# Transform the given data into variables
data_labels = ['Crime Type', 'Number of Cases']
line_labels = data['Crime Type']
data_values = data['Number of Cases']

# Create a DataFrame
df = pd.DataFrame(data)

# Create the figure and axis for the histogram
plt.figure(figsize=(14, 10))
ax = plt.subplot()

# Use seaborn to create a vertical histogram
sns.barplot(x='Crime Type', y='Number of Cases', data=df, ax=ax)

# Set plot title and labels
ax.set_title('Annual Crime Case Distribution by Type')

# Add the background grid
ax.grid(True)

# Rotate the x-axis labels to prevent overlapping
plt.xticks(rotation=45, ha='right')

# Adjust subplots to fit figure area
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/demo/histogram/png/607.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)
plt.savefig(save_path)

# Clear the current figure
plt.clf()
