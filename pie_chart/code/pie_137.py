
import matplotlib.pyplot as plt
import numpy as np

labels = ['Rail', 'Air', 'Sea', 'Road']
percentage = [30, 15, 20, 35]

fig,ax = plt.subplots(figsize=(9, 9))
ax.pie(percentage, labels=labels, autopct='%1.1f%%', startangle=90, pctdistance=0.85)

centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

ax.axis('equal')  
ax.set_title("Distribution of Transportation Modes in the USA, 2023")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("pie chart/png/261.png")
plt.clf()