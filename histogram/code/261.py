import pandas as pd
import matplotlib.pyplot as plt

# Given data : skip the first '/n' as it's not part of the data.
data = """Trucks,72.5
Ships,65.2
Trains,58.4
Air Freight,21.3
Pipelines,34.1
Inland Waterways,19.8"""

# Convert string data into pandas DataFrame
from io import StringIO
data = pd.read_csv(StringIO(data), names=['Vehicle Type', 'Freight Volume (million tons)'])

# Set data labels and line labels
data_labels = data['Vehicle Type']
line_labels = data.columns[1]
data_values = data.iloc[:, 1]

# Create a figure with larger figsize to accommodate long labels
plt.figure(figsize=(10, 8))
ax = plt.subplot()

# Plot a vertical bar chart
bars = ax.bar(data_labels, data_values, color=plt.cm.tab10.colors)

# Add grid, title, and rotate the labels if necessary
ax.set_title('Freight Volume by Transportation Mode in the European Union', fontsize=15)
ax.grid(True)
plt.xticks(rotation=45, ha='right')
plt.xlabel(line_labels)
plt.ylabel('Volume (million tons)')

# Dynamically adjust the layout and save the figure at the given location
plt.tight_layout()
save_path = '/cpfs01/user/liuqi/workspace/plotchart/demo/histogram/png/611.png'
plt.savefig(save_path)

# Clear the current figure's state
plt.clf()
