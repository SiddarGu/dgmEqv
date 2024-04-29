import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Data
data_labels = ['Profit Margins (%)', 'Frequency']
line_labels = ['0-5', '5-10', '10-15', '15-20', '20-25', '25-30', '30-35', '35-40', '40-45']
data = [12, 20, 18, 22, 15, 10, 4, 2, 1]

# Construct data into DataFrame
df = pd.DataFrame(list(zip(line_labels, data)), columns=data_labels)

# Create a figure and a set of subplots
fig, ax = plt.subplots(figsize=(10, 6))

# Plot using seaborn
sns.barplot(x='Profit Margins (%)', y='Frequency', data=df, ax=ax, palette="viridis")

# Set title and labels
ax.set_title('Frequency of Profit Margins for Various Businesses')
ax.set_xlabel('Profit Margins (%)')
ax.set_ylabel('Frequency')

# Rotate x labels if necessary
plt.xticks(rotation=45)

# Set the style
sns.set_style("whitegrid")

# Automatically adjust subplot params to give specified padding.
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/88.png')

# Clear the current figure to make sure the state is clean for future plotting
plt.clf()
