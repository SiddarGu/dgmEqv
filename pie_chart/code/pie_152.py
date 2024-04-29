
import matplotlib.pyplot as plt

plt.figure(figsize=(10,5))
ax = plt.subplot()
labels = ['High School', "Bachelor's Degree", "Master's Degree", 'Doctorate Degree', 'Professional Degree'] 
sizes = [30, 25, 20, 15, 10]
explode = [0, 0, 0, 0, 0]
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=180,  textprops={'fontsize': 10, 'wrap': True, 'rotation': 0})
ax.set_title("Educational Attainment in the USA, 2023")
plt.tight_layout()
plt.xticks(rotation=0)
plt.savefig('pie chart/png/66.png')
plt.clf()