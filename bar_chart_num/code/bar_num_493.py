
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)

Countries = ["USA","UK","Germany","France"]
Number_of_Laws = [1000, 900, 1100, 800]
Number_of_Cases = [1200, 1300, 1400, 1500]

rects1 = ax.bar(Countries, Number_of_Laws, bottom=Number_of_Cases, color='green')
rects2 = ax.bar(Countries, Number_of_Cases, color='orange')

ax.set_xticks(Countries)
ax.set_xticklabels(Countries, rotation=0, fontsize=13)
ax.set_title("Number of laws and cases in four countries in 2021")
ax.set_ylabel("Number")

ax.legend((rects1[0], rects2[0]), ('Number of Laws', 'Number of Cases'))

for index,rect in enumerate(rects1):
    height = rect.get_height()
    ax.annotate('{}'.format(Number_of_Laws[index]), xy=(rect.get_x() + rect.get_width() / 2, height), xytext=(0, 3), 
                textcoords="offset points", ha='center', va='bottom', fontsize=13)

for index,rect in enumerate(rects2):
    height = rect.get_height()
    ax.annotate('{}'.format(Number_of_Cases[index]), xy=(rect.get_x() + rect.get_width() / 2, height+Number_of_Laws[index]), xytext=(0, 3), 
                textcoords="offset points", ha='center', va='bottom', fontsize=13)

plt.tight_layout()
plt.savefig('Bar Chart/png/293.png', format='png', dpi=300)
plt.clf()