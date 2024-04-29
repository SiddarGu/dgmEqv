
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(111)
Country = ['USA', 'UK', 'Germany', 'France']
Number_of_Houses = [800, 600, 400, 700]
Average_Price = [200000, 250000, 230000, 220000]

ax.bar(Country, Number_of_Houses, width=0.4, label='Number of Houses')
ax.bar(Country, Average_Price, width=0.4, bottom=Number_of_Houses, label='Average Price')

ax.set_title('Number of Houses and Average Price in four countries in 2021')
ax.set_xlabel('Country')
ax.set_ylabel('Number and Price')
ax.set_xticklabels(Country, rotation=45, ha="right")
ax.legend(loc='best')
plt.tight_layout()
plt.savefig('bar chart/png/74.png')
plt.clf()