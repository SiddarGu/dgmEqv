import pandas as pd
import matplotlib.pyplot as plt

# Given data
data_labels = ['Crime Category', 'Number of Cases']
line_labels = ['Assault', 'Burglary', 'Cybercrime', 'Drug Offenses', 'Fraud', 
               'Human Trafficking', 'Robbery', 'White Collar Crimes', 'Environmental Crimes']
data = [3500, 1500, 1200, 2700, 2100, 700, 900, 1100, 400]

# Transforming the data
df = pd.DataFrame(data, index=line_labels, columns=[data_labels[1]])

# Create the figure and the axes
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

# Plotting the data
df.plot(kind='bar', ax=ax, color='skyblue')

# Set the title
ax.set_title('Annual Number of Legal Cases by Crime Category')

# Set x-axis label
ax.set_xlabel(data_labels[0])

# Set y-axis label
ax.set_ylabel(data_labels[1])

# Enable grid
ax.grid(True)

# Rotate x-axis labels if they are too long
ax.set_xticklabels(line_labels, rotation=45, ha="right")

# Automatically resize the image and layout
plt.tight_layout()

# Save the image to the absolute path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/demo/histogram/png/630.png'
plt.savefig(save_path, format='png', dpi=300)

# Clear the current image state
plt.clf()
