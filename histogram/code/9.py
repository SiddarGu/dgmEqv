import matplotlib.pyplot as plt
import seaborn as sns
import os

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ["Annual Revenue Range ($Million)", "Number of Restaurants"]
data = [
    [0, 1, 2, 5, 10, 15, 20, 50, 100],
    [45, 35, 50, 40, 30, 20, 15, 10, 5]
]
line_labels = ["0-1", "1-2", "2-5", "5-10", "10-15", "15-20", "20-50", "50-100", "100+"]

# Create a figure
plt.figure(figsize=(10, 8))
ax = plt.subplot()

# Create a vertical histogram
sns.barplot(x=line_labels, y=data[1])

# Set title and labels
ax.set_title("Annual Revenue Distribution in the Food and Beverage Industry")
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
# If the text length of the label is too long, rotate labels
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")

# Improve layout
plt.tight_layout()

# Create directories if they don't exist
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/9.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)

# Save the figure
plt.savefig(save_path)

# Clear the current figure's state
plt.clf()
