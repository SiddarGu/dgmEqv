
import matplotlib.pyplot as plt
plt.figure(figsize=(10,5))
labels = ['Bachelor\'s Degree', 'Associate\'s Degree', 'High School', 'Master\'s Degree', 'Doctorate', 'Other']
sizes = [43, 22, 15, 10, 5, 5]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#f2a2a2','#cc99ff']
explode = [0, 0, 0, 0, 0, 0]

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, pctdistance=0.85, explode=explode)

centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.tight_layout()
plt.title('Education Level of Employees in the Workforce in 2023')
plt.axis('equal')
plt.savefig("pie chart/png/504.png")
plt.show()
plt.clf()