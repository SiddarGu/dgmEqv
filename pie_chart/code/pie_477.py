
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

labels = ['Renewable', 'Nuclear', 'Fossil Fuels', 'Other']
sizes = [38, 18, 34, 10]

plt.figure(figsize=(7, 7))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, wedgeprops={'linewidth': 2}, shadow=True)
plt.title('Energy Sources for Electricity Generation in the USA, 2023', fontsize=15, y=1.1)
plt.axis('equal')
plt.tight_layout()
plt.xticks([])
plt.savefig('pie chart/png/138.png')
plt.show()
plt.clf()