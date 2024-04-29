
import matplotlib.pyplot as plt
import numpy as np

labels = ['High School', "Associate's Degree","Bachelor's Degree","Master's Degree","Doctoral Degree"]
sizes = [25,20,30,15,10]
colors  = ['#FFD700','#FFA500','#FF8C00','#FF4500','#FF0000']

plt.figure(figsize=(6,4))
plt.pie(sizes, colors=colors, autopct='%1.1f%%',labels=labels,startangle=90,pctdistance=0.6,labeldistance=1.1,center=(0.5,0.5))
plt.title("Education Level Distribution in the USA, 2023",fontsize=18) 
plt.axis('equal')
plt.tight_layout()
plt.xticks(np.arange(0,1.1,0.1))
plt.savefig("pie chart/png/61.png")
plt.clf()