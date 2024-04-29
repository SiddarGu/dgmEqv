import matplotlib.pyplot as plt
import squarify

# Given data in a raw string format
raw_data = """
Internet Activity,Usage Share (%)
Social Media,25
Streaming Services,20
E-commerce,15
Online Gaming,13
Email Communication,10
Cloud Services,9
Online Education,5
Cybersecurity,3
"""

# Process the raw_data into the required format
lines = raw_data.strip().split('\n')
data_labels = lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in lines[1:]]
data = [float(line.split(',')[1]) for line in lines[1:]]

# Set the size of the figure (this is adjusted to be a bit larger)
plt.figure(figsize=(12, 8), dpi=100)

# Create a color palette, mapped to data values
cmap = plt.cm.viridis
mini=min(data)
maxi=max(data)
norm = plt.Normalize(vmin=mini, vmax=maxi)
colors = [cmap(norm(value)) for value in data]

# Plotting the treemap
squarify.plot(sizes=data, label=line_labels, color=colors, alpha=0.8, text_kwargs={'fontsize':9})

# Set the title of the figure and adjust the layout
plt.title('Share of Internet Activities in the Digital Era', fontsize=18)

# Ensure the entire layout is within the figure limits and text is clear
plt.axis('off')
plt.tight_layout()

# Save the figure (making sure to include the absolute path)
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/116.png'
plt.savefig(save_path, format='png', bbox_inches='tight')

# Clear current figure state to prevent reuse
plt.clf()
