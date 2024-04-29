
import matplotlib.pyplot as plt

# Create figure
plt.figure(figsize=(6, 6), dpi=100)

# Data to plot
labels = ['Undergraduate', 'Graduate', 'Doctorate', 'Post-Doctorate', 'Other']
sizes = [45, 35, 10, 5, 5]

# Plot
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 14})

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')  

# Plot Title
plt.title('Distribution of Student Levels in the USA in 2023', fontsize=16)

# Save the figure
plt.savefig('pie chart/png/84.png', bbox_inches='tight')

# Clear the image state
plt.clf()