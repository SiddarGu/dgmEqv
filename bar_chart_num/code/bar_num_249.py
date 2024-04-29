
import matplotlib.pyplot as plt
import numpy as np

Country = ["USA", "UK", "Germany", "France"]
Hospitals = [200, 150, 175, 225]
Doctors = [2500, 2000, 1800, 2200]
Patients = [3000, 2700, 2500, 3000]

x = np.arange(len(Country))

plt.figure(figsize=(8,6))

p1 = plt.bar(x, Hospitals, label='Hospitals')
p2 = plt.bar(x, Doctors, bottom=Hospitals, label='Doctors')
p3 = plt.bar(x, Patients, bottom=np.array(Hospitals)+np.array(Doctors), label='Patients')

plt.xticks(x, Country)
plt.ylabel("Number")
plt.title("Number of hospitals, doctors and patients in four countries in 2021")
plt.legend()

for i in range(len(Country)):
    plt.annotate(Hospitals[i], xy=(p1[i].get_x() + p1[i].get_width() / 2, p1[i].get_height()/2), ha='center', va='center', rotation=90)
    plt.annotate(Doctors[i], xy=(p2[i].get_x() + p2[i].get_width() / 2, p2[i].get_height()/2 + p1[i].get_height()), ha='center', va='center', rotation=90)
    plt.annotate(Patients[i], xy=(p3[i].get_x() + p3[i].get_width() / 2, p3[i].get_height()/2 + p2[i].get_height() + p1[i].get_height()), ha='center', va='center', rotation=90)
plt.tight_layout()
plt.savefig("Bar Chart/png/61.png")
plt.clf()