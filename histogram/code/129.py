import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Provided data in raw format
raw_data = """0-5,12
5-10,30
10-15,45
15-20,25
20-25,18
25-30,10
30-35,9
35-40,6
40-45,4
45-50,2"""

# Parsing the data
data_lines = raw_data.split('\n')
data_labels = ['Ticket Price Range ($)', 'Number of Films']
line_labels = [line.split(',')[0] for line in data_lines]
data = [int(line.split(',')[1]) for line in data_lines]

# Creating DataFrame
df = pd.DataFrame(data, index=line_labels, columns=[data_labels[1]])

# Plotting
plt.figure(figsize=(10, 6))
ax = plt.subplot()
sns.set_theme()
sns.barplot(x=df.index, y=df[data_labels[1]], ax=ax, palette="viridis")
ax.set_title('Movie Ticket Price Range and Film Count in 2023')
ax.set_ylabel(data_labels[1])
ax.set_xlabel(data_labels[0])
plt.xticks(rotation=45, ha="right", rotation_mode="anchor")

# Automatically adjust subplot params so that the subplot(s) fits into the figure area.
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/129.png'
plt.savefig(save_path)

# Clear the current figure state
plt.clf()
