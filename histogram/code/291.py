import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Provided data
data = """
Government Expenditure Category,Amount (Billion $)
Defense,721.5
Education,590.2
Healthcare,980.3
Infrastructure,470.4
Research and Development,320.7
Social Welfare,860.1
Environmental Protection,210.8
Public Safety,310.5
"""

# Splitting the data into lists
lines = data.strip().split('\n')
data_labels = lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in lines[1:]]
data = np.array([[float(value) for value in line.split(',')[1:]] for line in lines[1:]])

# Create a figure and set size
plt.figure(figsize=(12, 8))
ax = plt.subplot(111)

# Using seaborn to plot a vertical histogram
sns.barplot(x=line_labels, y=data.flatten(), palette='viridis')

# Aesthetics and labels
plt.title('Allocation of Government Expenditure by Policy Category (2023)', fontsize=18)
plt.xlabel('Policy Category', fontsize=14)
plt.ylabel('Amount (Billion $)', fontsize=14)
plt.xticks(rotation=45, wrap=True)

# Setting the grid
ax.grid(axis='y')

# Automatically adjust subplot params to give specified padding
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/demo/histogram/png/641.png'
plt.savefig(save_path, format='png')

# Clear the current figure
plt.clf()
