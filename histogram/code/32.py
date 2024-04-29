import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Given data
data_info = """
1-10,50
10-20,35
20-30,20
30-40,15
40-50,10
50-60,7
60-70,3
70-80,2
80-90,1
90-100,1
"""

# Process data
data_lines = data_info.strip().split("\n")
data_labels = ["Revenue Range (Billion USD)", "Number of Corporations"]
line_labels = [line.split(',')[0] for line in data_lines]
data = [int(line.split(',')[1]) for line in data_lines]

# Create DataFrame
df = pd.DataFrame(data, index=line_labels, columns=[data_labels[1]])

# Plotting setup
plt.figure(figsize=(12, 8))
ax = plt.subplot()

# Create seaborn histogram
sns.barplot(x=df.index, y=data_labels[1], data=df, ax=ax, palette="viridis")

# Set title
ax.set_title('Corporate Revenue Distribution Across Various Sectors')

# Set axis labels
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

# Rotate x-axis labels if too long
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)

# Adjust layout
plt.tight_layout()

# Save the image
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/32.png'
plt.savefig(save_path)

# Clear the current image state
plt.clf()
