
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[1000,4500,1000000], [800,4000,900000], [900,3500,800000], [1100,5000,700000]])

Country = np.array(["USA","UK","Germany","France"])
Hospitals = data[:,0]
Doctors = data[:,1]
Patients = data[:,2]

fig = plt.figure(figsize=(20,10))
ax = fig.add_subplot(111)
ax.bar(Country, Hospitals, width=0.2, color='b', align='center', label='Hospitals')
ax.bar(Country, Doctors, width=0.2, bottom=Hospitals, color='g', align='center', label='Doctors')
ax.bar(Country, Patients, width=0.2, bottom=Doctors+Hospitals, color='r', align='center', label='Patients')
ax.set_title("Number of hospitals, doctors and patients in four countries in 2021")
ax.set_xlabel("Country")
ax.set_ylabel("Numbers")
ax.legend(loc="upper right")

plt.xticks(Country)
plt.tight_layout()
plt.savefig("bar chart/png/505.png")
plt.clf()