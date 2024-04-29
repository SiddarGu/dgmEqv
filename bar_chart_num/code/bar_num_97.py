
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(111)

Country = ['USA', 'UK', 'Germany', 'France']
Crop_Yield = [4000, 3000, 2000, 3500]
Livestock = [5000, 6000, 7000, 6500]

bar1 = ax.bar(Country, Crop_Yield, color='red', label='Crop Yield')
bar2 = ax.bar(Country, Livestock, bottom=Crop_Yield, color='green', label='Livestock')

ax.set_title('Crop yield and livestock numbers in four countries in 2021')
ax.set_xlabel('Country')
ax.set_ylabel('Number')
ax.legend()

plt.xticks(Country)

for bar1, bar2 in zip(bar1, bar2):
    y1 = bar1.get_height()
    y2 = bar2.get_height()

    ax.annotate('{}{}'.format(y1, y2),
                xy=(bar1.get_x() + bar1.get_width() / 2, y1 + y2 / 2),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom')

plt.tight_layout()
plt.savefig('Bar Chart/png/22.png')
plt.clf()