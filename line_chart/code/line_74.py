

import matplotlib.pyplot as plt
plt.figure(figsize=(8,6))
plt.plot([2001,2002,2003,2004], [100,120,140,180],label='Wheat Production')
plt.plot([2001,2002,2003,2004], [200,220,210,230],label='Rice Production')
plt.plot([2001,2002,2003,2004], [300,330,360,320],label='Corn Production')
plt.title("Crop Production Trends in the United States from 2001 to 2004")
plt.xticks([2001,2002,2003,2004])
plt.xlabel('Year')
plt.ylabel('Production (million bushels)')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('line chart/png/243.png')
plt.clf()