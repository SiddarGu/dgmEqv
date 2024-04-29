
import matplotlib.pyplot as plt
import numpy as np

Region = ['North', 'South', 'East', 'West']
Hospital_Beds = [400, 350, 450, 500]
Doctors = [1500, 1300, 1700, 2000]

plt.figure(figsize=(8,6))
ax = plt.subplot()
ax.bar(Region, Hospital_Beds, label='Hospitals Beds', width=0.4, bottom=0, align='edge', color='b')
ax.bar(Region, Doctors, label='Doctors', width=0.4, bottom=Hospital_Beds, align='edge', color='r')

for i, v in enumerate(Hospital_Beds):
    ax.text(i-0.3, v+20, str(v), color='b', fontsize=12)
for i, v in enumerate(Doctors):
    ax.text(i-0.3, v+20, str(v), color='r', fontsize=12)

plt.title('Availability of Hospital Beds and Doctors in Four Regions in 2021')
plt.xlabel('Region')
plt.ylabel('Number')
plt.legend(loc='upper right')
plt.xticks(np.arange(len(Region)), Region)
plt.tight_layout()
plt.savefig('Bar Chart/png/564.png')
plt.clf()