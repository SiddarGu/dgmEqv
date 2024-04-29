
import matplotlib.pyplot as plt

#setting figure size
plt.figure(figsize=(10,5))

#set subplot
ax = plt.subplot()

#set legend
labels = ['18-24','25-34','35-44','45-54','55-64','65+']

#set data 
sizes = [25,20,18,16,12,9]

#set colors
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#ffb3e6','#c2c2f0']

#plot pie chart
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
        shadow=True, startangle=90, pctdistance=0.85)

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')  

#set title
plt.title("Age Distribution of the US Population in 2023")

#set legend
ax.legend(labels, loc='upper right', bbox_to_anchor=(1.2, 0.5))

#resize fig
plt.tight_layout()

#save
plt.savefig('pie chart/png/207.png')

#clear
plt.clf()