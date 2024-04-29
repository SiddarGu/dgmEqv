
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10,7))
plt.plot(['January','February','March','April','May','June','July','August'],
         [50,55,60,65,70,75,80,85], label='Wind Energy', marker='*')
plt.plot(['January','February','March','April','May','June','July','August'],
         [40,45,50,55,60,65,70,75], label='Solar Energy', marker='o', color='red')

plt.xlabel('Month')
plt.ylabel('Energy Production')
plt.title('Renewable Energy Production in California, 2021')
plt.xticks(np.arange(8), ('January','February','March','April','May','June','July','August'))
plt.legend(loc='best', labelspacing=0.5)
plt.grid(linestyle='--', linewidth=0.5, alpha=0.3)
plt.tight_layout()
plt.savefig('line chart/png/49.png')
plt.clf()