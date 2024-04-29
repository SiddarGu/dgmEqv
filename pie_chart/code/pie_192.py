
import matplotlib.pyplot as plt
labels = ['Individuals','Foundations','Corporations','Government','Other']
sizes = [45,25,15,10,5]
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax.axis('equal')
ax.legend(loc='upper left', bbox_to_anchor=(-0.1, 1.))
ax.set_title('Distribution of Donors in the Nonprofit Sector,2023', fontsize=20)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('pie chart/png/181.png')
plt.clf()