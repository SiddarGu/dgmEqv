import pandas as pd
import matplotlib.pyplot as plt

# Data provided
data_str = """Product Defect Rate (%),Number of Facilities
0-2,30
2-4,45
4-6,25
6-8,10
8-10,5
10-12,3
12-14,2
14-16,1"""

# Transform the data into a DataFrame
data_lines = data_str.split('\n')
data_labels = data_lines[0].split(',')
line_labels = [line.split(',')[0] for line in data_lines[1:]]
data = [line.split(',')[1] for line in data_lines[1:]]
data_float = list(map(float, data))  # Convert data strings to float

# Creating the DataFrame
df = pd.DataFrame(list(zip(line_labels, data_float)), columns=data_labels)

# Plotting
plt.figure(figsize=(10, 7))  # Set the figure size to prevent content from being cramped
ax = plt.subplot(111)
ax.bar(df['Product Defect Rate (%)'], df['Number of Facilities'])

# Set title and labels
plt.title('Facility Quality Performance: Product Defect Rates in Manufacturing')
plt.xlabel('Product Defect Rate (%)')
plt.ylabel('Number of Facilities')

# Add grid, improve layout and wrap text for long labels
ax.set_xticks(df['Product Defect Rate (%)'])
ax.set_xticklabels(df['Product Defect Rate (%)'], rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Save figure to the specified path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/164.png'
plt.savefig(save_path, dpi=300)  # Save with high resolution

# Clear the current figure state
plt.clf()
