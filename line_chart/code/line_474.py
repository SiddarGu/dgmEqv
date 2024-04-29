
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[2000,1000,800,1200,1500],
                 [2001,1200,900,1100,1600],
                 [2002,800,1100,1300,1200],
                 [2003,1500,1200,1400,800]])

plt.figure(figsize=(10,6))
plt.plot(data[:,0],data[:,1],label='Wheat Production')
plt.plot(data[:,0],data[:,2],label='Rice Production')
plt.plot(data[:,0],data[:,3],label='Corn Production')
plt.plot(data[:,0],data[:,4],label='Barley Production')
plt.title('Crop Production Trends in Canada from 2000 to 2003')
plt.xlabel('Year')
plt.ylabel('Production(tonnes)')
plt.legend()
plt.xticks(data[:,0])
plt.tight_layout()
plt.savefig('line chart/png/466.png')
plt.clf()