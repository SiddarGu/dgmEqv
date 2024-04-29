
import matplotlib.pyplot as plt

plt.figure(figsize=(15, 7))
x = ["USA", "UK", "Germany", "France"]
hospitals = [300, 400, 250, 350]
doctors = [25000, 20000, 23000, 22000]
patients = [200000, 180000, 170000, 190000]

ax = plt.subplot()
ax.bar(x, hospitals, label="Hospitals")

bottom = [i + j for i, j in zip(hospitals, doctors)]
ax.bar(x, doctors, bottom=hospitals, label="Doctors")

bottom = [i + j for i, j in zip(bottom, patients)]
ax.bar(x, patients, bottom=bottom, label="Patients")

ax.set_title("Number of hospitals, doctors and patients in four countries in 2021")
ax.set_xticks(x)
ax.legend(loc="upper left")
ax.annotate(300, xy=(0, 300), xytext=(-0.1, 350), fontsize=10)
ax.annotate(25000, xy=(0, 25000), xytext=(-0.1, 30000), fontsize=10)
ax.annotate(200000, xy=(0, 200000), xytext=(-0.1, 250000), fontsize=10)
ax.annotate(400, xy=(1, 400), xytext=(0.9, 450), fontsize=10)
ax.annotate(20000, xy=(1, 20000), xytext=(0.9, 25000), fontsize=10)
ax.annotate(180000, xy=(1, 180000), xytext=(0.9, 230000), fontsize=10)
ax.annotate(250, xy=(2, 250), xytext=(1.9, 300), fontsize=10)
ax.annotate(23000, xy=(2, 23000), xytext=(1.9, 28000), fontsize=10)
ax.annotate(170000, xy=(2, 170000), xytext=(1.9, 220000), fontsize=10)
ax.annotate(350, xy=(3, 350), xytext=(2.9, 400), fontsize=10)
ax.annotate(22000, xy=(3, 22000), xytext=(2.9, 27000), fontsize=10)
ax.annotate(190000, xy=(3, 190000), xytext=(2.9, 240000), fontsize=10)

plt.tight_layout()
plt.savefig("Bar Chart/png/178.png")
plt.clf()