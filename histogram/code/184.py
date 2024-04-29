import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

# Given data
raw_data = """
January,50
February,45
March,60
April,55
May,65
June,70
July,75
August,80
September,85
October,90
November,95
December,100
"""

# Parsing the data
data_lines = raw_data.strip().split('\n')
data_labels = ["Monthly Sales ($Million)"]
line_labels = [line.split(',')[0] for line in data_lines]
data = [[int(line.split(',')[1])] for line in data_lines]

# Convert data into a DataFrame for Seaborn
df = pd.DataFrame(data, columns=data_labels, index=line_labels)

# Create a figure and a single subplot
plt.figure(figsize=(14, 10))
ax = sns.barplot(x=line_labels, y=[d[0] for d in data], orient='v', palette='viridis')
ax.set_title("Monthly Sales Distribution Among Retailers", fontsize=16)
ax.set_ylabel(data_labels[0])
ax.set_xlabel('Number of Retailers')
plt.xticks(rotation=45, ha='right')
plt.yticks(wrap=True)

# Adjust layout
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/hancheng/histogram/png_val/184.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)
plt.savefig(save_path, format='png')

# Clear the current figure's state
plt.clf()
