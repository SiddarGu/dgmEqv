import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

# Input data
data_input = """
CO2 Emissions (Million Metric Tons),Country
USA,5000
China,10000
India,2200
Russia,1600
Germany,800
UK,600
Canada,550
France,500
Italy,450
"""

# Transforming the input data into pandas DataFrame
data = pd.read_csv(StringIO(data_input), sep=",")

# Extracting data_labels and line_labels
data_labels = data.columns.tolist()[1:]
line_labels = data.iloc[:, 0].tolist()

# Set up the matplotlib figure and axis
plt.figure(figsize=(10, 8))
ax = plt.subplot(111)

# Create the histogram
data.plot(kind='bar', ax=ax, color=plt.cm.Paired(range(len(data))))

# Set the title, labels, and grid
ax.set_title('CO2 Emissions of Major Countries in 2023', fontsize=14)
ax.set_xlabel(data.columns[1], fontsize=12)
ax.set_ylabel(data.columns[0], fontsize=12)
ax.grid(linestyle='--', linewidth=0.5)

# Rotate x-axis labels if they are too long
ax.set_xticklabels(data['CO2 Emissions (Million Metric Tons)'], rotation=45, ha="right")

# Arrange layout so that everything fits well into the figure
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/chart_simulation_final/histogram/png/289.png'
plt.savefig(save_path, dpi=300)

# Clear the current figure state to prevent re-plotting on top of the previous one
plt.clf()