import matplotlib.pyplot as plt
import seaborn as sns

# Given data
data_labels = ["Social Media Platform", "Monthly Active Users (Millions)"]
line_labels = ["Facebook", "Twitter", "Instagram", "TikTok", "LinkedIn", "WhatsApp", "Snapchat", "YouTube", "WeChat", "Pinterest"]
data = [500, 250, 1000, 1500, 300, 800, 400, 1200, 700, 600]

# Transform data for plotting
df = {data_labels[0]: line_labels, data_labels[1]: data}

# Create a DataFrame
import pandas as pd
df = pd.DataFrame(df)

# Set up the matplotlib figure
plt.figure(figsize=(10, 8))
ax = plt.subplot()

# Create a seaborn bar plot
sns.barplot(x=data_labels[0], y=data_labels[1], data=df, ax=ax, palette="viridis")

# Rotate x-axis labels if they are too long
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right', wrap=True)

# Selecting background style
plt.style.use('ggplot')

# Set the title
plt.title('Monthly Active User Counts Across Various Social Media Platforms')

# Automatically adjust subplot params for the figure to fit into the area
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/46.png'
plt.savefig(save_path, format='png', dpi=300)

# Clear the current figure's state
plt.clf()
