import pandas as pd
import matplotlib.pyplot as plt

# Given data
data_labels = ['CO2 Emissions (Million Metric Tons)', 'Region']
line_labels = ['North America', 'Europe', 'Asia', 'South America', 'Africa', 'Oceania', 'Antarctica']
data = [5000, 4500, 8000, 2500, 1500, 1200, 5]

# Create a DataFrame from the data
df = pd.DataFrame(data, index=line_labels, columns=['CO2 Emissions'])

# Create a figure and an subplot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot()

# Plot a vertical bar graph
df.plot(kind='bar', ax=ax, color='skyblue', grid=True, edgecolor='black')

# Add title and labels with adjustments for long texts
ax.set_title("Global Distribution of CO2 Emissions by Region")
ax.set_xlabel(data_labels[1])
ax.set_ylabel(data_labels[0])
ax.tick_params(axis='x', labelrotation=45, labelsize=8)

# Automatically adjust subplot params for a nice fit & save the figure
plt.tight_layout()
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/224.png'
plt.savefig(save_path, format='png')

# Clear the current figure's state
plt.clf()
