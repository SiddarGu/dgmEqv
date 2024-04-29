
import matplotlib.pyplot as plt
import numpy as np

#Create figure and set figsize
fig = plt.figure(figsize=(8, 6))

ax = fig.add_subplot(111)

#Set data
Category = ['Music', 'Theatre', 'Art Galleries', 'Museums']
Expenditure = [140, 120, 160, 150]
Organizers = [25, 30, 35, 40]

#Create bar chart
x = np.arange(len(Category))
ax.bar(x, Expenditure, label='Expenditure', color='#007acc', width=0.4)
ax.bar(x+0.4, Organizers, label='Organizers', color='#e5ae37', width=0.4)

#Set x ticks
ax.set_xticks(x+0.4/2)
ax.set_xticklabels(Category)

#Set legend
plt.legend(loc='best')

#Set title
plt.title('Expenditure and number of organizers in four arts and culture categories in 2021')

#Set labels for each data point
for i, v in enumerate(Expenditure):
    ax.text(x[i] - 0.1,  v + 5, str(v))

for i, v in enumerate(Organizers):
    ax.text(x[i] + 0.3,  v + 5, str(v))

#Resize the image
plt.tight_layout()

#Save the image
plt.savefig('Bar Chart/png/192.png')

#Clear the current image state
plt.clf()