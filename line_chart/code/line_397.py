
import matplotlib.pyplot as plt

plt.figure(figsize=(14,6))
ax = plt.subplot()

x_data = [2018, 2019, 2020, 2021]
y_data1 = [20000, 25000, 30000, 35000]
y_data2 = [11000, 13000, 15000, 17000]

plt.plot(x_data, y_data1, label = 'Number of Crimes')
plt.plot(x_data, y_data2, label = 'Number of Arrests')

ax.set_title('Crime rate and arrests in the United States from 2018 to 2021')
plt.xticks([2018, 2019, 2020, 2021], fontsize = 10, rotation = 30)
plt.legend(loc='best', fontsize = 10)
plt.tight_layout()
plt.savefig('line chart/png/122.png')
plt.clf()