import pandas as pd
import matplotlib.pyplot as plt

# Data
data_labels = ['Donation Range ($)', 'Number of Nonprofits']
line_labels = ['0-1000', '1000-5000', '5000-10000', '10000-50000', '50000-100000', '100000-500000', '500000-1000000', '1000000-5000000']
data = [15, 25, 20, 30, 18, 12, 8, 5]

# Create DataFrame
df = pd.DataFrame(data, index=line_labels, columns=['Number of Nonprofits'])

# Plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

# Vertical Histogram
df.plot(kind='bar', ax=ax, color='skyblue', edgecolor='black')

# Setting title, labels and configurations
ax.set_title('Donation Size Distribution Among Nonprofits')
ax.set_xlabel('Donation Range ($)')
ax.set_ylabel('Number of Nonprofits')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Automatically resize the image
plt.tight_layout()

# Save figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/50.png'
plt.savefig(save_path)

# Clear the current image state
plt.clf()
