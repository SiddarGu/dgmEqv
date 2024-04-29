import matplotlib.pyplot as plt
import seaborn as sns

# Data processing
data_labels = ['Number of Daily Active Users (Millions)']
line_labels = ['Twitter', 'Pinterest', 'Snapchat', 'LinkedIn', 'TikTok', 'Instagram', 'Facebook']
data = [50, 100, 150, 200, 250, 300, 450]

# Plotting the histogram
plt.figure(figsize=(10, 8))
ax = plt.subplot()

sns.barplot(x=data, y=line_labels, palette="viridis")

# Set the title and labels
ax.set_title('Daily Active Users Across Various Social Media Platforms')
ax.set_xlabel('Number of Daily Active Users (Millions)')
ax.set_ylabel('Social Media Platform')

# Enhance readability 
plt.xticks(rotation=45)
plt.yticks(wrap=True)

# Grid
sns.set_style("whitegrid")

# Tight layout to prevent content cutting off
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/136.png')

# Clear the current figure state
plt.clf()
