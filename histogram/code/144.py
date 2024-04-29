import matplotlib.pyplot as plt

# Data provided
data_str = """
CO2 Emission Range (MtCO2),Number of Countries
0-10,50
10-20,30
20-30,25
30-40,15
40-50,10
50-60,5
60-70,3
70-80,2
80-90,1
90-100,1
"""

# Parsing the data into the required variables
data_lines = data_str.strip().split('\n')
data_labels = data_lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in data_lines[1:]]
data = [list(map(float, line.split(',')[1:])) for line in data_lines[1:]]

# Initialize the matplotlib figure with larger figsize
fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(111)

# Add grid for better readability
ax.set_axisbelow(True)
ax.yaxis.grid(color='gray', linestyle='dashed', alpha=0.7)

# Create the histograms
for index in range(len(data)):
    ax.bar(line_labels[index], data[index], align='center', label=line_labels[index])

# Set title and labels
plt.title('Global Distribution of CO2 Emissions by Country')
plt.xlabel('CO2 Emission Range (MtCO2)')
plt.ylabel('Number of Countries')

# Auto-rotate x-axis labels to prevent overlap if needed
plt.xticks(rotation=45, ha='right')

# Automatically resize the plot area before saving
plt.tight_layout()

# Save the image
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/144.png'
plt.savefig(save_path, format='png')

# Clear the current figure's state to prevent re-draws on re-execution of the cell
plt.clf()
