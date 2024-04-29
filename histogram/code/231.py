import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Data preparation
data = np.array([5000, 10000, 2400, 1700, 1200, 800, 700, 600, 500, 400])
data_labels = ['USA', 'China', 'India', 'Russia', 'Japan', 'Germany', 'Canada', 'South Korea', 'UK', 'France']
line_labels = 'CO2 Emissions (Million Metric Tons)'

# Create a DataFrame for the dataset
df = pd.DataFrame({
    'Country': data_labels,
    'CO2 Emissions (Million Metric Tons)': data
})

# Plotting
plt.figure(figsize=(10, 8))
ax = plt.subplot()

# Plot the histogram using Seaborn
sns.barplot(x='Country', y='CO2 Emissions (Million Metric Tons)', data=df, ax=ax, palette="viridis")

# Set title, label rotation and adjustment for long labels.
ax.set_title('Global CO2 Emissions Distribution by Top Emitting Countries')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
plt.tight_layout()

# Saving the figure to the specific path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/231.png'
plt.savefig(save_path, format='png', dpi=300)

# Clear the current figure's state
plt.clf()
