
import matplotlib.pyplot as plt
import numpy as np

labels = ['Grains','Fruits and Vegetables','Dairy Products','Nuts and Seeds','Livestock','Other']
values = [30,25,15,10,10,10]

plt.figure(figsize=(8,6))
ax = plt.subplot()
explode = (0, 0, 0, 0, 0.2, 0)
ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, pctdistance=0.85, explode=explode, textprops={'fontsize':14})
ax.set_title('Distribution of Agricultural Output in the USA,2023', fontsize=18)
centre_circle = plt.Circle((0,0),0.70,fc='white')
ax.add_artist(centre_circle)
plt.tight_layout()
plt.savefig('pie chart/png/375.png')
plt.clf()