
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot()

country = ['USA', 'UK', 'Germany', 'France']
gdp_billion = [20.7, 2.8, 3.9, 2.2]
unemployment_rate = [7.9, 4.7, 6.3, 8.5]

ax.bar(country, gdp_billion, width=0.4, label='GDP (billion)')
ax.bar(country, unemployment_rate, bottom=gdp_billion, width=0.4, label='Unemployment Rate(%)')

ax.set_title('GDP and unemployment rate of four countries in 2021')
ax.set_xlabel('Country')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), fancybox=True, shadow=True, ncol=2)
plt.xticks(rotation=45, fontsize=8)
plt.tight_layout()
plt.savefig('bar_177.png', bbox_inches='tight')
plt.clf()