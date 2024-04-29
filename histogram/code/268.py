import matplotlib.pyplot as plt
import seaborn as sns
import os

# Parsing the given data
data_str = """
500,Engineering
600,Business
450,Health Sciences
250,Arts & Humanities
300,Social Sciences
350,Natural Sciences
150,Education
200,Information Technology
100,Law
"""

# Splitting the data into lines and then into labels and values
data_rows = data_str.strip().split('\n')
data_labels = ['Field of Study']
line_labels = []
data = []

for row in data_rows:
    values = row.split(',')
    line_labels.append(values[1])
    data.append(int(values[0]))

# Visualization
plt.figure(figsize=(10, 8))
ax = plt.subplot()

# Drawing the histogram using seaborn
sns.barplot(x=line_labels, y=data, palette="viridis")

# Set the title and labels
ax.set_title('Number of Graduates by Field of Study')
ax.set_ylabel('Number of Graduates')
ax.set_xlabel('Field of Study')

# Improve the clarity of x labels by rotating them if they are too long
plt.xticks(rotation=45, ha='right', wrap=True)

# Adjust subplot params so that the subplot(s) fits in to the figure area
plt.tight_layout()

# Saving the figure to the specified path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/demo/histogram/png/618.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)
plt.savefig(save_path)

# Clearing the current figure's state for a new plot
plt.clf()
