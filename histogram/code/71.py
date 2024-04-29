import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

# Data processing to convert the raw string into structured data
data_str = """Grade Range,Average GPA
K-2,2.9
3-5,3.1
6-8,3.3
9-10,3.4
11-12,3.5"""
data_lines = data_str.split('\n')
data_labels = data_lines[0].split(',')
line_labels, data = zip(*(line.split(',') for line in data_lines[1:]))
data = [float(i) for i in data]

# Convert data into a DataFrame for seaborn
df = pd.DataFrame(list(zip(line_labels, data)), columns=data_labels)

# Visualization
plt.figure(figsize=(10, 6))  # Set the size of the figure to be large enough
ax = plt.subplot()

# Create a vertical bar plot
sns.barplot(x='Grade Range', y='Average GPA', data=df, ax=ax)

# Set the title
ax.set_title('Average Grade Point Average (GPA) by Education Level in Elementary and Secondary Schools')

# Customize the plot with seaborn style
sns.set_style("whitegrid")

# Rotate x labels if they are too long
plt.xticks(rotation=45, ha='right', wrap=True)

# Automatically adjust subplot params for a better fit
plt.tight_layout()

# Create directories if not exist
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/71.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)

# Save the figure
plt.savefig(save_path)

# Clear the current figure state
plt.clf()
