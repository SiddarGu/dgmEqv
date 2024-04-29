import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Given data
data_str = """January,40
February,35
March,50
April,65
May,70
June,60
July,75
August,80
September,50
October,55
November,85
December,90"""

# Process data into data_labels, data, line_labels
lines = data_str.strip().split('\n')
data_labels = ['Monthly Sales Revenue ($Million)']
line_labels = [line.split(',')[0] for line in lines]
data = [int(line.split(',')[1]) for line in lines]

# Create a DataFrame
df = pd.DataFrame(data, index=line_labels, columns=data_labels)

# Plot settings
sns.set(style="whitegrid")

# Create a figure and add a subplot
fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(111)

# Create the histogram
sns.barplot(x=df.index, y=data_labels[0], data=df, ax=ax)

# Set the title and labels
ax.set_title('Monthly Sales Revenue in Retail and E-commerce Sector', fontsize=16)
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Sales Revenue ($Million)', fontsize=12)

# Rotate x labels to avoid overlapping
plt.xticks(rotation=45, ha='right')

# Resize the image with tight_layout and save to the specified path
plt.tight_layout()
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/1006.png', dpi=300, bbox_inches='tight')

# Clear the current figure to prevent re-plotting on top of existing data
plt.clf()
