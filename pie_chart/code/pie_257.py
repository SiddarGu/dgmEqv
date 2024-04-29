
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Create figure before plotting
fig, ax = plt.subplots(figsize=(10, 10))

# Plot the data
labels = ['Manufacturing', 'Distribution', 'Logistics', 'Machinery', 'Automation', 'Robotics']
sizes = [30, 20, 20, 15, 10, 5]
explode = (0.1, 0, 0, 0, 0, 0)
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax.axis('equal')

# Set the legend
manufacturing = mpatches.Patch(color='#ffb000', label='Manufacturing')
distribution = mpatches.Patch(color='#ff7800', label='Distribution')
logistics = mpatches.Patch(color='#ff7800', label='Logistics')
machinery = mpatches.Patch(color='#ff7800', label='Machinery')
automation = mpatches.Patch(color='#ff7800', label='Automation')
robotics = mpatches.Patch(color='#ff7800', label='Robotics')
plt.legend(handles=[manufacturing, distribution, logistics, machinery, automation, robotics], loc="best")

# Set the title
plt.title("Breakdown of Production Technologies in the Manufacturing Sector, 2023")

# Start to show the image, and automatically resize the image by tight_layout()
plt.xticks(rotation='vertical')
plt.tight_layout()

# Save the image as pie chart/png/414.png
plt.savefig('pie chart/png/414.png')

# Clear the current image state at the end of the code
plt.clf()