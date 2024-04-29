import pandas as pd
import matplotlib.pyplot as plt

# Define the data
data_labels = ['Research Funding (Million USD)', 'Number of Projects']
line_labels = ['0-50', '50-100', '100-150', '150-200', '200-250', 
               '250-300', '300-350', '350-400', '400-450', '450-500']
data = [75, 60, 50, 40, 30, 20, 15, 10, 5, 2]

# Transform the data into a DataFrame
df = pd.DataFrame(data, index=line_labels, columns=[data_labels[1]])

# Create a figure and a subplot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

# Plot the data
df.plot(kind='bar', ax=ax, color='skyblue', width=0.8)

# Set the title and labels
ax.set_title('Allocation of Research Funding Across Science and Engineering Projects')
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

# Set grid, legend, and rotation for x-axis labels to avoid overlapping
ax.grid(True)
ax.legend().set_visible(False)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')

# Automatically adjust subplot params to give specified padding
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/37.png'
plt.savefig(save_path, format='png')

# Clear the current figure
plt.clf()
