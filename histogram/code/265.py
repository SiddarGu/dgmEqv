import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Given data
data = [
    [0, 100, 4],
    [100, 500, 12],
    [500, 1000, 15],
    [1000, 1500, 20],
    [1500, 2000, 10],
    [2000, 2500, 7],
    [2500, 3000, 5],
    [3000, 3500, 2],
    [3500, 4000, 1]
]

# Transform into three variables
data_labels = ['CO2 Emissions Range (Metric Tons)', 'Number of Countries']
line_labels = [f"{row[0]}-{row[1]}" for row in data]
data_values = [row[2] for row in data]

# Create DataFrame
df = pd.DataFrame(list(zip(line_labels, data_values)), columns=data_labels)

# Create a larger figure to prevent content from being cramped
plt.figure(figsize=(12, 8))

# Create subplot
ax = plt.subplot()

# Create horizontal bar plot using seaborn
sns.barplot(x="Number of Countries", y="CO2 Emissions Range (Metric Tons)", data=df, ax=ax)

# Add grid to the plot
ax.grid(True)

# Set title
ax.set_title('Global Distribution of CO2 Emissions by Country')

# If the text length of the label is too long, rotate or wrap the text
ax.set_yticklabels(ax.get_yticklabels(), rotation=45, ha='right', wrap=True)

# Automatically adjust subplot params so that the subplot(s) fits in to the figure area
plt.tight_layout()

# Save figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/demo/histogram/png/615.png'
plt.savefig(save_path, dpi=300)

# Clear the current figure after saving it
plt.clf()
