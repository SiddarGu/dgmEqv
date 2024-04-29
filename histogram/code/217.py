import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Input data
data_dict = {
    "Revenue Range ($Billion)": ["0.1-0.5", "0.5-1.0", "1.0-2.5", "2.5-5.0", "5.0-7.5", "7.5-10.0", "10.0-20.0", "20.0-30.0", "30.0-50.0"],
    "Number of Companies": [35, 29, 42, 33, 17, 11, 6, 3, 2]
}

# Transform data into a DataFrame
df = pd.DataFrame(data_dict)

# Plotting
plt.figure(figsize=(12, 8))
ax = plt.subplot()

# Using seaborn for the histogram
sns.barplot(ax=ax, data=df, x="Revenue Range ($Billion)", y="Number of Companies", palette='viridis')

# Set title and labels properties
ax.set_title('Revenue Distribution Across Various Companies', fontsize=16)
ax.set_xlabel('Revenue Range ($Billion)', fontsize=14)
ax.set_ylabel('Number of Companies', fontsize=14)

# Rotating the x-axis labels to prevent overlapping
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right", fontsize=12)

# Adding background grid for better readability
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=.25)

# Adjust layout to ensure clear visibility of labels
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/217.png'
plt.savefig(save_path, format='png', transparent=False)

# Clear the current figure's state 
plt.clf()
