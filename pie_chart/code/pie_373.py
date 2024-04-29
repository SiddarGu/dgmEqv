
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 8))

sources = ['Domestic Sources', 'International Sources']
percentage = [40, 60]

plt.pie(percentage, labels=sources, autopct='%1.1f%%', startangle=90,
        textprops={'fontsize': 14}, 
        wedgeprops={'edgecolor': 'black'},
        labeldistance=1.1,
        rotatelabels=True)

plt.title('Production Sources for the Manufacturing Industry, 2023', fontsize=20)
plt.tight_layout()
plt.savefig('pie chart/png/199.png')
plt.clf()