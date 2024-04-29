
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot()

region = ['North America', 'South America', 'Europe', 'Asia']
donations = [20000, 10000, 15000, 13000]
volunteer = [300, 400, 500, 600]

barWidth = 0.2
r1 = np.arange(len(donations))
r2 = [x + barWidth for x in r1]

plt.bar(r1, donations, width=barWidth, label='Charitable Donations($)', color='#e74c3c')
plt.bar(r2, volunteer, width=barWidth, label='Volunteer Hours', color='#3498db')

plt.xticks([r + barWidth/2 for r in range(len(donations))], region, rotation=20, wrap=True)
plt.title('Charitable donations and volunteer hours in four regions in 2021')
plt.xlabel('Region')
plt.ylabel('Amount')
plt.legend()
plt.tight_layout()
plt.savefig('bar chart/png/503.png')
plt.clf()