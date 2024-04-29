
import matplotlib.pyplot as plt 
import numpy as np

region = np.array(['North','South','East','West'])
hospitals = np.array([20,25,30,35])
patients = np.array([20000,25000,30000,35000])

fig,ax = plt.subplots(figsize=(10,6))
ax.bar(region, hospitals, color='#0072BC', label='Hospitals')
ax.bar(region, patients, bottom=hospitals, color='#ED1C24', label='Patients')

for i in range(len(region)):
    ax.text(x = i-0.15 , y = hospitals[i] + patients[i]/2, s = patients[i], size = 14)
    ax.text(x = i-0.15 , y = hospitals[i]/2, s = hospitals[i], size = 14)

ax.set_title('Number of hospitals and patients in four regions in 2021', fontsize=16)
ax.set_xticks(region)
ax.set_ylabel('Number of hospitals and patients', fontsize=12)
ax.set_xlabel('Region', fontsize=12)
ax.legend(loc='upper left')

plt.tight_layout()
plt.savefig('Bar Chart/png/469.png')
plt.clf()