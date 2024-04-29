import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Define the data
raw_data = """
Output (In Metric Units),Number of Factories
50-100,8
100-150,15
150-200,20
200-250,12
250-300,7
300-350,5
350-400,3
400-450,2
450-500,1
"""

# Process the data
data = [line.split(',') for line in raw_data.strip().split('\n')]
data_labels = data[0]
line_labels = [row[0] for row in data[1:]]
data = [int(row[1]) for row in data[1:]]

# Convert to DataFrame for plotting
df = pd.DataFrame(data={'Output (In Metric Units)': line_labels, 'Number of Factories': data})

# Create the figure for plotting
plt.figure(figsize=(12,8))
ax = plt.subplot()

# Plot horizontal histogram using Seaborn
sns.barplot(x="Number of Factories", y="Output (In Metric Units)", data=df, orient='h', palette="viridis")

# Add the title and format the plot
plt.title('Factory Output Distribution in the Manufacturing Sector')
plt.xlabel(data_labels[1])
plt.ylabel(data_labels[0])
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
plt.tight_layout()

# Save the plot to the specified path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/212.png'
plt.savefig(save_path, dpi=300)

# Clear the current figure's state
plt.clf()
