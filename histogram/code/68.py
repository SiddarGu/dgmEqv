import pandas as pd
import matplotlib.pyplot as plt

# Define the data
data_labels = ['Daily Active Users (Millions)']
line_labels = ['0-0.5', '0.5-1', '1-1.5', '1.5-2', '2-2.5', '2.5-3', '3-3.5', '3.5-4', '4-4.5']
data = [50, 45, 40, 30, 25, 20, 15, 10, 5]

# Create a DataFrame
df = pd.DataFrame(data, index=line_labels, columns=data_labels)

# Plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(1, 1, 1)
df.plot(kind='bar', ax=ax, color='skyblue')

# Set titles, labels, and options
ax.set_title('Daily Active User Distribution Across Different Websites')
ax.set_xlabel('User Range (in millions)')
ax.set_ylabel('Number of Websites')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor', wrap=True)
ax.grid(True, linestyle='--', alpha=0.7)

# Make the plot presentable
plt.legend(title='Range')
plt.tight_layout()
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/1000.png', format='png', dpi=300)

# Clear the current figure state at the end of the code to avoid memory issues
plt.clf()
