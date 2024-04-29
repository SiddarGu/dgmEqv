
import matplotlib.pyplot as plt
plt.figure(figsize=(12,6))
plt.plot([2001,2002,2003,2004,2005,2006,2007,2008], [1000,1200,1300,1400,1500,1600,1700,1800], linewidth=3.0)
plt.plot([2001,2002,2003,2004,2005,2006,2007,2008], [15,20,25,30,35,40,45,50], linewidth=3.0)
plt.xlabel('Year')
plt.ylabel('Emissions and Renewable Energy Usage')
plt.title('Carbon Emissions and Renewable Energy Usage in the U.S. from 2001 to 2008')
plt.legend(['Carbon Emissions (million tonnes)','Renewable Energy Usage (percentage)'],loc='upper left')
plt.grid(True, axis='y', linestyle='-.')
plt.xticks([2001,2002,2003,2004,2005,2006,2007,2008])
plt.tight_layout()
for a,b in zip([2001,2002,2003,2004,2005,2006,2007,2008], [1000,1200,1300,1400,1500,1600,1700,1800]): 
    plt.text(a, b, str(b), fontsize=10, rotation=45, wrap=True)
for a,b in zip([2001,2002,2003,2004,2005,2006,2007,2008], [15,20,25,30,35,40,45,50]): 
    plt.text(a, b, str(b), fontsize=10, rotation=45, wrap=True)
plt.savefig('line chart/png/462.png')
plt.clf()