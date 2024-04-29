import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

# Transforming the given data into three variables
data_labels = ["Donation Range ($Thousands)", "Number of Charities"]
line_labels = ["0-10", "10-50", "50-100", "100-500", "500-1000", "1000-5000", "5000-10000", "10000+"]
data = [28, 45, 36, 21, 10, 7, 2, 1]

# Creating a dataframe
df = pd.DataFrame(list(zip(line_labels, data)), columns=data_labels)

# Creating figure and adding subplots
plt.figure(figsize=(10, 8))
ax = plt.subplot()

# Seaborn barplot to create the horizontal histogram
sns.barplot(x='Number of Charities', y='Donation Range ($Thousands)', data=df, ax=ax)

# Title and labels
plt.title('Charity Donation Levels Across Nonprofit Organizations')
ax.set_xlabel('Number of Charities')
ax.set_ylabel('Donation Range ($Thousands)')

# Improving the aesthetics
sns.set_style('whitegrid')
plt.xticks(rotation=45)
ax.tick_params(axis='x', which='major', labelsize=10)
ax.tick_params(axis='y', which='major', labelsize=10)

# Automatically resize the figure
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/demo/histogram/png/605.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)
plt.savefig(save_path)

# Clearing the current image state
plt.clf()
