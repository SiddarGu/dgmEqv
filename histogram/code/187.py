import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
from textwrap import wrap

# Data provided
data = """
Public Policy Issue,Number of Legislative Actions
Economic Policy,28
Healthcare Reform,33
Education Policy,25
Climate Action,30
National Security,22
Criminal Justice,27
Tax Reform,24
Immigration Policy,26
Cybersecurity,20
"""

# Parse the data
data = data.strip().split('\n')
data_labels = data[0].split(',')
data_rows = [row.split(',') for row in data[1:]]
line_labels = [row[0] for row in data_rows]
data = [int(row[1]) for row in data_rows]

# Create a DataFrame for Seaborn
df = pd.DataFrame(list(zip(line_labels, data)), columns=data_labels)

# Create a figure and add a subplot
plt.figure(figsize=(12, 8))
ax = plt.subplot()

# Plotting the vertical histogram using seaborn
sns.barplot(x='Public Policy Issue', y='Number of Legislative Actions', data=df, ax=ax, palette="viridis")

# Improve the layout
plt.title('Number of Legislative Actions by Public Policy Issue')
plt.xticks(rotation=45, ha='right', wrap=True)
plt.grid(axis='y')

# Adjust layout to fit the figure neatly
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/187.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)
plt.savefig(save_path)

# Clear the current figure's state
plt.clf()
