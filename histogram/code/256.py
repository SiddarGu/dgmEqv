import pandas as pd
import matplotlib.pyplot as plt

# Given data
data_content = [
    ["50-100", 18],
    ["100-150", 15],
    ["150-200", 20],
    ["200-250", 25],
    ["250-300", 10],
    ["300-350", 8],
    ["350-400", 6],
    ["400-450", 4],
    ["450-500", 2],
    ["500-550", 1],
]

# Transforming the data into three variables.
data_labels = ['Annual CO2 Emissions (Million Metric Tons)', 'Number of Countries']
line_labels = [entry[0] for entry in data_content]  # CO2 Emissions Range
data = [entry[1] for entry in data_content]         # Number of Countries

# Create a DataFrame for plotting.
df = pd.DataFrame(data_content, columns=data_labels)

# Create the figure and add a subplot.
fig = plt.figure(figsize=(14, 8))  # figsize set to be larger to prevent content from being cluttered
ax = fig.add_subplot()

# Plotting the data using pandas.
df.plot(kind='bar', x='Annual CO2 Emissions (Million Metric Tons)', y='Number of Countries', ax=ax, legend=False)

# Enhance chart visualization
ax.set_title('Global CO2 Emissions Range and Country Distribution')
ax.set_ylabel('Number of Countries')
ax.set_xlabel('Annual CO2 Emissions (Million Metric Tons)')
ax.grid(axis='y', linestyle='--', alpha=0.7)
ax.tick_params(axis='x', rotation=45)  # Rotate x labels to prevent overlap
ax.set_xticklabels(line_labels, rotation=45, ha='right', fontsize=10, wrap=True)  # Adjust x-axis labels

# Automatically resize the layout and save the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/demo/histogram/png/606.png')

# Clear the current image state
plt.clf()
