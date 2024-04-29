import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Data preparation
data_labels = ['Carbon Footprint Range (Metric Tons CO2e)', 'Number of Households']
line_labels = ['0-5', '5-10', '10-15', '15-20', '20-25', '25-30', '30-35', '35-40', '40-45', '45-50']
data = [
    [200],
    [180],
    [150],
    [120],
    [90],
    [60],
    [30],
    [10],
    [5],
    [2]
]

# Create pandas DataFrame
df = pd.DataFrame(data, index=line_labels, columns=data_labels[1:])

# Visualization
plt.figure(figsize=(12, 8))
ax = plt.subplot()
sns.barplot(x=df.index, y=data_labels[1], data=df, ax=ax)

# Rotate x labels if they are too long
for item in ax.get_xticklabels():
    item.set_rotation(45)
    item.set_wrap(True)

# Title setup
plt.title('Household Carbon Footprint Distribution in a Sustainable City')

# Adding background grid
ax.set_axisbelow(True)
ax.yaxis.grid(color='gray', linestyle='dashed', alpha=0.7)

# Automatically adjust subplot params so that the subplot(s) fits in to the figure area.
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/22.png', dpi=300)

# Clear the current figure state
plt.clf()
