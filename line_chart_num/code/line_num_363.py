
import matplotlib.pyplot as plt
import numpy as np 

Country = ['USA','Canada','Mexico','Japan','China','India','France','Germany']
Number_of_visitors = [60,30,20,10,40,15,25,20]

fig = plt.figure(figsize=(10,8))
plt.plot(Country, Number_of_visitors)
plt.xticks(np.arange(len(Country)), Country, rotation=45, wrap=True)
plt.title('International Tourist Visitation in 2021')
plt.ylabel('Number of visitors (million)')
for a,b in zip(Country, Number_of_visitors):
    plt.annotate(b,xy=(a,b))
plt.tight_layout()
plt.savefig('line chart/png/522.png')
plt.clf()