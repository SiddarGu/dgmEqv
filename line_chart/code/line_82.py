
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[2010, 15, 10, 20], 
                 [2011, 20, 14, 25], 
                 [2012, 25, 17, 30], 
                 [2013, 30, 20, 35], 
                 [2014, 35, 24, 40]])

years, art_galleries, museums, theaters = data.T

plt.figure(figsize=(15, 8))
plt.plot(years, art_galleries, label='Art Galleries') 
plt.plot(years, museums, label='Museums') 
plt.plot(years, theaters, label='Theaters')
plt.title('Expansion of Arts and Cultural Venues in a City from 2010 to 2014', fontsize=18)
plt.xlabel('Year', fontsize=14) 
plt.ylabel('Number of Venues', fontsize=14)
plt.xticks(years)
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig('line chart/png/238.png')
plt.clf()