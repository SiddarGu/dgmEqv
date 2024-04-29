import matplotlib.pyplot as plt
import squarify

# Given data in a string format.
data_string = """Region,Tourist Visits (%)
Europe,30
Asia-Pacific,25
North America,20
South America,10
Middle East,8
Africa,5
Oceania,2"""

# Splitting the data string into lines and then into labels and values.
lines = data_string.strip().split('\n')
data_labels = ["Tourist Visits (%)"]
line_labels = [line.split(',')[0] for line in lines[1:]]  # Exclude the header
data = [float(line.split(',')[1]) for line in lines[1:]]  # Exclude the header

# Now plotting the treemap.
fig = plt.figure(figsize=(12, 8))
squarify.plot(sizes=data, label=line_labels, alpha=0.7)

# Set title and remove axes.
plt.title("Global Tourist Visits Distribution by Region")
plt.axis('off')

# Resize plot based on the parameters set previously.
plt.tight_layout()

# Specify the exact path to save the image.
save_path = "/cpfs01/user/liuqi/workspace/plotchart/demo/treemap/png/1045.png"
plt.savefig(save_path, format='png', bbox_inches='tight')

# Clear the current figure.
plt.clf()
