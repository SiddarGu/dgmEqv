import matplotlib.pyplot as plt
import squarify

# Parsing the input data
raw_data = """Travel Sector,Revenue Contribution (%)
Accommodation,30
Food Services,25
Travel Agencies,15
Leisure Activities,10
Transportation,10
Tourism Marketing,5
Convention Services,5"""

# Split the input data into lines
lines = raw_data.split('\n')

# Extract data and labels from the input data
data_labels = lines[0].split(',')[1:] 
line_labels = [line.split(',')[0] for line in lines[1:]]
data = [float(line.split(',')[1]) for line in lines[1:]]

# Draw the treemap
plt.figure(figsize=(12, 8))
squarify.plot(sizes=data, label=line_labels, alpha=0.8, text_kwargs={'fontsize':9, 'wrap':True})

# Add title and remove axes
plt.title('Percentage Distribution of Revenue in the Tourism and Hospitality Industry')
plt.axis('off')

# Automatically resize the image and save the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/225.png', format='png')

# Clear the current image state
plt.clf()
