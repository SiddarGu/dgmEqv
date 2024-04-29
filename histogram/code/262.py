import pandas as pd
import matplotlib.pyplot as plt

# Data provided
raw_data = """
Ticket Price Range ($),Number of Concerts
0-50,40
50-100,55
100-150,70
150-200,45
200-250,30
250-300,20
300-350,10
350-400,5
400-450,3
450-500,2
"""

# Transform data
lines = raw_data.strip().split('\n')
data_labels = lines[0].split(',')[1:]
line_labels = [row.split(',')[0] for row in lines[1:]]
data = [int(row.split(',')[1]) for row in lines[1:]]

# Convert data into a DataFrame
df = pd.DataFrame(data, index=line_labels, columns=data_labels)

# Create figure and add subplot
plt.figure(figsize=(12, 8))
ax = plt.subplot(111)

# Create histogram
df.plot(kind='bar', legend=False, ax=ax, color='skyblue', width=0.8)

# Add grid, labels, title, and customize axis labels
plt.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.7)
plt.xlabel('Ticket Price Range ($)', labelpad=15, fontsize=12)
plt.xticks(rotation=45, ha='right', wrap=True)
plt.ylabel('Number of Concerts', labelpad=15, fontsize=12)
plt.title('Price Distribution for Sports and Entertainment Events', pad=20, fontsize=15)

# Automatically adjust subplot params to give specified padding
plt.tight_layout()

# Save the image
save_path = '/cpfs01/user/liuqi/workspace/plotchart/demo/histogram/png/612.png'
plt.savefig(save_path, format='png')

# Clear the current figure state
plt.clf()
