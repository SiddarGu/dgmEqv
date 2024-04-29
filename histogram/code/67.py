import matplotlib.pyplot as plt
import seaborn as sns

# Given data
data_labels = ['Housing Price Range (Thousands USD)', 'Number of Homes Sold']
line_labels = ['100-200', '200-300', '300-400', '400-500', '500-600', '600-700', '700-800', '800-900', '900-1000']
data = [200, 450, 350, 300, 150, 100, 50, 25, 10]

# Convert the data into a dictionary for Seaborn
data_dict = {data_labels[0]: line_labels, data_labels[1]: data}

# Create a DataFrame
import pandas as pd
df = pd.DataFrame(data_dict)

# Create a figure and a set for the histogram
plt.figure(figsize=(14, 8))
sns.set_style('whitegrid')

ax = sns.barplot(x=data_labels[0], y=data_labels[1], data=df, palette='viridis')

# Set title and labels with rotation for better readability
ax.set_title('Home Sales Distribution by Price Range in the U.S. Housing Market')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right", wrap=True)

# Automatically adjust subplot params
plt.tight_layout()

# Save figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/67.png', format='png')

# Clear the current figure
plt.clf()
