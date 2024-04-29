
import matplotlib.pyplot as plt

#Set labels and titles
labels = ['Manufacturing','Agricultural','Service'] 
countries = ['USA','UK','Germany','France'] 
title = 'Manufacturing, Agricultural, and Service Output of four countries in 2021'

#Set the figure size
plt.figure(figsize=(10,6))

#Create a subplot
ax = plt.subplot()

#Set the data
x_pos = [i for i, _ in enumerate(countries)]
manufacturing_data = [2.5,1.8,2.2,2.1]
agricultural_data = [1.2,1.3,1.4,1.5]
service_data = [3.4,2.7,3.1,2.9]

#Draw bar chart
ax.bar(x_pos,manufacturing_data,width=0.2,label=labels[0])
ax.bar([x + 0.2 for x in x_pos],agricultural_data,width=0.2,label=labels[1])
ax.bar([x + 0.4 for x in x_pos],service_data,width=0.2,label=labels[2])

#Set x axis
ax.set_xticks([x + 0.2 for x in x_pos])
ax.set_xticklabels(countries)

#Set y axis
ax.set_ylabel('Output(billion)')

#Set title
ax.set_title(title)

#Add legend
ax.legend(loc='upper right')

#Automatically resize the image
plt.tight_layout()

#Save the image
plt.savefig('bar chart/png/345.png')

#Clear the current image state
plt.clf()