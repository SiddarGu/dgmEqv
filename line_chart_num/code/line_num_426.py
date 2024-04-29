
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot()

year = [2007, 2008, 2009, 2010, 2011, 2012, 2013]
taxRate = [15, 18, 19, 20, 21, 22, 23]
unemploymentRate = [4.8, 5.8, 9.3, 9.6, 8.7, 7.8, 7.3]
gdpGrowthRate = [2.5, 0.2, -2.8, 2.8, 1.6, 2.2, 1.7]

ax.set_title('Tax Rate, Unemployment Rate, and GDP Growth Rate in the U.S. from 2007 to 2013')
ax.set_xlabel('Year')
ax.set_ylabel('Rate (%)')
ax.plot(year, taxRate, label='Tax Rate')
ax.plot(year, unemploymentRate, label='Unemployment Rate')
ax.plot(year, gdpGrowthRate, label='GDP Growth Rate')
ax.legend(loc='upper left')
ax.grid()

for x, ytax, yunem, ygdp in zip(year, taxRate, unemploymentRate, gdpGrowthRate):
    ax.annotate('Tax: {}\nUnem: {}\nGDP: {}'.format(ytax, yunem, ygdp), 
                xy=(x, (ytax+yunem+ygdp)/3), 
                xytext=(x, (ytax+yunem+ygdp)/3), 
                rotation=45, 
                wrap=True)

plt.xticks(year)
plt.tight_layout()
plt.savefig('line chart/png/434.png')
plt.clf()