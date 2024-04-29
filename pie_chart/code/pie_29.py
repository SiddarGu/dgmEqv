
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# Create figure
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)

# Data
labels = ['Adventure','Cultural','Nature','City','Luxury']
sizes = [20,25,15,25,15]

# Plotting the pie chart
ax.pie(sizes, labels=labels, autopct='%1.1f%%', textprops={'fontsize': 18})

# Customizing the pie chart
ax.set_title('Global Distribution of Different Types of Tourism in 2023', fontsize=20)
ax.legend(bbox_to_anchor=(1, 0.8), loc="lower right", fontsize=14)
ax.axis('equal')

# Resizing the image
plt.tight_layout()

# Save the image
plt.savefig('pie chart/png/487.png', bbox_inches='tight')

# Clear the current image state
plt.clf()