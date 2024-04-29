
import matplotlib.pyplot as plt

plt.figure(figsize=(20, 10))
ax = plt.subplot()
ax.set_title('Donations to three charities from 2015 to 2019')
ax.set_xlabel('Year')
ax.set_ylabel('Donations')
year = [2015, 2016, 2017, 2018, 2019]
donations_A = [1000, 1200, 1500, 1800, 2000]
donations_B = [800, 900, 1100, 1300, 1400]
donations_C = [400, 500, 600, 700, 800]
plt.xticks(year)
ax.plot(year, donations_A, label="Donations A")
ax.plot(year, donations_B, label="Donations B")
ax.plot(year, donations_C, label="Donations C")
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig('line chart/png/108.png')
plt.clf()