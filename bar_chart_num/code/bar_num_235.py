
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot()

regions = ["North America", "South America", "Europe", "Asia"]
hospitals = [50,60,70,80]
doctors = [120,140,160,180]
nurses = [450,500,550,600]

x = range(len(regions))
bottom1 = [i+j for i,j in zip(hospitals, doctors)]
bottom2 = [i+j+k for i,j,k in zip(hospitals, doctors, nurses)]

ax.bar(x, hospitals, label='Hospitals', width=0.2)
ax.bar(x, doctors, label='Doctors', bottom=hospitals, width=0.2)
ax.bar(x, nurses, label='Nurses', bottom=bottom1, width=0.2)

for a,b in zip(x, bottom2):
    ax.annotate(str(b), xy=(a, b+20), color="g")

plt.title("Number of healthcare providers in four regions in 2021")
plt.xticks(x, regions)
plt.legend(loc="upper right")
plt.tight_layout()
plt.savefig("Bar Chart/png/493.png")
plt.clf()