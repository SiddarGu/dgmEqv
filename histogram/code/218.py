import matplotlib.pyplot as plt

# Given data
data_labels = ['1-5', '6-10', '11-15', '16-20', '21-25', '26-30', '31-35', '36-40', '41-45']
data = [112, 90, 75, 60, 50, 30, 20, 12, 8]
line_labels = ['Artwork Sales']

# Create figure and add subplot
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# Plot histogram
ax.bar(data_labels, data, color='skyblue')

# Set title and labels
ax.set_title('Artwork Sales Related to Exhibition Duration')
ax.set_xlabel('Duration of Exhibition (Days)')
ax.set_ylabel('Artwork Sales')

# Customize ticks and labels
ax.set_xticklabels(data_labels, rotation=45, ha='right')
ax.yaxis.grid(True)

# Adjust layout to prevent content from being clipped and to resize automatically
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/218.png')

# Clear the current figure
plt.clf()
