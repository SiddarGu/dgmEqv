
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

# Create figure 
fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(111)
 
# Pie chart
labels = 'Renewable','Nuclear','Natural Gas','Coal','Petroleum'
sizes = [45,15,20,10,10]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']
explode = (0.05, 0, 0, 0, 0)
plt.title('Distribution of Energy Sources in the USA, 2023')
ax.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True, startangle=90)
ax.axis('equal')

# legend
ax.legend(labels,loc='upper right', fontsize='small')

# xticks
plt.xticks(rotation=90)

# tight_layout
plt.tight_layout()

# save image
plt.savefig('pie chart/png/422.png')

# clear the current image state
plt.clf()