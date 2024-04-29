
import matplotlib.pyplot as plt

plt.figure(figsize=(8,6))
ax = plt.subplot()

Country = ['USA', 'UK', 'Germany', 'France']
Hospitals = [100, 80, 120, 90]
Patients = [20000, 15000, 18000, 17000]

ax.bar(Country, Hospitals, label='Hospitals')
ax.bar(Country, Patients, bottom=Hospitals, label='Patients')

ax.set_title('Number of hospitals and patients in four countries in 2021')
ax.set_xticklabels(Country, rotation=45, ha="right", rotation_mode="anchor")

ax.legend(loc='upper right')

plt.tight_layout()
plt.savefig('bar chart/png/458.png')
plt.clf()