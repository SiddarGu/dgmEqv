import matplotlib.pyplot as plt
import squarify  # Provides treemap layout algorithm

# Given data
data_raw = """
Energy Source,Usage (%)
Natural Gas,34
Coal,24
Nuclear,20
Renewables,12
Petroleum,8
Other,2
"""

# Process the data into separate lists
data_lines = data_raw.strip().split('\n')
data_labels = [line.split(',')[0] for line in data_lines[1:]]
data = [float(line.split(',')[1]) for line in data_lines[1:]]
line_labels = [line.split(',')[0] for line in data_lines[0:1]]

# Generate colors for each segment
colors = plt.cm.viridis(range(len(data_labels)), alpha=0.7)  # Adjust alpha for transparency

# Create a figure with larger size for better visibility
fig = plt.figure(figsize=(12, 8))

# Create a treemap
squarify.plot(sizes=data, label=data_labels, color=colors, pad=True)

# Add title
plt.title('Energy Utilization Breakdown by Source in the Utilities Sector')

# Remove the axes for a cleaner look
plt.axis('off')

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/demo/treemap/png/1001.png'
plt.savefig(save_path, bbox_inches='tight')

# Clear the current figure's state to prevent replotting
plt.clf()
