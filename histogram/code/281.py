import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from io import StringIO

# Data processing
data_content = """
Revenue Range ($Billion),Number of Companies
0.0-0.5,18
0.5-1.0,22
1.0-1.5,15
1.5-2.0,11
2.0-2.5,9
2.5-3.0,7
3.0-3.5,5
3.5-4.0,4
4.0-4.5,2
4.5-5.0,1
"""
data = pd.read_csv(StringIO(data_content), header=0)
data_labels = list(data.columns[1:])
line_labels = list(data.iloc[:, 0])

# Plot setup
plt.figure(figsize=(10, 8))
ax = plt.subplot()

# Creating the histogram using Seaborn
sns.barplot(x=line_labels, y=data_labels[0], data=data, color="skyblue", ax=ax)

# Rotate the x labels if they are too long
plt.xticks(rotation=45, ha='right')

# Set plot title and labels
ax.set_title('Revenue Distribution Within the Food and Beverage Industry')
ax.set_xlabel(data.columns[0])
ax.set_ylabel(data.columns[1])

# Set background grid
ax.set_axisbelow(True)
ax.yaxis.grid(color='gray', linestyle='dashed')

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/chart_simulation_final/histogram/png/281.png'
plt.savefig(save_path, format='png', dpi=300)

# Clear the current image state
plt.clf()
