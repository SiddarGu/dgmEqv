import pandas as pd
import matplotlib.pyplot as plt

# Data provided
data_info = """
Criminal Law,1225
Civil Litigation,1569
Family Law,985
Corporate Law,500
Intellectual Property,350
Environmental Law,415
Labor and Employment,750
Tax Law,620
Real Estate,870
International Law,160
"""

# Parse the given data into lists
data_labels = ['Number of Cases Filed']
rows = data_info.strip().split("\n")
line_labels, data = zip(*(row.split(',') for row in rows))

# Convert the lists to the correct type
line_labels = list(line_labels)
data_values = [int(value) for value in data]

# Create a DataFrame for visualization
df = pd.DataFrame(data_values, index=line_labels, columns=data_labels)

# Create the figure and axis for the histogram
plt.figure(figsize=(10, 8))
ax = plt.subplot(111)

# Plot the histogram
df.plot(kind='bar', ax=ax, legend=False)

# Set title, labels and options
ax.set_title('Annual Case Filings by Category in the Legal System', fontsize=14)
ax.set_xlabel('Case Category', fontsize=12)
ax.set_ylabel('Number of Cases Filed', fontsize=12)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', fontsize=11, wrap=True)

# Fancying up the chart: setting a grid, color patterns
ax.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.7)
colors = plt.cm.viridis_r([x / len(data_values) for x in range(len(data_values))])
bars = ax.get_children()[0:10]  # Gets the bars
for bar, color in zip(bars, colors):
    bar.set_color(color)  # Apply color to each bar

# Adjust layout to prevent content from being displayed poorly
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/121.png'
plt.savefig(save_path, dpi=300)

# Clear the current figure state
plt.clf()
