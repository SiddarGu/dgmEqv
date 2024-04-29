
import matplotlib.pyplot as plt
import numpy as np

Country= ['USA','UK','Germany','France']
Manufacturing_Output = np.array([1000,900,1100,800])
Export_Volume = np.array([400,500,600,700])

fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot()
ax.bar(Country, Manufacturing_Output, label='Manufacturing output', bottom=Export_Volume, color='#3F51B5')
ax.bar(Country, Export_Volume, label='Export Volume', color='#FF9800')
ax.set_title('Manufacturing output and export volume from four countries in 2021')

for i, v in enumerate(Manufacturing_Output):
    ax.text(i, v+100, str(v), ha='center', va='bottom')

for i, v in enumerate(Export_Volume):
    ax.text(i, v+100, str(v), ha='center', va='bottom')

plt.legend(loc='upper right')
plt.xticks(Country)
plt.tight_layout()
plt.savefig('Bar Chart/png/322.png')
plt.clf()