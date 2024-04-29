import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

# Prepare the data
data_labels = ['CO2 Emissions Range (Million Metric Tons)', 'Number of Countries']
line_labels = [
    '0-50', '50-100', '100-150', '150-200', '200-250',
    '250-300', '300-350', '350-400', '400-450', '450-500'
]
data = [
    [35], [25], [20], [10], [5],
    [3], [2], [2], [1], [1]
]

# Creating DataFrame
df = pd.DataFrame(data, columns=data_labels[1:], index=line_labels)

# Setting the aesthetic style of the plots
sns.set_style('whitegrid')

# Create a figure and add a subplot
plt.figure(figsize=(12, 8))
ax = plt.subplot()

# Create a vertical barplot
sns.barplot(x=df.index, y=df['Number of Countries'], ax=ax)

# Set the chart labels and title 
ax.set_xlabel(data_labels[0], fontsize=12, wrap=True)
ax.set_ylabel(data_labels[1], fontsize=12)
ax.set_title('Global Distribution of CO2 Emissions by Country', fontsize=14)

# Rotate x labels if necessary
plt.xticks(rotation=45)

# Automatically adjust subplot params for the figure to fit into the figure area
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/169.png'
# Ensure the directory exists
os.makedirs(os.path.dirname(save_path), exist_ok=True)
plt.savefig(save_path, format='png', dpi=300)

# Clear the current figure state
plt.clf()
