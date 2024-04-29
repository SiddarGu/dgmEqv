
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(8, 5))

Country = ['USA', 'UK', 'Germany', 'France']
Museums = [200, 180, 220, 190]
Galleries = [150, 130, 170, 140]
Theatres = [100, 80, 120, 90]
x = np.arange(len(Country))

ax.bar(x, Museums, label='Museums', color='#999999')
ax.bar(x, Galleries, label='Galleries', bottom=Museums, color='#CCCCCC')
ax.bar(x, Theatres, label='Theatres', bottom=np.array(Museums)+np.array(Galleries), color='#E5E5E5')
ax.set_xticks(x)
ax.set_xticklabels(Country)
ax.set_title('Number of Arts and Culture facilities in four countries in 2021')
ax.legend(loc='upper left')

for i in range(len(Country)):
    ax.annotate(Museums[i], xy=(x[i] - 0.2, Museums[i] + 5), rotation=90)
    ax.annotate(Galleries[i], xy=(x[i] - 0.2, Museums[i] + Galleries[i] + 5), rotation=90)
    ax.annotate(Theatres[i], xy=(x[i] - 0.2, Museums[i] + Galleries[i] + Theatres[i] + 5), rotation=90)

fig.tight_layout()
plt.savefig('Bar Chart/png/401.png')
plt.clf()