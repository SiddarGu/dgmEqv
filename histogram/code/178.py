import matplotlib.pyplot as plt

# Given data
data_raw = """Freight Type,Revenue ($ Billion)
Road,123.45
Rail,84.21
Air,95.34
Water,76.89
Pipeline,64.22
Intermodal,58.76"""

# Split the data into lines and then into labels and values
lines = data_raw.strip().split('\n') # Remove whitespace and split by lines
data_labels = lines[0].split(',')[1:] # The first row and from the second column
data_tuples = [line.split(',') for line in lines[1:]] # Split the rest of the data
line_labels = [d[0] for d in data_tuples] # Get the first column for line labels
data = [float(d[1]) for d in data_tuples] # Convert the second column to floats

# Plot configuration
fig = plt.figure(figsize=(10, 8))  # Set the figure size to prevent cramped display
ax = fig.add_subplot(111)

# Create the histogram
ax.bar(line_labels, data, color='skyblue', edgecolor='black')

# Set title and labels
ax.set_title('U.S. Transportation Revenue by Freight Type (2023)', fontsize=15)
ax.set_xlabel('Freight Type', fontsize=12)
ax.set_ylabel('Revenue ($ Billion)', fontsize=12)

# Rotate the x-axis labels if they are too long
plt.xticks(rotation=45, ha='right')

# To prevent clipping of the label at the bottom
plt.tight_layout()

# Adding a grid for better readability
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/178.png'
plt.savefig(save_path, format='png')

# Clear the figure to prevent replotting issues later
plt.clf()
