import matplotlib.pyplot as plt
import squarify

# Given data
raw_data = """
Hospitality Segment,Revenue Share (%)
Hotels,40
Restaurants,30
Travel Agencies,15
Theme Parks,8
Cruises,4
Tourist Attractions,3
"""

# Processing data into separate variables
# Convert raw data into lines and split each line into parts
lines = raw_data.strip().split("\n")
data_labels = lines[0].split(",")[1:]  # Labels of each column except the first column
line_labels = [line.split(",")[0] for line in lines[1:]]  # Labels for rows
data = [float(line.split(",")[1]) for line in lines[1:]]  # Numerical data

# Plotting treemap
plt.figure(figsize=(12, 8))  # Set a larger figure size to prevent content from being cut
# Use squarify to plot the treemap
squarify.plot(sizes=data, label=line_labels, alpha=0.7)
plt.title("Revenue Share in the Tourism and Hospitality Industry")
plt.axis('off')  # Disable the axis

# To avoid label text overlapping, we may need to adjust the text properties
plt.rc('font', size=10)  # Adjust font size as necessary to fit long text
plt.tight_layout()  # Automatically adjust the subplot params to give specified padding

# Save the figure to the specified path
save_path = "/cpfs01/user/liuqi/workspace/plotchart/demo/treemap/png/1007.png"
plt.savefig(save_path, dpi=300)  # Save with high dpi for clarity

# Clear the current figure's state
plt.clf()
