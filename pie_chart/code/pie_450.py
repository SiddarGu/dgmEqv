
import matplotlib.pyplot as plt

labels = ['Coal','Natural Gas','Nuclear','Renewables','Oil']
sizes = [20,30,20,25,5]

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)

ax.pie(sizes,labels=labels,autopct='%1.1f%%',shadow=True,startangle=90)
ax.axis('equal')
ax.set_title('Distribution of Energy Sources in the USA in 2023')

plt.xticks(rotation=45,ha='right')
plt.tight_layout()
plt.savefig('pie chart/png/308.png')
plt.clf()