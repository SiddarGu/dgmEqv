
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
plt.title('Average House and Rent Prices in the US from 2001 to 2009', fontsize=18)
plt.plot(['2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009'],
         [250, 300, 350, 400, 450, 500, 550, 600, 650], label='Average House Price (thousands dollars)')
plt.plot(['2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009'],
         [50, 55, 60, 65, 70, 75, 80, 85, 90], label='Average Rent Price (thousands dollars)')
plt.xlabel('Year', fontsize=16)
plt.ylabel('Price (thousands dollars)', fontsize=16)
plt.xticks(['2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009'], rotation='vertical')
plt.legend(loc='upper left')
plt.grid(linestyle='--')
plt.tight_layout()
plt.savefig('line chart/png/469.png')
plt.clf()