import matplotlib.pyplot as plt
import seaborn as sns

# Transforming the raw data into variables
data_labels = ['Number of Users (Million)']
line_labels = ['<1', '1-2', '2-3', '3-4', '4-5', '5-6', '6-7', '7-8', '8+']
data = [45.3, 75.2, 88.9, 67.0, 52.1, 38.4, 27.6, 18.3, 12.5]

# Create a DataFrame for visualization with seaborn
import pandas as pd
df = pd.DataFrame(data, index=line_labels, columns=data_labels)

# Setting the figsize to ensure content is clearly displayed
plt.figure(figsize=(12, 8))
ax = plt.subplot()

# Plotting the histogram using seaborn
sns.barplot(data=df, x=df.index, y='Number of Users (Million)', palette='viridis', ax=ax)

# Ensuring the x-labels are clear and not overlapping
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', wrap=True)

# Adding grid lines, setting title, and labels
ax.grid(True)
ax.set_title('Daily Internet Usage Patterns among Users')
ax.set_xlabel('Hours Spent Daily')
ax.set_ylabel('Number of Users (Million)')

# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/170.png')

# Clear the current image state
plt.clf()
