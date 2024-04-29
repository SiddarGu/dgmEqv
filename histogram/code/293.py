import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Data
data_raw = """0-100,18
100-200,30
200-300,25
300-400,20
400-500,15
500-600,12
600-700,10
700-800,8
800-900,5
900-1000,3"""

# Parsing data into the required format
data_lines = data_raw.strip().split('\n')
data_labels = ['CO2 Emissions Range (Million Metric Tons)', 'Number of Countries']
line_labels, data = [], []

for line in data_lines:
    label, value = line.split(',')
    line_labels.append(label)
    data.append(int(value))

data_frame = pd.DataFrame({'CO2 Emissions Range (Million Metric Tons)': line_labels, 'Number of Countries': data})

# Plotting
plt.figure(figsize=(10, 8))
ax = plt.subplot()

sns.barplot(x='CO2 Emissions Range (Million Metric Tons)', y='Number of Countries',
            data=data_frame,
            ax=ax,
            palette="viridis")

# Improve the visualization
ax.set_title('Global Distribution of CO2 Emissions by Countries', fontsize=16)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right", wrap=True)
ax.grid(True)

plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/demo/histogram/png/643.png'
plt.savefig(save_path)

# Clear the current figure's state
plt.clf()
