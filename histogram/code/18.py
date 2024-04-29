import pandas as pd
import matplotlib.pyplot as plt

# Transform the data into three variables
data_labels = ['Road', 'Rail', 'Air', 'Water', 'Pipeline']
data = [1575.2, 1652.3, 988.4, 1256.7, 1339.5]
line_labels = ['Year']

# Create a dataframe from the data
df = pd.DataFrame(data, index=data_labels, columns=line_labels)

# Initialize the plot
fig = plt.figure(figsize=(10, 6))  # figsize larger to avoid tight content
ax = fig.add_subplot(111)

# Plotting using pandas
df.plot(kind='bar', legend=False, ax=ax, rot=0)

# Set the aesthetics for the plot
ax.set_title('Annual Freight Volume by Transportation Mode')
ax.set_ylabel('Freight Volume (Million Tons)')
ax.set_xlabel('Transportation Mode')
ax.grid(True)

# Handling long labels if necessary
ax.set_xticklabels(data_labels, rotation=45, ha='right')

# Customize the look with tight_layout and fancy colors
plt.tight_layout()
for patch in ax.patches:
    patch.set_facecolor('#3498DB')  # A fancy blue color for each bar

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/18.png', format='png')

# Clear the current figure state to avoid overlap if the plot is reused
plt.clf()
