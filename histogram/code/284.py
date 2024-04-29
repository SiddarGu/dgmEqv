import matplotlib.pyplot as plt

# Provided data
data_labels = ['0-50', '50-100', '100-150', '150-200', '200-250', '250-300', '300-350', '350-400', '400-450']
line_labels = ['Number of Users']
data = [15000, 18000, 25000, 22000, 17000, 15000, 13000, 8000, 6000]

# Create the figure and a single subplot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)

# Plotting the histogram
ax.bar(data_labels, data, color='skyblue', edgecolor='black')

# Adding title and labels to the axes
ax.set_title('Monthly Internet Data Usage Among Users', fontsize=18)
ax.set_xlabel('Monthly Data Usage (TB)', fontsize=14)
ax.set_ylabel('Number of Users', fontsize=14)

# Enhancing the look of the histogram by adding grid, increasing label size and rotating if necessary
ax.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)
ax.tick_params(axis='x', labelsize=12, rotation=45)
ax.tick_params(axis='y', labelsize=12)

# Automatically adjust the subplot params to give specified padding
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/demo/histogram/png/634.png'
plt.savefig(save_path, format='png')

# Clear the current figure state
plt.clf()
