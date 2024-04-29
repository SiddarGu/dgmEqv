
import matplotlib.pyplot as plt
import numpy as np

#create figure
fig = plt.figure(figsize=(15, 10)) 

#plot data
plt.plot(np.arange(2001, 2005), [1000, 1300, 1100, 1400], label='Criminal Cases')
plt.plot(np.arange(2001, 2005), [1200, 1100, 1400, 1600], label='Civil Cases')
plt.plot(np.arange(2001, 2005), [1500, 1400, 1600, 1800], label='Family Cases')
plt.plot(np.arange(2001, 2005), [800, 900, 1000, 1200], label='Traffic Cases')

#label for x and y-axis
plt.xlabel('Year')
plt.ylabel('Number of Cases Filed')

#title of figure
plt.title('Number of Cases Filed Annually in U.S. Courts')

#xticks
plt.xticks(np.arange(2001, 2005))

#add legend
plt.legend(loc='upper right')

#annotate
plt.annotate('Criminal Cases: 1400', xy=(2004, 1400))
plt.annotate('Civil Cases: 1600', xy=(2004, 1600))
plt.annotate('Family Cases: 1800', xy=(2004, 1800))
plt.annotate('Traffic Cases: 1200', xy=(2004, 1200))

#tight layout
plt.tight_layout()

#save figure
plt.savefig('line chart/png/500.png')

#clear figure
plt.clf()