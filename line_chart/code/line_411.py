
import matplotlib.pyplot as plt
import numpy as np

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
solarEnergy = [1200, 1400, 1500, 1600, 1900, 2200, 2400, 2000, 1800, 1500, 1300, 1200]
windEnergy = [1300, 1200, 1500, 1700, 1800, 2100, 2300, 2500, 2100, 1800, 1400, 1300]

plt.figure(figsize=(8, 6))
plt.title("Renewable energy production in a year")
plt.xticks(np.arange(12), months, rotation=45, ha="right")
plt.plot(months, solarEnergy, label="Solar Energy", color="red")
plt.plot(months, windEnergy, label="Wind Energy", color="blue")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('line chart/png/97.png')
plt.clf()