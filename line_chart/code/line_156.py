
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

# set font size
mpl.rcParams['font.size'] = 12
# set figure size
plt.figure(figsize=(10,5))
# plot data
plt.plot(['USA', 'Canada', 'Mexico', 'Brazil', 'Argentina'], 
         [20.5, 1.8, 1.2, 2.2, 0.4], label='GDP')
plt.plot(['USA', 'Canada', 'Mexico', 'Brazil', 'Argentina'], 
         [4.5, 7.1, 4.6, 12.3, 10.2], label='Unemployment')
plt.plot(['USA', 'Canada', 'Mexico', 'Brazil', 'Argentina'], 
         [330, 37.7, 128.4, 209, 45.4], label='Population')
# set title and labels
plt.title('Economic Indicators of Four Countries in 2021')
plt.xlabel('Country')
plt.ylabel('Value')
# set grid
plt.grid(linestyle='--', linewidth=0.5)
# set xticks to prevent interpolation
plt.xticks(np.arange(5), ['USA', 'Canada', 'Mexico', 'Brazil', 'Argentina'],rotation=30)
# set legend
plt.legend(loc='best', prop={'size': 12})
# adjust the position to make sure the title and labels can display properly
plt.tight_layout()
# save figure
plt.savefig('line chart/png/66.png')
# clear figure
plt.clf()