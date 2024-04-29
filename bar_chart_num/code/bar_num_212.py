
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(10, 6))

Country = ['USA', 'UK', 'Germany', 'France']
Lawyers = [50000, 40000, 45000, 35000]
Judges = [30000, 25000, 27000, 20000]

ax.bar(Country, Lawyers, label='Lawyers', bottom=Judges, color='#D9A620')
ax.bar(Country, Judges, label='Judges', color='#13294B')

for i, v in enumerate(Judges):
    ax.text(i-0.125, v+10000, v, fontsize='small', color='black')
for i, v in enumerate(Lawyers):
    ax.text(i-0.125, v+Judges[i]+10000, v, fontsize='small', color='black')

ax.set_xticks(Country)
ax.set_title('Number of Lawyers and Judges in Four Countries in 2021')
ax.set_ylabel('Number of People')
ax.legend(loc='upper right')

plt.tight_layout()
plt.savefig('Bar Chart/png/332.png')
plt.clf()