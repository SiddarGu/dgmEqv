import matplotlib.pyplot as plt
import seaborn as sns

# Given data
data_labels = ['Revenue Band ($Million)', 'Number of Firms']
line_labels = ['0-50', '50-100', '100-150', '150-200', '200-250', '250-300', '300-350', '350-400', '400-450', '450-500']
data = [12, 15, 18, 20, 15, 9, 7, 4, 2, 1]

# Transform data into a proper format for seaborn
data_for_plot = {
    data_labels[0]: line_labels,
    data_labels[1]: data
}

# Create a DataFrame
df = pd.DataFrame(data_for_plot)

# Create figure and plot space
plt.figure(figsize=(12, 8))
ax = plt.subplot()

# Create a horizontal bar plot
sns.barplot(x=data_labels[1], y=data_labels[0], data=df, orient='h', palette="viridis")

# Add gridlines, title, and labels
ax.set_title('Revenue Distribution Across Firms in the Financial Year', fontsize=16)
ax.set_xlabel(data_labels[1], fontsize=14)
ax.set_ylabel(data_labels[0], fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12, rotation=0, wrap=True)

# Automatically adjust subplot params for the subplot(s) to fit in to the figure area.
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/179.png')

# Clear the current figure's state
plt.clf()
