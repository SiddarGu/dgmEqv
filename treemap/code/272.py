import matplotlib.pyplot as plt
import squarify

# Given data string
data_str = """Category,Attendance (%)
Museums,25
Live Music,20
Theater,15
Film Screenings,12
Art Galleries,10
Dance Performances,8
Literary Events,5
Opera,3
Cultural Festivals,2"""

# Parsing the data string into the desired variables
lines = data_str.split('\n')
data_labels = lines[0].split(',')[1:]  # 'Attendance (%)'

# Extract line_labels and data
line_labels = []
data = []
for line in lines[1:]:
    parts = line.split(',')
    line_labels.append(parts[0])
    data.append(float(parts[1]))  # convert string to float for the data part

# Plotting with squarify
fig = plt.figure(figsize=(12, 8))
squarify.plot(sizes=data, label=line_labels, alpha=0.8)

# Set the title of the figure
plt.title('Public Engagement in Arts and Culture Events')

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/demo/treemap/png/1022.png'
plt.savefig(save_path, format='png')

# Clear the current image state at the end of the code
plt.clf()
