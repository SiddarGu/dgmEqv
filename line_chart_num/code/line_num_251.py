
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10,6))
plt.title("Literacy, Poverty, and Crime Rates in the US from 2000 to 2005")
ax = plt.subplot()

year = np.array([2000, 2001, 2002, 2003, 2004, 2005])
literacy = np.array([80, 82, 84, 86, 88, 90])
poverty = np.array([20, 17, 15, 17, 15, 12])
crime = np.array([10, 8, 9, 11, 13, 14])

plt.plot(year, literacy, label="Literacy Rate (%)")
plt.plot(year, poverty, label="Poverty Rate (%)")
plt.plot(year, crime, label="Crime Rate (%)")

plt.xticks(year)
ax.annotate('80', xy=(2000, 80))
ax.annotate('82', xy=(2001, 82))
ax.annotate('84', xy=(2002, 84))
ax.annotate('86', xy=(2003, 86))
ax.annotate('88', xy=(2004, 88))
ax.annotate('90', xy=(2005, 90))
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.tight_layout()
plt.savefig('line chart/png/529.png', dpi=500)
plt.clf()