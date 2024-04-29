
import matplotlib.pyplot as plt
import numpy as np

# data
Country = ["USA","UK","Germany","France"]
Hospitals = [1000,1200,1500,1400]
Doctors = [7000,6000,8000,7000]
Nurses = [15000,14000,13000,12000]

# figure
fig, ax = plt.subplots(figsize=(10, 8))

# plot
ax.bar(Country, Hospitals, color='#2c5aaf', label='Hospitals')
ax.bar(Country, Doctors, bottom=Hospitals, color='#dbe9f7', label='Doctors')
ax.bar(Country, Nurses, bottom=[sum(x) for x in zip(Hospitals, Doctors)], color='#a3e4f9', label='Nurses')

# legend
ax.legend(loc='upper right')

# x-axis
plt.xticks(Country, Country)

# y-axis
plt.ylabel('Number')

# title
plt.title('Number of hospitals, doctors and nurses in four countries in 2021')

# adjust
plt.tight_layout()

# save
plt.savefig('Bar Chart/png/56.png')

# clear
plt.clf()