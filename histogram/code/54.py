import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Given data
data_labels = ['Ticket Sales (Million USD)', 'Number of Movies']
line_labels = ['0-50', '50-100', '100-150', '150-200', '200-250', '250-300', '300-350', '350-400', '400-450']
data = [18, 25, 30, 20, 15, 10, 5, 3, 2]

# Creating dataframe from given data
df = pd.DataFrame(data, index=line_labels, columns=[data_labels[1]])

# Create the figure and axis objects
plt.figure(figsize=(14, 8))
ax = plt.subplot()

# Create a vertical bar plot
sns.barplot(x=df.index, y=df[data_labels[1]], ax=ax)

# Rotate x labels for better visibility if they are too long
plt.xticks(rotation=45)

# Set plot title
plt.title('Movie Industry Revenue Distribution from Ticket Sales')

# Setting grid
ax.yaxis.grid(True)

# Handling text overlapping
plt.gcf().autofmt_xdate()

plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/54.png')

# Clear the current figure's state
plt.clf()
