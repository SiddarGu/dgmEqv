
import matplotlib.pyplot as plt

# Set Figure size
plt.figure(figsize=(8,8))

# Create pie chart
subplot = plt.subplot()
labels = ["Renewable Energy","Coal","Natural Gas","Oil","Nuclear"]
percentage = [50,25,15,5,5]
pie_wedge_collection = subplot.pie(percentage, labels=labels, autopct='%.2f%%')

# Set title
plt.title("Distribution of Energy Sources in the US, 2023")

# Set legend
plt.legend(pie_wedge_collection[0],labels,bbox_to_anchor=(1,0.5), loc="center right", fontsize=10, 
           bbox_transform=plt.gcf().transFigure)

# Tighten layout
plt.tight_layout()

# Set ticks
subplot.set_xticks([])

# Save image
plt.savefig('pie chart/png/195.png', bbox_inches='tight')

# Clear image
plt.clf()