import matplotlib.pyplot as plt

# Given data
data_labels = ['0-10', '10-25', '25-50', '50-75', '75-100', '100-150', '150-200', '200-300', '300-500', '500+']
line_labels = ['Number of Households (Millions)']
data = [2, 8, 15, 20, 22, 18, 10, 5, 3, 2]

# Create the figure and axis
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(1, 1, 1)

# Create the histogram
bars = ax.bar(data_labels, data, color=plt.cm.Paired(range(len(data_labels))))

# Add the grid, labels, and title
ax.set_xlabel('Internet Speed (Mbps)')
ax.set_ylabel('Number of Households (Millions)')
ax.set_title('Distribution of Household Internet Speeds')
plt.xticks(rotation=45, horizontalalignment="right")
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Resize the image properly
plt.tight_layout()

# Saving the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/226.png'
plt.savefig(save_path, format='png')

# Clear the current figure
plt.clf()
