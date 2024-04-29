
import matplotlib.pyplot as plt

labels = ['18-25', '26-35', '36-45', '46-55', '56+']
sizes = [25, 30, 20, 15, 10]

# Create figure and subplots
fig, ax = plt.subplots(figsize=(8, 8)) 

# Plot pie chart
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90,
       wedgeprops=dict(width=0.5))

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')  

# Add a title
ax.set_title('Age Distribution of Employees in the US in 2023')

# Custom legend
ax.legend(labels, bbox_to_anchor=(1.05, 0.5), loc="center left", 
          bbox_transform=plt.gcf().transFigure)

# Adjust figure
plt.tight_layout()

# Save figure
plt.savefig('pie chart/png/82.png')

# Clear the current image state
plt.clf()