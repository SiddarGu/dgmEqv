import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Data setup
data_labels = ['Average Weekly Attendance (Thousands)', 'Number of Weeks']
line_labels = ['1-5', '5-10', '10-15', '15-20', '20-25', '25-30', '30-35', '35-40', '40-45', '45-50']
data = [30, 45, 20, 18, 12, 10, 8, 6, 5, 3]

# Convert to DataFrame for seaborn
df = pd.DataFrame(list(zip(line_labels, data)), columns=data_labels)

# Create a larger figure to accommodate the labels and data
plt.figure(figsize=(10, 8))
ax = plt.subplot()

# Plotting histogram
sns.barplot(x='Average Weekly Attendance (Thousands)', y='Number of Weeks', data=df, ax=ax)

# Setting title and labels
ax.set_title('Trends in Weekly Sports and Entertainment Attendance')
ax.set_xlabel(data_labels[0], fontsize=12)
ax.set_ylabel(data_labels[1], fontsize=12)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', fontsize=10)

# Customizing aesthetics
sns.despine()  # Remove the top and right spines
sns.set_style("whitegrid")  # Add a background grid for better readability

# Automatically adjusting the sizes and positions of the elements in the plot
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/95.png'
plt.savefig(save_path, dpi=300)

# Clear the current figure's state to prevent interference with future plots
plt.clf()
