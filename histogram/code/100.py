import matplotlib.pyplot as plt
import seaborn as sns

# Given data
data_raw = """
0-30,52.7
30-60,65.3
60-90,59.8
90-120,45.1
120-150,38.9
150-180,26.4
180-210,17.2
210-240,14.5
240+,10.6
"""

# Transforming data into required variables
data_lines = data_raw.strip().split('\n')
data_labels = ['Daily Time Spent (Minutes)']
line_labels = [line.split(',')[0] for line in data_lines]
data = [float(line.split(',')[1]) for line in data_lines]

# Create a figure and a single subplot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(1, 1, 1)

# Create vertical histograms
sns.barplot(x=line_labels, y=data, palette="viridis", ax=ax)

# Setting the title of the histogram
ax.set_title('Daily Time Spent on Social Media by Users', fontsize=14)

# Set the labels for the x-axis and y-axis
ax.set_xlabel(data_labels[0], fontsize=12)
ax.set_ylabel('User Population (Millions)', fontsize=12)

# Optional: Rotate labels if they are too long
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")

# Use tight_layout to automatically resize the image 
plt.tight_layout()

# Saving the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/100.png'
plt.savefig(save_path, format='png', dpi=300)

# Clear the current image state
plt.clf()
