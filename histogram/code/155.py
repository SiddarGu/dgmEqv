import matplotlib.pyplot as plt
import seaborn as sns

# Given data
data_str = """0-50, 18
50-100, 15
100-150, 12
150-200, 10
200-250, 8
250-300, 5
300-350, 3
350-400, 2
400-450, 1
450-500, 1"""

# Parsing data
rows = data_str.split('\n')
data_labels = ['Research Expenditure ($Million)', 'Number of Projects']
line_labels = [row.split(', ')[0] for row in rows]  # Left column as line labels
data = [int(row.split(', ')[1]) for row in rows]     # Right column as data

# Plotting
sns.set_theme(style="whitegrid")
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot()

# Create a bar plot using Seaborn
sns.barplot(x=line_labels, y=data, palette="viridis", ax=ax)

# Set the title and labels
ax.set_title('Research Funding Allocation Across Science and Engineering Projects')
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

# Rotate x-axis labels if they are too long
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")

# Automatically adjust subplot params for the subplot to fit into the figure area.
plt.tight_layout()

# Save the figure
save_path = "/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/155.png"
plt.savefig(save_path)

# Clear the current figure state to prevent overlap with future plots
plt.clf()
