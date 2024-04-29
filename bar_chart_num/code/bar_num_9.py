
import matplotlib.pyplot as plt
import numpy as np

Country = ['USA', 'UK', 'Germany', 'France']
Hospitals = [500, 400, 350, 450]
Doctors = [3000, 3500, 4000, 3800]

fig = plt.figure(figsize=(13,7))
ax = fig.add_subplot()
ax.bar(Country, Hospitals, label='Hospitals')
ax.bar(Country, Doctors, bottom=Hospitals, label='Doctors')
ax.set_title("Number of hospitals and doctors in four countries in 2021")
ax.legend(loc='upper left')
ax.set_xlabel('Country')
ax.set_ylabel('Number of hospitals and doctors')

for i in range(len(Country)):
    ax.annotate(Hospitals[i], xy=(i-0.15, Hospitals[i]/2), fontsize=14)
    ax.annotate(Doctors[i], xy=(i-0.15, (Hospitals[i]+Doctors[i])/2), fontsize=14)

ax.set_xticks(np.arange(len(Country)))
ax.set_xticklabels(Country, rotation=45, fontsize=14, horizontalalignment='right')
plt.tight_layout()
plt.savefig('Bar Chart/png/172.png')
plt.clf()