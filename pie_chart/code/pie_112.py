
import matplotlib.pyplot as plt

labels = ['Wheat','Rice','Maize','Soybean','Other']
sizes = [30,25,20,15,10]

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)
ax.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90, pctdistance=0.9, labeldistance=1.2)
plt.title('Distribution of Major Crops in the World, 2023', fontsize=20)
plt.axis('equal')
plt.tight_layout()
plt.xticks(rotation=0)
plt.savefig('pie chart/png/72.png', bbox_inches='tight')
plt.clf()