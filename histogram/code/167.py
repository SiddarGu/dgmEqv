import pandas as pd
import matplotlib.pyplot as plt

# Provided data
data = """
Housing Price Range (Thousands $),Number of Houses Sold
100-200,150
200-300,135
300-400,125
400-500,95
500-600,75
600-700,65
700-800,50
800-900,30
900-1000,20
"""

# Split the data into lines and remove leading/trailing spaces.
lines = data.strip().split('\n')

# Parse the labels for columns and data rows
data_labels = lines[0].split(',')
line_labels = [line.split(',')[0] for line in lines[1:]]
data_values = [int(line.split(',')[1]) for line in lines[1:]]

# Create a DataFrame for the data
df = pd.DataFrame({'Housing Price Range (Thousands $)': line_labels, 'Number of Houses Sold': data_values})

# Create the figure and a subplot
plt.figure(figsize=(10, 8))
ax = plt.subplot()

# Plot the horizontal bar chart
df.plot(kind='barh', x='Housing Price Range (Thousands $)', y='Number of Houses Sold', ax=ax, legend=False)

# Set the title and labels
ax.set_title('Sales Distribution Across Housing Price Ranges')
ax.set_xlabel('Number of Houses Sold')
ax.set_ylabel('Housing Price Range (Thousands $)')

# Display the grid
plt.grid(True)

# Set x-axis labels to wrap if too long
ax.tick_params(axis='y', labelrotation=0)
plt.setp(ax.get_yticklabels(), wrap=True)

# Adjust layout to not overlap and save the figure with the full path
plt.tight_layout()
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/167.png'
plt.savefig(save_path)

# Clear the current figure state
plt.clf()
