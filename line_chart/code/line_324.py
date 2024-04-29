
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

plt.figure(figsize=(10, 5))
ax = plt.subplot()
ax.set_title('Cultural Activity in the US from 2001 to 2004')

plt.plot(['2001', '2002', '2003', '2004'], [200, 250, 220, 180], color='green', marker='o', linewidth=2, label='Number of Museums')
plt.plot(['2001', '2002', '2003', '2004'], [150, 180, 170, 220], color='blue', marker='^', linewidth=2, label='Number of Art Galleries')
plt.plot(['2001', '2002', '2003', '2004'], [300, 350, 400, 450], color='red', marker='s', linewidth=2, label='Number of Concerts')
plt.plot(['2001', '2002', '2003', '2004'], [400, 420, 380, 340], color='purple', marker='*', linewidth=2, label='Number of Plays')

ax.xaxis.set_major_locator(ticker.MultipleLocator(base=1.0))
plt.xticks(['2001', '2002', '2003', '2004'])
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig('line chart/png/498.png')
plt.clf()