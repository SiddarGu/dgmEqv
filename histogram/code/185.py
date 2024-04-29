import matplotlib.pyplot as plt

# Given data set
raw_data = """
100-200,35
200-300,45
300-400,55
400-500,50
500-600,30
600-700,20
700-800,15
800-900,10
900-1000,5
1000+,3
"""

# Split the raw data into lines and then into labels and values
lines = raw_data.strip().split('\n')
data_labels = [line.split(',')[0] for line in lines]
data = [int(line.split(',')[1]) for line in lines]

# Create a new figure for the histogram
plt.figure(figsize=(10, 8))
ax = plt.subplot()

# Create a horizontal bar chart
ax.barh(data_labels, data, color='skyblue', edgecolor='black')

# Set the title of the figure
ax.set_title('Residential Property Sales Distribution by Price Range')

# Add grid for better readability
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Automatically adjust subplot params for better layout
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/185.png'
plt.savefig(save_path, format='png')

# Clear the current figure to prevent re-plotting the same data
plt.clf()
