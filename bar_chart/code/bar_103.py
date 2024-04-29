
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)
ax.set_title('Number of hospitals, doctors and nurses in four countries in 2021')

country = ['USA', 'UK', 'Germany', 'France']
hospitals = [1000, 800, 900, 1200]
doctors = [9000, 8000, 7000, 6000]
nurses = [20000, 18000, 17000, 15000]

x = np.arange(len(country))
ax.bar(x - 0.2, hospitals, width=0.2, label='hospitals')
ax.bar(x, doctors, width=0.2, label='doctors')
ax.bar(x + 0.2, nurses, width=0.2, label='nurses')

ax.set_xticks(x)
ax.set_xticklabels(country, rotation=45, wrap=True)
ax.legend(loc='upper right')

plt.tight_layout()
plt.savefig('bar chart/png/3.png')
plt.clf()