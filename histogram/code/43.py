import matplotlib.pyplot as plt
import seaborn as sns

# Data transformation
data_labels = ['Average Occupancy Rate (%)']
line_labels = ['1-Star', '2-Star', '3-Star', '4-Star', '5-Star']
data = [60, 70, 80, 85, 75]

# Prepare DataFrame for Seaborn
import pandas as pd
df = pd.DataFrame(data, index=line_labels, columns=data_labels)

# Plot settings
plt.figure(figsize=(10, 8))
ax = plt.subplot()

# Create seaborn barplot (horizontal)
sns.barplot(x=data, y=line_labels, palette='viridis', ax=ax)
plt.title('Average Hotel Occupancy Rates by Star Rating')
plt.xlabel('Average Occupancy Rate (%)')

# Improve layout, save the figure, and clear the plot state
plt.tight_layout()
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/43.png')
plt.clf()
