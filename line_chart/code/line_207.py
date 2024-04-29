

import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
year = [2000, 2001, 2002, 2003, 2004, 2005]
avg_home_price = [150, 170, 180, 190, 220, 250]
avg_rental_price = [50, 55, 60, 65, 70, 75]
plt.plot(year, avg_home_price, label="Average Home Price")
plt.plot(year, avg_rental_price, label="Average Rental Price")
plt.title("Changes in Average Home and Rental Prices in the U.S. from 2000 to 2005")
plt.xlabel("Year")
plt.ylabel("Price (in thousands of dollars)")
plt.legend(loc='upper left')
plt.xticks(year)
plt.grid(True)
plt.tight_layout()
plt.savefig('line chart/png/176.png')
plt.clf()