
import matplotlib.pyplot as plt 
import numpy as np 

Year = [2006, 2007, 2008, 2009, 2010, 2011, 2012]
Online_sales = [100, 150, 200, 250, 300, 350, 400]
Offline_sales = [200, 250, 300, 350, 400, 450, 500]
Total_sales = [300, 400, 500, 600, 700, 800, 900]

plt.figure(figsize=(10,7))
plt.plot(Year, Online_sales, 'g-', label='Online Sales')
plt.plot(Year, Offline_sales, 'b-', label='Offline Sales')
plt.plot(Year, Total_sales, 'r-', label='Total Sales')
plt.title("Online and Offline Retail Sales Growth in the US from 2006 to 2012")
plt.xlabel("Year")
plt.ylabel("Sales (billion dollars)")
plt.xticks(Year, rotation='vertical')
plt.legend(loc=1, prop={'size': 8, 'family': 'Times New Roman'}, bbox_to_anchor=(1.1, 1), borderaxespad=0.)

for a, b in zip(Year, Online_sales):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
for a, b in zip(Year, Offline_sales):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
for a, b in zip(Year, Total_sales):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.savefig('line chart/png/429.png')
plt.clf()