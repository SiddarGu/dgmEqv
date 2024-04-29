
import matplotlib.pyplot as plt
import numpy as np

Country = ['USA', 'UK', 'Germany', 'France']
Manufacturing_Output = np.array([6000, 4000, 3500, 3000])
Export = np.array([900, 700, 1000, 800])

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot()
ax.bar(Country, Manufacturing_Output, width=0.5, label='Manufacturing Output(million)')
ax.bar(Country, Export, width=0.5, bottom=Manufacturing_Output, label='Export(million)')

ax.set_title('Manufacturing and export output in four countries in 2021')
ax.set_xticks(Country)
ax.legend(loc='upper left')
plt.tight_layout()

plt.savefig('bar chart/png/407.png')
plt.clf()