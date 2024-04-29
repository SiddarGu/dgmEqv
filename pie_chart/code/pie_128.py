
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

#Create figure 
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)

#Data
labels=['Education', 'Healthcare', 'Technology', 'Business', 'Arts and Entertainment', 'Government']
sizes=[20,25,15,20,10,10]

#Pie chart
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 12})

#Title
ax.set_title('Job Distribution in the US, 2023')

#Legend
ax.legend(loc="upper right", bbox_to_anchor=(1.2,1))

#No extra words
plt.tight_layout()

#Save figure
plt.savefig('pie chart/png/426.png')

#Clear figure
plt.clf()