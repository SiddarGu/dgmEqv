
import matplotlib.pyplot as plt
import numpy as np

Country = ['USA','UK','Germany','France']
Doctors = [260, 350, 450, 400]
Nurses = [600, 800, 1000, 950]
Hospital_Beds = [735, 890, 930, 860]

fig = plt.figure(figsize=(15,7))
ax = fig.add_subplot()
ax.bar(Country, Doctors, label='Doctors', width=.2, bottom=Nurses)
ax.bar(Country, Nurses, label='Nurses', width=.2, bottom=Hospital_Beds)
ax.bar(Country, Hospital_Beds, label='Hospital Beds', width=.2)

ax.set_xticklabels(Country, rotation=0, wrap=True)
ax.set_title('Healthcare professionals and hospital beds in four countries in 2021')
ax.legend()
fig.tight_layout()
plt.savefig('bar chart/png/521.png')
plt.clf()