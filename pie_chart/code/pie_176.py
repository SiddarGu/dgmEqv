
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8,8))
plt.title("Education Level Distribution in the USA, 2023", size=20, pad=20)
labels = ['High School diploma', 'Bachelor\'s degree', 'Associates\'s degree', 'Master\'s degree', 'Doctoral degree']
sizes = [30, 25, 20, 17, 8]
explode = [0.1, 0, 0, 0, 0]

plt.pie(sizes, labels=labels, autopct='%1.1f%%', explode=explode, shadow=True, startangle=90, radius=1.2)
plt.legend(loc='lower left', fontsize='large')
plt.tight_layout()
plt.savefig('pie chart/png/6.png', dpi=300)
plt.clf()