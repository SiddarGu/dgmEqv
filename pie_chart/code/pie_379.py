
import matplotlib.pyplot as plt
import matplotlib as mpl

# Set the figure size
plt.figure(figsize=(10,6))

# Create the pie chart
types_houses = ["Single Detached Houses","Apartments","Semi-Detached Houses","Townhouse","Mobile Homes"]
percentage = [40,25,15,10,10]
plt.pie(percentage,labels=types_houses, autopct='%.1f%%',startangle=90,textprops={'fontsize': 10})

# Set the title
plt.title("Distribution of Housing Types in USA, 2023",fontsize=15)

# Add the legend
plt.legend(loc="best", bbox_to_anchor=(1, 0, 0.3, 1))

# Rotate the label
plt.xticks(rotation=45)

# Resize the figure to prevent content from being displayed
plt.tight_layout()

# Save the figure
plt.savefig('pie chart/png/133.png')

# Clear the image state
plt.clf()