

import matplotlib.pyplot as plt

plt.figure(figsize=(8, 8))

labels = ['North America','Europe','Asia','South America','Africa','Oceania']
sizes = [25, 25, 25, 13, 10, 2]

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 11}, labeldistance=1.2)

plt.title('Global Tourist Hotspots in 2023', fontsize=15)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=13)

plt.tight_layout()
plt.savefig('pie chart/png/501.png', bbox_inches='tight')
plt.show()
plt.clf()