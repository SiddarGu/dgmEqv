
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10, 5)) 
ax = fig.add_subplot(111)
ax.set_title('Median Home Price and Average Rent from 2020 to 2023')
year = [2020, 2021, 2022, 2023]
median_home_price = [500, 550, 600, 650]
average_rent = [1000, 1100, 1200, 1300]
p1 = ax.bar(year, median_home_price, width=0.5, label='Median Home Price', color='#00FFFF')
p2 = ax.bar(year, average_rent, width=0.5, label='Average Rent (monthly)', color='#FFFF00', bottom=median_home_price)
plt.xticks(year)
ax.legend(loc='upper left')
ax.set_xlabel('Year')
ax.set_ylabel('Price & Rent')
for x, y, t in zip(year, median_home_price, median_home_price):
    ax.text(x, y + 0.05, '$%s' % t, ha='center', va='bottom')
for x, y, t in zip(year, median_home_price, average_rent):
    ax.text(x, y + t - 100, '$%s' % t, ha='center', va='bottom')
plt.tight_layout()
plt.savefig('Bar Chart/png/589.png')
plt.clf()