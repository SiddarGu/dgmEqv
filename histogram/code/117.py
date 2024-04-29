import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Data setup
data_labels = ['Revenue Range ($Million)', 'Number of Franchises']
line_labels = [
    '0-50', '50-100', '100-150', '150-200', '200-250', 
    '250-300', '300-350', '350-400', '400-450'
]
data = [
    18, 24, 29, 15, 10, 7, 4, 2, 1
]

# Creating a DataFrame
df = pd.DataFrame(data=np.array(data).reshape(-1, 1), index=line_labels, columns=data_labels[1:])

# Creating the figure
plt.figure(figsize=(14, 8))
ax = plt.subplot()

# Creating horizontal histogram using seaborn
sns.barplot(x=data_labels[1], y=df.index, data=df, orient='h', palette="viridis")

# Setting title, labels, and grid
ax.set_title('Financial Performance of Sports and Entertainment Franchises')
ax.set_xlabel(data_labels[1])
ax.set_ylabel(data_labels[0])
ax.grid(True, linestyle='--', alpha=0.7)

# Rotating the x-axis labels if too long
plt.xticks(rotation=45)
plt.yticks(wrap=True)

# Ensuring layout fits the labels and prevents content from being cut off
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/117.png'
plt.savefig(save_path, format='png')

# Clear the current image state
plt.clf()
