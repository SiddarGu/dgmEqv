import matplotlib.pyplot as plt
import squarify

# Given data
raw_data = """
Subject Area,Research Funding (%)
Psychology,18
Sociology,15
History,15
Philosophy,12
Linguistics,10
Anthropology,10
Economics,10
Political Science,5
Cultural Studies,5
"""

# Transform the data into three variables
data_lines = raw_data.strip().split('\n')
data_labels = [label.strip() for label in data_lines[1:]]  # Extracting only labels for data
line_labels = [line.split(',')[0] for line in data_lines[1:]]  # Extracting line labels
data = [float(line.split(',')[1]) for line in data_lines[1:]]  # Extracting only the numerical values

# Create a treemap
fig = plt.figure(figsize=(12, 8))
squarify.plot(sizes=data, label=line_labels, alpha=0.8)
plt.title('Allocation of Research Funding in Social Sciences and Humanities')
plt.axis('off')

# Adjust layout to prevent content from being cut off
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/242.png'
plt.savefig(save_path, format='png')

# Clear the current figure's state
plt.clf()
