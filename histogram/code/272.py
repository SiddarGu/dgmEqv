import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Given data
data_labels = ['Carbon Emission Reduction Targets (Million Metric Tons)', 'Number of Countries']
line_labels = ['0-50', '50-100', '100-150', '150-200', '200-250', '250-300', '300-350', '350-400', '400-450']
data = [28, 22, 18, 15, 10, 6, 4, 2, 1]

# Create a DataFrame
df = pd.DataFrame(list(zip(line_labels, data)), columns=data_labels)

# Create figure and axis
plt.figure(figsize=(10, 8))
ax = plt.subplot()

# Create histogram
sns.barplot(x=data_labels[0], y=data_labels[1], data=df, ax=ax)

# Set title
ax.set_title('Global Carbon Emission Reduction Goals by 2030')

# Rotate x-axis labels if necessary
ax.set_xticklabels(df[data_labels[0]], rotation=45, ha='right', wrap=True)

# Fancy styling
sns.set_style("whitegrid")
palette = sns.color_palette("Spectral", len(df))
sns.set_palette(palette)

# Adjust the layout
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/demo/histogram/png/622.png')

# Clear the current figure state
plt.clf()
