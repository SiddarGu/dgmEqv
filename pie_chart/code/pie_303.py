
import matplotlib
import matplotlib.pyplot as plt

labels = ['Male','Female']
sizes = [45,55]
colors = ['lightblue','pink']

plt.figure(figsize=(5,5))
plt.pie(sizes, colors=colors, labels=labels, autopct='%1.1f%%',textprops={'fontsize': 15}, startangle=90,pctdistance=0.85)

centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.axis('equal')  
plt.tight_layout()
plt.title('Gender Distribution among Employees in the USA, 2023',y=1.08)
plt.savefig('pie chart/png/221.png')

plt.clf()