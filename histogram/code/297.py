import matplotlib.pyplot as plt
import pandas as pd

# Data preparation
data_str = """Visitors Per Day (Thousands),Website
0-50,30
50-100,25
100-150,20
150-200,18
200-250,15
250-300,12
300-350,8
350-400,5
400-450,3
450-500,2"""
data_lines = data_str.split("\n")
data_labels = data_lines[0].split(",")[1:]
line_labels = [line.split(",")[0] for line in data_lines[1:]]
data = [int(line.split(",")[1]) for line in data_lines[1:]]

# Converting data into a DataFrame
df = pd.DataFrame(data, index=line_labels, columns=data_labels)

# Creating figure and plotting
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
df.plot(kind='bar', color=['skyblue'], ax=ax)

# Adding fancy elements
ax.set_title('Daily Traffic Distribution Across Various Websites', fontsize=14)
ax.set_xlabel('Visitor Range')
ax.set_ylabel('Number of Visitors (Thousands)')
ax.grid(axis='y', linestyle='--')

# Avoid overlapping labels
ax.tick_params(axis='x', which='major', labelsize=7)
plt.xticks(rotation=45)
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/demo/histogram/png/647.png')

# Clearing the current image state
plt.clf()
plt.close(fig)
