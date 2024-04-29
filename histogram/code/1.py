import matplotlib.pyplot as plt
import seaborn as sns
import os

# Provided data
raw_data = """
Gallery Visitors (Thousands),Number of Galleries
0-5,14
5-10,22
10-15,19
15-20,13
20-25,9
25-30,7
30-35,5
35-40,3
40-45,2
45-50,1
"""

# Transforming data into variables
data_rows = raw_data.strip().split('\n')
data_labels = data_rows[0].split(',')
line_labels = [row.split(',')[0] for row in data_rows[1:]]
data = [int(row.split(',')[1]) for row in data_rows[1:]]

# Create figure and add subplot
plt.figure(figsize=(10, 8))
ax = sns.barplot(x=data, y=line_labels, orient='h', palette="viridis")

# Setting grid, labels, and title
ax.set_xlabel(data_labels[1])
ax.set_ylabel(data_labels[0])
ax.set_title('Visitor Distribution Across Art Galleries')
plt.grid(True, axis='x', linestyle='--', linewidth=0.5, alpha=0.7)

# Check if label text is too long and adjust rotation or wrap accordingly
ax.tick_params(axis='y', labelsize=10)
for label in ax.get_yticklabels():
    if len(label.get_text()) > 15:
        label.set_wrap(True)

# Make the layout of the figure tight
plt.tight_layout()

# Define the absolute path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/1.png'

# Ensure the directory exists as it is required for os.makedirs
os.makedirs(os.path.dirname(save_path), exist_ok=True)

# Save and clear the current figure
plt.savefig(save_path)
plt.clf()
