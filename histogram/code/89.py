import matplotlib.pyplot as plt
import seaborn as sns

# Given data
data = [
    [0, 100, "Misdemeanors"],
    [100, 500, "Felonies"],
    [500, 1000, "Civil Lawsuits"],
    [1000, 1500, "Family Law Cases"],
    [1500, 2000, "Corporate Litigations"],
    [2000, 2500, "Property Disputes"],
    [2500, 3000, "Intellectual Property Cases"],
    [3000, 3500, "Personal Injury Cases"]
]

# Tranform data
data_labels = ['Number of Cases', 'Category']
line_labels = [row[2] for row in data]
data = [row[1] for row in data]

# Create the plot
sns.set(style="whitegrid")
plt.figure(figsize=(10, 8))
ax = plt.subplot()

# Create the horizontal bar plot
sns.barplot(x=data, y=line_labels, palette="viridis")

# Set the title and labels
ax.set_title('Annual Case Volume by Legal Category')
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

# Improve aesthetics of long category labels
ax.set_yticklabels(ax.get_yticklabels(), rotation=0, wrap=True)

# Automatically adjust subplot params for the figure to fit into the canvas
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/89.png'
plt.savefig(save_path, format='png')

# Clear the current figure state
plt.clf()
