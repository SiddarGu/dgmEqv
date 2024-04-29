import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Prepare the data
data_labels = ['Revenue Range ($Million)', 'Number of Companies']
line_labels = ['0-50', '50-100', '100-150', '150-200', '200-250', '250-300', '300-350', '350-400', '400-450', '450-500']
data = [18, 23, 24, 20, 15, 10, 6, 4, 3, 2]

# Create a DataFrame
df = pd.DataFrame(list(zip(line_labels, data)), columns=data_labels)

# Create the figure
plt.figure(figsize=(12, 8))
ax = plt.subplot()

# Plot the data
sns.barplot(x=data_labels[0], y=data_labels[1], data=df, ax=ax)

# Set the aesthetics
ax.set_title('Corporate Revenue Distribution Across Different Financial Brackets')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right", wrap=True)
ax.grid(True)

# Automatically adjust the layout
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/174.png'
plt.savefig(save_path, dpi=300)

# Clear the current image state
plt.clf()
