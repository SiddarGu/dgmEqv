import pandas as pd
import matplotlib.pyplot as plt

# Data parsing
data_labels = ['Average Daily Rate (USD)', 'Number of Hotels']
line_labels = ['Under 50', '50-100', '100-150', '150-200', '200-250', '250-300', '300-350', '350-400', '400-450']
data = [7, 15, 25, 22, 18, 10, 5, 2, 1]

# Create DataFrame
df = pd.DataFrame(list(zip(line_labels, data)), columns=data_labels)

# Create figure and subplot
plt.figure(figsize=(10, 6))
ax = plt.subplot()

# Plotting histogram
df.plot(kind='bar', x='Average Daily Rate (USD)', y='Number of Hotels', ax=ax, color='skyblue', legend=False)

# Customize the plot
ax.set_title('Hotel Pricing Trends: Average Daily Rate Distribution', fontsize=14)
ax.set_xlabel('Average Daily Rate (USD)', fontsize=12)
ax.set_ylabel('Number of Hotels', fontsize=12)
ax.grid(True, axis='y', linestyle='--', alpha=0.7)
ax.set_xticklabels(ax.get_xticklabels(), rotation=30, ha='right', rotation_mode='anchor', wrap=True)

# Adjust layout
plt.tight_layout()

# Save figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/142.png'
plt.savefig(save_path, format='png', dpi=300)

# Clear the figure
plt.clf()
