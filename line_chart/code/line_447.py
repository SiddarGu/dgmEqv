
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

plt.figure(figsize=(10,6))
ax = plt.subplot()

plt.plot(['2001', '2002', '2003', '2004'],[1.2,1.5,2.0,2.5], label='GDP(trillions)')
plt.plot(['2001', '2002', '2003', '2004'],[2.3,2.4,1.9,2.8], label='Inflation Rate', color='r')
plt.plot(['2001', '2002', '2003', '2004'],[4.5,5.6,4.2,3.6], label='Unemployment Rate', color='g')

ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
plt.xticks(rotation=45)
plt.title("Economic performance in the US from 2001 to 2004")
plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig('line chart/png/201.png')
plt.clf()