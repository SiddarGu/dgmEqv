import matplotlib.pyplot as plt
import squarify

# Raw data
raw_data = """Education Level,Enrollment Rate (%)
Preschool,5
Elementary,25
Middle School,20
High School,30
Undergraduate,15
Postgraduate,5"""

# Parse the raw data
lines = raw_data.split("\n")
data_labels = lines[0].split(",")[1:]
line_labels = [line.split(",")[0] for line in lines[1:]]
data = [int(line.split(",")[1]) for line in lines[1:]]

# Plot the treemap
plt.figure(figsize=(12, 8))
squarify.plot(sizes=data, label=line_labels, alpha=0.8, text_kwargs={'wrap': True})
plt.title('Enrollment Rates Across Various Educational Levels')
plt.axis('off')

# Automatically resize the image
plt.tight_layout()

# Save the image
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/135.png'
plt.savefig(save_path, bbox_inches='tight', dpi=300)

# Clear the current image state
plt.clf()
