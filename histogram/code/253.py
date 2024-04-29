import pandas as pd
import matplotlib.pyplot as plt

# Prepare data
data = {
    "Donation Amount ($)": ["0-50", "50-100", "100-250", "250-500", "500-1000", "1000-2500", "2500-5000", "5000-10000", "10000+"],
    "Number of Donations": [120, 80, 60, 40, 20, 15, 5, 2, 1]
}
df = pd.DataFrame(data)

# Define labels
data_labels = ["Donation Amount ($)"]
line_labels = df["Donation Amount ($)"].values

# Create figure and plot histogram
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)
df.plot(kind='bar', x='Donation Amount ($)', y='Number of Donations', ax=ax, color='skyblue')

# Customize the plot
ax.set_title('Frequency of Donation Amounts to Charity and Nonprofit Organizations')
ax.set_xlabel('Donation Amount ($)')
ax.set_ylabel('Number of Donations')
ax.grid(True)

# Improve label visibility
plt.xticks(rotation=45, ha='right')
ax.tick_params(axis='x', labelsize=8)

# Automatically adjust the subplot params for better layout
plt.tight_layout()

# Save figure to absolute path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/demo/histogram/png/603.png'
plt.savefig(save_path, format='png')

# Clear the current figure's state
plt.clf()
