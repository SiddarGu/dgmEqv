
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10,6))

data = [[200,1000],[210,1200],[220,1400],[230,1600]]

x_ticks = ['2020','2021','2022','2023']

plt.bar(x_ticks, [row[0] for row in data], label='Donations(million)', width=0.5)
plt.bar(x_ticks, [row[1] for row in data], bottom=[row[0] for row in data], label='Volunteers', width=0.5)

plt.title('Total donations and volunteers for charity organizations from 2020 to 2023')
plt.xlabel('Year')
plt.ylabel('Count')
plt.xticks(np.arange(len(x_ticks)),x_ticks, rotation=45, ha='right')
plt.legend(loc='upper left') 
plt.tight_layout()

plt.savefig('bar chart/png/516.png')
plt.clf()