import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Data preparation
data_labels = ['Annual Revenue ($ Billion)', 'Number of Firms']
line_labels = ['0.1-0.5', '0.5-1', '1-2', '2-3', '3-4', '4-5', '5-6', 
               '6-7', '7-8', '8-9', '9-10']
data = np.array([[12], [15], [25], [20], [18], [10], [5], [2], [1], [0], [1]])

# Create DataFrame
df = pd.DataFrame(data, index=line_labels, columns=data_labels[1:])

# Create figure and axis
plt.figure(figsize=(14, 8))
ax = plt.subplot()

# Plot histogram
sns.barplot(x=df.index, y=df['Number of Firms'], ax=ax, palette='viridis')

# Set labels and title
ax.set_xlabel(data_labels[0], fontsize=12)
ax.set_ylabel(data_labels[1], fontsize=12)
ax.set_title('Analysis of Firm Sizes by Annual Revenue in the Financial Sector', fontsize=14)

# Improve appearance
plt.xticks(rotation=45, ha='right', wrap=True)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Automatically resize the image
plt.tight_layout()

# Saving the image
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/209.png'
plt.savefig(save_path, format='png')

# Clear the current image state
plt.clf()
