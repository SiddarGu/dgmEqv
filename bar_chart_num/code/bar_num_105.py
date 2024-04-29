
import matplotlib.pyplot as plt
import numpy as np

data = [['USA', 80000, 4000, 300000],
        ['UK', 60000, 2500, 230000],
        ['Germany', 75000, 3000, 270000],
        ['France', 70000, 3500, 250000]]

Country, Physicians, Hospitals, Nurses = [list(i) for i in zip(*data)]

x = np.arange(4)
width = 0.25

fig, ax = plt.subplots(figsize=(12, 8))
ax.bar(x, Physicians, width, label='Physicians')
ax.bar(x + width, Hospitals, width, label='Hospitals')
ax.bar(x + width + width, Nurses, width, label='Nurses')

ax.set_title('Number of physicians, hospitals and nurses in four countries in 2021')
ax.set_xticks(x + width)
ax.set_xticklabels(Country)
ax.legend(loc='best')

for i in range(len(Country)):
    ax.annotate('{}'.format(Physicians[i]), xy=(x[i], Physicians[i]), xytext=(0, 3), 
    textcoords="offset points", ha='center', va='bottom', rotation=45)
    ax.annotate('{}'.format(Hospitals[i]), xy=(x[i] + width, Hospitals[i]), xytext=(0, 3), 
    textcoords="offset points", ha='center', va='bottom', rotation=45)
    ax.annotate('{}'.format(Nurses[i]), xy=(x[i] + width + width, Nurses[i]), xytext=(0, 3), 
    textcoords="offset points", ha='center', va='bottom', rotation=45)

plt.tight_layout()
plt.savefig('Bar Chart/png/336.png')
plt.clf()