
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10,8))

year = [2015, 2016, 2017, 2018, 2019, 2020]
hours = [10, 12, 15, 17, 19, 20]
users = [100, 120, 140, 160, 180, 200]

plt.plot(year, hours, color='blue', linestyle='solid', label='Hours')
plt.plot(year, users, color='red', linestyle='dashed', label='Users')

plt.xlabel('Year')
plt.ylabel('Average Usage Duration & Average Number of Users')

plt.title('Increase in Technology Usage Over the Last 6 Years')
plt.legend(loc='upper right', fontsize='large')
plt.xticks(year, rotation=45)
plt.tight_layout()
plt.savefig('line chart/png/305.png')
plt.clf()