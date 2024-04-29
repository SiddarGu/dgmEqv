

import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(12, 6))
plt.title('Crop Yield Variations Across Different Seasons in the Midwest Region')

months = ['January', 'February', 'March', 'April', 'May', 'June']
yieldA = [100, 110, 130, 120, 140, 160] 
yieldB = [90, 95, 100, 105, 115, 130]
yieldC = [80, 85, 90, 95, 105, 120]

plt.plot(months, yieldA, label = 'Yield A')
plt.plot(months, yieldB, label = 'Yield B')
plt.plot(months, yieldC, label = 'Yield C')

plt.xticks(np.arange(6), months, rotation=45)
plt.legend(loc='lower left', bbox_to_anchor=(0.0, 1.01), ncol=3, 
            borderaxespad=0, frameon=False)

plt.tight_layout()
plt.savefig(r'line chart/png/51.png')
plt.clf()