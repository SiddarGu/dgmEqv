
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot()

country = ['USA', 'UK', 'Germany', 'France']
GDP = [21, 3, 4, 3.4]
growth_rate = [3.7, 2.1, 2.2, 2.3]

ax.bar(country, GDP, width = 0.6, bottom = 0, align = 'center', color = '#F08080', label = 'GDP (trillion)')
ax.bar(country, growth_rate, width = 0.3, bottom = 0, align = 'edge', color = '#87CEFA', label = 'Growth Rate')

ax.set_xticklabels(country, rotation = 0, ha = 'center', wrap = True)
ax.set_title('GDP and growth rate of four countries in 2021')
ax.legend(loc = 'best')

plt.tight_layout()
plt.savefig('bar chart/png/507.png')
plt.clf()