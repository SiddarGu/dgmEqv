
import matplotlib.pyplot as plt
import numpy as np

x = [2017, 2018, 2019, 2020, 2021, 2022, 2023]
y1 = [20, 22, 25, 30, 35, 40, 45]
y2 = [150, 200, 250, 300, 350, 400, 450]

plt.figure(figsize=(10,6))
plt.plot(x, y1, '-o', color='blue', label='Tourist Arrivals(millions)')
plt.plot(x, y2, '-o', color='red', label='Average Spend per Person(dollars)')
plt.xticks(x)
plt.title('Tourist Arrivals and Average Spend per Person in the US from 2017 to 2023')
plt.xlabel('Year')
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.25), frameon=False, ncol=2, fontsize=13)

for a,b,c in zip(x, y1, y2):
    plt.annotate('{}'.format(b), xy=(a,b), xytext=(a-0.25, b+2))
    plt.annotate('{}'.format(c), xy=(a,c), xytext=(a-0.25, c+2))

plt.tight_layout()
plt.savefig('line chart/png/212.png')
plt.clf()