
import matplotlib.pyplot as plt
import numpy as np

Country = ["USA", "UK", "Germany", "France"]
Doctors = np.array([450, 350, 400, 370])
Hospitals = np.array([200, 150, 180, 210])

fig = plt.figure(figsize=(7,4))
ax = fig.add_subplot(1,1,1)
ax.bar(Country, Doctors, label='Doctors', bottom=Hospitals)
ax.bar(Country, Hospitals, label='Hospitals')
ax.set_title('Number of doctors and hospitals in four countries in 2021')
ax.set_xticklabels(Country, rotation=45, ha="right", rotation_mode="anchor")
plt.legend()
plt.tight_layout()
plt.savefig('bar chart/png/220.png')
plt.clf()