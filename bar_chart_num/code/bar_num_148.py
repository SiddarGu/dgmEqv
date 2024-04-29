
import matplotlib.pyplot as plt
import numpy as np

Country = ['USA','UK','Germany','France']
Lawyers = [1.2, 0.8, 1.0, 0.9]
Judges = [0.4, 0.3, 0.5, 0.4]

fig = plt.figure(figsize=(7.5,5.5))
ax = fig.add_subplot(111)
ax.bar(Country, Lawyers, color='#5DAF9F', label='Lawyers (thousands)', bottom=Judges)
ax.bar(Country, Judges, color='#D19FE3', label='Judges (thousands)')
plt.xticks(Country)
plt.legend(loc='best') 
plt.title('Number of Lawyers and Judges in four countries in 2021')
for i, v in enumerate(Lawyers):
    ax.text(i-0.2, v/2+Judges[i]+0.1, str(v), fontsize=11)
for i, v in enumerate(Judges):
    ax.text(i-0.2, v/2, str(v), fontsize=11)
plt.tight_layout()
plt.savefig('Bar Chart/png/155.png')
plt.clf()