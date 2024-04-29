
import matplotlib.pyplot as plt
plt.figure(figsize=(10,5))
plt.plot([2001,2002,2003,2004],[20,25,30,35], label = 'Stock Price A(USD)')
plt.plot([2001,2002,2003,2004],[25,30,35,40], label = 'Stock Price B(USD)')
plt.plot([2001,2002,2003,2004],[15,20,25,30], label = 'Stock Price C(USD)')
plt.plot([2001,2002,2003,2004],[10,15,20,25], label = 'Stock Price D(USD)')
plt.title('Stock Prices of four Companies in 2001-2004')
plt.xlabel('Year')
plt.ylabel('Stock Price (USD)')
plt.xticks(ticks=[2001,2002,2003,2004], labels=['2001','2002','2003','2004'])
plt.legend(loc='upper left', bbox_to_anchor=(1,1), ncol=1, frameon=False)
plt.tight_layout()
plt.savefig('line chart/png/116.png')
plt.clf()