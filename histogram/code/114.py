import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Given data
data_labels = ['Budget Allocation ($ Billion)']
line_labels = ['Defense', 'Healthcare', 'Education', 'Social Security', 'Infrastructure', 'Justice', 'Energy', 'Environment', 'Foreign Affairs', 'Science and Technology']
data = np.array([
    [750],  # Estimated average of 500-1000
    [475],  # Estimated average of 450-500
    [275],  # Estimated average of 250-300
    [225],  # Estimated average of 200-250
    [175],  # Estimated average of 150-200
    [125],  # Estimated average of 100-150
    [75],   # Estimated average of 50-100
    [35],   # Estimated average of 20-50
    [15],   # Estimated average of 10-20
    [7.5],  # Estimated average of 5-10
])

# Transform the data into a DataFrame
df = pd.DataFrame(data, index=line_labels, columns=data_labels)

# Create figure and axes
plt.figure(figsize=(14, 8))
ax = plt.subplot()

# Create histogram
sns.barplot(data=df, x=df.index, y=data_labels[0], palette='viridis', ax=ax)
ax.set_title('US Federal Budget Allocation Across Various Departments', fontsize=16)

# Set x-axis labels with rotation for better readability
plt.xticks(rotation=45, ha='right', fontsize=12)

# Improve layout to avoid content overflow
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/114.png'
plt.savefig(save_path)

# Clear the current figure's state
plt.clf()
