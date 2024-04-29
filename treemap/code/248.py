import matplotlib.pyplot as plt
import squarify

# Given data in a string format
data_string = """Platform,Usage Share (%)
Facebook,25
YouTube,20
WhatsApp,15
Instagram,15
WeChat,10
TikTok,9
Reddit,3
Twitter,2
LinkedIn,1"""

# Extract labels and data
lines = data_string.split("\n")
data_labels = lines[0].split(",")[1:]
line_labels = [line.split(",")[0] for line in lines[1:]]
data = [float(line.split(",")[1]) for line in lines[1:]]

# Set up the figure size to make sure content is not cramped
plt.figure(figsize=(12, 8), dpi=100)

# Plot the Treemap
squarify.plot(sizes=data, label=line_labels, alpha=0.8, text_kwargs={'fontsize':10, 'wrap':True})

# Set the title of the figure
plt.title('Global Social Media Usage Share Distribution', fontsize=16)

# Hide axes
plt.axis('off')

# Automatically resize the image
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/248.png'
plt.savefig(save_path, format='png')

# Clear the current figure's state to avoid any overlay with upcoming plots
plt.clf()
