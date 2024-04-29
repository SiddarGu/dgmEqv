

import matplotlib.pyplot as plt
import numpy as np

#Data
Year = np.array([2000, 2001, 2002, 2003, 2004, 2005, 2006])
Median_Home_Price = np.array([300000, 310000, 330000, 350000, 370000, 390000, 410000])
Rental_Price = np.array([2000, 2100, 2200, 2300, 2500, 2800, 3000])

#Plotting
fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(111)
ax.plot(Year, Median_Home_Price, label="Median Home Price")
ax.plot(Year, Rental_Price, label="Rental Price")
ax.set_xlabel("Year")
ax.set_ylabel("Price")
ax.set_xticks(Year)
ax.set_title("Home and rental prices in the US from 2000 to 2006")
ax.legend(loc="upper left")
plt.tight_layout()

#Save Image
plt.savefig("line chart/png/302.png")

#Clear Image State
plt.cla()