
import matplotlib.pyplot as plt
import numpy as np

#Create figure
fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot()

#Data
year = np.array([2001, 2002, 2003, 2004])
cropA = np.array([1000, 1200, 800, 1500])
cropB = np.array([800, 900, 1100, 1200])
cropC = np.array([1200, 1100, 1300, 1400])
cropD = np.array([1500, 1600, 1200, 800])

#Plot
plt.plot(year, cropA, label="Crop A (tonnes)")
plt.plot(year, cropB, label="Crop B (tonnes)")
plt.plot(year, cropC, label="Crop C (tonnes)")
plt.plot(year, cropD, label="Crop D (tonnes)")

#Labels and title
plt.xlabel('Year')
plt.ylabel('Crop Production (tonnes)')
plt.xticks(year)
plt.title('Crop Production in four regions from 2001 to 2004')
plt.legend(loc='upper left')

#Save
plt.tight_layout()
plt.savefig('line chart/png/172.png')

#Clear
plt.clf()