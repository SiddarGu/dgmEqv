
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
ax = plt.subplot()
ax.bar(['USA','UK','Germany','France'], [450,350,400,400], label='Hospitals', width=0.2, color='b')
ax.bar(['USA','UK','Germany','France'], [3000,2000,2500,2300], bottom=[450,350,400,400], label='Doctors', width=0.2, color='g')
ax.bar(['USA','UK','Germany','France'], [1000000,800000,900000,950000], bottom=[4350,2350,4200,4200], label='Patients', width=0.2, color='r')
ax.set_title('Number of hospitals, doctors and patients in four countries in 2021')
ax.set_xticklabels(['USA','UK','Germany','France'], rotation=45, ha='right')
ax.legend(loc='upper left')
ax.grid(linestyle='--', color='gray', alpha=0.5)
plt.tight_layout()
plt.savefig('bar chart/png/486.png')
plt.clf()