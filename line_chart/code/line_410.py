
import matplotlib.pyplot as plt
plt.figure(figsize=(12,8))
plt.plot([2001, 2002, 2003, 2004, 2005, 2006], [10, 12, 11, 15, 14, 17], label='Revenue')
plt.plot([2001, 2002, 2003, 2004, 2005, 2006], [3, 4, 5, 6, 8, 9], label='Profit')
plt.title('Net Profits and Revenue of ABC Company from 2001 to 2006')
plt.xlabel('Year')
plt.ylabel('Amount (million dollars)')
plt.xticks([2001, 2002, 2003, 2004, 2005, 2006])
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig('line chart/png/286.png')
plt.clf()