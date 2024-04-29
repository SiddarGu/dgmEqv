
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
plt.plot(['2018','2019','2020','2021'], [300000, 325000, 350000, 375000],
         label='Median Home Price', marker='o', color='green', linewidth=3)
plt.plot(['2018','2019','2020','2021'], [4500, 5000, 5500, 6000],
         label='No. of Home Sales', marker='o', color='blue', linewidth=3)
plt.plot(['2018','2019','2020','2021'], [1800, 2000, 2500, 2800],
         label='Average Rent', marker='o', color='orange', linewidth=3)
plt.title('Housing market trends in the USA from 2018 to 2021')
plt.xlabel('Year')
plt.xticks(['2018','2019','2020','2021'])
plt.ylabel('Price')
plt.legend(loc='upper left', fontsize=12, ncol=3, frameon=False,
           columnspacing=1, handletextpad=0.3, labelspacing=0.3)
plt.tight_layout()
plt.savefig('line chart/png/415.png')
plt.clf()