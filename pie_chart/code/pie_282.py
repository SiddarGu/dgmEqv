
import matplotlib.pyplot as plt

# Create figure
figure = plt.figure(figsize=(8,8))
ax = figure.add_subplot(1,1,1)

# Set data
labels = ['Single-Family Homes', 'Townhouses', 'Condominiums', 'Multi-Family Homes', 'Vacation Homes']
sizes = [45, 20, 20, 10, 5]

# Set color
colors = ['#D45F41','#5CB8E6','#FFCE54','#4DBD33','#444444']
explode = (0, 0, 0, 0, 0.1)

# Draw pie chart
ax.pie(sizes, colors=colors, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90, pctdistance=0.7,
        labeldistance=1.1, textprops={'fontsize': 14})

# Set title
ax.set_title('Types of Properties in the Housing Market in the USA, 2023', fontsize=18)

# Set legend
ax.legend(labels, bbox_to_anchor=(1.5, 0.7), shadow=False, fontsize=14)

# Save image
plt.tight_layout()
plt.savefig('pie chart/png/348.png')

# Clear current image state
plt.clf()