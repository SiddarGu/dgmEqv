import matplotlib.pyplot as plt

# Data processing
data = """
Painting Genre,Artworks Sold
Renaissance,120
Impressionism,95
Modernism,78
Abstract,65
Surrealism,58
Pop Art,50
Cubism,45
Expressionism,30
Minimalism,25
"""
lines = data.strip().split('\n')
data_labels = lines[0].split(',')[1:]  # excluding first column
line_labels = [line.split(',')[0] for line in lines[1:]]  # excluding first row
data_values = [int(line.split(',')[1]) for line in lines[1:]]

# Create the figure and axis objects
fig = plt.figure(figsize=(10, 8))  # setting a larger figsize
ax = fig.add_subplot(111)

# Create horizontal bar chart
ax.barh(line_labels, data_values, color=plt.cm.Paired.colors, edgecolor='black')

# Adding data labels for each bar
for index, value in enumerate(data_values):
    ax.text(value, index, str(value), color='black', va='center')

# Set title and labels
ax.set_title('Sales of Artworks by Painting Genre')
ax.set_xlabel('Number of Artworks Sold')
plt.yticks(wrap=True)

# Set grid
ax.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)

# Ensure the labels on Y-axis are fully readable by rotating them or using wrap=True
plt.xticks(rotation=45)

# Automatically adjust subplot params so that the subplot(s) fits in to the figure area
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/1002.png'
plt.savefig(save_path, format='png')

# Clear the current figure state to avoid overlap with further plots
plt.clf()
