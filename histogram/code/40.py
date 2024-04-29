import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Given data
data_labels = ['Cargo Volume (Million metric tons)', 'Number of Carriers']
line_labels = ['1-5', '5-10', '10-15', '15-20', '20-25', '25-30', '30-35', '35-40', '40-45', '45-50']
data = [25, 20, 15, 12, 8, 6, 4, 2, 1, 1]

# Transform the data into a DataFrame
df = pd.DataFrame(list(zip(line_labels, data)), columns=data_labels)

# Create a figure and a single subplot
plt.figure(figsize=(12, 8))
ax = plt.subplot()

# Seaborn barplot to create a histogram
sns.barplot(x='Cargo Volume (Million metric tons)', y='Number of Carriers', data=df, ax=ax)

# Set the title
ax.set_title('Cargo Volume Handled by Transport and Logistics Carriers')

# Set the x labels to rotate for better readability
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode='anchor', wrap=True)

# Use tight_layout to automatically adjust subplot params to give specified padding
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/40.png'
plt.savefig(save_path, format='png')

# Clear the current figure state to prevent overlap with any future plots
plt.clf()
